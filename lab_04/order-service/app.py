from flask import Flask, request, jsonify
import requests
import time
import os

app = Flask(__name__)

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:5001")

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    retries = 3

    for attempt in range(retries):
        try:
            response = requests.get(
                f"{PRODUCT_SERVICE_URL}/products/{product_id}",
                timeout=2
            )

            if response.status_code == 200:
                product = response.json()
                return jsonify({
                    "message": "Order created",
                    "product": product,
                    "quantity": quantity
                })

        except requests.exceptions.RequestException:
            time.sleep(1)

    return {"error": "Product service unavailable"}, 503


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)