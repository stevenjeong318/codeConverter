from flask import Flask
from flask import render_template
from flask import request
import openai
import json
import os

app = Flask(__name__)

#load api keys from environment
openai.api_key = os.getenv("API_KEY")

#serves home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

#serves converted page with endpoint done
@app.route('/done', methods=['GET', 'POST'])
def result():
    dropdown1_value = request.form.get('dropdown1') #saves choice of 1st dropdown from index.html
    dropdown2_value = request.form.get('dropdown2') #saves choice of 2nd dropdown from index.html
    same_value = dropdown1_value == dropdown2_value #bool variable checking if 1st (input lang) and 2nd (output lang) are same
    code = request.form['input-code'] #saves input code from index.html
    s = f"Convert \n {code} \n from {dropdown1_value} to {dropdown2_value}"
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=s,
            max_tokens=200,
            n=1,
    )
    answer = response.choices[0].text.strip()
    return render_template('result.html', bool=same_value, in_opt=dropdown1_value, out_opt=dropdown2_value, input_code=code, output_code=answer)


if __name__ == '__main__':
    app.run(debug=True)
