# arXivScraper

**arXivScraper** is a lightweight paper management tool designed to help you find, filter, and rank new arXiv papers based on your research interests. It offers flexible search and ranking criteria, as well as seamless integration with Obsidian. This project was the foundations from which [ChiScraper](https://github.com/ChiScraper/ChiScraper) added many useful extensions. `ChiScraper` has now surpassed `arXivScraper`, and I suggest you go check it out instead (see more details [here](https://chiscraper.github.io/)).

![Logo](./logo.jpg)

---

## Features

### 1. Find Papers

`arXivScraper` allows you to create different topics or research categories, where you can calibrate each category's filtering criteria to find you the papers you care about. You can define
- Relevant arXiv categories to search
- Keywords or phrases to filter by, as well as logical relationships between these words/phrases
See `./docs/search-profiles.md` for examples.

To start a search, use:

```python main.py --search```

You will be promted to pass the config-name of the research category (`.json` file containing the filtering criatera) you want to search for.

### 2. Fetch a Paper
Fetch a specific paper by passing its arXiv ID:

```python main.py --fetch --download```

You’ll be prompted to enter the paper’s arXiv ID. The script will display the paper’s title, author list, and abstract for confirmation. Use `--download` (or `-d`) as an optional flag to download the PDF.

### 3. Rank Papers
Customise paper ranking with a personal profile (defined in `./configs/user_profile.txt`) and get a tailored ranking that suits your interests. This feature uses OpenAI’s GPT API, which requires you to purchace access tokens. See `./docs/ai-ranking.md` for details on how to set this up. Once you've done so, initiate the ranking process via:

```python main.py --rank```

### 4. Read, Download, Remove (via Obsidian)
You can use Obsidian to manage your papers, and interface with `arXivScraper`. Create a vault in the project folder (I have provided default settings under `.Obsidian`).

With Obsidian, you can:
- View, manage, and filter papers based on your research categories, or their published/updated dates
- Add papers to your "to-read" or "to-download" lists

## Installation

To get started, clone the repository and install the dependencies.

```
git clone https://github.com/yourusername/git
cd arXivScraper
pip install -r requirements.txt
```

## Usage Summary

1. Search for new papers: ```python main.py --search```
2. Fetch a specific paper: ```python main.py --fetch```
3. Rank papers: ```python main.py --rank```
4. Download papers with "to-download" status: ```python main.py --download```

You can also string together `--search` (or `-s`) along with other commands (e.g., `-r` or `-p`). You can also download (`-d`) the paper you have fetched (`-f`).

## Configuration files

- Runtime settings: Customise runtime settings in `./configs/settings.yaml`

- JSON Profile Configurations: Define search criteria in JSON files located in `./configs/*.json`

- User Profile (for AI-ranking): Define a ranking profile in `./configs/user_profile.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
