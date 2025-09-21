from flask import Flask, render_template
from datetime import datetime

# create a Flask app
app = Flask(__name__)

# function to get a greeting based on the time
def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# home page route
@app.route('/')
def home():
    greeting = get_greeting()
    return render_template("index.html", greeting=greeting)

# about page route
@app.route('/about')
def about():
    return render_template("about.html")

# run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



