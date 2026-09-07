```markdown
# ChronoParser

ChronoParser is a Python tool for fetching UCI Downhill World Cup data from the ChronoRace API,
saving the raw timing data as semi-structured JSON output as well as generating structured CSV output
on a seasonal, per-World Cup level. It supports World Cup timing data from the 2025 DHI World Cup
season onwards (Timed Training, Q1, Q1 and Finals).

## Features

- Requests race results data from ChronoRace API on
  a seasonal as well as a per-world cup level
- Builds semi-structured (JSON) and structured data output (CSV)
  across World Cups and seasons (2025 onwards)

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
