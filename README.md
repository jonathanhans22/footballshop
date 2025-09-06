"# footballshop" 
Nama : Jonathan Hans Emanuelle

NPM : 2406414025

Kelas : PBP B

1. jadi step by step nya 
    - saya membuat repository di github terlebih dahulu
    - lalu kalau sudah saya kaitkan dengan folder yang sudah saya buat
    - ketika sudah nyambung saya buat main yang sama seperti di tutorial (jangan lupa env,requirments, buat templates berisikan main.html, dan masih banyak lagi)
    - jika sudah terpasang semua saya membuat models nya terlebih dahulu dengan menambahkan brand karena menurut saya di footballshop brand adalah suatu yang penting juga
    - selanjutnya saya melakukan routing untuk di urls nya jadi saya bisa menyambungkan untuk ke main html nya
    - jika semua sudah saya push ke pws master agar bisa nyambung ke pws nya dan bisa dilihat oleh teman-teman saya melalui link nya
2.  pengguna meminta halaman web dengan mengetik URL 
    ->  menerima permintaan HTTP GET untuk path ->  
    File urls.py seperti papan petunjuk atau daftar isi, Django mencari pola URL yang cocok dengan yang diminta user, nanti Django akan memanggil fungsi dari views.py 
    -> View akan berkomunikasi dengan models.py untuk mengambil data produk dari database 
    -> masuk ke models.py,  models.py mendefinisikan struktur tabel database,  Data produk (nama, harga, deskripsi) dikembalikan ke views.py 
    ->  Setelah mendapatkan data produk, views.py akan menggabungkan data tersebut dengan sebuah template HTML, lalu view mengirimkan data produk ke dalam template 
    -> Lalu nanti template akan menyesuaiakn data yang sudah ada, nanti hasil akhirnya adalah sebuah file HTML lengkap yang siap dikirim. HTML ini juga dinamis sesuai dengan yang data yang di request -> sekarang memiliki halaman HTML yang utuh dari yang diminta di awal
    -> terakhir  browser nya akan menerima respons berupa kode HTML, browser kemudian membaca HTML tersebut dan menampilkannya sebagai halaman web yang bisa dilihat oleh pengguna.
3. settings.py adalah file pertama yang dibaca Django saat proyek dijalankan. File ini mengatur semua "aturan main" sebelum permintaan (request) dari pengguna diproses oleh urls.py dan views.py. contoh nyaq seperti ini Bayangkan proyek Django Anda adalah sebuah roket yang siap untuk diluncurkan. Maka, file settings.py adalah ruang kendali nya. Sebelum roket (aplikasi web) bisa diluncurkan atau bahkan merespons perintah apa pun, di Ruang Kendali Misi harus mengatur semuanya terlebih dahulu. Nah jadi sama seperti web nya settings ini sebagai control awal dari semua web nya itu berjalan
4. fungsi dari  makemigrations tidak mengubah database Anda sama sekali tapi fungsinya untuk membuat catatan dari perubahan yang Anda buat di models.py . lalu kedua migrate ini berfungsi sebagai membaca file-file migrasi (catatan), lalu enerjemahkannya menjadi perintah SQL, lalu terakhir mengeksekusi perintah SQL tersebut untuk mengubah database Anda secara fisik (misalnya menambah kolom atau tabel baru).
5. karena ini kan pembelajaran pertama kita jadi anggap lah kita sebagai pemula. Bayangkan Anda ingin memasak. Anda bisa membeli setiap bahan dan alat masak secara terpisah, atau Anda bisa membeli sebuah meal kit premium yang sudah berisi semua bahan berkualitas dan instruksi yang jelas. Nah karena Django ini sudah menjadi satu kesatuan karena di framework lain kita harus memilih sendiri cara terhubung ke database (ORM), cara mengelola otentikasi pengguna, cara membuat panel admin, dan lain-lain. Karena menggunakan Django kita sebagai pemula bisa langsung fokus mempelajari konsep inti pengembangan web (seperti model data, logika bisnis, dan tampilan) tanpa harus pusing merakit alat-alat dasarnya terlebih dahulu.
6. tidak ada feedback, semua aman, dan jelas untuk penjelasan tutorial nya.