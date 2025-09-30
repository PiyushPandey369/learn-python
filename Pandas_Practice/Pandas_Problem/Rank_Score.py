import pandas as pd
data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})



def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    print(scores)
    scores['rank']=scores['score'].rank(method="dense",ascending=False)
    print(scores.sort_values('rank',inplace=True))
    scores=scores.drop(columns='id').reset_index(drop=True)
    return scores
    
print(order_scores(scores))