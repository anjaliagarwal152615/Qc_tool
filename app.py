from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Defect Tracking Tool"

@app.route('/defects')
def view_defects():
    # Read defect data from CSV using pandas
    defect_data = pd.read_csv(r'C:\Users\Anjali\Desktop\Qc tool\creditcard.csv')

    # Convert defect data to a list of dictionaries
    defects = defect_data.to_dict('records')

    return render_template('defects.html', defects=defects)

if __name__ == '__main__':
    app.run(debug=True)
