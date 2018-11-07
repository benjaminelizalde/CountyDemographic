from flask import Flask, request, Markup, render_template
import os
import json

app = Flask(__name__)

with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)
        
@app.route("/")
def render_main():
    if "States" not in request.args:
        return render_template('part1.html', state = get_state_options())
    else:
        return render_template('part1.html', state = get_state_options(), funfact = fun_fact(request.args["States"]) )

        
def get_state_options():
     listOfStates = []
     for county in counties:
        if not county["State"] in listOfStates:
            listOfStates.append(county["State"])
     options = ""
     for state in listOfStates:
        options = options +  Markup("<option value=\"" + state + "\">" + state + "</option>")
     return options
     
     
     
def fun_fact(state):
    fact = counties[0]["Education"]["Bachelor's Degree or Higher"]
    for county in counties:
        if county["State"] == state:
            fact = county["Education"]["Bachelor's Degree or Higher"]
            
    return fact
        

   
   
if __name__=="__main__":
    app.run(debug=True, port=54321)