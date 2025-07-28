# app.py
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Path to store data
DATA_FILE = "data.txt"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the name and age from the form
        name = request.form['name']
        age = request.form['age']

        # Store the name and age in a file
        with open(DATA_FILE, 'a') as f:
            f.write(f"Name: {name}, Age: {age}\n")

        return f"Thank you, {name}. Your data has been saved!"

    # Render the form if GET request
    return render_template_string('''
        <!doctype html>
        <title>Enter Your Details</title>
        <body >
        <h1>apk2</h1>
        <h1>Enter your name and age</h1>
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
