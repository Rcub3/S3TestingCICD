import random
import string
from flask import Flask, render_template_string

app = Flask(__name__)

def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the set and join them to form the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

@app.route('/')
def index():
    # Generate a password
    password = generate_password(12)
    # HTML template to render the password
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Generator</title>
        <style>
          body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
          .password-container { font-size: 24px; font-weight: bold; margin-top: 20px; }
          .generate-button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
        </style>
      </head>
      <body>
        <h1>Random Password Generator</h1>
        <div class="password-container">
          Generated Password: {{ password }}
        </div>
        <form method="get" action="/">
          <button type="submit" class="generate-button">Generate New Password</button>
        </form>
      </body>
    </html>
    """
    return render_template_string(html, password=password)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

