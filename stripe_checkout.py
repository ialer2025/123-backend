

import stripe
stripe.api_key = "dein_stripe_secret_key"

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout():
    data = request.json  # z. B. Warenkorb mit Preis & Name
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "eur",
                "product_data": {"name": data["name"]},
                "unit_amount": int(data["price"] * 100)
            },
            "quantity": data["quantity"]
        }],
        mode="payment",
        success_url="http://localhost:3000/success",
        cancel_url="http://localhost:3000/cancel"
    )
    return jsonify({"id": session.id})

