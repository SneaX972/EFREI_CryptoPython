from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Génération et gestion de la clé de cryptage
key = Fernet.generate_key()  # Génère une clé unique
f = Fernet(key)  # Initialisation de Fernet avec la clé

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    """
    Chiffre une valeur donnée.
    :param valeur: Valeur en texte brut à chiffrer.
    :return: Texte chiffré.
    """
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Chiffrement
    return f"Valeur encryptée : {token.decode()}"  # Conversion bytes -> str pour l'affichage

@app.route('/decrypt/<string:valeur_chiffree>')
def decryptage(valeur_chiffree):
    """
    Décrypte une valeur chiffrée.
    :param valeur_chiffree: Texte chiffré (token).
    :return: Texte déchiffré.
    """
    try:
        valeur_bytes = valeur_chiffree.encode()  # Conversion str -> bytes
        valeur_dechiffree = f.decrypt(valeur_bytes)  # Décryptage
        return f"Valeur décryptée : {valeur_dechiffree.decode()}"  # Conversion bytes -> str
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
