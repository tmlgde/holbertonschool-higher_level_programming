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
            with open("products.json", "r") as f:
                data = json.load(f)
        except Exception:
            return render_template("product_display.html", error="JSON file not found")

    elif source == "csv":
        try:
            with open("products.csv", "r") as f:
                reader = csv.DictReader(f)
                data = list(reader)
        except Exception:
            return render_template("product_display.html", error="CSV file not found")

    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        data = [item for item in data if str(item.get("id")) == str(product_id)]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)
