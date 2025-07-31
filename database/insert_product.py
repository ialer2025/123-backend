import sqlite3

def insert_products():
    conn = sqlite3.connect("database/shop.db")
    cursor = conn.cursor()

    cursor.executescript("""
        INSERT INTO products (name, description, price, stock, image_path)
        VALUES
        ('Filorga NCEF', 'Intensiv regenerierendes Serum 30ml', 112.20, 5, 'filorga.jpg'),
        ('Nutri Filler', 'Reichhaltige Anti-Aging Pflege 50ml', 80.40, 3, 'nutri.jpg'),
        ('Time Filler 5XP', 'Glättende Creme gegen Falten 30ml', 89.00, 4, 'time.jpg');
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_products()