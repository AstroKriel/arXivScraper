# arXivScraper

**arXivScraper** is a lightweight paper management tool designed to help you find, filter, and rank new arXiv papers based on your research interests. It offers flexible search and ranking criteria, as well as seamless integration with Obsidian. This project was the foundations from which [ChiScraper](https://github.com/ChiScraper/ChiScraper) added many useful extensions. `ChiScraper` has now surpassed `arXivScraper`, and I suggest you go check it out instead (see more details [here](https://chiscraper.github.io/)).

![Logo](./logo.jpg)

---

## Features

### 1. Find Papers

Define your paper search criteria in a JSON configuration file, specifying:
- Relevant arXiv categories to search
- Keywords or phrases and logical relationships for paper filtering
- Flexible criteria for creating paper groups or categories

Your custom JSON profile allows granular search definitions (see `./docs/json-profiles.pdf` for detailed examples). With a `./configs/settings.yaml` file, specify:
- The desired time frame to search
- Which JSON-configuration to use

To start a search, use:

```python main.py --search```

### 2. Fetch a Paper
Fetch a specific paper by its arXiv ID with the command:

```python main.py --fetch --download```

You’ll be prompted to enter the paper’s arXiv ID. The script will display the paper’s title, author list, and abstract for confirmation. Use `--download` (or `-d`) as an optional flag to download the PDF.

### 3. Rank Papers
Customise paper ranking with a personal profile (defined in ./configs/user_profile.txt) and get tailored ranking that suits your interests. This feature uses OpenAI’s GPT API, which requires token purchases. Initiate the ranking process via:

```python main.py --rank```

### 4. Read, Download, Remove (via Obsidian)
Using Obsidian for paper management, create a vault in the project folder (default settings provided). With Obsidian, you can:

- View and manage papers in your unread list
- Add papers to your "to-read" or "to-download" lists
- Filter out irrelevant papers from your lists

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
