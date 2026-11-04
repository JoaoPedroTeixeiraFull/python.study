import tkinter as tk

# Function to update the display text when buttons are clicked
def press_button(num):
    current_content = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_content + str(num))

# Function to clear the display (C button)
def clear_display():
    display.delete(0, tk.END)

# Function to calculate the final result (= button)
def calculate():
    try:
        expression = display.get()
        # eval automatically calculates the mathematical string (e.g., "2+3*5")
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Creating the main window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

# Creating the display (text field where numbers appear)
display = tk.Entry(window, font=("Arial", 20), justify="right", bd=10, insertwidth=4, width=14)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# List with the text of each button in display order
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Variables to control rows and columns in the grid
row = 1
column = 0

# Creating and positioning the buttons automatically
for text in buttons:
    # Defines the correct function depending on the button clicked
    if text == '=':
        command = calculate
    elif text == 'C':
        command = clear_display
    else:
        # lambda is used to pass the specific number/operator as an argument
        command = lambda x=text: press_button(x)
    
    # Creating the button component on the screen
    btn = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=command)
    btn.grid(row=row, column=column, padx=5, pady=5)
    
    column += 1
    # When it reaches the fourth column, it moves to the next row
    if column > 3:
        column = 0
        row += 1

# Keeps the window open and running
window.mainloop()
