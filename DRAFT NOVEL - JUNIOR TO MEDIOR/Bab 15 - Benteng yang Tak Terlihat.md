# Bab 15: Benteng yang Tak Terlihat

## 15.1 Nasi Kenduri dari Ibu Cahyo

Pagi itu, kantor Garda Teknologi Nusantara beraroma lain. Bukan aroma kopi tubruk seperti biasa, melainkan wangi rempah yang kaya—kunyit, serai, daun salam, dan santan yang dimasak lama. Binto yang baru tiba langsung mencari sumber aroma itu.

Di meja tengah, Cahyo sedang menata rantang besar. Tangannya cekatan mengeluarkan piring-piring kertas dan sendok plastik.

"Wah, Dik. Ada apa ini?" tanya Binto.

Cahyo tersenyum malu. "Ini, Mas. Ibu saya masakin. Katanya buat teman-teman di kantor. Soalnya ini hari terakhir saya PKL."

Satu per satu lauk keluar dari rantang. Nasi kuning yang dibentuk kerucut. Sepotong ingkung ayam lodho utuh—ayam kampung yang dimasak dengan bumbu kuning kental, teksturnya empuk, warnanya kuning tua meresap sampai ke tulang. Ada urap-urap: sayuran rebus dengan parutan kelapa berbumbu, pedas manis, aromanya menggelitik hidung. Ada juga tempe goreng, perkedel kentang, dan sambal bawang yang merah menggoda.

Mbak Rara yang baru masuk langsung berdecak. "Ya ampun, Dik. Ibumu repot-repot. Ini masakan istimewa."

"Ibu saya senang masak, Mbak. Katanya, kalau anaknya sudah selesai belajar, harus bawa nasi kenduri. Biar ilmunya berkah."

Pakde Suhar datang dan langsung duduk di dekat meja. "Wah, ini namanya selametan kecil. Bagus, bagus. Sini, kita makan bareng dulu. Nanti kerjanya."

Mereka berenam—Pakde, Mas Alin, Mbak Rara, Mas Andik, Binto, dan tentu saja Cahyo—duduk mengelilingi meja. Sendok plastik beradu dengan piring kertas. Suapan pertama nasi kuning dengan suwiran ayam lodho langsung membuat semua orang mengangguk.

"Enak tenan iki," gumam Mas Andik. "Bumbunya meresep."

Cahyo tersenyum bangga. Ibunya pasti senang mendengar pujian ini.

## 15.2 Satu Pelajaran Terakhir

Setelah nasi mulai habis dan tinggal tulang ingkung yang bersih, Cahyo memberanikan diri. "Mas Alin, Mbak Rara, Mas Binto. Sebelum saya pulang, saya boleh minta satu pelajaran terakhir?"

Mas Alin menaruh sendoknya. "Monggo, Dik. Apa yang mau kamu tanyakan?"

Cahyo berpikir sejenak. "Apa sih satu hal yang paling penting tapi sering dilupakan programmer pemula? Kayak saya ini."

Mas Alin menyandarkan punggungnya. Matanya menerawang ke langit-langit. "Keamanan."

"Keamanan?" Cahyo mengulang. "Maksudnya biar gak di-hack?"

"Itu sebagian kecilnya. Keamanan itu luas, Dik. Banyak programmer—termasuk saya dulu—cuma mikir, 'Yang penting kodeku jalan. Aplikasiku kecil, siapa yang mau retas?' Padahal celah keamanan gak pandang bulu."

Binto ikut mendengarkan dengan serius. Ia teringat betapa dulu ia juga berpikir seperti itu.

## 15.3 Cara Andik Mengajar

Mas Alin tersenyum. "Tapi di sini... ahlinya bukan saya."

Ia menoleh ke Mas Andik yang sedari tadi diam dengan dua layar menyala — satu penuh kode, satu lagi penuh... entah. *Mungkin matrix*, pikir Binto.

"Andik. Giliranmu."

Andik menatap ke arah mereka. Alisnya naik sedikit. Lalu ia menghela napas pendek — bukan napas malas, tapi napas seseorang yang tahu apa yang akan terjadi selanjutnya.

Ia menarik kursi. Duduk di samping Cahyo.

"Kamu," katanya, suaranya datar, "punya aplikasi yang sudah kamu deploy?"

Cahyo mengangguk. "Punya, Mas. Aplikasi inventaris kecil. Deploy di server gratisan."

"Buka."

Cahyo membuka laptopnya. Menampilkan kode aplikasinya.

"Sekarang..." Andik menatap kode itu, "coba kamu serang."

"Maksudnya...?" Cahyo bingung.

"Coba bobol. Injeksi SQL. Parameter tampering. Apa aja. Coba."

Cahyo bengong. "Tapi... ini kan aplikasi saya sendiri?"

"Justru."

Dan di situlah pelajaran pertama dari Andik:

*Musuh terbaik adalah diri sendiri.*

Bukan dalam arti motivasi. Tapi dalam arti: kalau kamu tidak bisa membobol kode kamu sendiri, jangan harap bisa mengamankan dari orang lain.

Binto tersentak. Ia tidak pernah memikirkannya seperti itu.

Cahyo mencoba. Tangannya sedikit gemetar. Ia mengetik sesuatu di kolom pencarian aplikasinya. Tidak terjadi apa-apa. Ia coba lagi. Kali ini pakai karakter aneh.

"Hampir," kata Andik. Matanya menyipit. "Kamu benar coba ke arah itu. Tapi aplikasimu sudah pakai prepared statement. Aman. Sekarang coba XSS."

Satu jam berikutnya berjalan seperti itu. Andik tidak pernah menjelaskan — ia memancing. Ia membuat Cahyo — dan Binto — menemukan sendiri celah-celah di kode mereka. Setiap kali mereka menemukan lubang, Andik hanya mengangguk kecil.

"Orang-orang pikir security itu soal tools," katanya di tengah sesi. "Firewall. Antivirus. SSL. Itu penting. Tapi benteng yang paling tak terlihat... adalah cara berpikir."

Ia menatap Cahyo.

"Kalau kamu sudah bisa melihat kode dengan mata musuh... kamu sudah setengah jalan jadi security engineer."

Cahyo menelan ludah. Buku catatannya belum sempat ia buka satu halaman pun. Tapi pelajaran hari itu... akan ia ingat selamanya.

---

## 15.4 Tiga Pilar: CIA Triad

Mas Alin mengambil selembar tisu bekas dan pulpen. Ia menggambar segitiga.

"Di dunia keamanan, ada tiga pilar utama. Namanya CIA Triad. Bukan badan intelijen Amerika, ya. Tapi singkatan dari Confidentiality, Integrity, Availability."

Ia menunjuk sudut pertama. "Confidentiality—kerahasiaan. Data yang seharusnya rahasia, ya tetap rahasia. Misalnya, data simpanan anggota koperasi. Cuma pengurus yang boleh lihat. Kalau bocor ke orang luar? Itu pelanggaran Confidentiality."

Sudut kedua. "Integrity—keutuhan. Data tidak boleh diubah sembarangan. Kalau ada orang iseng bisa ubah saldo tabungan dari lima juta jadi lima puluh juta tanpa izin? Itu Integrity rusak."

Sudut ketiga. "Availability—ketersediaan. Sistem harus bisa diakses kapan pun dibutuhkan. Insiden disk penuh kemarin? Itu masalah Availability. Aplikasi gak bisa dipakai karena servernya penuh."

Cahyo manggut-manggut. "Jadi keamanan itu gak cuma soal cegah hacker?"

"Persis. Banyak orang cuma fokus di Confidentiality—takut data dicuri. Padahal Integrity dan Availability sama pentingnya. Bayangin aplikasi e-commerce. Aman dari hacker, tapi sering down. Pelanggan kabur semua."

## 15.5 SQL Injection & XSS: Ancaman Klasik pada CIA

"Contoh kecil," Mas Alin melanjutkan. "SQL Injection. Kamu tahu?"

Cahyo mengangguk ragu. "Pernah dengar, Mas. Tapi gak terlalu paham."

"Sederhananya: ada orang iseng masukin perintah SQL lewat form login atau kolom pencarian. Kalau kita gak validasi, dia bisa lihat data (Confidentiality bocor) atau ubah data (Integrity rusak)."

Mbak Rara yang sedari tadi mendengarkan tiba-tiba angkat bicara, nadanya serius. "Wah iya aku jadi inget. Dulu waktu aku di Surabaya, kantor temanku kena SQL injection. Aplikasi *e-commerce* kecil, toko online lokal. Seseorang masukin perintah lewat kolom pencarian. Database bocor. Data pelanggan—nama, alamat, nomor HP—dipakai buat penipuan sama pelakunya. Perusahaan kena teguran, klien kabur, reputasi hancur. Temanku *resign* karena malu dan merasa bersalah."

Cahyo menelan ludah. Cerita itu jauh lebih menakutkan dari penjelasan teknis mana pun.

Mas Alin mengangguk. "Misal di form login, dia masukin ' OR '1'='1. Kalau kode kita gak aman, dia bisa masuk tanpa password."

Binto menimpali. "Itu kayak yang dulu saya hampir lakukan, Dik. Untung di sini diajarin pakai *prepared statement* dan ORM yang aman."

"Betul. XSS juga. *Cross-Site Scripting*. Orang iseng masukin script JavaScript lewat kolom komentar. Begitu dibuka pengguna lain, script-nya jalan. Bisa curi cookie, redirect ke situs palsu. Itu serangan ke Confidentiality pengguna."

Cahyo mencatat cepat di buku kecilnya. "Pencegahannya?"

"Untuk SQL Injection: pakai *prepared statement* atau ORM. Jangan gabung string mentah buat query. Untuk XSS: selalu *escape* output. Jangan tampilkan data mentah dari pengguna."

## 15.6 Password Hashing: Jaga Confidentiality

"Satu lagi," Mas Alin menambahkan. "Password. Jangan pernah simpan password mentah di database."

Cahyo mengernyit. "Memangnya ada yang begitu?"

"Banyak. Saya dulu waktu kuliah juga begitu," Binto mengaku. "Bikin aplikasi, password disimpan apa adanya. Sekarang saya sadar, itu bahaya banget."

"Kalau database bocor," Mas Alin menjelaskan, "penyerang langsung lihat password asli pengguna. Dan karena banyak orang pakai password yang sama di mana-mana, akun mereka di tempat lain juga terancam."

"Solusinya?"

"Hashing. Password diacak satu arah pakai algoritma seperti bcrypt atau argon2. Jadi yang tersimpan cuma hasil acaknya. Sekali diacak, gak bisa dikembalikan ke aslinya. Waktu login, kita acak lagi input pengguna, bandingkan dengan yang di database. Kalau cocok, boleh masuk."

Cahyo mencatat lagi. "Ini Confidentiality ya, Mas?"

"Betul. Menjaga kerahasiaan kredensial pengguna."

## 15.7 Keamanan Bukan Cuma Kode: Infrastruktur Juga

Mas Andik yang sedari tadi diam ikut angkat bicara. "Dik, keamanan itu gak cuma di kode. Di server juga."

Ia mencontohkan. "Kamu tahu cara kami akses server production?"

"SSH, Mas?"

"Iya. Tapi gak bisa langsung. Harus lewat VPN dulu. Jadi walaupun kamu tahu IP server dan punya password, kamu gak bisa masuk kalau gak terkoneksi ke VPN kantor."

Cahyo mengangguk paham. "Kayak gerbang tambahan."

"Persis. Terus ada firewall. Hanya port tertentu yang terbuka. Ada fail2ban—kalau ada yang coba-coba login SSH berkali-kali dan gagal, IP-nya langsung diblokir otomatis."

"Ini semua untuk menjaga Availability dan Integrity," Mas Alin menambahkan. "Kalau server diretas, Availability hilang. Kalau data di server diubah, Integrity rusak."

## 15.8 Peran QA dalam Keamanan

Mbak Rara ikut nimbrung. "Aku juga punya andil lho, Dik."

Cahyo menoleh. "QA juga urusan keamanan, Mbak?"

"Di tim kecil kayak kita, iya. Idealnya QA juga bagian dari pengujian keamanan. Misalnya, aku coba input aneh-aneh di form—karakter spesial, script, angka negatif. Aku cek apakah ada data sensitif yang bocor di respons API. Aku coba akses endpoint yang harusnya cuma buat admin."

"Jadi QA itu kayak benteng kedua," kata Binto.

"Betul. Setelah developer nulis kode, QA coba jebol. Kalau lolos, berarti ada yang perlu diperbaiki."

## 15.9 Shift-Left Security: Keamanan Sejak Awal

"Nah," Mas Alin mencondongkan badan. "Ini konsep penting. Shift-Left Security."

"Shift-Left?" Cahyo mengulang.

"Iya. Ibaratnya, keamanan digeser ke kiri—ke tahap development. Jangan nunggu production kena baru panik. Dari awal nulis kode, sudah harus mikir keamanan."

Ia memberi contoh. "Unit test bisa cek validasi input. Pipeline CI/CD bisa jalanin *static security check*—ngecek apakah ada library usang yang rentan. Jadi sebelum kode naik ke production, banyak lapisan yang sudah memeriksa."

"Jadi gak cuma ngandalin QA di akhir?" tanya Cahyo.

"Persis. QA penting. Tapi kalau semua celah baru ketemu di QA, itu sudah terlambat. Idealnya, developer sudah menutup celah sejak awal. QA memastikan gak ada yang lolos."

## 15.10 Struktur Tim Keamanan: Kecil vs Besar

"Terus," Cahyo melanjutkan, "di perusahaan gede, keamanan itu tim sendiri ya, Mas?"

Mas Alin mengangguk. "Betul. Di perusahaan besar, biasanya ada tim khusus Security Engineer. Bahkan ada Pentester—tugasnya nyerang sistem sendiri buat cari celah sebelum orang jahat yang nemu."

"Kita di sini belum punya," kata Binto.

"Belum. Kita masih tim kecil. Semua merangkap. Developer mikir keamanan kode. QA tes keamanan. Infra jaga server. Itu sudah cukup untuk skala kita. Tapi kalian perlu tahu, di industri ada jenjang karir khusus keamanan. Siapa tahu nanti tertarik."

"Ada juga yang namanya DevSecOps," tambah Mas Andik. "Itu DevOps yang fokus ke keamanan. Dia yang setup pipeline keamanan, scan kerentanan, urus sertifikat SSL, dan sebagainya."

## 15.11 ISO 27001 dan Kepatuhan Formal

Pakde Suhar yang sedari tadi mendengarkan akhirnya bersuara. "Ngomong-ngomong soal keamanan, saya mau tambah dikit."

Semua menoleh.

"Beberapa klien enterprise, atau proyek pemerintah, suka tanya: 'Kalian sudah ISO 27001 belum?'"

"Apa itu, Pakde?" tanya Cahyo.

"ISO 27001 itu standar internasional untuk Sistem Manajemen Keamanan Informasi. Intinya, perusahaan yang punya sertifikasi ini sudah diakui punya proses keamanan yang matang. Dari kebijakan, prosedur, sampai teknis."

"Kita perlu?" tanya Binto.

Pakde menggeleng. "Untuk proyek kecil kayak Koperasi Sekar Patria atau Pabrik Garum, gak perlu. Klien kita gak minta. Tapi kalau suatu saat kita garap proyek perbankan atau pemerintah, bisa jadi syarat wajib."

Mas Alin menimpali. "Jadi kalian gak perlu hafal isi ISO-nya. Cukup tahu bahwa standar seperti itu ada. Dan prinsip-prinsip dasarnya—seperti CIA Triad—adalah fondasi yang sama."

## 15.12 Pesan untuk Cahyo

Acara makan sudah benar-benar selesai. Piring kertas dan tulang ayam sudah dibereskan. Cahyo berdiri, merapikan tas ranselnya.

"Saya pamit, ya, Pakde, Mas, Mbak. Terima kasih banyak untuk sebulan ini. Saya belajar lebih banyak di sini daripada tiga tahun di sekolah."

Pakde Suhar menepuk bahunya. "Kamu anak baik, Dik. Lanjutkan belajar. Jangan pernah merasa pintar."

Mas Alin menambahkan. "Ingat CIA Triad. Ingat Shift-Left. Jaga keamanan dari semua sisi. Jangan cuma jadi programmer yang cuma mikirin kode jalan."

Mbak Rara menyodorkan sebuah kotak kecil. "Ini oleh-oleh dari kami. Stiker karakter lucu buat laptopmu. Biar ingat sama kita."

Cahyo menerimanya dengan mata berkaca-kaca. "*Matur suwun*."

Binto ikut bersalaman. "Semangat, Dik. Nanti kalau udah kerja, kabari."

Cahyo mengangguk. Ia melangkah keluar, menuju motor bututnya. Sebelum menyalakan mesin, ia menoleh sekali lagi ke kantor ruko sederhana itu. Tempat ia belajar bahwa koding bukan cuma soal algoritma, tapi soal tanggung jawab.

## 15.13 Refleksi Binto

Setelah Cahyo pergi, Binto kembali ke mejanya. Ia menatap laptop, tapi pikirannya melayang.

Beberapa bulan lalu, ia datang ke tempat ini dengan kepala tegak. Lulusan PTN top. Merasa jago. Merasa tahu segalanya.

Hari ini, ia menyadari betapa sedikit yang ia tahu waktu itu.

Git. Scrum. Database. API. QA. Staging. CI/CD. Logging. Dan sekarang keamanan—dengan CIA Triad, shift-left, dan segala kompleksitasnya.

*Perjalanan dari junior ke medior bukan tentang gelar*, pikirnya. *Bukan tentang kampus top. Tapi tentang kemauan untuk terus belajar. Tentang rendah hati. Tentang tanggung jawab.*

Ia menatap papan *sticky notes* di dekat dispenser. Stiker bebek Mas Alin. Stiker kelinci Mbak Rara. Stiker monyet Wawan. Dan sekarang, satu stiker baru dari Cahyo—stiker burung hantu, simbol kebijaksanaan.

Binto tersenyum. Cahyo sudah pergi. Tapi ilmunya menetap. Dan perjalanan Binto sendiri masih panjang.

Ia membuka laptop, siap untuk tugas berikutnya. Benteng-benteng baru akan terus dibangun. Dan ia akan terus belajar menjaganya.

---
