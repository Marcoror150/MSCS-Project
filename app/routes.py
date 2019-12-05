from app import app
from flask import render_template, url_for, request
from sklearn.externals import joblib

from .constants import *

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/multiple_fatalities', methods=['GET', 'POST'])
def multiple_fatalities():
    if request.method == 'GET':
        return render_template("multiple_fatalities.html")
    if request.method == 'POST':
        loaded_model = joblib.load('finalized_model.sav')
        # print(request.form)
        data = {
            'make' : make_numbers[request.form['make']],
            'model' : model_numbers[request.form['model']]
        }
        prediction = loaded_model.predict([[data['make'], data['model'], request.form['year']]])
        if prediction == False:
            prediction = "Single Fatality"
        else:
            prediction = "Multiple Fatalities"
        return prediction
@app.route('/car_age', methods=['GET', 'POST'])
def car_age():
    if request.method == 'GET':
        return render_template("car_age.html")
@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'GET':
        return render_template("location.html")
    if request.method == 'POST':
        state = request.form['state']
        stateNum = int(stateDict[state])
        statePct = percentDict[stateNum]
        weightedPct = '{0:.2f}'.format(statePct / percentAvg)
        return "State percentage: " + str(statePct) \
            + "% and Weighted Percentage: " + str(weightedPct) \
            + " (times more likely to be involved in a fatal crash) "
@app.route('/metrics')
def metrics():
    return render_template("metrics.html")