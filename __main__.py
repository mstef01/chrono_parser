import json
import datetime

import pandas as pd

from data_extractor.url_builder import build_url
from data_extractor.response import get_data
from formatter.table_builder import build_rider_data

# build all URLs for the to make GET requests against ChronoRace API as defined in world_cups.json
season = input("Enter the season (e.g. 2026): ")
urls = build_url(season)

# get all full race results for the events defined in world_cups.json and save as json in downloads folder
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
filename = "full_data_results_"+ season + "_" + timestamp + ".json"
path = f"data_json\\{season}\\"
filepath = path + filename

with open(filepath, "w") as full_results:
    json.dump(get_data(urls), full_results, indent=2)
    print("Full race data written to full_data_results.json in the data_json subfolder.")

#build rider data from json data and save race results as csv
df = pd.DataFrame(build_rider_data(filepath))
df.to_csv(f"data_csv\\{season}\\race_data_{season}.csv")
print(f"\nRace results saved as race_data_{season}.csv to data_csv\\{season} subfolder.")