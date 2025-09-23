import datetime
import time
# Ask the user to enter a date
start = time.perf_counter()  # Start the timer
day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year (e.g., 2025): "))

    # Create a date object
    # 
date = datetime.date(year, month, day)
z=time.time()
y=datetime.datetime.now()
    # Get the day of the week
day_of_week = date.strftime("%A")
x=date.strftime("%A,%d %B %Y")
print(x)
print(y)
print(z)
    # Display the result
print(f"The day of the week for {day}/{month}/{year} is: {day_of_week}")

end = time.perf_counter()  # Stop the timer
execution_time = end - start
print(f"The code took {execution_time:.2f} seconds to run")




