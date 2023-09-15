import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def power(self, base, exponent):
        return base ** exponent
    
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor
    
    def log_base_2(self, number):
        return math.log2(number)
    
    def degree_to_radian(self, degree):
        return math.radians(degree)
    
    def radian_to_degree(self, radian):
        return math.degrees(radian)


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator GUI")
        
        self.calculator = Calculator()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.base_label = tk.Label(self.root, text="Enter Value:")
        self.base_label.pack()
        
        self.base_entry = tk.Entry(self.root)
        self.base_entry.pack()
        
        self.operation_label = tk.Label(self.root, text="Select Operation:")
        self.operation_label.pack()
        
        self.operation_var = tk.StringVar()
        self.operation_var.set("power")
        
        self.operations_menu = tk.OptionMenu(self.root, self.operation_var, "power", "divide", "log base 2", "radian to degree", "degree to radian")
        self.operations_menu.pack()
        
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.pack()
        
        self.result_display = tk.Label(self.root, text="")
        self.result_display.pack()
        
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()
        
    def calculate(self):
        try:
            value = float(self.base_entry.get())
            operation = self.operation_var.get()
            
            if operation == "power":
                exponent = float(input("Enter the exponent: "))
                result = self.calculator.power(value, exponent)
            elif operation == "divide":
                divisor = float(input("Enter the divisor: "))
                result = self.calculator.divide(value, divisor)
            elif operation == "log base 2":
                result = self.calculator.log_base_2(value)
            elif operation == "radian to degree":
                result = self.calculator.radian_to_degree(value)
            elif operation == "degree to radian":
                result = self.calculator.degree_to_radian(value)
                
            self.result_display.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
