from flask import Flask, render_template, request

import pickle

# load the model
with open("./Co2_emission_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/", methods=["GET"])

def index():
    return render_template("index.html")



@app.route("/predict", methods=["GET"])

def predict_profit():

    print(request.args)

    ENGINESIZE = float(request.args.get("ENGINESIZE"))
    CYLINDERS = int(request.args.get("CYLINDERS"))
    FUELCONSUMPTION_COMB = float(request.args.get("FUELCONSUMPTION_COMB"))
    CO2EMISSIONS = model.predict([[ENGINESIZE, CYLINDERS, FUELCONSUMPTION_COMB]])
    return f"<h1>Co2 Emission by this Engine will be {CO2EMISSIONS[0]}</h1>"


app.run(host = "localhost", port = 5000, debug = True)

