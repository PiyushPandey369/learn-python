import random
import time 


print("🎲Welcome To The Dice Roll Duel!")
time.sleep(2)
print("First To Reach 20 Points Wins👑 The Game\n")

p1_score = 0
p2_score = 0

def generate():
    return random.randint(1, 6)

def function1():
    score = 0
    for i in range(2):
        c = generate()
        print(f"Die {i+1}: {c}")
        # playsound("dice_roll.mp3") 
        score += c
    return score

round_num = 1

while p1_score < 20 and p2_score < 20:
    time.sleep(2)
    print(f"\n--- Round {round_num} ---")
    time.sleep(1)
    print("Player 1 Turn:")
    p1_turn_score = function1()
    p1_score += p1_turn_score
    print(f"Player 1 scored {p1_turn_score} this round. Total: {p1_score}")
    time.sleep(2)
    if p1_score >= 20:
        break

    print("Player 2 Turn:")
    p2_turn_score = function1()
    p2_score += p2_turn_score
    print(f"Player 2 scored {p2_turn_score} this round. Total: {p2_score}")

    round_num += 1

print("\n🎉 Game Over!")
time.sleep(2)
print(f"Final Scores:\nPlayer 1: {p1_score} | Player 2: {p2_score}")
time.sleep(1)
if p1_score >= 20 and p2_score >= 20:
    print("It's a tie!")
elif p1_score >= 20:
    print("🏆 Player 1 wins!")
else:
    print("🏆 Player 2 wins!")
