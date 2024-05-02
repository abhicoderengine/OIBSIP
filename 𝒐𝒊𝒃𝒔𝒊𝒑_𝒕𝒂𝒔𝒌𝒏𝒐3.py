import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Styling
        self.master.configure(bg="#f0f0f0")
        self.master.geometry("350x250")

        self.label_font = ("Helvetica", 12)
        self.entry_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")

        # Password Length
        self.length_label = tk.Label(master, text="Password Length:", font=self.label_font, bg="#f0f0f0")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.length_entry = tk.Entry(master, font=self.entry_font, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password Complexity
        self.complexity_label = tk.Label(master, text="Password Complexity:", font=self.label_font, bg="#f0f0f0")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")
        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, *self.complexity_options)
        self.complexity_menu.config(font=self.entry_font)
        self.complexity_menu.grid(row=1, column=1, padx=10, pady=10)

        # Generate Password Button
        self.generate_button = tk.Button(master, text="Generate Password", font=self.button_font, command=self.generate_password, bg="#4CAF50", fg="white")
        self.generate_button.grid(row=2, columnspan=2, padx=10, pady=10, sticky="we")

        # Generated Password Display
        self.password_label = tk.Label(master, text="Generated Password:", font=self.label_font, bg="#f0f0f0")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master, textvariable=self.password_var, font=self.entry_font, state='readonly', width=20)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", font=self.button_font, command=self.copy_to_clipboard, bg="#008CBA", fg="white")
        self.copy_button.grid(row=4, columnspan=2, padx=10, pady=10, sticky="we")

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()
        
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        if complexity == "Low":
            charset = lowercase + uppercase + digits
        elif complexity == "Medium":
            charset = lowercase + uppercase + digits + symbols
        elif complexity == "High":
            charset = lowercase + uppercase + digits + symbols + string.ascii_letters

        generated_password = ''.join(random.choice(charset) for _ in range(length))
        self.password_var.set(generated_password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        print("Password copied to clipboard")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
