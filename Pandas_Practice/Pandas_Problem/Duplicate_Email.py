import pandas as pd
import numpy as np

data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com'],[4, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    print(person)
    person=person[person[['email']].duplicated(keep=False)]
    print(person)
    person=pd.DataFrame(person['email'].unique(),columns=['Email'])
    print(person)
    return person.reset_index(drop=True)
  

print(duplicate_emails(person))