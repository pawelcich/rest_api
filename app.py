from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello World!')

@app.route('/hithere')
def hh():
    return('I just farted... /hithere')

@app.route('/add', methods=['POST', 'GET'])
def add_nums():
    data = request.get_json()
    x = data['x'] 
    y = data['y']
    retJSON = {
        "z": x + y
    }
    return jsonify(retJSON)

    
if __name__ == '__main__':
    app.run(debug=True)