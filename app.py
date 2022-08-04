from flask import Flask 
import numpy as np
import tensorflow as tf

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Starting ML projects"


if __name__ == "__main__":
    app.run(debug=True)


#email = fazlullahb@gmail.com
#api = ee45e5c4-24ed-4f15-b246-28d1af388c87
#name = machine-learn-regression-model

