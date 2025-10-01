import pandas as pd
import numpy as np

data = [[2, 'john@example.com'],[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    print(person)
    person.drop_duplicates(subset=['email'],inplace=True)
    print(person)
print(person)

delete_duplicate_emails(person)


