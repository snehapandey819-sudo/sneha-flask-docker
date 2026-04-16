from flask import Flask, request, render_template
from supabase import create_client
from dotenv import load_dotenv
import os

# Load .env file (only for local system)
load_dotenv(dotenv_path=".env")

# Get environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# DEBUG (REMOVE LATER IF NEEDED)
print("🔍 DEBUG SUPABASE_URL:", SUPABASE_URL)
print("🔍 DEBUG SUPABASE_KEY exists:", bool(SUPABASE_KEY))

# Safety check
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception(
        "❌ Environment variables missing. "
        "Check .env file, Docker --env-file, or GitHub Secrets."
    )

try:
    # Create Supabase client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    raise Exception(f"❌ Supabase client creation failed: {str(e)}")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')

    if not name or not message:
        return "❌ Name or message missing"

    try:
        response = supabase.table("feedback").insert({
            "name": name,
            "message": message
        }).execute()

        print("✅ Insert response:", response)

    except Exception as e:
        return f"❌ Database insert failed: {str(e)}"

    return f"""
    <h2 style="text-align:center; margin-top:50px;">
        Thank you {name}! 🎉<br>
        Your message has been saved successfully.
    </h2>
    <p style="text-align:center;">
        <a href="/">Go Back</a>
    </p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)