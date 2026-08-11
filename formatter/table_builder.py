import json

import pandas as pd
from progress.bar import ChargingBar

from formatter.utils import get_timing_id


def build_rider_data(filepath: str):
    """This function builds a row of rider data for each rider in an event from
    the json file passed in the argument. It appends every row of rider data
    to a list of dictionaries."""

    rider_data = []
    row_data = {}
    timing_data = {}

    bar = ChargingBar("Building rider data from json:", suffix="%(percent)d%%")

    with open(filepath, "r") as json_file:
        json_data = json.load(json_file)

    for index in range(len(json_data)):  
        # grab the rider data from this timing event (e.g. Timed Training) within a context
        for rider in json_data[index]["Riders"]:
            row_data.clear() # we have to clear row_data before writing new rider values

            row_data.update({"ContextName": json_data[index]["ContextName"]})
            row_data.update({"DisplayName": json_data[index]["DisplayName"]})  
            row_data.update(json_data[index]["Riders"][rider])

            # we need to build a 4-digit "timing_id" consisting of a category prefix and the RaceNr 
            # to use it as a key to access the timing data for each rider when Context is not a timed training
            row_data.update({"timing_id": get_timing_id(row_data["RaceNr"], row_data["CategoryCode"])})
            bar.next()
            # now we need to grab the timing data for this rider's RaceNr in this timing event
            # with "timing_id" as key
            for result in range(len(json_data[index]["Results"])):
                if row_data["timing_id"] == json_data[index]["Results"][result]["RaceNr"]:

                    # get status
                    row_data.update({"Status": json_data[index]["Results"][result]["Status"]})
                    # get speed on track
                    row_data.update({"Speed": json_data[index]["Results"][result]["Speed"]})

                    timing_data.clear() # clear timing data before writing new values
                    # create timing data per sector for each rider
                    if row_data["Status"] == "Finished" or row_data["Status"] == "DNF": 
                        try:
                            for sector in range(len(json_data[index]["Results"][result]["Times"])):
                                if isinstance(json_data[index]["Results"][result]["Times"][sector], dict):
                                        timing_data.update({f"Sector{sector+1}_RaceTime": json_data[index]["Results"][result]["Times"][sector]["RaceTime"]
                                                        ,f"Sector{sector+1}_TimeGap": json_data[index]["Results"][result]["Times"][sector]["TimeGap"]
                                                        ,f"Sector{sector+1}_Position": json_data[index]["Results"][result]["Times"][sector]["Position"]
                                                        })
                        except: pass
                            # row_data.update(timing_data)
                            # rider_data.append(row_data.copy())  
                        # add timing_data to row_data and append full row to rider_data
                        row_data.update(timing_data)
                        rider_data.append(row_data.copy())              
                        # row_data.clear()
                    elif row_data["Status"] == "DNS":
                        # save complete row in rider_data
                        rider_data.append(row_data.copy())

                    else: 
                        timing_data.update({f"Sector{sector+1}_RaceTime": None
                                            ,f"Sector{sector+1}_TimeGap": None
                                            ,f"Sector{sector+1}_Position": None
                                            })
                        row_data.update(timing_data)
                        rider_data.append(row_data.copy())
    bar.finish
    return rider_data

if __name__ == "__main__":

    path = "data_json\\full_data_results_2026-08-10_13-35-12.json"
    # build_rider_data(path)
    df = pd.DataFrame(build_rider_data(path))
    # df.to_csv("output.csv")
    # dnfs = df.loc[df["Status"] == "DNF", ["ContextName", "DisplayName", "PrintName", "Status", "Sector1_RaceTime", "Sector2_RaceTime", "Sector5_RaceTime"]]
    # dns = df.loc[df["Status"] == "DNS", ["ContextName", "DisplayName", "PrintName", "Status", "Sector1_RaceTime", "Sector2_RaceTime", "Sector5_RaceTime"]]
    dns_or_dnf = df.loc[(df["Status"] == "DNS") | (df["Status"] == "DNF"), ["ContextName", "DisplayName", "PrintName", "Status"]]
    print(dns_or_dnf.sort_values(by=["ContextName", "DisplayName", "Status"]))
    # print(f"{len(dnfs.index)} riders did not finish.")
    # print(f"{len(dns.index)} riders did not start.")

    pass