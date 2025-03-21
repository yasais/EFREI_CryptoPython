from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
         

app = Flask(__name__)

@app.route('/')
def home():
    return """<h1>Bienvenue sur l'API CryptoPython</h1>
    <style>
    body {
      background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #f0f0f0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }

    h1 {
      background: linear-gradient(to right, #00c6ff, #0072ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-size: 3em;
      text-align: center;
      margin: 0 20px;
      animation: fadeIn 2s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>"""
         

@app.route('/encrypt/<string:key>/<string:message>')
def encrypt_message(key, message):
    try:
        key_bytes = key.encode()  # Convertir la clé en bytes
        f = Fernet(key_bytes)  # Créer un objet Fernet avec cette clé
        encrypted = f.encrypt(message.encode())  # Chiffrer le message
        return encrypted.decode()  # Retourne le message chiffré
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt/<string:key>/<string:token>')
def decrypt_message(key, token):
    try:
        key_bytes = key.encode()  # Convertir la clé en bytes
        f = Fernet(key_bytes)  # Créer un objet Fernet avec cette clé
        decrypted = f.decrypt(token.encode())  # Déchiffrer le message
        return decrypted.decode()  # Retourne le message déchiffré
    except Exception as e:
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
