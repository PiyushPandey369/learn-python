import pandas as pd
import numpy as np

# --------------------------------------------------
# Load COVID-19 global deaths and confirmed cases data
# --------------------------------------------------
death = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\time_series_covid19_deaths_global.csv"
)
confrim = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\time_series_covid19_confirmed_global.csv"
)

# --------------------------------------------------
# Reshape (melt) the deaths DataFrame
#   - Keep Province/State, Country/Region, Lat, Long fixed
#   - Convert all date columns into rows (long format)
#   - Rename melted columns as 'Date' and 'no_of_deaths'
# --------------------------------------------------
death = death.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    var_name='Date',
    value_name='no_of_deaths'
)
print("Melted deaths DataFrame:\n", death.head())


# --------------------------------------------------
# Reshape (melt) the confirmed cases DataFrame
#   - Same logic as deaths
#   - Rename melted values as 'no_of_cases'
# --------------------------------------------------
confrim = confrim.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
    var_name='Date',
    value_name='no_of_cases'
)
print("\nMelted confirmed cases DataFrame:\n", confrim.head())


# --------------------------------------------------
# Merge deaths & confirmed cases on common columns
#   - Merge using Province/State, Country/Region, Lat, Long, Date
#   - Keep only Country/Region, Date, no_of_deaths, no_of_cases
# --------------------------------------------------
data = death.merge(
    confrim,
    on=['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']
)[['Country/Region', 'Date', 'no_of_deaths', 'no_of_cases']]

print("\nMerged Data (Country, Date, Deaths, Cases):\n", data.head())
