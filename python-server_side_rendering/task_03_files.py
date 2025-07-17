from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get("source")

    if source == "json":
        with open('products.json', "r") as file:
            data = json.load(file)
            return str(data) 

    elif source == "csv":
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return str(data) 

    else:
        return "Wrong Source"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
