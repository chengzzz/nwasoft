from flask import Flask
from flask_restful import Api, Resource, reqparse
import csv

app = Flask(__name__)
api = Api(app)

items = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class Item(Resource):
    def get(self, name):
        for user in items:
            if (name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("length")
        parser.add_argument("width")
        parser.add_argument("height")
        parser.add_argument("weight")
        parser.add_argument("color")
        args = parser.parse_args()

        item = {
            "id": id,
            "length": args["length"],
            "width": args["width"],
            "height": args["height"],
            "weight": args["weight"],
            "color": args["color"]
        }

        filename = id + '.csv'
        csvfile = open(filename, 'w', newline='')
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for key,value in item.items():
            csvwriter.writerow([key, value])

        return id, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(Item, "/item/<string:id>")
app.run(debug=True)

@app.route("/")
def hello():
    return "Hello, World! This feels good."

if __name__ == "__main__":
    app.run()