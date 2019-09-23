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
   2.2 Installasi Postman <br>
   2.3 Instruksi Deploy Model dengan Menggunakan Postman<br>

# 1. Pengenalan Model
## 1.1 Data
Data yang digunakan pada case ini (tersedia direpositori ini) adalah data historical kredit dengan 14 feature dan 1 label, dan dari data ini tidak semua feature akan digunakan. Feature yang digunakan adalah :
1. LIMIT_BAL = batas pemindahan saldo tagihan dari satu kartu kredit (yang digunakan saat ini) ke kartu kredit lain <br>
2. MARRIAGE = status pernikahan <br>
3. EDUCATION = tingkat pendidikan <br>
4. SEX = jenis kelamin <br>
5. AGE = usia  <br>

## 1.2 Model
Model yang digunakan untuk memprediksi credit scoring berdasarkan historical data adalah Random Forest dengan tingkat akurasi 81%. Model ini dibentuk dalam format .pkl sehingga model ini termasuk dengan data nya sudah dapat di deploy dengan mudah. model.pkl akan di deploy dalam Flask pada python anywhere sehingga model ini dapat digunakan oleh siapapun.

## 1.3 Flask
Setelah tahap pembuatan model, maka selanjutnya dibentuk Machine Learning API dengan menggunakan Flask yaitu suatu web framework python. Dari Flask tersebut dapat digunakan sebagai server pada web python anywhere. 

# 2. Postman API
![Gambar Postman](https://4.bp.blogspot.com/-VqgPEhQKIa8/WoXNjwiAv5I/AAAAAAAHxh0/HXQ7aJycSaoK0TjQ2wuAjZqqxSKc6pLTACLcBGAs/s1600/postman_logo.png)

## 2.1 Hal yang Perlu Diketahui Tentang Postman
Postman adalah client HTTP yang sangat bagus untuk web service testing, mengembangkan dan mendokumenkan API dengan memperbolehkan pengguna untuk menaruhkan request HTTP yang sederhana dan yang kompleks. Postmand tersedia pada Google Chrome, pada tahap berikutnya akan dijelaskan bagaimana proses installasi Postman diChrome. Postman REST Client adalah salah satu applikasi yang paling produktif di Chrome Web Store, dengan lebih dari 348.000 user dan lebih dari 63.000 collections shared lewat Postman, itulah alasannya kita akan memakai postman untuk mendeploy model. 

## 2.2 Installasi Postman
Download Postman pada [Chrome Web Store](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), setelah didownload lalu add to chrome extension. Jika sudah dilakukan, launch postman sehingga terdapat tampilan awal Postman seperti gambar dibawah
![Gambar Awal Postman](https://developers.sap.com/tutorials/api-tools-postman-install/_jcr_content.github-proxy.1564056317.file/03.png)

## 2.3 Instruksi Deploy Model dengan Menggunakan Postman
### Step 1 
Step 1, pada tampilan awal Postman pilih header lalu pada kolom key isi dengan Content-type, selanjutnya isi value dengan application/json. Jika sudah maka tampilan akan seperti dibawah 
![Step 1](https://github.com/TopikZulkarnain/Deployment-Model-Flask/blob/master/Step1.JPG?raw=true)

### Step 2
Langkah selanjutnya pilih kolom Body,  klit raw, kemudian isi params dengan 'znik41@pythonanywhere.com/api' dengan metode POST. Gambar dari step ini dapat dilihat dibawah ini
![Step 2](https://github.com/TopikZulkarnain/Deployment-Model-Flask/blob/master/step2.JPG?raw=true)

### Step 3
Pada langkah ini, akan diinput nilai-nilai dari feature untuk memprediksi status credit scoring dengan contoh-contoh sebagai berikut :

#### Untuk satu observasi dapat dilihat pada gambar berikut :
![Step 3](https://github.com/TopikZulkarnain/Deployment-Model-Flask/blob/master/step3.JPG?raw=true)
Pada gambar diatas terlihat bahwa hanya dicari status credit scoring hanya satu orang (satu observasi) berdasarkan feature yang ada pada model.pkl . Berdasarkan hasil prediksi, didapatkan kesimpulan bahwa status credit scoringnya 'not pass'

#### Untuk dua atau lebih observasi dapat dilihat pada gambar berikut :
![Step 4](https://github.com/TopikZulkarnain/Deployment-Model-Flask/blob/master/step4.JPG?raw=true)
Untuk input dua atau lebih orang pada satu kali request dengan cara mengulangi input dan memishkan antara inputnya dengan separator ',' sebagai mana pada contoh gambar diatas (pada contoh diatas 10 observasi). Didapatkan bahwa hanya 3 orang yang memiliki status credit scoring "pass"

ini adalah akhir dari instruksi penggunaan model prediksi credit scoring dengan menggunakan Postman.

Semoga bermanfaat 

n_n
