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
   Untuk migrasi model langkah yang diambil juga sama dengan tutorial. Untuk bagian menghubungkan view dengan template, step-by-step yang dilakukan juga sama, hanya berbeda untuk value dari key 'name' dan 'class' (disesuaikan dengan informasi pribadi). Untuk konfigurasi routing pada aplikasi main langkah-langkahnya sama, tetapi untuk routing URL proyek, saya melakukan sedikit modifikasi. Saya menambahkan path /main/ seperti pada soal tetapi saya juga menambahkan path kosong sehingga jika web dibuka tanpa path /main/ maka web akan tetap menampilkan page seperti pada /main/. Untuk unit testing, saya menggunakan 2 dari tutorial dan 2 lagi sebagai hasil experimen untuk unit testing Django yang saya lakukan.
   
1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   - Tes
1. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   - Tes
1. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   - Tes
