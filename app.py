from flask import Flask,jsonify,request
from model import Prediction
app = Flask(__name__)

@app.route("/alphabet_predict",methods = ["POST"])
def Predict():
    image = request.files.get("alphabet")
    predict = Prediction(image)
    return jsonify ({'data':predict , "message":"the alphabet is sucessfully recognized"})

if __name__ == '__main__':
    app.run(debug = True)