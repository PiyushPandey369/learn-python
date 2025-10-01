import pandas as pd
import numpy as np


data = [[1, '2015-01-05', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30],[5, '2015-01-01', 25]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})


    

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate',inplace=True)
    print(weather)
    return weather[ (weather['temperature'].diff() > 0)  & (weather['recordDate'].diff().dt.days == 1)][['id']]

print(weather)
print(rising_temperature(weather))