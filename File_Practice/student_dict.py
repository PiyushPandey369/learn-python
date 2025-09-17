'''
    Write a program that reads students.txt (each line has a name and marks, e.g. "Alice 85") and prints:

    Student with the highest marks

    All students who scored more than 80
    
'''
with open("students.txt") as f:
    data=f.readlines()

dict={}

for line in data:
    name, marks = line.strip().split()   
    dict[name] = int(marks)    
max=0
name1=""
for n,m in dict.items():
    if(m>max):
        max=m
        name1=n
    if(m>=80):
        print(n,m)

print(f"Highest marks by: {name1} , Marks: {max}")

    
    
