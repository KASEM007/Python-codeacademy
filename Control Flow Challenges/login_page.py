import tkinter as tk

# Data

# Functions

# GUI Set_up

root = tk.Tk()  # Capitalized methods are constructors

# Step 1: Creat a widget/object
frame = tk.Frame(root, padx=20, pady=20, bg="#4E4187")

lab1 = tk.Label(frame, text="Enter First Name:", bg="#4E4187")
lab2 = tk.Label(frame, text="Enter Last Name:", bg="#4E4187")
lab3 = tk.Label(frame, text="Enter Pass code:", bg="#4E4187")

text1 = tk.Text(
    frame, width=30, height=1, fg="#7DDE92", borderwidth=2, relief=tk.GROOVE
)
text2 = tk.Text(
    frame, width=30, height=1, fg="#7DDE92", borderwidth=2, relief=tk.GROOVE
)
text3 = tk.Text(
    frame, width=30, height=1, fg="#7DDE92", borderwidth=2, relief=tk.GROOVE
)

btn = tk.Button(frame, text="LOGIN")
# ADD ALL MY WIDGET TO MY FRAME


# step 2: configure

lab1.grid(row=0, column=0, stick="NESW")
lab2.grid(row=1, column=0)
lab3.grid(row=2, column=0)

text1.grid(row=0, column=1, columnspan=2)
text2.grid(row=1, column=1, columnspan=2)
text3.grid(row=2, column=1, columnspan=2)

btn.grid(row=3, column=1, sticky="NESW")

# STEP 3: Add to the window
frame.pack()


print("start")
root.mainloop()
print("end")
