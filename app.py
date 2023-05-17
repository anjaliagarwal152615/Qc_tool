from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

defects = []

@app.route('/')
def home():
    return "Welcome to the Defect Tracking Tool"

@app.route('/defects', methods=['GET', 'POST'])
def view_defects():
    if request.method == 'POST':
        defect = {
            'ID': request.form['id'],
            'Description': request.form['description'],
            'Assigned To': request.form['assigned_to'],
            'Status': request.form['status']
        }
        defects.append(defect)
        return redirect('/defects')

    return render_template('defects.html', defects=defects)

if __name__ == '__main__':
    app.run(debug=True)

