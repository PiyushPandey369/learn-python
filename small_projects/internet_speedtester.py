import speedtest 
import tkinter as tk

def check_speed():
    sp=speedtest.Speedtest()
    best_server=sp.get_best_server()
    download_speed=str(round(sp.download(),3)/(10**6))+"Mbps"
    lb3.config(text=download_speed)
    upload_speed=str(round(sp.upload(),3)/(10**6))+"Mbps"
    lb5.config(text=upload_speed)
    print(best_server)
    
root=tk.Tk()

root.geometry("800x800")
root.config(bg="gray")

lb1=tk.Label(root,text="Internet Speed Tester",font=("Times New Roman",40,"bold"),fg="blue")
lb1.place(x=0,y=40,width=800,height=50)

lb2=tk.Label(root,text="Downloading Speed",font=("Times New Roman",30,"bold"),fg="blue")
lb2.place(x=160,y=130,width=400,height=50)

lb3=tk.Label(root,font=("Times New Roman",30,"bold"),fg="blue")
lb3.place(x=160,y=200,width=400,height=50)

lb4=tk.Label(root,text="Uploading Speed",font=("Times New Roman",30,"bold"),fg="blue")
lb4.place(x=160,y=300,width=400,height=50)

lb5=tk.Label(root,font=("Times New Roman",30,"bold"),fg="blue")
lb5.place(x=160,y=370,width=400,height=50)

btn=tk.Button(root,text="Check Speed",font=("Times New Roman",35,"bold"),fg="red",command=check_speed)
btn.place(x=200,y=450,width=300,height=50)

root.mainloop()
