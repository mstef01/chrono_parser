import json
import datetime

import pandas as pd

from data_extractor.url_builder import build_url
from data_extractor.response import get_data
from formatter.table_builder import build_rider_data

# build all URLs for the to make GET requests against ChronoRace API as defined in world_cups.json
urls = build_url()

# get all full race results for the events defined in world_cups.json and save as json in downloads folder
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
filename = "full_data_results_" + timestamp + ".json"
path = "data_json\\"

with open(path+filename, "w") as full_results:
    json.dump(get_data(urls), full_results, indent=2)
    print("Full race data written to full_data_results.json in the data_json subfolder.")

#build rider data from json data and save race results as csv
df = pd.DataFrame(build_rider_data(path+filename))
df.to_csv("data_csv\\race_data.csv")
print("Race results saved as race_data to data_csv")