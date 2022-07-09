OLEH : Budi Santoso | BudiAtu.GITHUB.IO | 11 Januari 2022

=============================================================================================================================
STEP 1 : GENERATE CNN MODEL AS .H5
=============================================================================================================================

▷ Siapkan model.h5 kamu, pastikan size maksimal 20MB. Bagaimana cara membuat model CNN dibawah 20MB? Gunakan arsitektur
  Pre-trained model MobileNetV2 (include_top=False), lalu sesuaikan bagian top/classifier/fully connected layernya, lalu
  lakukan training lalu save, model yang tergenerate hanya akan berukuran 10-30MB (hanya jika Dense dan jumlah Neuron
  didalamnya tidak terlalu banyak, namun jika jumlah Neuron banyak, ini akan memperbesar size model yang tergenerate).
▷ Jika bingung, gunakan template coding CNN siap pakai di folder "01-klasifikasi-cabai-cnn-google-colab" by Budi.S.
▷ Atau langsung next ke STEP 2 untuk memakai model yang sudah ada (studi kasus : klasifikasi 2 penyakitcabai dan 1 cabai sehat).

=============================================================================================================================
STEP 2 : .H5 MODEL TO FLASK APP PYTHON		Sumber: https://github.com/mtobeiyf/keras-flask-deploy-webapp
=============================================================================================================================

▷ Install Miniconda, download di: https://docs.conda.io/en/latest/miniconda.html
▷ Mulai dari sini setiap perintah $... dibawah gunakan "Anaconda Prompt Miniconda3"
▷ Buat folder dengan nama cabai-classifier, lalu buka "Anaconda Prompt Miniconda3"

$ conda -V					Tampilkan versi miniconda
$ cd /d anggrek-classifier			Pindah ke folder project cabai-classifier
$ conda create --name skripsi python=3.6	Buat Environment (env) baru dengan python versi 3.6.12
$ conda env list				Tampilkan seluruh env yang tersedia
$ conda activate skripsi			Aktifkan env skripsi
$ conda list --name skripsi			Tampilkan seluruh package dalam env skripsi
$ conda remove --name <nama_env> --all		⚠️TAMBAHAN: Hapus environment tertentu yang dipilih

$ pip install Flask==1.1.1
$ pip install gunicorn==20.0.4
$ pip install gevent==1.4.0
$ pip install Pillow==6.1.0
$ pip install tensorflow-cpu==2.2
$ pip install tensorflow-gpu==2.2		⚠️TAMBAHAN: Jika ingin memakai GPU (size package besar = 450MB)

▷ Atau install semua sekaligus : $ pip install Flask==1.1.1 gunicorn==20.0.4 gevent==1.4.0 Pillow==6.1.0 tensorflow-cpu==2.2

$ pip freeze					Tampilkan seluruh package dalam env skripsi beserta versinya
$ pip freeze > requirements.txt			Simpan info seluruh package kedalam file requirements.txt (nanti dipakai)

▷ Copy paste template coding Flask Web App CNN siap pakai di folder "02-deploy-cnn-model-flask-framework" ke folder project
▷ Jika kamu menggunakan studi kasus dan model kamu sendiri (bukan contoh studi kasus dan model anggrek-classifier),
  kamu perlu modifikasi file "app.py" dan simpan model kamu kedalam folder "models"

$ python app.py					Run project cabai-classifier, buka di default : http://127.0.0.1:5000/

▷ Daftar dan login Heroku di : https://www.heroku.com/
▷ Klik tombol "Create new app", lalu beri nama app dengan nama "anggrek-classifier" (sesuaikan nama jika sudah dipakai)
▷ Klik tombol "Open app", maka project akan terbuka secara online, misal: https://cabai.herokuapp.com/
▷ Install Git (jika belum ada di pc kamu) di : https://git-scm.com/downloads
▷ Install Heroku-CLI di : https://devcenter.heroku.com/articles/heroku-cli#download-and-install
▷ Buka "Anaconda Prompt Miniconda3" dan jalankan perintah dibawah ini

$ cd /d cabai			Masuk/pindah ke folder project cabai-classifier sebelumnya (STEP 2)
$ conda activate skripsi			Aktifkan env skripsi
$ heroku login					Login ke heroku
$ pip install virtualenv			Install virtualenv (harus, untuk keperluan deployment)
$ virtualenv env				Buat virtualenv dalam folder project (env local project dalam env skripsi)
$ env\Scripts\activate				Aktifkan env local project (check folder env/Scripts/activate.bat)
$ deactivate					⚠️TAMBAHAN: Nonaktifkan env local project
$ pip install Flask==1.1.1 gunicorn==20.0.4 gevent==1.4.0 Pillow==6.1.0 tensorflow-cpu==2.2	Install semua kebutuhan

$ git init					Inisialisasi git ke folder project
$ heroku git:remote -a anggrek-classifier	⚠️SESUAIKAN⚠️ (Hubungkan ke project di heroku)
$ pip freeze > requirements.txt			Simpan info seluruh package kedalam file requirements.txt (nanti dipakai)
$ git add .					Masukkan semua perubahan file baru kedalam git
$ git commit -am "siap push!"			Tambahan catatan perubahan kedalam git
$ git push heroku master			Push & Compile python project ke heroku

▷ Reload project (dalam kasus ini: https:/cabai.herokuapp.com/)
▷ Selesai! Selamat! sekarang project Deep Learning CNN kamu sudah Live! semua orang bisa mengakses.
▷ Catatan:
  - Saat push & compile project, batas maksimal seluruh file termasuk package yaitu 500MB
  - Pastikan kecepatan upload internet kamu cepat, jika lambat akan terjadi error karena timeout
  - Pastikan model cnn (.h5) yang digunakan maksimal tidak lebih dari 20MB jika memungkinkan
  - Didalam "app.py" ada alternative load model via URL, namun ini memberatkan project saat online

=============================================================================================================================
STEP 3++ : CONTOH APLIKASI FLASK SEDERHANA 	(SEBAGAI KERANGKA CONTOH PENULISAN PROJECT DI FLASK)
=============================================================================================================================

>>> app.py isi dengan:

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Welcome!!!</h1>"
if __name__ == '__main__':
    app.run(debug=True)

>>> Procfile isi dengan:

web: gunicorn app:app
