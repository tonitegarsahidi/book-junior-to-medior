# **Bab 13: Buku Harian Sistem**

## **13.1 Error Aneh di Production**

Pagi itu, kantor Garda Teknologi Nusantara mendadak riuh.

Pakde Suhar setengah berlari dari ruang depan, telepon genggamnya masih menempel di telinga. "Lin! Binto! Pak Haji telepon! Katanya aplikasinya error, sales-nya gak bisa input produk baru!" Wajahnya yang biasanya kalem kini memerah.

Mas Alin mengangkat tangannya dengan tenang. "Tenang dulu, Pakde. Bilang ke Pak Haji, kita sedang cek. Lima belas menit."

Pakde mengangguk, lalu kembali bicara di telepon dengan nada yang berusaha menenangkan: "*Nggih*, Pak Haji. Sebentar ya. Tim kami sedang menangani..."

Hampir bersamaan, Mbak Rara dari meja kerjanya bersuara. "Mas Binto! Mas Alin! Fitur tambah produk di Kalimantan memang error!"

Binto yang baru saja menyesap teh hangatnya buru-buru menoleh. "Error gimana, Mbak?"

Mbak Rara berjalan cepat ke meja Binto, membawa laptopnya. "Ini, lihat. Aku coba tambah produk baru. Harusnya kalau validasi gagal, pesannya jelas: 'Nama produk harus diisi' atau 'Harga harus angka'. Tapi ini cuma muncul 'Gagal menyimpan data'. Gak informatif."

Binto membuka laptopnya, mencoba fitur yang sama di lingkungan lokal. Normal. Ia coba di staging. Normal.

"Hanya di production yang error," gumamnya.

Cahyo yang duduk di pojok ikut penasaran. "Wah, aneh ya, Mas. Padahal kodenya sama."

Mas Alin yang sedari tadi diam akhirnya bangkit dari kursinya. "Kita lihat log-nya."

## **13.2 Mencari Jejak**

Mas Alin membuka terminal dan SSH ke server production proyek Kalimantan. Ia navigasi ke folder storage/logs dan membuka file laravel.log. Layar menampilkan ribuan baris teks.

"Ini log-nya. Setiap kejadian di aplikasi tercatat di sini. Error, warning, info—semua ada." Mas Alin menggulir perlahan. "Kita cari sekitar jam tadi pagi."

Matanya menyusuri baris-baris log. Tangannya berhenti di satu titik.

"local.ERROR: Unable to write to file... Disk quota exceeded."

Ia membaca ulang. "Disk penuh."

Mas Andik yang kebetulan lewat membawa gelas kopi langsung berhenti. "Disk penuh? Production?" Ia buru-buru mengecek server. Benar saja. Partisi tempat aplikasi menyimpan file temporary hampir 100% terpakai. Rupanya ada script lama yang menghasilkan file cache tanpa pernah dibersihkan.

"Wah, ini kenapa gak ketahuan dari kemarin," gumam Mas Andik sambil mulai membersihkan file-file tak terpakai.

Beberapa menit kemudian, disk kembali lega. Mbak Rara mencoba lagi fitur tambah produk. Kali ini berhasil.

"Alhamdulillah," desahnya.

Pakde Suhar langsung mengambil teleponnya dan menghubungi Pak Haji. Binto bisa mendengar percakapannya dari meja sebelah.

"*Nggih*, Pak Haji. Sudah beres. Tadi ada file yang numpuk di server, sudah kami bersihkan. *InsyaAllah* gak terulang lagi. Maaf ya mengganggu pagi-paginya."

Suara Pak Haji di ujung sana terdengar lega. Pakde menutup telepon dengan senyum. Binto mencatat dalam hati: *menyelesaikan masalah teknis itu setengah pekerjaan. Setengahnya lagi adalah mengomunikasikannya ke klien dengan baik.*

## **13.3 Kenapa Log Penting?**

Setelah insiden reda, Cahyo mendekati Binto. "Mas, kok kita bisa tahu penyebabnya? Kan error-nya cuma 'Gagal menyimpan data'."

Binto tersenyum. "Karena ada log, Dik. Sistem mencatat setiap kejadian. Tanpa log, kita cuma bisa nebak. Mungkin kita kira bug di kode, padahal cuma disk penuh."

Mas Alin mendengar dan ikut duduk. "Betul. Log itu saksi bisu. Dia cerita apa yang terjadi, kapan, dan oleh siapa. Kode cuma tunjukin apa yang *seharusnya* terjadi. Log tunjukin apa yang *benar-benar* terjadi."

Cahyo manggut-manggut. "Jadi kayak buku harian?"

"Persis. Buku harian sistem."

## **13.4 Logging di Framework Modern**

Mas Alin membuka kembali file laravel.log di laptopnya. "Lihat, Dik. Framework seperti Laravel itu otomatis bikin file log. Setiap error, warning, info—tercatat di sini. Kita tinggal buka foldernya."

Ia menunjukkan isi file itu. "Ini sudah ada sejak project dibuat. Tinggal kita manfaatkan. Gak perlu bikin sistem logging dari nol."

Binto menimpali. "Dulu saya kira logging itu ribet. Ternyata tinggal pakai yang sudah disediakan."

"Itulah enaknya pakai framework modern," kata Mas Alin. "Tapi tetap kita harus tahu cara bacanya dan cara nambahin log sendiri."

## **13.5 Level Severity: Info, Warning, Error, Critical**

Mas Alin menyorot beberapa baris di file log.

"Coba perhatikan. Setiap baris log punya level."

Ia menunjuk satu per satu.

* \[2024-03-15 08:30:15\] production.INFO: User 123 login.  
* \[2024-03-15 09:12:03\] production.WARNING: Stok produk "Rinso 1kg" tinggal 5\.  
* \[2024-03-15 10:05:22\] production.ERROR: Unable to write to file. Disk quota exceeded.

"INFO untuk kejadian normal—user login, pesanan dibuat. WARNING untuk sesuatu yang perlu perhatian tapi belum fatal—stok menipis, API lambat merespons. ERROR untuk kesalahan yang bikin fitur gagal—disk penuh, database error. Ada juga CRITICAL untuk yang fatal—sistem down total."

Cahyo mencatat di buku kecilnya. "Jadi gak semua log sama pentingnya?"

"Betul. Dengan level ini, kita bisa filter. Kalau lagi sibuk, kita fokus ke ERROR dan CRITICAL dulu. Kalau lagi santai, baru lihat WARNING."

## **13.6 Log Bisa Dialirkan ke Tools Khusus**

Mas Alin melanjutkan. "Ngomong-ngomong soal log, sebenarnya file kayak laravel.log ini cuma cara paling sederhana. Di proyek yang lebih besar, log biasanya dialirkan ke tools khusus."

"Kayak apa, Mas?" tanya Cahyo.

"Dulu saya pernah pakai Sentry. Setiap kali ada error di production, langsung muncul di dashboard Sentry. Bisa lihat detail error, grafik kejadian, bahkan notifikasi otomatis ke Telegram. Jadi gak perlu SSH ke server dan buka file log manual."

Ia menyebutkan beberapa nama lain. "Ada juga Seq, ELK—Elasticsearch, Logstash, Kibana—atau SigNoz. Prinsipnya sama: mengumpulkan log dari berbagai sumber, menampilkannya di satu tempat, dan memudahkan pencarian."

"Kita di sini pakai?" tanya Binto.

"Belum. Untuk tim sekecil kita, file log masih cukup. Tapi gak ada salahnya tahu. Nanti kalau proyek makin besar, kita bisa pakai."

## **13.7 Log vs Database: Jangan Salah Pilih**

Binto teringat sesuatu. "Mas, saya pernah lihat di forum, ada yang nyimpan log ke database. Itu boleh?"

Mas Alin mengangguk. "Boleh, untuk kasus tertentu. Misalnya, kita mau catat setiap request dan response dari API pihak ketiga—kayak API RajaOngkir atau Midtrans. Itu bisa disimpan di tabel api\_logs. Nanti kalau ada sengketa atau klaim, kita punya bukti."

"Tapi..." ia mengangkat telunjuk, "log yang sebenarnya tetap harus ada di file atau tools logging. Kenapa?"

Binto berpikir. "Karena... database pakai transaksi?"

"Tepat. Bayangin kita simpan request-response ke tabel api\_logs. Terus terjadi error di tengah proses. Transaksi database di-*rollback*. Data di api\_logs ikut batal. Padahal error-nya beneran terjadi. Kita jadi kehilangan jejak."

"Tapi kalau kita tulis ke file log," Mas Alin melanjutkan, "file log gak terpengaruh transaksi database. Error tetap tercatat. Kita bisa tahu apa yang salah."

Cahyo manggut-manggut. "Jadi dua-duanya boleh, asal tahu batasannya."

"Persis."

## **13.8 Log Rotation: Jangan Sampai Disk Penuh**

Mas Andik yang sudah selesai membersihkan disk ikut nimbrung. "Ngomong-ngomong soal log, kalian tahu kenapa disk production bisa penuh tadi?"

"Banyak file sampah?" tebak Cahyo.

"Bukan cuma itu. File laravel.log\-nya sendiri udah gede banget. Ratusan megabyte. Itu karena gak pernah di-*rotate*."

"Rotate?" Cahyo mengulang.

"Iya. Log Rotation. File log yang sudah lama diarsipkan atau dihapus. Jadi gak numpuk selamanya."

Mas Alin menambahkan. "Di Laravel, kita bisa atur log rotation harian. Jadi setiap hari bikin file baru: laravel-2024-03-15.log. File lama bisa dihapus otomatis setelah beberapa hari. Jadi disk tetap aman."

"Ooh, jadi kayak buang sampah rutin," kata Cahyo.

"*Nggih*. Log itu penting, tapi kalau gak diurus, dia bisa jadi masalah baru."

## **13.9 Praktik: Menambahkan Log di Kode**

"Sekarang kita praktik," kata Mas Alin. "Binto, Cahyo, kalian tambahkan log manual di endpoint pesanan."

Mereka bertiga membuka kode. Mas Alin memandu.

"Di sini, setelah pesanan berhasil dibuat, tambahkan Log::info() dengan pesan yang jelas. Sebutkan ID pesanan, user yang membuat, dan totalnya."

Binto mengetik mengikuti arahan.

"Lalu di sini, pas cek stok menipis, tambahkan Log::warning(). Biar kita tahu produk apa yang hampir habis."

Cahyo ikut menambahkan di bagian catch exception. "Ini Log::error() ya, Mas? Biar kalau ada exception, tercatat."

"Betul. Tapi ingat," Mas Alin menaikkan suara, "jangan pernah log data sensitif. Password? Jangan. Nomor kartu kredit? Jangan. Data pribadi yang gak perlu? Jangan. Log itu bisa dibaca banyak orang. Jaga privasi pengguna."

## **13.10 Log Itu Ada di Mana-Mana**

Sore hari, setelah semua selesai, Mas Alin meregangkan badan.

"Ingat, Dik. Log itu gak cuma di aplikasi kita. Sistem sebagus apa pun pasti punya log."

Ia mencontohkan. "Windows ada Event Viewer. Linux ada syslog, journalctl. Router ada log. Database ada log. Bahkan HP kalian juga punya log sistem."

"Kenapa semua punya log, Mas?" tanya Cahyo.

"Karena log adalah jejak digital. Audit trail. Kalau ada masalah—entah aplikasi error, server diretas, atau jaringan putus—log adalah tempat pertama yang diperiksa. Tanpa log, investigasi itu kayak cari jarum di tumpukan jerami, tapi lampunya mati."

Binto merenung. Ia teringat insiden tadi pagi. Tanpa file laravel.log, mereka mungkin masih bingung dan saling tuduh. *Log itu seperti kotak hitam pesawat*, pikirnya. *Merekam semua sampai detik terakhir.*

## **13.11 Penutup: Jejak yang Tertinggal**

Menjelang maghrib, Cahyo merapikan buku catatannya. Ia menulis dengan rapi:

*Log \= buku harian sistem. Level: Info, Warning, Error, Critical. Framework modern sudah sediakan file log. Bisa dialirkan ke Sentry/ELK. Jangan cuma andalkan database—log file lebih andal untuk error. Log rotation biar disk gak penuh. Jangan log data sensitif.*

Binto melihat catatan itu dan tersenyum. Dulu, beberapa bulan lalu, ia juga mencatat hal-hal seperti ini. Kini, ia sudah bisa menjelaskannya ke orang lain.

"Kamu cepat belajar, Dik," kata Binto.

Cahyo tersipu. "Ini semua berkat Mas Binto dan Mas Alin."

Mas Alin yang mendengar dari pojokannya hanya tersenyum kecil.

Di luar, pohon rambutan bergoyang pelan. Buahnya sudah lama habis. Daunnya tetap hijau, menunggu musim berikutnya. Seperti ilmu yang terus tumbuh, tak kenal musim.

Dan Binto tahu, ini satu langkah lagi menuju *medior*.