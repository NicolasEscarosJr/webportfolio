import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create the entry field for displaying the result
        self.result_var = tk.StringVar()
        self.result_var.set("")
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, width=20, bd=5, justify=tk.RIGHT)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Create the calculator buttons
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "=",  # Add the "Equal" button
        ]
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(self.master, text=button_text, width=5, height=2, command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == "C":
            # Clear the result entry
            self.result_var.set("")
        elif text == "=":
            # Evaluate the expression and display the result
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            # Append the clicked button text to the result entry
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
