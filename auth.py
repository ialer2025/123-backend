import hashlib

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    password_hash = hashlib.sha256(data["password"].encode()).hexdigest()
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (data["username"], password_hash)).fetchone()
    if user:
        return jsonify({"id": user["id"], "username": user["username"], "is_admin": bool(user["is_admin"])})
    return jsonify({"error": "Invalid credentials"}), 401


#registerung & login (backend Flask)

import hashlib

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    password_hash = hashlib.sha256(data["password"].encode()).hexdigest()
    conn = get_db()
    conn.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", (data["username"], password_hash, False))
    conn.commit()
    return jsonify(success=True)

