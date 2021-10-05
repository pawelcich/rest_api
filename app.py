from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)

api = Api(app)

def check(postedData, method):
    if method == 'add':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
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
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass


@app.route('/')
def hello_world():
    return('Hello World!')

api.add_resource(Add, "/add")

if __name__ == '__main__':
    app.run(debug=True)