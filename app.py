from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/done', methods=['GET', 'POST'])
def result():
    dropdown1_value = request.form.get('dropdown1')
    dropdown2_value = request.form.get('dropdown2')
    same_value = dropdown1_value == dropdown2_value
    code = request.form['input-code']
    s = f"Convert \n {code} \n from {dropdown1_value} to {dropdown2_value}"
    print(dropdown1_value, dropdown2_value)
    return render_template('result.html', bool=same_value, in_opt=dropdown1_value, out_opt=dropdown2_value, input_code=code, output_code=s)


if __name__ == '__main__':
    app.run(debug=True)
