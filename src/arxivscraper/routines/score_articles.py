## { MODULE

##
## === DEPENDENCIES
##

## stdlib
import json
import sys
import time
import tomllib
from typing import Any

## third-party
from openai import OpenAI

## local
from arxivscraper.io_configs import directories, file_names
from arxivscraper.utils import argparse_utils, article_utils, io_utils

##
## === PROVIDER CONFIG
##

_DEFAULT_MODEL = "gpt-4o-mini"


def load_provider_config(
    *,
    cli_model: str | None = None,
    cli_base_url: str | None = None,
) -> dict[str, Any] | None:
    """Load AI provider config from `ai_provider.toml`, falling back to the legacy `api_key.txt`.

    CLI arguments override any config file values.
    """
    provider_path = directories.configs_dir / file_names.ai_provider
    if provider_path.is_file():
        try:
            with provider_path.open("rb") as file_pointer:
                config = tomllib.load(file_pointer)
        except Exception as error:
            print(f"Error reading {provider_path.name}: {error}")
            return None
    else:
        ## fall back to legacy api_key.txt
        key_path = directories.configs_dir / file_names.ai_api_key
        if not key_path.is_file():
            print(
                f"Error: no AI config found.\n"
                f"Create configs/{file_names.ai_provider} "
                f"(see configs/{file_names.ai_provider_example}) "
                f"or the legacy configs/{file_names.ai_api_key}.",
            )
            return None
        api_key = None
        for line in key_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip().strip("'").strip('"')
            if stripped:
                api_key = stripped
                break
        if not api_key:
            print(f"Error: {file_names.ai_api_key} is empty.")
            return None
        config = {"api_key": api_key, "base_url": None, "model": _DEFAULT_MODEL}

    ## CLI overrides
    if cli_model:
        config["model"] = cli_model
    if cli_base_url:
        config["base_url"] = cli_base_url

    if not config.get("api_key"):
        print(
            "Error: no api_key in provider config."
            "Local servers (Ollama, LM Studio) use a placeholder like 'local'.",
        )
        return None
    if not config.get("model"):
        print("Error: no model specified in provider config.")
        return None

    return config


##
## === AI CLIENT SETUP
##


def build_ai_client(
    api_key: str,
    *,
    base_url: str | None = None,
) -> OpenAI:
    client_kwargs: dict[str, Any] = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    return OpenAI(**client_kwargs)


##
## === AI RESPONSE
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
    if not article_title:
        return {
            "status": "error",
            "error": "Missing article title.",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": None,
        }
    if not article_abstract:
        return {
            "status": "error",
            "error": "Missing article abstract.",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": None,
        }
    prompt_input = f"{prompt_criteria}\n\nTITLE: {article_title}\n\nABSTRACT: {article_abstract}"
    try:
        ai_response = ai_client.chat.completions.create(
            model=ai_model,
            messages=[
                {
                    "role": "system",
                    "content": prompt_rules,
                },
                {
                    "role": "user",
                    "content": prompt_input,
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
            "ai_response": None,
        }
    response_text = ""
    try:
        response_text = (ai_response.choices[0].message.content or "").strip()
        response_dict = json.loads(response_text)
        ai_rating = float(response_dict["rating"])
        ai_reason = response_dict["reason"]
        return {
            "status": "success",
            "ai_rating": ai_rating,
            "ai_reason": ai_reason,
            "ai_response": response_text,
        }
    except Exception as error:
        return {
            "status": "error",
            "error": f"JSON parsing failed: {error}",
            "ai_rating": None,
            "ai_reason": None,
            "ai_response": response_text,
        }


##
## === SCORE ARTICLE
##


def get_ai_score(
    *,
    article: article_utils.Article,
    ai_client: OpenAI,
    prompt_rules: str,
    prompt_criteria: str,
    ai_model: str,
) -> bool:
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
        print("Error:", response_dict.get("error", "<unknown error>"))
        ai_response = response_dict.get("ai_response")
        if ai_response:
            print("Raw LLM response:", ai_response)
        return False
    print("arXiv-id:", article.arxiv_id)
    print("Title:", article.title.strip())
    print("Rating:", response_dict.get("ai_rating"))
    print(f"Elapsed time: {time_elapsed:.2f} seconds.")
    article.ai_rating = response_dict.get("ai_rating")
    article.ai_reason = response_dict.get("ai_reason")
    return True


##
## === MAIN
##


def main():
    user_inputs = argparse_utils.GetUserInputs(include_score=True)
    score_inputs = user_inputs.get_score_inputs()

    config = load_provider_config(
        cli_model=score_inputs.get("model"),
        cli_base_url=score_inputs.get("base_url"),
    )
    if not config:
        raise RuntimeError("Failed to load AI provider config.")

    ai_client = build_ai_client(
        api_key=config["api_key"],
        base_url=config.get("base_url"),
    )
    print(f"Model: {config['model']}")
    if config.get("base_url"):
        print(f"Base URL: {config['base_url']}")

    print("Reading in all articles...")
    articles = article_utils.read_all_markdown_files()
    articles = [article for article in articles if article.ai_rating is None]
    num_articles = len(articles)
    print(f"Preparing to score {num_articles} articles.")
    prompt_rules = io_utils.read_text_file(directories.configs_dir / file_names.ai_rules)
    prompt_criteria = io_utils.read_text_file(directories.configs_dir / file_names.ai_criteria)
    for article_index, article in enumerate(articles):
        print(f"({article_index+1}/{num_articles})")
        is_scored = get_ai_score(
            article=article,
            ai_client=ai_client,
            prompt_rules=prompt_rules,
            prompt_criteria=prompt_criteria,
            ai_model=config["model"],
        )
        if is_scored:
            article_utils.save_article(
                article,
                force=True,
            )
        print(" ")


##
## === ENTRY POINT
##

if __name__ == "__main__":
    main()
    sys.exit(0)

## } MODULE
