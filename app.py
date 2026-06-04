from flask import Flask, render_template, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#--SECRET KEY--
app.secret_key = os.getenv("SECRET_KEY")

#--RATE LIMITING--
#stops people from spamming your routese
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "20 per hour"]
    )

#--HTTPS & SECURITY HEADERS--
#Forces HTTPS and adds security headers
Talisman(app, force_https=False) #Set True when deployed

WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")


@app.route("/")
@limiter.limit("30 per hour")
def home():
    return render_template("index.html")

@app.route("/whatsapp")
@limiter.limit("10 per hour")
def whatsapp():
    url = f"https://wa.me/{WHATSAPP_NUMBER}"
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)
    