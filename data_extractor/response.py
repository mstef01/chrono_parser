import json

import requests
from progress.bar import ChargingBar

from .url_builder import build_url

def get_data(urls: list):
    """This function retrieves the GET response from ChronoRace API to fetch all DHI results from a list of URLs.
     Returns a list of race data JSON objects as a python list of dictionaries. """

    full_data = []
    bar = ChargingBar("Fetching race data:", max=len(urls), suffix="%(percent)d%%")    
    for url in urls:
        url = url

        headers = {
        "Referer": "https://prod.chronorace.be/angular/results.html",
        "Accept": "application/json"
        }

        race_data = requests.get(url, headers=headers).json()
        if race_data is not None:
            full_data.append(race_data)
        else: print(f"No race data found for: {url}")
        bar.next()
    bar.finish()
    return full_data

if __name__ == "__main__":

    urls = ['https://prod.chronorace.be/api/results/generic/uci/20260528_mtb/dh?key=91', "https://prod.chronorace.be/api/results/generic/uci/20260528_mtb/dh?key=6"]
    # typ = json.dumps(get_data((urls)), indent=2)
    # print(type(typ))

    # urls = build_url()
    # print(type(get_data(urls)))
    # print(get_data(urls))

    with open("data_json\\full_data_results.json", "w") as full_results:
        json.dump(get_data(urls), full_results, indent=2)
        print("Full race data written to full_data_results.json in the downloads subfolder.")
