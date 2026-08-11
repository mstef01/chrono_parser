import json

from .key_builder import build_key

def build_url(season: str):
    """This function builds an URL for each event that is maintained in the "world_cups.json" file
    for each season. It returns a list of URLs that are used for the GET request to retrieve data accross categories
    and race types from ChronoRace API.
     The key part for the URL is retrieved from the "cat_mapping.json" mapping file. """

    filepath = f"config_files\\seasons\\{season}\\world_cups_{season}.json"
    season = season
    urls = []

    with open(filepath, "r") as world_cups_file:
        world_cups = json.load(world_cups_file)

    # get the necessary values from world_cups.json
        for i, world_cups in world_cups.items():
            for world_cup in world_cups:
                season = world_cup.get("season")
                event_id = world_cup.get("event_id")
                name = world_cup.get("name")
                round = world_cup.get("round")
                discipline = world_cup.get("discipline")

                # retrieve keys and iterate over key list to build the URL for each category and race type
                keys = build_key()
                for key in keys:
                    key = key
                    url = f"https://prod.chronorace.be/api/results/generic/uci/{event_id}/{discipline}?key={key}"
                    urls.append(url)

    return urls

if __name__ == "__main__":
    print(build_url())