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