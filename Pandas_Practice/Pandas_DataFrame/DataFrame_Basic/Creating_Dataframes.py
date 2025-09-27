import pandas as pd
# using list
student_data=[
    [100,80,10],
    [120,90,15],
    [90,70,5],
    [80,65,3],
    [0,0,0],
    [0,0,0]
]
student1=pd.DataFrame(student_data,columns=['iq','marks','package'])
# print(student1)

# using dict
student_dict={
    'iq': [100,120,90],
    'marks':[89,79,67],
    'package':[12,8,4]
}
student2=pd.DataFrame(student_dict)
# print(student2)

ipl=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\ipl-matches.csv')
# print(ipl)

movie=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\example\learn-python\learn-python\Pandas_Practice\csv_file\movies.csv')
# print(movie)