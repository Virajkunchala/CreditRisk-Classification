from flask import Flask, request, render_template
import numpy as np


app = Flask(__name__,template_folder='templates')

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    input_data = request.form.to_dict() # convert the form data to a dictionary
    
    for x in input_data:
        return x
    # print(input_data)
    return f'Form data received!: {input_data}'

    # input_data = request.json
    # input_array = np.array(input_data['input'])
   
    
    # # Process input data as needed
    # return f'You entered: {input_data}'

if __name__ == '__main__':
    app.run(debug=True)