from tkinter import *

# Create the main window
win = Tk()
win.title("Arithmetic Calculator")
win.geometry('400x400')
win.configure(bg="#FF8DAA")  # Change background color

# Define font style
font_style = ("Helvetica", 12)

def calculate():
    try:
        num1 = float(ent1.get())
        num2 = float(ent2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
    
    operation = oper_var.get()
    
    if operation == "+":
        res = num1 + num2
    elif operation == "-":
        res = num1 - num2
    elif operation == "*":
        res = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result.config(text="Cannot divide by zero.")
            return
        res= num1 / num2
    elif operation == "%":
        res = num1 % num2
    elif operation == "**":
        res = num1 ** num2
    else:
        res.config(text="Please select an operation.")
        return
    
    result.config(text=f"Result: {res}")

# First number label and entry
label1 = Label(win, text="Number 1:", bg="#1E90FF", font=font_style)
label1.grid(row=0, column=0, padx=10, pady=5)

ent1 = Entry(win, font=font_style)
ent1.grid(row=0, column=1, padx=10, pady=5)

# Second number label and entry
label2 = Label(win, text="Number 2:", bg="#1E90FF", font=font_style)
label2.grid(row=1, column=0, padx=10, pady=5)

ent2 = Entry(win, font=font_style)
ent2.grid(row=1, column=1, padx=10, pady=5)

# Operation label and radio buttons
oper_var = StringVar()
oper_var.set("+")

label3 = Label(win, text="Operation:", bg="#1E90FF", font=font_style)
label3.grid(row=2, column=0, padx=10, pady=5)

oper_frame = Frame(win, bg="#e0f7fa")
oper_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add = Radiobutton(oper_frame, text="+", variable=oper_var, value="+", bg="#e0f7fa", font=font_style)
radio_add.pack(side=LEFT)

radio_subtract = Radiobutton(oper_frame, text="-", variable=oper_var, value="-", bg="#e0f7fa", font=font_style)
radio_subtract.pack(side=LEFT)

radio_multiply = Radiobutton(oper_frame, text="*", variable=oper_var, value="*", bg="#e0f7fa", font=font_style)
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(oper_frame, text="/", variable=oper_var, value="/", bg="#e0f7fa", font=font_style)
radio_divide.pack(side=LEFT)

radio_modulus = Radiobutton(oper_frame, text="%", variable=oper_var, value="%", bg="#e0f7fa", font=font_style)
radio_modulus.pack(side=LEFT)

radio_exponent = Radiobutton(oper_frame, text="**", variable=oper_var, value="**", bg="#e0f7fa", font=font_style)
radio_exponent.pack(side=LEFT)

# Submit button
submit_button = Button(win, text="Calculate", command=calculate, bg="#800080", fg="white", font=font_style)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to show the result
result = Label(win, text="Result: ", bg="#e0f7fa", font=font_style)
result.grid(row=4, column=0, columnspan=2, pady=5)

win.mainloop()
