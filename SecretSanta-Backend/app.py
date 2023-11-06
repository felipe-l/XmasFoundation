from flask import Flask, request, jsonify
from secretSanta import shuffleNames
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/process_names', methods=['POST'])
def process_names():
    data = request.get_json()

    if 'names' in data:
        names = data['names']
        # Process the names or perform any desired operations here
        # For example, you can create a dictionary with the processed names
        shuffled_names = shuffleNames(names)
        # Return the processed names as JSON
        return jsonify(shuffled_names)
    else:
        return jsonify({'error': 'Invalid data format'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)