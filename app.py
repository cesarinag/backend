from flask import Flask
from flask import request
from flask_cors import CORS

import pickle
import pandas
import numpy

app = Flask(__name__)
CORS(app)

# load our prediction model
def load_model():
    return pickle.load(open("./model/logr_gs.p", "rb"))


# load our base data frame
def load_df():
    return pandas.read_csv("./model/X_test.csv")


# enable specific features for our data frame
def build_frame(params):
    df = load_df()
    df["nonprofit"] = params["nonprofit"]
    df["jobsreported"] = params["jobsreported"]

    zip = params["zip"]
    df[f"zip_{zip}"] = 1

    naics = params["naics"]
    df[f"naicscode_{naics}"] = 1

    lender = params["lender"]
    df[f"lender_{lender}"] = 1

    return df


# generate our loan probabilities
def predict_probabilites():
    model = load_model()
    df = build_frame(request.get_json())
    return model.predict_proba(df)[0]


@app.route("/", methods=["POST"])
def gen_probabilites():
    probabilities = predict_probabilites().tolist()
    response = {"probabilities": probabilities}
    return response
