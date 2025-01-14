import numpy as np
import pandas as pd

def model(dbt, session):
    # dbt configuration
    dbt.config(packages=["pandas==1.5.3","numpy"])

    # get upstream data
    pit_stops_joined = dbt.ref("mrt_pit_stops").to_pandas()

    # provide year so we do not hardcode dates 
    year=2021

    # describe the data
    pit_stops_joined["PIT_STOP_SECONDS"] = pit_stops_joined["PIT_STOP_MILLISECONDS"]/1000
    fastest_pit_stops = pit_stops_joined[(pit_stops_joined["RACE_YEAR"]==year)].groupby(by="CONSTRUCTOR_NAME")["PIT_STOP_SECONDS"].describe().sort_values(by='mean')
    fastest_pit_stops.reset_index(inplace=True)
    fastest_pit_stops.columns = fastest_pit_stops.columns.str.upper()
    
    return fastest_pit_stops.round(2)