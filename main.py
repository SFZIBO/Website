from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi SQLAlchemy
db = SQLAlchemy(app)

# Model untuk tabel 'Item'
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Membuat tabel
with app.app_context():
    db.create_all()

# Endpoint untuk menambah item
@app.route('/api/items', methods=['POST'])
def add_item():
    name = request.json.get('name')
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added!"}), 201

# Endpoint untuk mendapatkan item
@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
