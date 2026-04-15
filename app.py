from flask import Flask, request, render_template
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Missing Supabase ENV variables")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')

    supabase.table("feedback").insert({
        "name": name,
        "message": message
    }).execute()

    return f"""
    <h2 style="text-align:center; margin-top:50px;">
        Thank you {name}! 🎉<br>
        Your message has been saved successfully.
    </h2>
    <p style="text-align:center;">
        <a href="/">Go Back</a>
    </p>
    """