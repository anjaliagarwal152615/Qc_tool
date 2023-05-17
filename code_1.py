from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Defect Tracking Tool"

@app.route('/defects')
def view_defects():
    # Fetch defects from the database or a dataset
    # Pass the defects to the template for rendering
    defects = [...]  # Replace [...] with the actual defect data
    return render_template('defects.html', defects=defects)


