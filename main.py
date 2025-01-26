from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)  # Inisialisasi Flask
app.secret_key = 'secret_key_for_session'

# Simpan akun di memori untuk keperluan demo (gunakan database di produksi)
users = {
    'admin@example.com': {
        'password': 'admin123',  # Kata sandi admin
        'role': 'admin'         # Tipe akun admin
    }
}
@app.route('/')
def home():
    # Render file HTML dari folder templates
    return render_template('index.html')

@app.route('/admin')
def admin():
    # Render file HTML dari folder templates
    return render_template('home_admin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/product_list')
def product_list():
    return render_template('product_list.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Login logika
        user = users.get(email)
        if user and user['password'] == password:
            session['user'] = email
            session['role'] = user['role']
            return render_template('dashboard.html')
            #return redirect(url_for('dashboard'))
        else:
            return render_template('join.html', error="Email atau kata sandi salah.")
    return render_template('join.html')

@app.route('/create_admin', methods=['GET', 'POST'])
def create_admin():
    if 'role' in session and session['role'] == 'admin':
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # Menambahkan akun admin baru
            if email in users:
                return render_template('create_admin.html', error="Email sudah terdaftar.")
            users[email] = {'password': password, 'role': 'admin'}
            return redirect(url_for('dashboard'))
        return render_template('create_admin.html')
    return redirect(url_for('join'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('join'))


if __name__ == '__main__':
    # Jalankan aplikasi Flask
    app.run(debug=True)

#myenv\Scripts\activate
