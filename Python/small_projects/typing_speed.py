import random
import time


def check_error(para_in,user_in):
    error=0
    # error_words=[]
    max_len=max(len(para_in),len(user_in))
    for i in range(max_len):
        if i<len(para_in) and i<len(user_in):
            if user_in[i]!=para_in[i]:
                error+=1
                # error_words.append(user_in[i])
        elif i<len(para_in):
            error+=1
            # error_words.append("_")
        else:
            error+=1
            # error_words.append("*")
    # accuracy=abs(1-error/len(user_in))*100
    return error
   
def speed_Calculate(time_e, time_s, user_in):
    time_taken = time_e - time_s  
    minutes = time_taken / 60
    if minutes == 0:  # avoid division by zero
        minutes = 1/60
    wpm = (len(user_in) / 5) / minutes
    return round(wpm)

   
list1=["A quick brown fox jumps over the lazy dog",
       "Crazy Fredericka bought many very exquisite opal jewels",
       "Heavy boxes perform quick waltzes and jump",
       "Pack my box with five red jugs"
       ]

print("----- Welcome to Typing Test -----")
time.sleep(2)
while True:
    test1=random.choice(list1)
    print(test1)
    time_1=time.time()
    test2=input("Enter: \n")
    time_2=time.time()
    no_of_error=check_error(test1,test2)
    speed=speed_Calculate(time_2,time_1,test2)
    print(f"Number of errors in texts: {no_of_error}")
    print(f"Typing Speed: {speed}w/min")
    ch=input("Do you want to test more ?(yes/no)").strip().lower()
    if ch=="no":
        break

print("-----   Thank You -----")