import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.configure(bg="#f0f0f0")
        
        self.label_weight = tk.Label(root, text="Weight (kg):", font=("Arial", 12), bg="#f0f0f0")
        self.label_weight.grid(row=0, column=0, padx=10, pady=10)
        self.entry_weight = tk.Entry(root, font=("Arial", 12))
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_height = tk.Label(root, text="Height (feet):", font=("Arial", 12), bg="#f0f0f0")
        self.label_height.grid(row=1, column=0, padx=10, pady=10)
        self.entry_height = tk.Entry(root, font=("Arial", 12))
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)
        
        self.calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12), command=self.calculate_bmi, bg="#4CAF50", fg="white", relief="raised")
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height_feet = float(self.entry_height.get())
            height_meter = height_feet * 0.3048  # Convert feet to meters
            bmi = weight / (height_meter ** 2)
            self.display_bmi(bmi)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")
    
    def display_bmi(self, bmi):
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"
        
        self.result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
