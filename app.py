from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    in_lang = request.form['dropdown1']
    out_lang = request.form['dropdown2']
    code = request.form['input-code']
    r = f"You converted \n {code} \n from {in_lang} to {out_lang}"
    return r
    

if __name__ == '__main__':
    app.run(debug=True)