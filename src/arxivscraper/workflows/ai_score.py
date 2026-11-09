## { SCRIPT

##
## === DEPENDENCIES
##

## stdlib
import json
import re
import time
import tomllib
from typing import Any

## third-party
from openai import OpenAI

## personal
from huginn import manage_log, manage_shell

## local
from arxivscraper.config_paths import directories, files as config_files
from arxivscraper.support import articles, file_io

##
## === AI PROVIDER CONFIG
##


def load_provider_config(
    *,
    cli_model: str | None = None,
    cli_base_url: str | None = None,
) -> dict[str, Any]:
    """Load AI provider config from `configs/ai/ai_provider.toml`; exit with an error if it is missing or incomplete.

    CLI arguments override any config file values.
    """
    provider_path = directories.get_ai_configs_dir() / config_files.ai_provider
    if not provider_path.is_file():
        manage_log.exit_with_error(
            f"no AI config found; create `{provider_path}` (see `{config_files.ai_provider_example}`)",
        )
    try:
        with provider_path.open("rb") as file_pointer:
            config = tomllib.load(file_pointer)
    except (tomllib.TOMLDecodeError, OSError) as error:
        manage_log.exit_with_error(f"could not read `{provider_path}`: {error}")
    if cli_model:
        config["model"] = cli_model
    if cli_base_url:
        config["base_url"] = cli_base_url
    if not config.get("api_key"):
        manage_log.exit_with_error(
            "no `api_key` in the provider config; local servers (Ollama, LM Studio) use a placeholder like `local`",
        )
    if not config.get("model"):
        manage_log.exit_with_error("no `model` in the provider config")
    return config


##
## === AI CLIENT
##


def create_ai_client(
    api_key: str,
    *,
    base_url: str | None = None,
) -> OpenAI:
    """Create and return an `OpenAI` client configured with `api_key` and optional `base_url`."""
    client_kwargs: dict[str, Any] = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    return OpenAI(**client_kwargs)


##
## === AI SCORING
##


def get_ai_response(
    *,
    ai_client: OpenAI,
    article_title: str,
    article_abstract: str,
    prompt_rules: str,
    prompt_criteria: str,
    ai_model: str,
) -> dict[str, Any]:
    """Send `article_title` and `article_abstract` to the AI model and return the parsed response dict."""
    if not article_title:
        return {
            "status": "error",
            "error": "Missing article title.",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": None
        }
    if not article_abstract:
        return {
            "status": "error",
            "error": "Missing article abstract.",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": None
        }
    prompt_input = f"{prompt_criteria}\n\nTITLE: {article_title}\n\nABSTRACT: {article_abstract}"
    try:
        ai_response = ai_client.chat.completions.create(
            model=ai_model,
            messages=[
                {
                    "role": "system",
                    "content": prompt_rules
                },
                {
                    "role": "user",
                    "content": prompt_input
                },
            ],
            temperature=0.0,
        )
    except Exception as error:
        return {
            "status": "error",
            "error": f"API call failed: {error}",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": None
        }
    response_text = ""
    try:
        response_text = (ai_response.choices[0].message.content or "").strip()
        ## sanitise invalid JSON escape sequences (e.g. LaTeX \gt, \cdot) before parsing
        sanitised = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', response_text)
        response_dict = json.loads(sanitised)
        ai_rating = float(response_dict["rating"])
        ai_reason = response_dict["reason"]
        return {
            "status": "success",
            "ai_rating": ai_rating,
            "ai_reason": ai_reason,
            "ai_response": response_text
        }
    except Exception as error:
        fallback = _fallback_parse_rating_reason(response_text)
        if fallback is not None:
            return {
                "status": "success",
                "ai_rating": fallback["rating"],
                "ai_reason": fallback["reason"],
                "ai_response": response_text
            }
        return {
            "status": "error",
            "error": f"JSON parsing failed: {error}",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": response_text
        }


def _fallback_parse_rating_reason(
    response_text: str,
) -> dict[str, Any] | None:
    """Recover `rating`/`reason` via regex when the model emits near-JSON with an unclosed or malformed string."""
    rating_match = re.search(r'"rating"\s*:\s*([0-9]+(?:\.[0-9]+)?)', response_text)
    reason_match = re.search(r'"reason"\s*:\s*"(.*)"\s*\}?\s*$', response_text, re.DOTALL)
    if not rating_match or not reason_match:
        return None
    reason_text = reason_match.group(1).replace('\\"', '"').replace("\n", " ").strip()
    return {
        "rating": float(rating_match.group(1)),
        "reason": reason_text,
    }


def check_provider_reachable(
    *,
    ai_client: OpenAI,
    ai_model: str,
) -> None:
    """Send one minimal request to `ai_model`; exit with an error if it fails.

    Runs once before the scoring loop so a down/misconfigured provider fails fast with a single
    diagnostic, instead of repeating the same connection/model error once per article.
    """
    response_dict = get_ai_response(
        ai_client=ai_client,
        article_title="Connectivity check.",
        article_abstract="Connectivity check.",
        prompt_rules='Reply with exactly this JSON: {"rating": 0, "reason": "ok"}',
        prompt_criteria='Reply with exactly this JSON: {"rating": 0, "reason": "ok"}',
        ai_model=ai_model,
    )
    if response_dict.get("status") != "success":
        manage_log.exit_with_error(f"AI provider check failed: {response_dict.get('error', '<unknown error>')}")


def get_ai_score(
    *,
    article: articles.Article,
    ai_client: OpenAI,
    prompt_rules: str,
    prompt_criteria: str,
    ai_model: str,
) -> bool:
    """Score `article` using the AI model; set its `ai_rating` and `ai_reason`, and report the result."""
    time_start = time.time()
    response_dict = get_ai_response(
        ai_client=ai_client,
        article_title=article.title,
        article_abstract=article.abstract,
        prompt_rules=prompt_rules,
        prompt_criteria=prompt_criteria,
        ai_model=ai_model,
    )
    time_elapsed = time.time() - time_start
    if response_dict.get("status") != "success":
        failure_items = {"error": response_dict.get("error", "<unknown error>")}
        ai_response = response_dict.get("ai_response")
        if ai_response:
            failure_items["raw response"] = ai_response
        manage_log.log_outcome(
            "could not score this paper",
            status=manage_log.OutcomeStatus.FAILURE,
            items=failure_items,
        )
        return False
    article.ai_rating = response_dict.get("ai_rating")
    article.ai_reason = response_dict.get("ai_reason")
    manage_log.log_outcome(
        f"rated {article.ai_rating}",
        status=manage_log.OutcomeStatus.SUCCESS,
        items={
            "title": article.title.strip(),
            "time": f"{time_elapsed:.2f} s",
        },
    )
    return True


def _read_prompt_file(
    file_name: str,
) -> str:
    prompt_path = directories.get_ai_configs_dir() / file_name
    if not prompt_path.is_file():
        manage_log.exit_with_error(f"no prompt file found; create `{prompt_path}`")
    return file_io.read_text_file(prompt_path)


##
## === COMMAND
##


def cmd_score(
    *,
    model: str | None,
    base_url: str | None,
) -> None:
    """Rate every unscored paper with the AI provider, saving each rating as it arrives."""
    manage_log.log_task("checking the AI provider")
    config = load_provider_config(
        cli_model=model,
        cli_base_url=base_url,
    )
    ai_client = create_ai_client(
        api_key=config["api_key"],
        base_url=config.get("base_url"),
    )
    provider_items = {"model": config["model"]}
    if config.get("base_url"):
        provider_items["base url"] = config["base_url"]
    check_provider_reachable(
        ai_client=ai_client,
        ai_model=config["model"],
    )
    manage_log.log_outcome(
        "the AI provider answered",
        status=manage_log.OutcomeStatus.SUCCESS,
        items=provider_items,
    )
    manage_log.log_task("finding unscored papers")
    unscored_articles = [_article for _article in articles.read_all_markdown_files() if _article.ai_rating is None]
    if not unscored_articles:
        manage_log.log_outcome(
            "every paper is already scored",
            status=manage_log.OutcomeStatus.SKIPPED,
        )
        return
    manage_log.log_outcome(
        f"{len(unscored_articles)} papers to score",
        status=manage_log.OutcomeStatus.SUCCESS,
    )
    prompt_rules = _read_prompt_file(config_files.ai_rules)
    prompt_criteria = _read_prompt_file(config_files.ai_criteria)
    num_scored = 0
    for article_index, article in enumerate(unscored_articles):
        manage_log.log_task(f"scoring {article.arxiv_id} ({article_index + 1}/{len(unscored_articles)})")
        article_is_scored = get_ai_score(
            article=article,
            ai_client=ai_client,
            prompt_rules=prompt_rules,
            prompt_criteria=prompt_criteria,
            ai_model=config["model"],
        )
        if article_is_scored:
            manage_shell.run_fn(
                description=f"save {article.arxiv_id}.md",
                fn=lambda: articles.save_article(article),
            )
            num_scored += 1
    if num_scored < len(unscored_articles):
        summary_status = manage_log.OutcomeStatus.WARNING
    else:
        summary_status = manage_log.OutcomeStatus.SUCCESS
    manage_log.log_outcome(
        f"scored {num_scored} of {len(unscored_articles)} papers",
        status=summary_status,
    )

## } SCRIPT
