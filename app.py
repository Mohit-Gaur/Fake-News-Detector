import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
with open('Model.pkl', 'rb') as pf:
    model=pickle.load(pf)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():
    input_form=[request.form.get("news")]
    print(f"Initial input is {input_form}")
    final_input=[str(input_form)]
    print(f"Final input is {final_input}")
    prediction=model.predict(final_input)
    print(f"Model prediction is {prediction}")
    prediction_str=' '.join([str(elem) for elem in prediction])
    print(prediction_str)

    return render_template('index.html', output=f'News is:{prediction_str}')

if __name__ == "__main__":
    app.run(debug=True)
