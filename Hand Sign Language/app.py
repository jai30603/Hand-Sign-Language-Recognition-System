# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_detection', methods=['GET'])
def start_detection():
    # Run inference_classifier.py when this endpoint is accessed
    import inference_classifier
    return 'Hand gesture detection started.'

@app.route('/result', methods=['POST'])
def result():
    result = request.form['result']
    print("Received result:", result)
    return 'Result received'

if __name__ == '__main__':
    app.run(debug=True)
