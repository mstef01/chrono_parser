import json

from .key_builder import build_key

def build_world_cup_data(season: str):
    """This function builds a dictionary object containing URLs and additional information for
    each event that is maintained in the "world_cups.json" file for each season.
    It returns a list of dictionaries that are used for the GET request to retrieve data accross categories
    and race types from ChronoRace API. The key part for the URL is retrieved from
    the "cat_mapping.json" mapping file. """

    filepath = f"config_files\\seasons\\{season}\\world_cups_{season}.json"
    season = season
    wc_data_tbl = []
    wc_data_row = {}

    with open(filepath, "r") as world_cups_file:
        world_cups = json.load(world_cups_file)

    # get the necessary values from world_cups.json
        for i, world_cups in world_cups.items():
            for world_cup in world_cups:
                wc_data_row.clear() # clear wc_data before writing new values
                wc_data_row.update({
                    "season": world_cup.get("season"),
                    "event_id": world_cup.get("event_id"),
                    "venue": world_cup.get("venue"),
                    "round": world_cup.get("round"),
                    "discipline": world_cup.get("discipline")
                })

                # retrieve keys and iterate over key list to build the URL for each category and race type
                keys = build_key()
                for key in keys:
                    key = key
                    wc_data_row.update({"url": f"https://prod.chronorace.be/api/results/generic/uci/{wc_data_row['event_id']}/{wc_data_row['discipline']}?key={key}"})
                    wc_data_tbl.append(wc_data_row.copy())

    return wc_data_tbl