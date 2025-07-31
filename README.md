FRONTEND   REACT + CSS
BACKEND    FLASK + SQLITE
HOSTING FRONTEND NETLIFY
HOSTING BACKEND RENDER

WOLLTE AUTHENTIFIZIERUNG lOGIN & REGISTRIERUNG
ADMIN -Produktpflege und Lagerverwaltung Zahlung Simulierte Zahlung /stripe möglich! --> daran hab ich gearbeitet aber ist nicht fertig.

🧱 Projektstruktur
skincare-shop/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── database/
│   │   ├── shop.db
│   │   └── schema.sql
├── frontend/
│   ├── public/images/        ← Produktbilder
│   ├── src/
│   │   ├── App.js
│   │   ├── Product.js
│   │   ├── AdminPanel.js
│   │   ├── CartContext.js
│   │   ├── LoginForm.js
│   │   ├── RegisterForm.js
│   │   ├── Checkout.js
│   │   └── styles.css

in Backend :
-> pip install -r requirements.txt
sqlite3 database/shop.db
phython app.py

Installation von SQL

Frontend (React 
npm install 
npm start
npm run build

Render Backend Github push-> New Web Service -> Phyton app.py

Funktion:
-Registrierung & Login für Kunden und Admin
-Proukte anzeigen mit Bild, Beschreibung, Preis
-Lagerbestand prüfen & graue Darstellung bei Ausverkauf
-Admin-Modul: Produkte hinzufügen, löschen, Lager ändern
-Warenkorb mit dynamische Anzahl und automatischer Prüfung
-Checkout: Einkauf bestätigen oder via Stripe (optional)

