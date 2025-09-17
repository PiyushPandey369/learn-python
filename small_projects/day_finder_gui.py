import tkinter as tk

import datetime

def day_finder():
 try:
    dd=int(txt1.get())
    mm=int(txt2.get())
    yy=int(txt3.get())
    date = datetime.date(yy, mm, dd)
    day_of_week = date.strftime("%A")
    lbl4.config(text=f"The day of the week for {dd}/{mm}/{yy} is: {day_of_week}")
 except Exception as e:
     lbl4.config(text="Invalid date! Please try again.")
root=tk.Tk()

root.geometry("800x800")
root.config(bg="gray")

lbl1=tk.Label(root,text="Enter the day(1-30): ",font=("Times New Roman",20),fg="red")
lbl1.place(x=50,y=40,width=250,height=50)

txt1=tk.Entry(root,font=("Times New Roman",20),fg="red")
txt1.place(x=310,y=40,width=50,height=50)

lbl2=tk.Label(root,text="Enter the month(1-12): ",font=("Times New Roman",20),fg="red")
lbl2.place(x=50,y=100,width=255,height=50)

txt2=tk.Entry(root,font=("Times New Roman",20),fg="red")
txt2.place(x=310,y=100,width=50,height=50)

lbl3=tk.Label(root,text="Enter the year: ",font=("Times New Roman",20),fg="red")
lbl3.place(x=50,y=160,width=255,height=50)

txt3=tk.Entry(root,font=("Times New Roman",20),fg="red")
txt3.place(x=310,y=160,width=70,height=50)

btn=tk.Button(root,text="Find Day",font=("Times New Roman",20),fg="green",bg="yellow",command=day_finder)
btn.place(x=70,y=220,width=200,height=50)

lbl4=tk.Label(root,font=("Times New Roman",20),fg="red")
lbl4.place(x=50,y=300,width=555,height=50)

root.mainloop()
