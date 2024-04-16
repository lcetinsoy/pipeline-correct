from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return """
        <form id="formulaire">
           <label>login</label>
        </form>
    """

@app.route("/api/customer")
def get_customer():
    customer = {
        "name": "john"
    }
    return jsonify(customer)


app.run()