# WillStore Inventory System
Link: https://willstore.adaptable.app/

## Tugas 2
### Pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   -  Pada saat proses pembuatan proyek Django baru, semua step-by-step yang dilakukan sama, hanya berbeda untuk nama project Django, dari shopping_list menjadi inventory. Kemudian untuk konfigurasi model di project inventory juga sama dengan tutorial. Untuk implementasi template, yang saya ubah adalah judul dari aplikasi web, sedangkan untuk name dan class masih sama, hanya mengubah value dari variabel tersebut di views.py. Untuk implementasi model, atribut pada objek Product mengalami penyesuaian dengan soal, yang di mana saya menambahkan atribut sebagai berikut:
      - nama = CharField
      - banyak = IntegerField
      - deskripsi = TextField
      - harga = IntegerField
      - jenis = CharField
   - Untuk migrasi model langkah yang diambil juga sama dengan tutorial. Untuk bagian menghubungkan view dengan template, step-by-step yang dilakukan juga sama, hanya berbeda untuk value dari key 'name' dan 'class' (disesuaikan dengan informasi pribadi). Untuk konfigurasi routing pada aplikasi main langkah-langkahnya sama, tetapi untuk routing URL proyek, saya melakukan sedikit modifikasi. Saya menambahkan path /main/ seperti pada soal tetapi saya juga menambahkan path kosong sehingga jika web dibuka tanpa path /main/ maka web akan tetap menampilkan page seperti pada /main/. Untuk unit testing, saya menggunakan 2 dari tutorial dan 2 lagi sebagai hasil experimen untuk unit testing Django yang saya lakukan.

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   - ![Bagan](https://github.com/NtapSlur/inventoryBang/assets/119404246/7e60e0fb-09c5-4ff0-a961-5f1c6858489f)
   - Penjelasan:
      - Pertama, client akan mengirim request ke web melalui browser
      - Kemudian, urls.py akan menghubungkan URL yang diterima dari request client ke URL yang sesuai
      - Setelah URL sesuai dengan yang direquest, views.py bertugas untuk memproses tampilan yang akan direturn (web response), yang di mana views.py akan mengecek berkas html dan mereturnnya sebagai web response. Jika ternyata html membutuhkan data dari database, maka views.py akan segera mengirim signal kepada models.py untuk segera mengambil data yang diperlukan dan ketika data sudah ada, maka views.py siap untuk mengreturn web response.

1. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   - Virtual Environment adalah sebuah tool untuk mengisolasi suatu proyek dengan library dan dependensi di satu tempat. Karena kemampuan virtual environment untuk mengisolasi suatu proyek, setiap virtual environment yang berbeda dapat memiliki versi-versi library dan dependensi yang berbeda-beda sehingga tidak mengganggu virtual environment lain yang membutuhkan library dan dependensi berbeda. Selain itu, menggunakan virtual environment dapat dikatakan lebih rapi dikarenakan semua library dan dependensi yang diperlukan sudah terletak di suatu environment dan tidak teracak-acak.
   - Sebenarnya, kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, dikarenakan tidak menggunakan virtual environment, maka library dan dependensi yang digunakan akan berasal dari penyimpanan secara global (di satu komputer). Hal ini akan menyulitkan jika terdapat dua proyek web Django berbeda yang membutuhkan versi Django yang berbeda juga. Karena versi Django yang digunakan berasal dari penyimpanan global komputer, maka tidak dapat menjalankan proyek Django yang memiliki perbedaan versi Django dengan versi global di komputer. Hal ini tentu dapat disolve dengan menggunakan virtual environment.
   - Jadi, sebaiknya buat suatu proyek Django dalam suatu virtual environment agar tidak perlu terjadi konflik untuk library dan dependensi. Dan juga, agar proyek Django yang dibuat dapat terlihat lebih rapi.

1. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   - MVC (Model - View - Controller)
      - MVC adalah suatu pola arsitektur yang terdiri atas tiga bagian:
         - Model
            - Komponen yang bertanggung jawab untuk mengelola data aplikasi dan logikanya
         - View
            - Komponen yang bertanggung jawab untuk menampilkan informasi dari model kepada user (Client-Side)
         - Controller
            - Komponen yang bertanggung jawab untuk mengontrol alur data kepada model berdasarkan perubahan data pada view
   - MVT (Model - View - Template)
      - MVT adalah suatu pola arsitektur software yang terdiri atas tiga bagian:
         - Model
            - Komponen yang bertanggung jawab untuk mengelola data, komponen ini juga dapat disebut sebagai interface dari data
         - View
            - Komponen yang bertanggung jawab untuk menampilkan informasi dari model kepada user (User Interface)
         - Template
            - Komponen yang menjembatani antara model dengan view. Komponen ini akan memindahkan data dari model ke view sehingga dapat ditampilkan sesuai dengan data yang diinginkan
   - MVVM (Model - View - ViewModel)
      - MVVM adalah suatu pola arsitektur software yang terdiri atas tiga bagian:
         - Model
            - Komponen yang bertanggung jawab untuk abstraksi data. Model dan Viewmodel bekerja secara bersamaan untuk mendapatkan dan menyimpan data
         - View
            - Komponen yang bertanggung jawab untuk menginformasikan aksi user kepada ViewModel dan untuk menampilkan data kepada user. Komponen ini mengobservasi ViewModel dan tidak mengandung logika untuk aplikasi. 
         - ViewModel
            - Komponen yang bertugas untuk mengkonversi data dari Model menjadi format yang dibutuhkan oleh View. Dapat dibilang bahwa ViewModel menjadi jembatan antara Model dengan View
   - Perbedaan utama dari ketiga pola arsitektur ini adalah pada MVC, pengatur alur logika aplikasi dilakukan oleh Controller. Untuk MVT, pengatur alur logika aplikasi dilakukan oleh Template. Dan untuk MVVM, pengatur alur logika aplikasi dilakukan oleh ViewModel. 

## Tugas 3
### Pertanyaan:
1. Apa perbedaan antara form POST dan form GET dalam Django?
   - Perbedaan utama dari POST dan GET adalah POST digunakan untuk mengirim data yang akan menyebabkan perubahan di server, seperti membuat, mengedit, atau menghapus data, sedangkan GET digunakan untuk mengirim request ke server untuk melihat, mengakses, dan mengambil data dari server tanpa mengubah isi dari server itu
   - Pada umumnya POST tidak di cache, sedangkan GET dapat di cache
   - Pada umumnya POST lebih secured karena data dikirim secara tersembunyi dalam body request HTTP, sedangkan GET kurang secured karena data terlihat di URL

1. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
   - XML menggunakan tag untuk mendefinisikan elemen-elemen data, serta atribut untuk memberikan informasi tambahan tentang elemen
   - JSON menggunakan pasangan key-value untuk menggambarkan datanya secara terstruktur (seperti Dictionary pada Python)
   - HTML pada umumnya hanya digunakan untuk menggambarkan struktur halaman web untuk ditampilkan ke browser, sehingga untuk menampilkan data, HTML perlu untuk menerima query terlebih dahulu dari views dan melakukan iterasi di HTML tersebut. Dengan melakukan hal itu, HTML baru dapat menampilkan data yang diinginkan

1. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   - Lebih cepat untuk memparsing data dari sisi server dengan JSON.parse()
   - Syntax yang lebih ringan dan berukuran lebih kecil, sehingga tidak memerlukan penyimpanan yang terlalu besar
   - Mendukung banyak bahasa pemograman lain

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
   - Untuk membuat form untuk menambahkan objek Product, saya mengikuti tutorial, hanya saja saya menambahkan field-field baru sesuai dengan yang saya butuhkan. 
   - Fungsi views dalam format HTML saya menggunakan for each pada main.html untuk menampilkan produk-produk yang sudah pernah dibuat, sedangkan fungsi views dalam format XML, JSON, XML by ID, dan JSON by ID saya mengikuti tutorial.
   - Membuat routing untuk semua fungsi yang ada pada views.py menyesuaikan dengan path yang diinginkan
   - Saya juga membuat suatu file default.html sehingga jika link dibuka tanpa path maka yang akan terbuka adalah default.html yang memiliki button untuk didirect ke main.html

XML by ID
![xmlbyid](https://github.com/NtapSlur/inventory/assets/119404246/f7290984-0af7-405f-88cc-dc7d8aa7085a)

XML
![xml](https://github.com/NtapSlur/inventory/assets/119404246/5bcdfc56-d24d-4a97-82f9-576eed081366)

JSON by ID
![jsonbyid](https://github.com/NtapSlur/inventory/assets/119404246/b3ae3ad7-b4df-4f32-a6ec-a6e09f281fbf)

JSON
![json](https://github.com/NtapSlur/inventory/assets/119404246/540973ec-6aee-4a9e-995c-2aaff90f917b)

HTML
![html](https://github.com/NtapSlur/inventory/assets/119404246/da3eb90e-9d78-4c3a-b4dc-b9e7d295181f)
