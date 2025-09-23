'''
    Write a Python program that creates a file called numbers.txt 
    and writes numbers from 1 to 20, one per line.

'''

with open("numbers.txt","w") as f:
   for i in range(1,21):
       f.write(str(i))
       f.write("\n")