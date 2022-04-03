import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
model=pickle.load(open('Model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():
    input_form=[request.form.get("news")]
    final_input=[str(input_form)]
    prediction=model.predict(final_input)

    return render_template('index.html', output=f'News is:{prediction}')

if __name__ == "__main__":
    app.run(debug=True)
