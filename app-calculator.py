import tkinter as tk
from tkinter import messagebox
import math

# Function to append number or operation to the input box
def append_to_input(char):
    entry_input.insert(tk.END, char)

# Function to clear input box
def clear_input():
    entry_input.delete(0, tk.END)

# Function to delete the last character from input box
def backspace():
    entry_input.delete(len(entry_input.get())-1, tk.END)

# Function to calculate result
def calculate():
    try:
        input_text = entry_input.get()
        
        # Evaluate the expression
        result = eval(input_text)
        
        # Display result
        entry_input.delete(0, tk.END)
        entry_input.insert(tk.END, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except Exception:
        messagebox.showerror("Error", "Invalid input. Please enter a valid expression.")

# Create main window
root = tk.Tk()
root.title("Enhanced Calculator")

# Configure window size and background color
root.geometry("500x600")
root.configure(bg="#FFFED3")  # Light blue background

# Create a frame for the calculator display and buttons
frame_display = tk.Frame(root, bg="#4C3BCF", padx=10, pady=10, bd=5, relief=tk.RIDGE)
frame_display.pack(padx=20, pady=20)

# Entry for input
entry_input = tk.Entry(frame_display, font=('Arial', 18), justify="right", bg="#ffffff", fg="#000000")
entry_input.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="ew")

# Number buttons
btn_7 = tk.Button(frame_display, text="7", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("7"))
btn_7.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

btn_8 = tk.Button(frame_display, text="8", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("8"))
btn_8.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

btn_9 = tk.Button(frame_display, text="9", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("9"))
btn_9.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

btn_4 = tk.Button(frame_display, text="4", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("4"))
btn_4.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

btn_5 = tk.Button(frame_display, text="5", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("5"))
btn_5.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

btn_6 = tk.Button(frame_display, text="6", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("6"))
btn_6.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

btn_1 = tk.Button(frame_display, text="1", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("1"))
btn_1.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

btn_2 = tk.Button(frame_display, text="2", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("2"))
btn_2.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

btn_3 = tk.Button(frame_display, text="3", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("3"))
btn_3.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

btn_0 = tk.Button(frame_display, text="0", font=('Arial', 14), fg="#ffffff", bg="#000000", relief=tk.RAISED, command=lambda: append_to_input("0"))
btn_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Operation buttons
btn_add = tk.Button(frame_display, text="+", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("+"))
btn_add.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

btn_subtract = tk.Button(frame_display, text="-", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("-"))
btn_subtract.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

btn_multiply = tk.Button(frame_display, text="*", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("*"))
btn_multiply.grid(row=3, column=3, padx=5, pady=5, sticky="ew")

btn_divide = tk.Button(frame_display, text="/", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("/"))
btn_divide.grid(row=4, column=3, padx=5, pady=5, sticky="ew")

btn_decimal = tk.Button(frame_display, text=".", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("."))
btn_decimal.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

btn_open_paren = tk.Button(frame_display, text="(", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("("))
btn_open_paren.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

btn_close_paren = tk.Button(frame_display, text=")", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input(")"))
btn_close_paren.grid(row=5, column=2, padx=5, pady=5, sticky="ew")

btn_sqrt = tk.Button(frame_display, text="√", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("math.sqrt("))
btn_sqrt.grid(row=4, column=4, padx=5, pady=5, sticky="ew")

btn_exp = tk.Button(frame_display, text="^", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("**"))
btn_exp.grid(row=3, column=4, padx=5, pady=5, sticky="ew")

btn_percent = tk.Button(frame_display, text="%", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=lambda: append_to_input("/100"))
btn_percent.grid(row=2, column=4, padx=5, pady=5, sticky="ew")

btn_backspace = tk.Button(frame_display, text="←", font=('Arial', 14), fg="#ffffff", bg="#ff6666", relief=tk.RAISED, command=backspace)
btn_backspace.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

# Clear button
btn_clear = tk.Button(frame_display, text="C", font=('Arial', 14), fg="#ffffff", bg="#FFCAD4", relief=tk.RAISED, command=clear_input)
btn_clear.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# Equal button
btn_equal = tk.Button(frame_display, text="=", font=('Arial', 18), fg="#ffffff", bg="#FCDC2A", relief=tk.RAISED, command=calculate)
btn_equal.grid(row=5, column=3, columnspan=2, padx=5, pady=5, sticky="ew")

# Start the GUI main loop
root.mainloop()
