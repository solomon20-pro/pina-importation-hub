from flask import Flask, render_template, redirect
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

WHATSAPP_NUMBER=2349053175822

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/whatsapp")
def whatsapp():
    url = f"https://wa.me/{WHATSAPP_NUMBER}"
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)