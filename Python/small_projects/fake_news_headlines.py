import random

subjects=[
        "Gautam",
        "KP",
        "Arzu Rana",
        "Sher Bahadur",
        "Paras",
        "Subash",
        "Balen Shah",
        "Deepak",
        "Maoist",
        "Janata Party"
         ]

actions=[
        "makes a promise",
        "dances in Parliament",
        "plays football badly",
        "steals mic",
        "forget speech",
        "cries on TV",
        "tweets angrily",
        "runs for PM",
        "admits mistake",
        "blames someone else"
        ]

objectives=[
           "to Kathmandu",
            "for votes",
            "in the election",
            "with democracy",
            "for free food",
            "on live TV",
            "to win the match",
            "against corruption",
            "with a cricket bat",
            "in front of the camera"
           ]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    objective=random.choice(objectives)
    
    heading="----Breaking News----"
    headlines=f"{subject} {action} {objective}"
    print(headlines)
    
    choices=input("Do you want to listen more news (yes/no)").strip().lower()
    
    if choices=="no":
        break

print("---Thank You---")