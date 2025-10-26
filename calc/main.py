from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        result = eval(expression, {"__builtins__": {}}, {})
        return jsonify({'result': str(result)})
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
