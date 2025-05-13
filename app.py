import random  # Importeert de 'random' module voor willekeurige selectie
import string  # Importeert de 'string' module om toegang te krijgen tot letter- en cijferreeksen
from flask import Flask, render_template_string  # Importeert Flask en een methode om HTML als string te renderen

# Initialiseer een Flask-applicatie
app = Flask(__name__)

def generate_password(length=12):
    """
    Genereert een willekeurig wachtwoord met de opgegeven lengte.
    
    Parameters:
        length (int): De lengte van het gegenereerde wachtwoord (standaard is 12).
    
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
    # Genereert een nieuw wachtwoord met een lengte van 12 tekens
    password = generate_password(12)
    
    # HTML-template om het wachtwoord weer te geven
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
        <h1>Random Password Generator(RPG)</h1>
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


