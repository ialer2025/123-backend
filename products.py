@app.route("/add-product", methods=["POST"])
def add_product():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO products (name, description, price, stock, image_path) VALUES (?, ?, ?, ?, ?)",
                 (data["name"], data["description"], data["price"], data["stock"], data["image_path"]))
    conn.commit()
    return jsonify(success=True)

@app.route("/delete-product/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    conn = get_db()
    conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    return jsonify(success=True)