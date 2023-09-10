# WillStore Inventory System
Link: https://willstore.adaptable.app/

Pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   -  Pada saat proses pembuatan proyek Django baru, semua step-by-step yang dilakukan sama, hanya berbeda untuk nama project Django, dari shopping_list menjadi inventory. Kemudian untuk konfigurasi model di project inventory juga sama dengan tutorial. Untuk implementasi template, yang saya ubah adalah judul dari aplikasi web, sedangkan untuk name dan class masih sama, hanya mengubah value dari variabel tersebut di views.py. Untuk implementasi model, atribut pada objek Product mengalami penyesuaian dengan soal, yang di mana saya menambahkan atribut sebagai berikut:
      - nama = CharField
      - banyak = IntegerField
      - deskripsi = TextField
      - harga = IntegerField
      - jenis = CharField
   - Untuk migrasi model langkah yang diambil juga sama dengan tutorial. Untuk bagian menghubungkan view dengan template, step-by-step yang dilakukan juga sama, hanya berbeda untuk value dari key 'name' dan 'class' (disesuaikan dengan informasi pribadi). Untuk konfigurasi routing pada aplikasi main langkah-langkahnya sama, tetapi untuk routing URL proyek, saya melakukan sedikit modifikasi. Saya menambahkan path /main/ seperti pada soal tetapi saya juga menambahkan path kosong sehingga jika web dibuka tanpa path /main/ maka web akan tetap menampilkan page seperti pada /main/. Untuk unit testing, saya menggunakan 2 dari tutorial dan 2 lagi sebagai hasil experimen untuk unit testing Django yang saya lakukan.

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   - Tes
1. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   - Virtual Environment adalah sebuah tool untuk mengisolasi suatu proyek dengan library dan dependensi di satu tempat. Karena kemampuan virtual environment untuk mengisolasi suatu proyek, setiap virtual environment yang berbeda dapat memiliki versi-versi library dan dependensi yang berbeda-beda sehingga tidak mengganggu virtual environment lain yang membutuhkan library dan dependensi berbeda. Selain itu, menggunakan virtual environment dapat dikatakan lebih rapi dikarenakan semua library dan dependensi yang diperlukan sudah terletak di suatu environment dan tidak teracak-acak.
   - Sebenarnya, kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, dikarenakan tidak menggunakan virtual environment, maka library dan dependensi yang digunakan akan berasal dari penyimpanan secara global (di satu komputer). Hal ini akan menyulitkan jika terdapat dua proyek web Django berbeda yang membutuhkan versi Django yang berbeda juga. Karena versi Django yang digunakan berasal dari penyimpanan global komputer, maka tidak dapat menjalankan proyek Django yang memiliki perbedaan versi Django dengan versi global di komputer. Hal ini tentu dapat disolve dengan menggunakan virtual environment.
   - Jadi, sebaiknya buat suatu proyek Django dalam suatu virtual environment agar tidak perlu terjadi konflik untuk library dan dependensi. Dan juga, agar proyek Django yang dibuat dapat terlihat lebih rapi.
1. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   - MVC (Model - View - Controller)
      - MVC adalah suatu pola arsitektur yang terdiri atas tiga bagian:
         - Model
         - View
         - Controller
   - MVT (Model - View - Template)
      -
   - MVVM (Model - View - ViewModel)
      -
