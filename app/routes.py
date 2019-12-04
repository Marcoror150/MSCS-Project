from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/multiple_fatalities')
def multiple_fatalities():
    return render_template("multiple_fatalities.html")
@app.route('/car_age')
def car_age():
    return render_template("car_age.html")
@app.route('/location')
def location():
    return render_template("location.html")
@app.route('/metrics')
def metrics():
    return render_template("metrics.html")