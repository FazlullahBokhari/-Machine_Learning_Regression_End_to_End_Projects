from flask import Flask 
import numpy as np

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Machine Learning Pipeline created CI/CD pipline"


if __name__ == "__main__":
    app.run(debug=True)


#email = fazlullahb@gmail.com
#api = <>
#name = machine-learn-regression-model

