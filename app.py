from flask import Flask 
import numpy as np
from housing.logger import logging 
from housing.exception import HousingException 
import sys 

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    """try:
        raise Exception("we are testing cutom exception ")
    except Exception as e:
        #housing = HousingException(e, sys)
        #logging.info(housing.error_message) 
        logging.info("We are testing logging module")"""
    return "Machine Learning Pipeline created CI/CD pipline"


if __name__ == "__main__":
    app.run(debug=True)


#email = fazlullahb@gmail.com
#api = <>
#name = machine-learn-regression-model

