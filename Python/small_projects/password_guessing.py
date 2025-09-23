import random

easy_words=["tiger","human","person","eagle"]
medium_words=["someone","women","elephant","school"]
hard_words=["general","octopus","banker","prime"]
count=0

print("-----Password Guessing-----")
user_input=input("Enter the difficulty level to guess (easy,medium,hard): ").strip().lower()

if user_input=="hard":
    password=random.choice(hard_words)
elif user_input=="medium":
    password=random.choice(medium_words)
else:
    password=random.choice(easy_words)
    

while True:
    guess=input("Enter the guess: ")
    count+=1
    if guess==password:
        break 
    hint=""
    for i in range(len(password)):
            if i<len(guess) and guess[i]==password[i]:
                hint+=guess[i]
            else:
                hint+="_"
    print("Hint: ",hint)

print(f"You guessed {password} in {count} attempts")