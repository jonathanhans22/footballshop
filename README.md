"# footballshop" 
Nama : Jonathan Hans Emanuelle

NPM : 2406414025

Kelas : PBP B

----------------TUGAS 3----------------
1. Data delivery sangat penting dalam implementasi sebuah platform karena platform modern pada dasarnya adalah kumpulan dari berbagai komponen terpisah yang harus dapat berkomunikasi secara efektif. Komponen-komponen ini mencakup front end yang dilihat oleh pengguna, logika di server , aplikasi mobile, hingga web development nya . Data delivery, yang umumnya diwujudkan melalui API, berfungsi sebagai jembatan penghubung yang memungkinkan semua bagian ini untuk bertukar informasi secara real-time dan terstandarisasi. data delivery juga krusial untuk menjalankan platform dengan layanan pihak ketiga, seperti sistem pembayaran. tanpa adanya sistem pengiriman data yang andal, setiap komponen akan terisolasi, sehingga platform tidak dapat berfungsi sebagai satu kesatuan.


2. ringan dan Cepat: Karena sintaks yang minimalis, ukuran data JSON lebih kecil daripada XML yang dimana perpindahan data melalui jaringan lebih cepat dan proses parsing lebih efisien.

ekosistem JavaScript: JSON adalah bagian dari JavaScript. Di era di mana JavaScript mendominasi pengembangan web , menggunakan JSON terasa alami dan tidak memerlukan library tambahan.

kemudahan Penggunaan: Strukturnya yang sederhana membuatnya sangat mudah dipelajari dan diimplementasikan di hampir semua bahasa pemrograman modern.

dan kebetulan saya juga sudah pernah menyentuh JSON saat saya bermagang menjadi web dev di suatu perusahaan. itu sangat mudah digunakan dan dipahami, saya dalam waktu singkat saya sudah paham cara kerja JSON

3. method is_valid() itu sepert  satpam atau  untuk data yang dikirim lewat form di Django. sebelum data diizinkan masuk lebih jauh ke dalam sistem (misalnya untuk disimpan ke database), method ini bakal ngecek dulu semuanya. dia bakal mastiin data yang diinput pengguna udah sesuai sama semua aturan yang kita buat, misalnya field yang wajib diisi, panjang karakter maksimal, sampai tipe datanya bener (contohnya kolom umur harus diisi angka bukan huruf). Kalau semua datanya lolos pengecekan, is_valid() bakal membersihkan data itu dan menaruhnya di sebuah tempat aman yang namanya form.cleaned_data, yang isinya data siap pakai. Tapi, kalau ada data yang ngaco, method ini bakal ngumpulin pesan error untuk setiap field yang salah, jadi kita bisa kasih tau ke pengguna apa yang perlu mereka perbaiki. Jadi, kita butuh banget method ini sebagai filter utama untuk menjaga kualitas data, mencegah data sampah atau bahkan data berbahaya masuk ke sistem, sekaligus ningkatin pengalaman pengguna dengan ngasih feedback yang jelas.

4. csrf_token itu pada dasarnya adalah jurus andalan Django buat nangkal serangan yang namanya CSRF (Cross-Site Request Forgery). contohnya kita lagi login di akun media sosial atau toko online. Terus, di tab lain, kita nggak sengaja buka link jebakan dari website lain. Tanpa kita sadar, website jebakan itu diam-diam ngirim perintah ke akunmu—misalnya perintah untuk "update status aneh" atau "hapus semua barang di keranjang". Servernya bisa ketipu karena perintah itu dikirim bareng "tiket login" atau biasa disebut cookie kita, jadi kelihatannya itu perintah beneran dari kita. di sinilah csrf_token berperan kayak kode rahasia atau tiket sekali pakai yang cuma diketahui sama browser mu dan server Django. Setiap kali Django nampilin form, dia ngasih satu kode unik yang tersembunyi. Waktu kita submit formnya, kode rahasia ini harus ikut dikirim. Website jebakan tadi nggak bakal tau kode rahasia ini, jadi setiap perintah palsu yang dia kirim pasti bakal ditolak mentah-mentah sama Django karena nggak punya "tiket" yang valid. Makanya, kalau kita lupa pasang csrf_token, kita kayak ngebiarin pintu keamanan kebuka lebar, bikin penyerang gampang "nitip" perintah berbahaya atas nama user yang lagi login.

5.  - buat awal saya mengikuti tutorial untuk xml json nya di views
    - selanjutnya saya membuat default html untuk form dan show detail nya
    - kalau sudah saya sambungkan dengan views dimana saya membuat fungsi create_product yang berfungsi untuk memunculkan form nya
    - lalu kalau sudah saya menyempurnakan isi dari html nya
    - saya tidak lupa untuk menambahkan di urls py nya untuk bisa nyambung path nya

6. tidak ada, menurut saya sudah jelas semua dan mudah dipahami. terima kasih 

link postman
https://docs.google.com/document/d/1HWYqaDsvJgzHOPaWzgw2DnTjjCmL82fk_5FJP5YmbyE/edit?usp=sharing


----------------TUGAS 2----------------
1. jadi step by step nya 
    - saya membuat repository di github terlebih dahulu
    - lalu kalau sudah saya kaitkan dengan folder yang sudah saya buat
    - ketika sudah nyambung saya buat main yang sama seperti di tutorial (jangan lupa env,requirments, buat templates berisikan main.html, dan masih banyak lagi)
    - jika sudah terpasang semua saya membuat models nya terlebih dahulu dengan menambahkan brand karena menurut saya di footballshop brand adalah suatu yang penting juga
    - selanjutnya saya melakukan routing untuk di urls nya jadi saya bisa menyambungkan untuk ke main html nya
    - jika semua sudah saya push ke pws master agar bisa nyambung ke pws nya dan bisa dilihat oleh teman-teman saya melalui link nya
2.  https://www.google.com/url?sa=i&url=https%3A%2F%2Fpbp-fasilkom-ui.github.io%2Fganjil-2023%2Fassignments%2Ftutorial%2Ftutorial-1%2F&psig=AOvVaw3eRnGBM5YJ8i4kaiUdwe-k&ust=1757502407505000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCPDotObEy48DFQAAAAAdAAAAABAE = sumber
    pengguna meminta halaman web dengan mengetik URL 
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