'''
    Given a dictionary of student names and marks:

    students = {"A": 85, "B": 90, "C": 78, "D": 92}

    Find the student with the highest marks
    
    Print all students who scored more than 80

'''

students = {"A": 85, "B": 90, "C": 78, "D": 92}
max_marks=0
name=""

for key,value in students.items():
    if(value>max_marks):
        max_marks=value
        name=key    
print(name,max_marks)