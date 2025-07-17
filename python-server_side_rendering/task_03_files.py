from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    data = []

    if source == "json":
        try:
            with open('products.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return render_template("product_display.html", error="JSON file not found")

    elif source == "csv":
        try:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except FileNotFoundError:
            return render_template("product_display.html", error="CSV file not found")

    else:
        return render_template("product_display.html", error="Wrong source")

    # Si un id est donné, filtrer
    if product_id:
        filtered = [item for item in data if str(item.get("id")) == product_id or str(item.get("id")) == str(product_id)]
        if not filtered:
            return render_template("product_display.html", error="Product not found")
        data = filtered

    return render_template("product_display.html", products=data)
