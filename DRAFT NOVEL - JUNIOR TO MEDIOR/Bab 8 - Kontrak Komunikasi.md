# Bab 8: Kontrak Komunikasi

## 8.1 Kabar dari Balikpapan

Pagi itu, kantor Garda Teknologi Nusantara masih lengang. Binto baru saja memarkirkan motornya ketika melihat Pakde Suhar mondar-mandir di teras sambil menempelkan ponsel ke telinga. Wajahnya sumringah.

"*Nggih*, Pak Haji... *Alhamdulillah*... Berapa? *Masya Allah*, selamat... *Nggih*, siap. Nanti saya rapatkan dengan tim... *Matur suwun*, Pak Haji."

Pakde menutup telepon dan menatap Binto dengan mata berbinar. "Mas Binto\! Kabar baik\!"

Belum sempat Binto bertanya, Mas Alin datang dengan Astrea Grand-nya. Disusul Wawan yang turun dari angkot sambil membawa *tumbler* raksasa. Pakde meminta semua berkumpul dulu—termasuk Mas Andik yang baru datang dengan helm proyeknya.

"Pak Haji Hamid dari Balikpapan barusan telepon," Pakde memulai. "Investornya deal. Bisnis minimarket mereka akan di-upgrade jadi *supply chain* grosir."

Wawan bersiul. "Wah, gede dong, Pakde?"

"Gede. Dari yang tadinya cuma di bawah sepuluh cabang minimarket, sekarang mereka akan jadi pemasok buat toko-toko kecil dan swalayan di Balikpapan dan sekitarnya. Tim sales akan diterjunkan ke lapangan untuk mengambil pesanan."

Binto mendengarkan dengan antusias. Ini kabar besar.

"Tapi ada satu permintaan khusus," Pakde melanjutkan. "Mereka butuh aplikasi *mobile* buat para sales. Biar bisa input pesanan langsung dari *smartphone*."

Ruangan hening sejenak.

"Aplikasi mobile?" Mas Andik menegakkan duduknya.

"*Nggih*. Dan ini berarti cara kerja kita harus berubah."

## 8.2 Rapat di Bawah Rambutan

Pakde mengajak semua ke teras. Udara pagi masih sejuk. Pohon rambutan di depan kini buahnya sudah banyak yang merah. Beberapa hari lalu mereka mencicipi buah pertama, dan sekarang buah-buah baru terus bermunculan.

Mas Alin duduk di bangku kayu, menghadap tim. "Selama ini kita bikin aplikasi monolitik. Satu kode, satu *deploy*. Web dan logika bisnis jadi satu. Itu cukup selama pengguna cuma akses lewat browser."

Ia menatap satu per satu. "Tapi sekarang kita butuh aplikasi mobile. Mau gak mau, kita harus pisah. *Frontend* sendiri, *backend* sendiri."

Binto mengernyit. "Maksudnya pisah, Mas?"

"Selama ini, kalau kamu buka halaman laporan di browser, server kita yang ngolah data, terus kirim HTML utuh ke browser. Itu monolitik. Sekarang, aplikasi mobile gak bisa terima HTML. Dia butuh data mentah. Data itu dikirim lewat API."

"API?" Wawan ikut penasaran.

"*Application Programming Interface*. Jembatan antara *frontend* dan *backend*."

Pakde menunjuk anggota tim satu per satu. "Andik, kamu kan paling penasaran sama teknologi baru. Gimana kalau kamu yang pegang *mobile*? Pakai Flutter aja, katanya lagi naik daun."

Andik mengangguk semangat. "Siap, Pakde. Saya malah udah mulai belajar sedikit-sedikit."

"Wawan, kamu bantu desain UI/UX untuk aplikasi mobile. Biar tampilannya profesional."

"Siap."

Pakde menatap Binto. "Mas Binto, kamu yang pegang *backend*. Bikin REST API buat dilayani ke aplikasi mobile."

Binto meneguk ludah. "Saya, Pakde? Saya belum pernah bikin API."

Mas Alin menepuk bahunya. "Tenang, *Le*. Saya bantu. Saya yang jadi *tech lead*\-nya. Kita belajar bareng."

## 8.3 Kuliah Singkat: Apa Itu API?

Setelah rapat bubar dan yang lain kembali ke meja masing-masing, Mas Alin mengajak Binto tetap di teras. Ia membawa dua cangkir enamel—kopi untuk dirinya, teh untuk Binto.

"Saya jelasin dari nol, ya," katanya sambil duduk. "Biar kamu punya gambaran utuh."

Binto mengangguk. Ia siap menyerap apa pun.

"Bayangin kamu di restoran. Restoran Padang, misalnya."

Binto tersenyum kecil. Membayangkan nasi rendang.

"Kamu duduk. Lihat menu di meja. Kamu panggil pelayan. 'Mbak, saya pesan nasi rendang, es teh manis.' Pelayan catat, pergi ke dapur, ambil makanan, antar ke kamu. Kamu makan. Selesai."

Mas Alin menatap Binto. "Nah, di situ kamu adalah *frontend*—aplikasi mobile. Dapur adalah *backend*—tempat data dan logika bisnis. Pelayan itu API. Jembatan yang menghubungkan kamu dan dapur."

Binto mulai membayangkan. "Jadi aplikasi mobile gak langsung ngambil data dari database?"

"Gak bisa. Dan gak boleh. Terlalu berbahaya. Aplikasi mobile harus lewat API. API yang akan mengambil data dari database, mengolahnya, lalu mengirim ke mobile dalam format yang disepakati."

"Terus pelayan itu tahu pesanan karena ada menu?"

"Persis. Menu itu namanya API Contract. Dokumen kesepakatan antara *frontend* dan *backend*. Isinya: alamat pesan, cara pesan, data yang harus dikirim, dan data yang akan diterima."

Binto manggut-manggut. Analogi ini membantu sekali.

## 8.4 Monolitik vs API-based

"Tapi Mas, selama ini kita bikin web monolitik. Itu bedanya apa?"

Mas Alin menyesap kopinya. "Monolitik itu kayak kamu masak sendiri di dapur restoran, terus juga jadi pelayan, kasir, dan tukang cuci piring. Semua jadi satu."

Ia menggambar di udara. "Satu aplikasi utuh. *Frontend* dan *backend* nyatu. Enaknya, simpel. Gak ribet. Cocok buat proyek kecil kayak Koperasi Sekar Patria."

"Kelemahannya?"

"Begitu aplikasi makin besar, susah dirawat. Mau ubah tampilan dikit, takut ngerusak logika. Mau nambah fitur, harus *deploy* ulang semuanya. Dan yang paling penting: gak bisa dipakai oleh aplikasi lain. Web ya cuma web."

Mas Alin menunjuk laptopnya. "Sekarang kita butuh aplikasi mobile. Kalau masih monolitik, kita harus bikin ulang semua logika bisnis di aplikasi mobile. Duplikasi. Buang-buang tenaga."

"Jadi API-based itu..."

"Pisah. *Backend* sendiri, *frontend* sendiri. *Backend* cuma nyediain API. *Frontend*—bisa web, bisa mobile, bisa aplikasi lain—tinggal panggil API yang sama. Sekali bikin *backend*, bisa dipakai banyak *frontend*. Efisien."

Binto mengangguk. "Jadi API itu kayak colokan listrik. Apa pun alatnya, asal colokannya sesuai, bisa nyala."

Mas Alin tersenyum lebar. "*Nah*, itu analogi yang lebih bagus. Persis. API adalah stop kontak. *Backend* sediain listrik, *frontend* tinggal colok."

## 8.5 Bahasa yang Dipahami: JSON ala Restoran Padang

"Terus, gimana caranya pelayan dan dapur ngomong? Mereka harus pakai bahasa yang sama."

Binto berpikir. "Bahasa apa?"

Mas Alin tersenyum. "Kita balik ke restoran Padang tadi. Pelayan dan koki di dapur itu sama-sama orang Minang. Mereka ngomong pakai bahasa Minang. Ada format pesanan yang sudah dipahami bersama."

Ia mencontohkan. "Misal kamu pesan: *'Limo porsi nasi rendang jo perkedel, bungkuih.'* Itu artinya: 5 porsi nasi rendang dan perkedel, dibungkus."

Binto manggut-manggut.

"Nah, format itu sudah standar. Jumlah disebut dulu, lalu menu, lalu keterangan makan di tempat atau bungkus. Pelayan tinggal teriak ke dapur dengan format itu. Koki langsung paham. Gak perlu tanya lagi: 'Rendangnya berapa? Perkedelnya berapa? Mau dibungkus apa di piring?' Semua sudah jelas dari format pesanan."

Mas Alin membuka laptop. "Di dunia API, bahasa yang dipakai adalah JSON. JavaScript Object Notation."

Ia mengetik sesuatu.

"Dulu zamannya XML. Bentuknya kayak gini:"

Ia mengetik:

```xml
<produk>
    <nama>Rinso</nama>
    <harga>5000</harga>
</produk>
```

"Ribet. Banyak kurung buka tutup. Boros tempat. Sekarang bandingkan dengan JSON."

Ia mengetik lagi:

```json
{
    "nama": "Rinso",
    "harga": 5000
}
```

"JSON itu ringkas. Mirip objek di JavaScript. Gampang dibaca manusia, gampang diolah mesin. Semua bahasa pemrograman modern bisa baca JSON."

"Jadi API kita nanti kirim data dalam bentuk JSON?"

"*Nggih*. *Request* dari mobile bisa dalam JSON. *Response* dari server juga JSON. Itu standar industri sekarang."

Mas Alin menambahkan. "Sama kayak format pesanan di restoran Padang tadi. Begitu kita sepakat pakai JSON, semua pihak tahu: data akan dikirim dalam bentuk pasangan nama\_properti: nilai. Mobile kirim JSON, server balas JSON. Gak ada salah paham."

## 8.6 Komponen REST API: Diterjemahkan ke Restoran Padang

Mas Alin mengambil kertas kosong dan spidol. "Sekarang kita bedah komponen REST API. Saya gambar biar jelas. Tapi kita tetap pakai analogi restoran Padang, ya."

Ia mulai mencoret-coret.

"Pertama, Endpoint. Ini alamat URL tempat kita minta data. Ibarat alamat restoran. Kamu mau makan, harus tahu restorannya di mana. Mau pesan rendang, ya ke Restoran Padang Sederhana, bukan ke restoran Jepang."

Ia menulis. "Di API, endpoint biasanya `/api/products` untuk urusan produk, `/api/orders` untuk urusan pesanan. Endpoint harus pakai kata benda, bukan kata kerja. Jangan `/getProducts`, tapi cukup `/products`."

"Kenapa, Mas?"

"Karena kata kerjanya sudah diwakili oleh HTTP Method." Mas Alin menulis di bawahnya. "Method itu ibarat jenis permintaan ke pelayan."

Ia menjelaskan dengan analogi. "Bayangin kamu di restoran Padang. Kamu bisa minta pelayan dengan beberapa cara:

* `GET` → Kamu cuma mau lihat daftar menu. 'Mbak, menu hari ini apa aja?' Pelayan kasih menu, kamu baca. Gak ada pesanan yang dibuat. Gak ada data yang berubah di dapur.
* `POST` → Kamu mau kirim pesanan baru. 'Mbak, saya pesan nasi rendang satu.' Pelayan catat, kirim ke dapur. Dapur mulai masak. Data baru tercipta.
* `PUT` atau `PATCH` → Kamu mau ubah pesanan yang sudah terlanjur dipesan. 'Mbak, yang tadi rendangnya jangan pakai jeroan, pakai daging semua.' Pelayan revisi pesanan. Data berubah.
* `DELETE` → Kamu mau batalkan pesanan. 'Mbak, es tehnya batal aja.' Pelayan coret pesanan. Data dihapus."

Binto tersenyum. Analogi ini sangat membumi.

"Ketiga, Headers." Mas Alin melanjutkan. "Ini informasi tambahan yang dikirim bareng *request*. Ibarat kamu kasih tahu pelayan: *'Saya alergi kacang, tolong dicatat.'* Atau *'Ini kunci kamar saya, bukti saya tamu hotel.'*"

"Di API, headers berisi hal-hal seperti tipe konten (Content-Type: application/json) atau token otentikasi (Authorization: Bearer \<token\>)."

"Keempat, Body." Mas Alin menulis. "Ini data utama yang dikirim. Ibarat detail pesanan kamu. 'Nasi rendang satu, es teh manis satu, sambal ijo dipisah.' Itu semua ada di body."

"Untuk method POST dan PUT, body ini wajib. Isinya data yang mau disimpan atau diubah. Untuk GET, biasanya kosong—kamu cuma minta lihat menu, gak bawa pesanan."

"Kelima, Status Code." Mas Alin memberi tanda bintang. "Ini kode dari server untuk kasih tahu hasilnya. Ibarat respons pelayan setelah kamu pesan."

## 8.7 Status Code: Respons Pelayan Restoran Padang

"Ini penting banget," Mas Alin menekankan. "Status code adalah bahasa universal yang dipahami semua *developer*. Kita terjemahkan ke pengalaman di restoran Padang."

Ia menulis daftar di kertas:

* 200 OK → *"Pesanan Anda sudah siap, Mbak. Ini nasinya."* Sukses. Data dikirim.
* 201 Created → *"Pesanan baru sudah dicatat, Mas. Silakan tunggu."* Sukses. Data baru berhasil dibuat.
* 400 Bad Request → *"Maaf, Mbak. Pesanannya kurang jelas. Rendangnya berapa porsi? Mau dibungkus apa makan di sini?"* Data yang kamu kirim salah format atau tidak lengkap.
* 401 Unauthorized → *"Maaf, Mas. Ini area khusus anggota. Anda harus tunjukkan kartu member dulu."* Kamu belum login. Tidak punya akses.
* 403 Forbidden → *"Maaf, Mbak. Menu rendang spesial hanya untuk pelanggan VIP. Anda anggota biasa."* Kamu sudah login, tapi tidak punya hak untuk akses ini.
* 404 Not Found → *"Maaf, Mas. Restoran Padangnya sudah pindah. Alamat ini kosong."* Alamat endpoint tidak ditemukan.
* 422 Unprocessable Entity → *"Maaf, Mbak. Pesanan nasi rendang 10 porsi bisa, tapi stok daging kami cuma cukup untuk 5 porsi."* Data yang dikirim valid formatnya, tapi tidak lolos aturan bisnis.
* 500 Internal Server Error → *"Maaf, Mas. Dapurnya kebakaran. Silakan kembali nanti."* Server yang error. Bukan salah kamu.

Binto tertawa kecil mendengar analogi "dapur kebakaran".

"Jadi kalau aplikasi mobile dapat 401, dia tahu harus arahkan pengguna ke halaman login. Kalau dapat 500, dia tahu harus tampilkan pesan 'Server sedang sibuk'. Gak perlu nebak-nebak."

"Ini jauh lebih rapi daripada cuma *echo* 'error' kayak yang sering saya lakukan di kampus," gumam Binto.

"*Nggih*. Dengan status code yang jelas, *frontend* bisa ngasih pesan yang tepat ke pengguna. Pengguna gak bingung. Itu profesional."

## 8.8 Stateful vs Stateless

"Mas, satu lagi. Gimana caranya server tahu siapa yang akses? Kan gak kayak web biasa yang ada sesi login."

Mas Alin mengangguk. "Nah, ini konsep kunci. Web biasa itu stateful. Server simpan sesi di memori. Begitu kamu login, server ingat kamu sampai logout. Tiap *request*, browser kirim *cookie* sesi. Server cocokkan dengan yang di memori."

"Itu bagus, kan?"

"Bagus buat web tradisional. Tapi buat API yang diakses aplikasi mobile, itu masalah."

"Kenapa?"

"Karena aplikasi mobile gak punya *cookie* seperti browser. Dan server yang menyimpan sesi jadi punya beban memori. Kalau penggunanya ribuan, server bisa kehabisan memori. Belum lagi kalau kita punya banyak server—sinkronisasi sesi antar server itu ribet."

"Jadi solusinya?"

"Stateless. Server gak ingat siapa kamu. Setiap *request* harus bawa bukti identitas sendiri."

## 8.9 Token: Kunci Kamar Hotel

Mas Alin mencari analogi. "Ibarat kunci kamar hotel."

"Hotel?"

"Kamu datang ke hotel. *Check-in* di resepsionis. Kasih KTP, isi formulir. Resepsionis verifikasi, lalu kasih kamu kunci kamar. Setelah itu, setiap kali kamu mau masuk kamar, kamu tinggal tunjukin kunci. Resepsionis gak perlu ingat kamu siapa, kamu di kamar nomor berapa. Kuncinya sudah cukup."

Binto mulai menangkap. "Jadi kunci itu..."

"Token. Setelah kamu login—kirim email dan password—server verifikasi. Kalau benar, server kasih token. Token ini yang akan kamu bawa di setiap *request* berikutnya. Server gak perlu simpan sesi. Dia cuma perlu cek: 'Token ini valid gak?' Kalau valid, ya sudah, layani."

"Token-nya dikirim di mana?"

"Di Header. Biasanya seperti ini: Authorization: Bearer \<token\>."

Binto mencatat dalam hati: *Bearer token*. Istilah baru lagi.

## 8.10 Autentikasi vs Otorisasi

"Ini yang sering ketuker," Mas Alin menambahkan. "Autentikasi dan Otorisasi. Dua hal yang berbeda."

Ia menulis di kertas.

"Autentikasi menjawab pertanyaan: *Siapa kamu?* Proses login itu autentikasi. Kamu buktikan bahwa kamu adalah pengguna yang sah—biasanya dengan email dan password."

"Otorisasi menjawab pertanyaan: *Apa yang boleh kamu lakukan?* Setelah server tahu siapa kamu, server akan cek: apa kamu boleh akses data ini? Boleh ubah? Boleh hapus?"

Binto mengangguk. "Jadi token itu urusan autentikasi?"

"Token itu bukti autentikasi. Tapi di dalam token, biasanya ada informasi tentang peran pengguna—misalnya 'sales' atau 'admin'. Server baca peran itu untuk otorisasi. 'Oh, token ini milik sales. Sales hanya boleh lihat produk, gak boleh hapus.'"

"Bedanya 401 dan 403 tadi ya, Mas?"

"Persis. 401 Unauthorized itu autentikasi gagal—token tidak valid atau tidak ada. 403 Forbidden itu autentikasi berhasil, tapi otorisasi gagal—kamu tidak punya hak."

## 8.11 Kenapa Bearer Token, Bukan API Key?

Binto ingat sesuatu. "Mas, saya pernah lihat ada yang pakai *API key*. Itu bedanya apa?"

Mas Alin mengangguk. "Pertanyaan bagus. *API key* itu kunci statis. Biasanya dipakai untuk otentikasi server-ke-server, bukan pengguna akhir. Kamu simpan *API key* di aplikasi mobile? Bahaya. Kalau ada yang bongkar aplikasimu, *API key*\-mu bocor. Bisa disalahgunakan."

"Bearer token bedanya?"

"Bearer token itu hasil dari proses login. Tiap pengguna dapat token berbeda. Token punya masa berlaku—biasanya beberapa jam atau hari. Jadi kalau bocor pun, dampaknya terbatas. Dan yang paling penting: token bisa di-*revoke*—dicabut—tanpa harus ganti *API key*."

Ia melanjutkan. "Bayangin di sistem kita nanti ada *sales* A dan *sales* B. Mereka login dengan *username* dan *password* masing-masing. Dapat token masing-masing. Token itu yang dipakai untuk akses API. Server bisa tahu ini *request* dari *sales* A atau *sales* B. Jadi kita bisa catat siapa melakukan apa. Itu penting buat audit."

Binto paham sekarang. *Bearer token* lebih aman dan lebih fleksibel untuk sistem dengan banyak pengguna.

## 8.12 API Contract: Menu yang Disepakati

Setelah sesi teori yang panjang, Mas Alin membuka laptop. "Sekarang kita praktik. Kita bikin API Contract dulu. Ini kayak menu di restoran tadi. Sebelum masak, kita sepakati dulu."

Ia membuat dokumen kosong. "Andik sebagai *mobile developer* harus tahu: endpoint apa saja, data apa yang harus dikirim, dan respons apa yang akan diterima. Jadi dia bisa mulai *ngoding* tanpa nunggu *backend* selesai."

Mereka mulai merancang.

Endpoint pertama: Login

* URL: `POST /api/login`
* Body (JSON):
  ```json
  {
      "email": "sales1@tokobangun.com",
      "password": "rahasia123"
  }
  ```
* Response sukses (200):
  ```json
  {
      "token": "eyJhbGciOiJIUzI1...",
      "user": {
          "id": 1,
          "nama": "Budi Santoso",
          "role": "sales"
      }
  }
  ```
* Response gagal (401):
  ```json
  {
      "message": "Email atau password salah"
  }
  ```

Endpoint kedua: Lihat Daftar Produk

* URL: `GET /api/products`
* Headers: `Authorization: Bearer <token>`
* Response sukses (200):
  ```json
  {
      "data": [
          {
              "id": 1,
              "nama": "Rinso 1kg",
              "harga": 18000,
              "stok": 50
          },
          {
              "id": 2,
              "nama": "Lifebuoy 100gr",
              "harga": 3500,
              "stok": 120
          }
      ]
  }
  ```

Mereka melanjutkan untuk endpoint lain: detail produk, buat pesanan, lihat riwayat pesanan. Semua ditulis dengan format yang sama: method, URL, headers, body, response.

"Ini baru dua endpoint," kata Mas Alin. "Nanti kita tambah sesuai kebutuhan. Yang penting, formatnya konsisten. Andik baca ini, langsung paham."

## 8.13 Binto Mulai Ngoding

Sore hari, Binto membuka laptopnya. Ia membuat proyek Laravel baru khusus untuk API. Sesuai arahan Mas Alin, ia akan menggunakan *Bearer Token* untuk otentikasi.

"Mas, untuk *generate* token-nya gimana?"

"Pakai paket yang sudah ada. Di Laravel ada Sanctum. Kamu tinggal pasang, konfigurasi dikit. Nanti pas login, cek email dan password. Kalau cocok, buat token. Kirim token itu sebagai respons."

Binto mulai mengetik. Ia membuat *controller* AuthController dengan method login. Ia validasi email dan password, lalu mengecek kredensial. Jika benar, ia membuat token menggunakan fitur bawaan framework.

Ia juga melindungi endpoint `/api/products` dengan *middleware* yang mengecek token. Hanya *request* dengan token valid yang bisa mengakses.

"Mas, ini saya bikin *resource* untuk produk. Biar respons JSON-nya terstruktur."

"Bagus. Itu *best practice*. Jangan lupa kasih status code yang sesuai."

Sesekali Binto bertanya, tapi sebagian besar ia kerjakan sendiri. Rasanya berbeda. Ia tidak lagi sekadar menambah fitur di aplikasi yang sudah ada. Ia sedang membangun fondasi untuk sistem baru. Sistem yang akan dipakai oleh banyak orang di Kalimantan.

## 8.14 Dokumentasi untuk Andik

Menjelang sore, Mas Andik menghampiri meja Binto. "Mas, gimana API-nya? Aku mau coba-coba nih."

Binto menoleh ke Mas Alin. "Dokumentasinya belum jadi, Mas."

Mas Alin mendekat. "Bikin sekarang. Pakai Postman aja, atau kalau mau sekalian, bikin *API documentation* dengan Scribe atau Scramble."

Binto membuka Postman. Ia membuat *collection* baru: "Minimarket API". Ia menambahkan *request* pertama: Login. Ia isi URL, method, body, dan contoh respons. Lalu *request* kedua: Get Products. Ia tambahkan header Authorization dengan nilai Bearer {{token}}.

"Ini biar Andik tinggal klik," katanya.

Mas Alin mengangguk setuju. "Nanti kalau sudah mantap, kita bisa *generate* dokumentasi HTML yang lebih rapi. Tapi untuk sekarang, Postman cukup. Andik bisa lihat langsung contohnya, coba-coba sendiri, gak perlu tanya-tanya terus."

Andik tersenyum. "Enak nih. Jadi gak saling tunggu. Aku bisa mulai *ngoding* Flutter sambil nunggu API selesai."

Wawan yang mendengar dari mejanya menimpali. "Nah, ini enaknya API. Kerja paralel. Gak kayak dulu, nunggu *backend* beres dulu baru *frontend* jalan."

## 8.15 Refleksi: Wajah Perusahaan

Sore mulai merunduk. Teh Binto tinggal setengah gelas. Kopi Mas Alin sudah dingin seperti biasa.

"Gimana rasanya bikin API pertama?" tanya Mas Alin.

Binto menatap layar laptopnya yang masih menampilkan endpoint dan payload. "Kayak bikin pintu, Mas. Dulu saya kira cukup asal bisa dibuka. Ternyata engselnya, kuncinya, bahkan cara orang ngetuk pun harus dipikirin."

Mas Alin tersenyum kecil. "Nah. Itu baru bukan sekadar ngoding."

Binto mengangguk pelan. Sekarang ia paham kenapa tadi mereka lama sekali membahas hal-hal yang kelihatannya remeh: nama field, status code, token, bentuk respons. Semua itu bukan hiasan. Itu sopan santun antar-sistem.

Kalau salah satu berantakan, yang repot bukan cuma orang di ruangan ini. Bisa Andik. Bisa tim mobile. Bisa klien. Bisa siapa saja yang datang belakangan dan mencoba menyambung ke pekerjaan mereka.

Mas Alin menaruh cangkirnya. "API itu wajah teknis perusahaan, *Le*. Orang boleh gak pernah lihat kode kita. Tapi dari situ mereka bisa tahu: kita rapi atau sembrono."

Binto menutup laptopnya pelan.

Di halaman, satu buah rambutan jatuh sendiri ke tanah. Bukan karena busuk. Memang sudah waktunya lepas.

Ia memungutnya, memutar buah itu di telapak tangan, lalu tersenyum kecil.

Besok mereka akan lanjut bikin endpoint lain.

Tapi hari ini, Binto sudah belajar satu hal penting: komunikasi yang baik ternyata bukan cuma urusan manusia.