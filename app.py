from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)

api = Api(app)

def check(postedData, method):
    if method in ('add', 'subtract', 'multiply'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    else: 
        if method == 'divide':
            if 'x' not in postedData or 'y' not in postedData:
                return 301
            elif int(postedData['y']) == 0:
                return 302
            return 200

class Add(Resource):
    def post(self):
        
        postedData = request.get_json()

        statusCode = check(postedData, 'add')

        if statusCode != 200:
            retJson = {
                "Message": "An error happened",
                'Status Code': statusCode
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])
        res = x+y
        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):

        postedData = request.get_json()

        statusCode = check(postedData, 'subtract')

        if statusCode != 200:
            retJson = {
                "Message": "An error happened",
                'Status Code': statusCode
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])
        res = x-y
        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
    
        postedData = request.get_json()

        statusCode = check(postedData, 'multiply')

        if statusCode != 200:
            retJson = {
                "Message": "An error happened",
                'Status Code': statusCode
            }
            return jsonify(retJson)

        x = int(postedData['x'])
        y = int(postedData['y'])
        res = x*y
        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        
        postedData = request.get_json()

        statusCode = check(postedData, 'divide')

        if statusCode != 200:
            retJson = {
                "Message": "An error happened",
                'Status Code': statusCode
            }
            return jsonify(retJson)

        x = float(postedData['x'])
        y = int(postedData['y'])
        res = x/y
        retMap = {
            'Message': res,
            'Status Code': 200
        }
        return jsonify(retMap)


@app.route('/')
def hello_world():
    return('Hello World!')

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

if __name__ == '__main__':
    app.run(debug=True)