from flask import Flask, request, jsonify
from ludwig import LudwigModel
import pandas as pd 

app = Flask(__name__)

#load the model
model = LudwigModel.load('./model')

@app.rout('/predict', method=['POST'])
def predict():
    #get POST request data
    data = request.get_json()
    #Make prediction
    df =pd.DataFrame([str(data['text'])], columns=['content'])
    print(df.head())
    pred = model.predict(data_df=df)
    print(pred)
    return jsonify(pred['airline_sentiment_predictions'][0])

if __name__ == '__main__' :
    app.run(port=4000, debug=True)