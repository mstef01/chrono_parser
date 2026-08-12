import json

def build_key():

    """This functions builds a list of keys from cat_mapping.json.
    These keys are used in the API GET request to retrieve race data
    according to each category and race type, e.g. Men's Q1 corresponds
    to a key value of "2"."""

    keys = []

    with open("config_files\\cat_map.json", "r") as cat_mapping_file:
        mapping = json.load(cat_mapping_file)

        for category, categories in mapping.items():
            for key in categories:
                key = categories.get(key)
                keys.append(key)

    return keys
