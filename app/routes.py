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
        data = request.get_json()
        print(data)
        response = {'responses':[]}
        for row in data['data']:
            dataIn = {
                'make' : make_numbers[row['make']],
                'model' : model_numbers[row['model']]
            }
        # data = {
        #     'make' : make_numbers[request.form['make']],
        #     'model' : model_numbers[request.form['model']]
        # }
            prediction = loaded_model.predict([[dataIn['make'], dataIn['model'], row['year']]])
            if prediction == False:
                response['responses'].append({
                    'make':row['make'],
                    'model':row['model'],
                    'year':row['year'],
                    'prediction':"Single Fatality"
                })
            else:
                response['responses'].append({
                    'make':row['make'],
                    'model':row['model'],
                    'year':row['year'],
                    'prediction':"Multiple Fatalities"
                })
        # responses = [prediction]
        return response
        # return data['data'][0]
@app.route('/car_age', methods=['GET', 'POST'])
def car_age():
    if request.method == 'GET':
        return render_template("car_age.html")
    if request.method == 'POST':
        year = str(request.form['year'])
        yearPct = agePctDict[year]
        weightedPct = '{0:.4f}'.format(yearPct / ageAvg)
        responses = [year + " Year percentage: " + str(yearPct) \
            + "% and Weighted Percentage: " + str(weightedPct) \
            + " (times more likely to be involved in a fatal crash) "]
        return {'responses':responses}
@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'GET':
        return render_template("location.html")
    if request.method == 'POST':
        state = request.form['state']
        stateNum = int(stateDict[state])
        statePct = percentDict[stateNum]
        weightedPct = '{0:.2f}'.format(statePct / percentAvg)
        responses = [state + " State percentage: " + str(statePct) \
            + "% and Weighted Percentage: " + str(weightedPct) \
            + " (times more likely to be involved in a fatal crash) "]
        return {'responses':responses}
@app.route('/metrics')
def metrics():
    return render_template("metrics.html", topTenMakes=topTenMakes,
        topTenModels=topTenModels, topTenStates=topTenStates, 
        topTenYears=topTenYears)