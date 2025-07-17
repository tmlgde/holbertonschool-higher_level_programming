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

    elif source == "csv":
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

    else:
        return render_template("product_display.html", error="Wrong Source")

    return render_template("product_display.html", products=data)
