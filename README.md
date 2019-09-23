# Deployment-Model-Flask
## Instruksi Penggunaan Model Prediksi Credit Scoring dengan Menggunakan Postman
#### Oleh Topik Zulkarnain

Repositori membahas tentang penggunaan model credit scoring yang bertujuan untuk memprediksi apakah seseorang layak untuk mendapatkan kredit berdasarkan beberapa parameter (kriteria) tertentu. Penggunaan model pada case ini adalah dengan menggunakan Postman API. Berikut adalah table of content tentang penjelasan model dan juga instruksi penggunaan model ini pada Postman API.


### Table of Content
1. Pengenalan Model <br>
   1.1 Data Credit Scoring <br>
   1.2 Model Credit Scoring <br>
   1.3 Flask <br>
2. Postman API<br>
   2.1 Hal yang perlu diketahui tentang Postman <br>
   2.2 Instruksi Deploy Model dengan Menggunakan Postman<br>

# 1 Pengenalan Model
## 1.1 Data
Data yang digunakan pada case ini (tersedia direpositori ini) adalah data historical kredit dengan 14 feature dan 1 label, dan dari data ini tidak semua feature akan digunakan. Feature yang digunakan adalah :
1. LIMIT_BAL = batas pemindahan saldo tagihan dari satu kartu kredit (yang digunakan saat ini) ke kartu kredit lain <br>
2. MARRIAGE = status pernikahan <br>
3. EDUCATION = tingkat pendidikan <br>
4. SEX = jenis kelamin <br>
5. AGE = usia  <br>

## 1.2 Model
Model yang digunakan untuk memprediksi credit scoring berdasarkan historical data adalah Random Forest dengan tingkat akurasi 81%. Model ini dibentuk dalam format .pkl sehingga model ini termasuk dengan data nya sudah dapat di deploy dengan mudah. model.pkl akan di deploy dalam Flask pada pythonanywher.com sehingga model ini dapat digunakan oleh siapapun.

## 1.3 Flask
Setelah tahap pembuatan model, maka selanjutnya dibentuk Machine Learning API dengan menggunakan Flask yaitu suatu web framework python. Dari Flask tersebut dapat digunakan sebagai server pada web pythonanywhere.com

# 2. Postman API
![Gambar Postman](https://4.bp.blogspot.com/-VqgPEhQKIa8/WoXNjwiAv5I/AAAAAAAHxh0/HXQ7aJycSaoK0TjQ2wuAjZqqxSKc6pLTACLcBGAs/s1600/postman_logo.png)
