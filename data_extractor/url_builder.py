import json

from .key_builder import build_key

def build_url():
    """This function builds an URL for each event that is maintained in the "world_cups.json" file.
    It returns a list of URLs that are used for the GET request to retrieve data accross categories
    and race types from ChronoRace API.
     The key part for the URL is retrieved from the "cat_mapping.json" mapping file. """

    urls = []

    with open(r"config_files\world_cups.json", "r") as events_file:
        events = json.load(events_file)

    # get the necessary values from world_cups.json
    for i,events in events.items():
        for event in events:
            season = event.get("season")
            event_id = event.get("event_id")
            name = event.get("name")            
            round = event.get("round")
            discipline = event.get("discipline")

            # retrieve keys and iterate over key list to build the URL for each category and race type
            keys = build_key()
            for key in keys:
                key = key
                url = f"https://prod.chronorace.be/api/results/generic/uci/{event_id}/{discipline}?key={key}"
                urls.append(url)

    return urls

if __name__ == "__main__":
    print(build_url())