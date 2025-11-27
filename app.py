from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menampilkan hasil input
@app.route('/hasil', methods=['POST'])
def hasil():
    nama = request.form['nama']
    email = request.form['email']
    pesan = request.form['pesan']
    return render_template('result.html', nama=nama, email=email, pesan=pesan)

# Menjalankan server Flask
if __name__ == '__main__':
    app.run(debug=True)
