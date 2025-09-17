import random

def select_random():
    return random.choice([-1, 0, 1])

player_score = 0
computer_score = 0
draw_point = 0

# Initial player input
p = input("1)Scissor\n2)Paper\n3)Rock\nEnter your call (s or S,r or R,p or P) (q to quit the game): ").lower()

while p != 'q':
    you_dict = {"s": -1, "p": 1, "r": 0}
    r_dict = {-1: "Scissor", 1: "Paper", 0: "Rock"}

    # Check for valid input first
    if p not in you_dict:
        print("Invalid input! Please choose 's', 'p', or 'r'.")
        p = input("Enter your call (q to quit the game): ").lower()
        continue  # Skip the rest of the loop if input is invalid

    # Proceed with the game logic if the input is valid
    player = you_dict[p]
    computer = select_random()
    print(f"Your choice is {r_dict[player]}\nComputer choice is {r_dict[computer]}")

    if computer == player:
        print("It's a draw.")
        draw_point += 1
    else:
        if (computer - player == -1) or (computer - player == 2):
            print("You Win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

    # Display current score
    print(f"Score -> Player: {player_score} | Computer: {computer_score} | Draw: {draw_point}")

    # Ask for the next input
    p = input("\n1)Scissor\n2)Paper\n3)Rock\nEnter your call (s,r,p) (q to quit the game): ").lower()

# Final score display
print("\nGame Over!")
print(f"Final Score -> Player: {player_score} | Computer: {computer_score} | Draw: {draw_point}")
if player_score == computer_score:
    print("It's a Draw!")
elif player_score > computer_score:
    print("You won the match!")
else:
    print("Computer won the match!")
