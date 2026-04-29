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

| Key | Action |
|---|---|
| `u` | unseen |
| `2` | 2read |
| `r` | read |
| `d` | download |
| `n` | no |
| `x` | mark for deletion |
| `X` | apply deletions |
| `o` | open PDF in browser |
| `f` | cycle status filter |
| `q` | quit |

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

Download PDFs for all papers with status `d` (to-download):

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

Each `.json` file in `configs/` defines one search profile. Pass the filename without extension as `--config_name`.

```toml
authors = []
categories = ["<arxiv-category>"]
keywords_to_exclude = []
keywords_to_include = ["<keyword>"]
```

### AI provider

Copy `configs/ai_provider.example.toml` to `configs/ai_provider.toml` and fill in your values. Supports OpenAI, Anthropic, Ollama, and any OpenAI-compatible API.

---

## License

This project is licensed under the MIT License; see [LICENSE](./LICENSE.md) for details.
