from flask import Flask, jsonify, request # Flask-Funktione
from flask_cors import CORS # Für Cross-Origin-Zugriff
import sqlite3 # Für die Datenbank-Verbindung


app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect("database/shop.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/products")
def products():
    conn = get_db()
    cur = conn.execute("SELECT * FROM products")
    items = [dict(row) for row in cur.fetchall()]
    return jsonify(items)

@app.route("/update-stock/<int:product_id>", methods=["POST"])
def update_stock(product_id):
    data = request.json
    conn = get_db()
    conn.execute("UPDATE products SET stock = ? WHERE id = ?", (data["stock"], product_id))
    conn.commit()
    return jsonify(success=True)
#meine image eingefügt
def insert_sample_products():
    conn = get_db()
    cur = conn.cursor()

    products = [
        ("Filorga Filler", "Intensives Anti-Aging-Serum", 49.90, 20, "/images/filorga_filler.jpg"),
        ("NCEF Konzentrat", "Regenerierende Hautpflege", 42.00, 15, "/images/ncef.jpg"),
        ("Nutri-Creme", "Feuchtigkeit für sensible Haut", 25.50, 30, "/images/nutri.jpg")
    ]
    cur.executemany("""
        INSERT INTO products (name, description, price, stock, image_path)
        VALUES (?, ?, ?, ?, ?)
    """, products)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_sample_products()
    app.run(debug=True)

