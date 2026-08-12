from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to 3C Restaurants!"

@app.route("/menu")
def menu():

    return jsonify([
        {
            "name": "Beef Burger",
            "price": 10.38
        },
        {
            "name": "Spicy Beef Burger",
            "price": 15.45
        },
        {
            "name": "Plain Pizza",
            "price": 10.00
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)