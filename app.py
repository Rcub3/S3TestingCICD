import random  # Importeert de 'random' module voor willekeurige selectie
import string  # Importeert de 'string' module om toegang te krijgen tot letter- en cijferreeksen
from flask import Flask, render_template_string  # Importeert Flask en een methode om HTML als string te renderen

# Initialiseer een Flask-applicatie
app = Flask(__name__)

def generate_password(length=14):
    """
    Genereert een willekeurig wachtwoord met de opgegeven lengte.
    
    Parameters:
        length (int): De lengte van het gegenereerde wachtwoord (standaard is 14).
    
    Returns:
        str: Een willekeurig wachtwoord bestaande uit letters, cijfers en speciale tekens.
    """
    # Alle mogelijke tekens die in het wachtwoord kunnen worden gebruikt
    all_characters = string.ascii_letters + string.digits + string.punctuation  
    # Willekeurig kiezen van tekens en samenvoegen tot een wachtwoord
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

@app.route('/')  # Definieert de route voor de homepage
def index():
    """
    Route handler voor de homepage.
    
    Returns:
        HTML-pagina met een willekeurig gegenereerd wachtwoord.
    """
    # Genereert een nieuw wachtwoord met een lengte van 14 tekens
    password = generate_password(14)
    
    # HTML-template om het wachtwoord weer te geven
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Generator</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
        <style>
          body { font-family: 'Inter', sans-serif; }
        </style>
      </head>
      <body>
        <h1>Random Password Generator</h1>
        <div class="password-container">
          Generated Password: {{ password }}  <!-- Weergave van het gegenereerde wachtwoord -->
        </div>
        <form method="get" action="/">  <!-- Formulier om een nieuw wachtwoord te genereren -->
          <button type="submit" class="generate-button">Generate New Password</button>
        </form>
      </body>
    </html>
    """
    # Render de HTML-pagina en geef het wachtwoord door aan de template
    return render_template_string(html, password=password)

# Start de Flask-webserver als het script direct wordt uitgevoerd
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Server draait op poort 5000 en is toegankelijk vanaf elk IP-adres


