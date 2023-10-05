from flask import Flask
from flask import render_template
from flask import request
from flask import flash


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/done', methods=['GET', 'POST'])
def result():
    in_lang = request.form['dropdown1']
    in_opt = request.args.get('stored_dropdown_value1', default=None)
    out_lang = request.form['dropdown2']
    out_opt = request.args.get('stored_dropdown_value2', default=None)
    code = request.form['input-code']
    s= f"Convert \n {code} \n from {in_lang} to {out_lang}"
    print(s)
    return render_template('result.html', in_code = in_opt, out_code = out_opt, input_code = code, output_code = s)
    

if __name__ == '__main__':
    app.run(debug=True)