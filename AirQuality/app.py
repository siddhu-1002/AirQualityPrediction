from flask import  Flask ,request ,render_template
import joblib
import numpy as np
import pandas as pd
import sklearn


app = Flask(__name__)                    # Named the app

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # new
# db = SQLAlchemy(app) # new

model = joblib.load("air_quality.pickle")
pred = None


@app.route("/", methods =["GET","POST"] )
def  insertvalues():

    global pred

    if request.method == "POST":

        year = request.form.get("year")
        month = request.form.get("month")
        day  = request.form.get("day")
        time = request.form.get("Time")
        co   =  request.form.get("CO")
        pt08  = request.form.get("PT08")
        nmhc  =  request.form.get("NMHC")

        try:
            pred = model.predict([[year, month, day, time, co, pt08, nmhc]])[0]
        except ValueError:
            pred = "Enter the values"

    return render_template("index.html", predictions = pred)

if __name__ == '__main__':
    app.run(debug=False)

