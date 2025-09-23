import tkinter as tk

def on_click():
    user = entry.get()
    label2.config(text=user)

root = tk.Tk()
root.title("First Program")
root.geometry("500x500")

# First label
label = tk.Label(root, text="Hello World", font=("Arial", 15), fg="blue", bg="yellow")
label.place(x=50, y=30, width=150, height=30)

# Second label (will show entry text)
label2 = tk.Label(root, text="", font=("Arial", 14))
label2.place(x=50, y=100, width=200, height=30)

# Entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.place(x=50, y=150, width=200, height=30)

# Button
button = tk.Button(root, text="Click here", font=("Arial", 14), command=on_click)
button.place(x=50, y=200, width=120, height=40)

root.mainloop()
