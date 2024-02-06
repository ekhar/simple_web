from flask import Flask, request, jsonify

from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Initialize CORS with your Flask app instance
@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        data = request.get_json()
        if 'number1' in data and 'number2' in data:
            num1 = data['number1']
            num2 = data['number2']
            result = num1 * num2
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Please provide two numbers in the request JSON.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

