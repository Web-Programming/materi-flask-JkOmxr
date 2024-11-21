from sqlalchemy.orm import joinedload # Mengimpor `joinedload` untuk eager loading
from flask import request, jsonify # Mengimpor objek `request` untuk menangkap data dari request, dan
`jsonify` untuk mengembalikan data JSON
from app import app, db # Mengimpor objek `app` dan `db` dari modul `app`
from models import Fakultas, Prodi, Mahasiswa # Mengimpor model Fakultas, Prodi, dan Mahasiswa
# Route GET untuk Fakultas
@app.route('/api/fakultas', methods=['GET']) # Endpoint untuk mendapatkan semua data Fakultas
def get_fakultas():
fakultas = Fakultas.query.all() # Query untuk mendapatkan semua data Fakultas dari database
output = []
for fac in fakultas: # Iterasi setiap Fakultas
prodi_list = [{'id': prodi.id, 'nama': prodi.nama} for prodi in fac.prodis]
# Mendapatkan daftar Prodi terkait
output.append({
'id': fac.id,
'nama': fac.nama,
'prodi': prodi_list # Tambahkan data Prodi ke dalam fakultas
})
return jsonify(output) # Mengembalikan data Fakultas dalam format JSON
# Output yang diharapkan Route GET Fakult