from flask import  Flask ,request ,render_template
import pickle
import numpy as np
import pandas as pd
import sklearn


app = Flask(__name__)                    # Named the app

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # new
# db = SQLAlchemy(app) # new

model = pickle.load(open("airquality.pkl", 'rb'))
pred = ""


@app.route("/", methods =["GET","POST"] )
def  insertvalues():

    global pred

    if request.method == "POST":

        year = request.form.get("year")
        month = request.form.get("month")
        day  = request.form.get("day")
        time = request.form.get("time")
        co   =  request.form.get("co")
        pt08  = request.form.get("pt08")
        ben = request.form.get("Benzene")
        nox = request.form.get("NOx")
        no2 = request.form.get("NO2")
        
        params = [year, month, day, time, co, ben, nox, no2, pt08]
        for vals in params:
            if vals is None:
                pred = "Enter all the values"
            else:
                pred = round(model.predict([[year, month, day, time, co, ben, nox, no2, pt08]])[0], 3)

    return render_template("index.html", predictions = pred)

if __name__ == '__main__':
    app.run(debug=False)

