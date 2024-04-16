from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/customer")
def get_customer():
    customer = {
        "name": "john"
    }
    return jsonify(customer)


app.run()