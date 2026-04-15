from flask import Flask, request, render_template
from supabase import create_client
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Submit form
@app.route('/submit')
def submit():
    name = request.args.get('name')
    message = request.args.get('message')

    # Insert into Supabase
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

def handler(request, context):
    return app