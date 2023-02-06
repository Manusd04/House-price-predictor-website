from flask import Flask , render_template,request
from flask_nav import Nav
from flask_nav.elements import Navbar,View,Text,Link
import numpy as np
import pickle

app = Flask(__name__, template_folder='templates',static_folder='static')
nav = Nav(app)
nav.register_element('my_navbar', Navbar(
    'thenav',
    View('Home Page', 'index'),
    View('About','about'),
    Link('Blog', 'https://sdmanu31.blogspot.com'),
    ))


model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/templates/about.html')
def about():
    return render_template('about.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['bedrooms']
    val2 = request.form['bathrooms']
    val3 = request.form['floors']
    val4 = request.form['yr_built']
    arr = np.array([val1, val2, val3, val4])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template('index.html', data=int(pred))

if __name__ == '__main__':
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=9000, 
        threaded=True)