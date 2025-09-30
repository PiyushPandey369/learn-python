import pandas as pd

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})

print(activity)
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    frame = activity.groupby('player_id', as_index=False)['event_date'].min()
    print(frame)
    # Format the date as YYYY-MM-DD
    frame['first_login'] = frame['event_date'].dt.strftime('%Y-%m-%d')
    print(frame)
    # Drop the original event_date column
    frame = frame.drop(columns='event_date')
    print(frame)
    # Sort by player_id
    frame = frame.sort_values('player_id').reset_index(drop=True)
    return frame
    
print(game_analysis(activity))