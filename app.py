# 1. Imports
from flask import Flask, render_template, session, url_for, redirect, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
import joblib

# 2. create an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asecretkey'

# 3. define a prediction function
def return_prediction(model, word1, word2, word3):

    sim_words = model.most_similar(positive=[word3, word2], negative=[word1])
    ##print("%s : %s :: %s : ?" % (word1, word2, word3))
    prediction = ("%s : %s :: %s : ? = %s" % (word1, word2, word3, sim_words[0][0]))

    return prediction

# 4. load our moment predictor model
model = joblib.load('bias.joblib')

# 5. create a WTForm Class
class PredictForm(FlaskForm):
    print('predictform')
    text = StringField("w1")
    text2 = StringField("w2")
    text3 = StringField("w3")

    submit = SubmitField("Predict")

# 6. set up our home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Create instance of the form
    form = PredictForm()

    # Validate the form
    if form.validate_on_submit():
        session['w1'] = form.text.data
        session['w2'] = form.text2.data
        session['w3'] = form.text3.data

        return redirect(url_for("prediction"))

    return render_template('home.html', form=form)

# 7. define a new "prediction" route that processes form input and returns a model prediction
@app.route('/prediction')
def prediction():
    content = {}
    content['w1'] = str(session['w1'])
    content['w2'] = str(session['w2'])
    content['w3'] = str(session['w3'])

    results = return_prediction(model, content['w1'], content['w2'], content['w3'])
    return render_template('prediction.html', results=results)

# Add the API there too
@app.route('/predict', methods=["GET", "POST"])
def moment_prediction():
    content = request.json
    results = return_prediction(model, content['w1'], content['w2'], content['w3'])
    return jsonify(results)

# 8. allows us to run flask using $ python app.py
if __name__ == '__main__':
    app.run()
