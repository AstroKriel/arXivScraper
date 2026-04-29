# arXivScraper

**arxivscraper** is a lightweight paper management tool for finding, filtering, and triaging arXiv papers.

![Logo](./logo.jpg)

---

## Workflow

### 1. Search

Search arXiv for papers matching a search profile:

```bash
uv run python main.py --search --config_name <profile> --lookback_days <n>
```

Papers are saved as markdown files in `md_files/`. If `--config_name` or `--lookback_days` are not passed, the script will prompt for them.

### 2. Browse

Open the TUI browser to read abstracts and triage saved papers:

```bash
uv run python main.py --browse
```

| Key | State |
|---|---|
| `p` | pending (default) |
| `q` | queued (marked to read) |
| `r` | read |
| `d` | mark for download |
| `D` | action downloads |
| `n` | n/a (not relevant) |
| `x` | mark for deletion |
| `X` | action deletions |
| `o` | open PDF in browser |
| `f` | cycle filter between `p`, `q`, `r`, `d`, `n`, and `x` statuses |
| `escape` | quit |

### 3. Score

Score all unrated papers using an AI provider:

```bash
uv run python -m arxivscraper.routines.score_articles
```

Pass `--model <model>` or `--base-url <url>` to override the values in `configs/ai_provider.toml`.

### 4. Fetch

Fetch a specific paper by arXiv ID:

```bash
uv run python main.py --fetch -id <arxiv-id>
```

The script displays the title, authors, and abstract for confirmation before saving.

### 5. Download

From the TUI browser, press `d` to mark a paper for download. Use `f` to cycle the filter to `download` to review which papers are queued before pressing `D` to action the download. Downloaded papers return them back to a `pending` (`p`) state.

Alternatively, you can also run the download step directly from the terminal:

```bash
uv run python main.py --download
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<username>/arXivScraper.git
cd arXivScraper
```

2. Install dependencies:

```bash
uv sync
```

---

## Configuration

| File | Purpose |
|---|---|
| `configs/<profile>.toml` | search criteria for one topic |
| `configs/ai_provider.toml` | AI provider settings (model, API key, base URL) |
| `configs/user_profile.txt` | scoring criteria sent to the AI |
| `configs/ai_guidelines.txt` | system prompt rules for AI scoring |

### Search profiles

Each `.toml` file in `configs/` defines one search profile. Pass the filename without extension as `--config_name`.

```toml
authors = []
categories = ["<arxiv-category>"]
keywords_to_exclude = []
keywords_to_include = ["<keyword>", ...]
```

Keywords use a nested list notation where the operator alternates every level: OR at even depth, AND at odd depth.

| Depth | Operator |
|---|---|
| 0 (top-level) | OR |
| 1 (nested) | AND |
| 2 (doubly-nested) | OR |
| ... | ... |

```toml
keywords_to_include = [
    "<keyword-a>",
    ["<keyword-b>", ["<keyword-c>", "<keyword-d>"]],
]
```

Matches: `<keyword-a>` OR (`<keyword-b>` AND (`<keyword-c>` OR `<keyword-d>`))

See `tests/test_filter.py` for examples in action.

### AI provider

Copy `configs/ai_provider.example.toml` to `configs/ai_provider.toml` and fill in your values. Supports OpenAI, Anthropic, Ollama, and any OpenAI-compatible API.

---

## License

This project is licensed under the MIT License; see [LICENSE](./LICENSE.md) for details.
