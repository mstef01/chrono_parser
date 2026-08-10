def get_timing_id(race_nr: int, category: str):
    """This function returns a 4-digit timing_id derived from the RaceNr and the category. 
    Category prefixes: men: 10, women: 20, mj: 30, wj: 40
    Categories: ME, WE, MJ, WJ"""
    race_nr = str(race_nr)
    timing_id = 0

    if len(race_nr) == 4:           # race_nr comes from timed training
        timing_id = race_nr
    elif len(race_nr) == 1 and category == "ME":
        timing_id = "100" + race_nr
    elif len(race_nr) == 1 and category == "WE":
        timing_id = "200" + race_nr
    elif len(race_nr) == 1 and category == "MJ":
        timing_id = "300" + race_nr
    elif len(race_nr) == 1 and category == "WJ":
        timing_id = "400" + race_nr 
    elif len(race_nr) == 2 and category == "ME":
        timing_id = "10" + race_nr
    elif len(race_nr) == 2 and category == "WE":
        timing_id = "20" + race_nr
    elif len(race_nr) == 2 and category == "MJ":
        timing_id = "30" + race_nr
    elif len(race_nr) == 2 and category == "WJ":
        timing_id = "40" + race_nr 
    elif len(race_nr) == 3 and category == "ME":
        timing_id = "1" + race_nr
    elif len(race_nr) == 3 and category == "WE":
        timing_id = "2" + race_nr
    elif len(race_nr) == 3 and category == "MJ":
        timing_id = "3" + race_nr
    elif len(race_nr) == 3 and category == "WJ":
        timing_id = "4" + race_nr 

    return int(timing_id)

if __name__ == "__main__":
    print(get_timing_id(31, "WE"))
    pass