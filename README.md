```markdown
# ChronoParser

ChronoParser is a Python tool for fetching downhill race results from the ChronoRace API,
saving the raw race data as JSON, and generating rider-level CSV output.

## Features

- Builds ChronoRace API URLs from season configuration files
- Fetches race event results across categories and race types
- Saves raw JSON output to `data_json/<season>/`
- Converts results into per-rider CSV files in `data_csv/<season>/`

## Requirements

- Python 3.x
- Dependencies in `requirements.txt`

## Installation

1. Clone or copy the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the repository from the project root:

```bash
python __main__.py
```

When prompted, enter the season year:

```text
Enter the season (e.g. 2026):
```

Outputs:
- Raw JSON saved to `data_json/<season>/full_data_results_<season>_<timestamp>.json`
- CSV saved to `data_csv/<season>/race_data_<season>.csv`

## Project Structure

- __main__.py
  - Main entry point
  - Builds URLs, retrieves race data, and writes JSON/CSV output

- data_extractor
  - url_builder.py — reads `config_files/seasons/<season>/world_cups_<season>.json` and builds API URLs
  - key_builder.py — reads cat_map.json to collect ChronoRace keys
  - response.py — fetches race data from the ChronoRace API

- formatter
  - table_builder.py — parses JSON data into rider rows and timing fields
  - utils.py — generates `timing_id` values for matching timing results

- config_files
  - `cat_map.json` — category mapping for API key construction
  - `seasons/<year>/world_cups_<year>.json` — event definitions for each season

- data_json
  - Generated raw JSON output

- data_csv
  - Generated CSV output

## Notes

- The project currently uses Windows-style paths in code.
- Ensure season config files exist under `config_files/seasons/<year>/`.
- utils.py contains the timing ID logic used to align rider results with timing rows.
