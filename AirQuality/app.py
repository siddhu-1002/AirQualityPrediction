from flask import  Flask ,request ,render_template
import joblib
import numpy as np
import pandas as pd
import sklearn


app = Flask(__name__)                    # Named the app

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # new
# db = SQLAlchemy(app) # new

model = joblib.load("air_quality.pickle")
pred = ""


@app.route("/", methods =["GET","POST"] )
def  insertvalues():

    global pred

    if request.method == "POST":

        year = request.form.get("year")
        month = request.form.get("month")
        day  = request.form.get("day")
        Time = request.form.get("Time")
        CO   =  request.form.get("CO")
        PT08  = request.form.get("PT08")
        NMHC  =  request.form.get("NMHC")

        try:
            pred = model.predict([[year, month, day, Time, CO, PT08, NMHC]])[0]
        except ValueError:
            pred = "Enter the values"

    return render_template("index.html", predictions = pred)

if __name__ == '__main__':
    app.run(debug=False)

