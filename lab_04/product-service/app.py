from flask import Flask, jsonify

app = Flask(__name__)

products = {
    1: {"id": 1, "name": "Laptop", "price": 1000},
    2: {"id": 2, "name": "Phone", "price": 500}
}

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/products")
def get_products():
    return jsonify(list(products.values()))

@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return {"error": "Product not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)