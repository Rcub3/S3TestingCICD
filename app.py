import random
import string
from flask import Flask, render_template_string

app = Flask(__name__)

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_characters) for _ in range(length))

@app.route('/')
def index():
    password = generate_password(12)
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Generator</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
        <style>
          body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
          }

          .container {
            background: #ffffff;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
            width: 90%;
          }

          h1 {
            font-size: 28px;
            color: #333;
          }

          .password-container {
            margin-top: 20px;
            font-size: 22px;
            font-weight: 700;
            word-wrap: break-word;
            color: #2a2a2a;
          }

          .button-row {
            margin-top: 30px;
            display: flex;
            flex-direction: column;
            gap: 10px;
          }

          .generate-button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
          }

          .generate-button:hover {
            background-color: #0056b3;
          }

          @media (max-width: 600px) {
            .container {
              padding: 20px;
            }

            .password-container {
              font-size: 18px;
            }

            .generate-button {
              width: 100%;
            }
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>🔐 Random Password Generator</h1>
          <div class="password-container" id="generated-password">{{ password }}</div>

          <div class="button-row">
            <form method="get" action="/">
              <button type="submit" class="generate-button">🔄 Generate New Password</button>
            </form>
            <button onclick="copyPassword()" class="generate-button">📋 Copy to Clipboard</button>
          </div>
        </div>

        <script>
          function copyPassword() {
            const text = document.getElementById("generated-password").innerText;
            navigator.clipboard.writeText(text).then(() => {
              alert("✅ Password copied to clipboard!");
            });
          }
        </script>
      </body>
    </html>
    """
    return render_template_string(html, password=password)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
