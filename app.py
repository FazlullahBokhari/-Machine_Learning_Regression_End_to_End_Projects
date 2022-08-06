from flask import Flask 
import numpy as np
from housing.logger import logging 


app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("We are testing logging module")
    return "Machine Learning Pipeline created CI/CD pipline"


if __name__ == "__main__":
    app.run(debug=True)


#email = fazlullahb@gmail.com
#api = <>
#name = machine-learn-regression-model

