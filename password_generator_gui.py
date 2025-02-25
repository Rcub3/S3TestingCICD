import random
import string
import tkinter as tk

def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the set and join them to form the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def on_generate_button_click():
    # Get a generated password
    password = generate_password(12)
    # Update the label with the generated password
    password_label.config(text=f"Generated Password: {password}")

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Create a label to display the password
password_label = tk.Label(window, text="Generated Password: ", font=("Helvetica", 14))
password_label.pack(pady=10)

# Create a button that calls the on_generate_button_click function
generate_button = tk.Button(window, text="Generate Password", command=on_generate_button_click, font=("Helvetica", 14))
generate_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
