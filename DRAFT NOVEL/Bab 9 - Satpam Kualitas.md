# Bab 9: Satpam Kualitas

## 9.1 "DUA BELAS?!"

Ini musim kemarau, namun semalam justru hujan deras. Pagi ini hawa dingin sisa hujan semalam masih menyisakan kelembapan yang melekat di dinding-dinding tembok kantor. Di luar, suara kepak sayap burung gereja yang berteduh di dahan-dahan rambutan terdengar samar, berselingan dengan bunyi gemerisik daun basah yang diterpa angin pagi. Di dalam ruangan, keheningan sempat merayap tenang, hanya dipecahkan oleh suara renyah Disket yang sedang lahap mengunyah makanan kering dari mangkuknya di dekat dispenser.

Namun, kedamaian pagi itu mendadak koyak.

"DUA BELAS?!"

Suara Binto memecah keheningan pagi di ruang tengah GTN.

Di tangannya, selembar print-out laporan testing yang masih terasa hangat dari baki printer. Mbak Rara berdiri di hadapannya dengan wajah tenang tanpa ekspresi—tatapan matanya datar, namun ada ketegasan dingin yang terpancar dari sana.

"Iya, Mas. Dua belas defect."

"Tapi Mbak... ini cuma fitur dashboard. Satu halaman doang. Masa iya ada dua belas?"

Mbak Rara narik napas. "Satu: input tanggal nggak divalidasi. Dua: response time di atas tiga detik. Tiga: error message belum user-friendly. Empat: warna indikator nggak sesuai guideline. Lima—"

"Iya iya, saya ngerti. Tapi kan itu... kecil-kecil."

Mbak Rara berhenti. Matanya natap Binto. Bukan dengan marah. Tapi dengan sesuatu yang lebih dalem. Kayak ada beban di situ.

"Mas Binto. Di dunia saya sebelumnya... nggak ada defect yang kecil."

Binto mau nyaut. Tapi sesuatu di nada suara Mbak Rara bikin dia berhenti.

"Kita bahas satu per satu nanti ya, Mas. Saya mau ambil kopi dulu."

Dan dia pergi. Meninggalkan Binto dengan kertas laporan di tangan. Dan perasaan nggak enak.

---

## 9.2 Uji Coba: Input Aneh, Token Kadaluarsa, Stok Minus

Seminggu terakhir ini, Mbak Rara memang jadi penguji paling teliti yang pernah Binto temui.

Setiap hari, minimal satu defect. Kadang dua. Kadang tiga. Bukan defect besar. Bukan yang bikin sistem crash. Tapi defect kecil. Remeh. Namun menusuk.

Siang itu, Mbak Rara mengambil alih laptop Binto. Ia membuka Postman dan mulai "bermain."

Pertama, ia membuka endpoint Login. Ia mengisi email dengan `' OR '1'='1` dan password kosong. Klik Send. Error 500. Internal Server Error.

Binto mengernyit. "Lho?"

Mbak Rara tidak berkomentar. Ia mencoba lagi: email `sales1@tokobangun.com` dengan password salah. Respons: "Email atau password salah." Itu sudah benar.

Lalu ia pindah ke endpoint Buat Pesanan. Ia mengirim data produk dengan jumlah -5. Error 500.

"Jumlah minus harusnya ditolak, Mas. Kasih tahu pengguna bahwa jumlah tidak valid. Jangan error 500."

Binto mulai gelisah.

Mbak Rara melanjutkan. Ia membuat pesanan dengan produk yang stoknya 0. API Binto memprosesnya. Stok menjadi minus 1.

"Nah, ini bahaya. Stok minus bisa bikin laporan kacau. Harusnya ada validasi."

Belum selesai. Mbak Rara mencoba masuk ke endpoint daftar pesanan menggunakan token milik sales B. Ia mengganti parameter ID menjadi ID milik sales A. Data sales A muncul utuh.

"Mas, ini datanya kok muncul yang bukan punya user ini?"

Mas Alin yang sedari tadi memperhatikan langsung mendekat. Wajahnya serius.

"Ini bukan cuma bug. Kalau salah user bisa lihat data orang lain... itu celah otorisasi yang fatal."

Suasana ruangan mendadak hening. Kipas angin Ufo yang berputar pelan kini terdengar jelas.

Untuk pertama kalinya, Binto merasa ini bukan sekadar error kecil yang bisa ditertawakan.

Setelah ditelusuri, ternyata query untuk melihat detail pesanan tidak memfilter berdasarkan kepemilikan user. Binto lupa menaruh filter pengecekan.

Mbak Rara menutup laptop. "Ini belum apa-apa, Mas. Bayangin kalau ini sudah dipakai sales di lapangan. Mereka bisa input angka minus. Stok kacau. Orang iseng ngintip data sales lain. Reputasi kita hancur."

---

## 9.3 Curhat ke Wawan

Siang itu, Binto cerita ke Wawan sambil makan di warung depan.

"Wan, Mbak Rara tuh teliti banget ya?"

Wawan nyeruput es teh. "Emang kenapa, Mas?"

"Dua belas defect, Wan. Untuk fitur dashboard doang."

"Wah. Banyak juga."

"Kan? Masa iya—"

"Tapi..." Wawan naruh gelasnya. "Mas Binto pernah denger cerita masa lalunya Mbak Rara?"

Binto mikir. "Belum."

"Ya udah. Makanya jangan komplain dulu."

"Emang kenapa?"

Wawan cuma geleng-geleng. "Tanya sendiri aja, Mas. Bukan hak saya buat cerita."

Binto menatap Wawan. Ada sesuatu di cara Wawan ngomong yang bikin penasaran. Bukan defensif. Tapi protektif.

---

## 9.4 Kenapa QA Itu Penting

Alih-alih marah setelah sesi testing, Mbak Rara duduk di sebelah Binto. Ia membuka buku catatannya.

"Aku ini bukan lulusan IT, Mas. Aku lulusan Manajemen. Gak ngerti coding dalem-dalem. Tapi aku ngerti gimana pengguna berpikir."

"Mereka bisa pencet apa aja. Bisa isi form dengan emoji, angka minus, huruf di field yang harusnya angka. Mereka gak peduli sama logika di balik layar. Yang mereka tahu: aplikasi harus jalan."

"Tugasku cuma satu: jadi satpam kualitas. Aku jagain gerbang biar gak ada yang aneh lolos ke production."

"Ada prinsip yang selalu aku pegang: Lebih baik error di sini, di tangan QA, daripada error di tangan pengguna. Di sini, error bisa diperbaiki diam-diam. Di sana, error jadi tontonan."

Mas Alin dari pojokannya ikut bersuara. "Betul, Ra. Di tim kecil kayak kita, QA itu investasi. Kita gak mau klien kita yang jadi QA."

---

## 9.5 Kitab Penjaga Mutu

Mas Alin bangkit dan berjalan mendekat. "Omong-omong soal testing profesional, sebenarnya ada standar internasional. Namanya ISO 29119. Versi terbarunya 2022."

"ISO? Kayak standar mutu pabrik?"

"Nggih. ISO 29119 itu standar untuk software testing. Isinya panduan proses testing yang sistematis: dari perencanaan, desain test, eksekusi, sampai pelaporan. Kita gak harus saklek. Tapi bagus buat jadi referensi biar testing kita gak asal-asalan."

Mbak Rara menambahkan. "Intinya: testing harus direncanakan, didokumentasikan, dan dilakukan secara independen. Independen artinya: jangan developer yang ngetes kodenya sendiri. Harus ada mata lain. Makanya ada aku."

Binto manggut-manggut. Ia baru tahu ada standar internasional untuk hal yang selama ini ia anggap remeh.

---

## 9.6 Membaca Arah Badai

"Salah satu konsep penting di ISO 29119," Mbak Rara melanjutkan, "adalah Risk-Based Testing."

Binto mengulang. "Risk-Based Testing?"

"Kita gak mungkin menguji semua kemungkinan. Waktu dan resource terbatas. Jadi kita harus pintar memilih: fitur mana yang paling berisiko? Yang kalau rusak dampaknya paling besar? Itu yang kita prioritaskan."

Ia menunjuk catatannya. "Fitur pesanan: kalau ada bug, stok minus, laporan kacau, klien marah. Risiko tinggi. Makanya aku buat banyak skenario. Fitur lihat produk: paling cuma tidak muncul. Risiko rendah. Aku tetap uji, tapi tidak sedalam pesanan."

"Tapi," Mas Alin menambahkan, "bukan berarti developer lepas tangan. Ada konsep Shift-Left: kualitas digeser ke kiri, ke tahap development. Developer harus nulis unit test untuk kodenya sendiri."

Mbak Rara mengangguk. "Aku senang kalau developer nulis unit test. Pekerjaanku jadi lebih ringan. Aku bisa fokus ke skenario kompleks, bukan validasi dasar."

---

## 9.7 Test Plan: Peta Perang Mbak Rara

Mbak Rara menunjukkan satu halaman penuh coretan ke Binto.

"Ini test plan sederhana buat API Kalimantan. Aku bikin sebelum kamu mulai ngoding. Harusnya aku kasih lihat dari awal, tapi aku keburu cuti."

Binto melihat halaman itu:

- Login: email valid + password benar (200), password salah (401), email kosong (422)
- Produk: dengan token valid (200), tanpa token (401), token kadaluarsa (401)
- Pesanan: jumlah valid (201), jumlah minus (422), melebihi stok (422), produk tidak ditemukan (404)

"Harusnya tiap kali ada backlog naik ke sprint, aku bikin test plan kayak gini. Developer bisa lihat, jadi tahu nanti API-nya akan diuji dari sisi mana. Bukan jebakan. Ini kolaborasi."

Binto mengangguk. Testing bukan sekadar mencari-cari kesalahan. Tapi proses yang terencana dan transparan.

---

## 9.8 Otomatisasi vs Manual

"Terus, Mbak. Apa semua testing harus manual kayak tadi?" tanya Binto.

Mbak Rara menggeleng. "Enggak. Itu cuma buat eksplorasi awal. Untuk test yang berulang—login, validasi form—kita bisa pakai automated testing."

"Setiap kali kamu nambah fitur, kamu harus pastiin fitur lama gak rusak. Itu regression testing. Kalau manual, habis waktu. Mending pakai script otomatis. Di Laravel ada PHPUnit. Di Postman bisa bikin collection yang di-run otomatis."

"Tapi gak semua harus otomatis?"

"Gak semua. Untuk eksplorasi, UX, atau kasus aneh, tetap perlu manual. Otomatisasi itu investasi: butuh waktu nulis script, tapi jangka panjang hemat waktu."

---

## 9.9 Mencari Tahu

Jam setengah enam sore. Kantor mulai sepi. Mas Alin sudah pulang. Wawan sudah cabut. Andik di depan rak server, entah ngapain.

Tinggal Binto dan Mbak Rara.

Mbak Rara masih di mejanya. Laptop menyala. Beberapa screenshot aplikasi ditandai panah merah.

Binto jalan pelan-pelan. Mendekat.

"Mbak... masih kerja?"

Mbak Rara menoleh. "Oh, Mas Binto. Iya, lagi ngecek test case buat besok."

"Mbak... saya boleh tanya sesuatu?"

Mbak Rara menutup laptopnya. "Silakan, Mas."

Binto duduk. Di kursi sebelah meja Rara. Tangannya mulai meremas ujung kemeja putihnya. Kebiasaan sejak kecil.

"Saya penasaran, Mbak. Soal kenapa Mbak segitunya soal testing?"

Mbak Rara diam. Lama. Sampai Binto mulai merasa tidak enak.

"Maaf, Mbak. Kalau nggak enak diceritain—"

"Nggak apa-apa, Mas." Dia menarik napas. Dalam. "Saya cerita ya. Tapi panjang."

"Saya dengerin, Mbak."

---

## 9.10 Cerita di Balik Ketelitian

"Sebelum di sini, saya kerja di pabrik obat herbal, Mas."

"Oh? Di bagian apa?"

"QC. Quality Control."

Binto terkejut. QC obat herbal sama QA software... mirip.

"Jadi Mbak memang sudah terbiasa ya?"

"Begitulah." Mbak Rara melihat ke jendela. Matanya menerawang.

"Waktu itu, saya masih baru. Masih muda. Masih terlalu percaya diri. Merasa semua sudah benar, sudah sesuai SOP."

Dia jeda.

"Suatu hari, ada batch produksi besar. Ribuan botol. Harus dikirim ke distributor besok paginya. Saya ditugaskan mengecek batch terakhir."

"Harusnya saya mengecek semua. Dari bahan baku, proses ekstraksi, sampai produk jadi. Tapi..." Mbak Rara berhenti. Tangannya sedikit gemetar. "Tapi saya kelewat satu step."

Binto tidak berani bernapas.

"Saya pikir, 'Ah, paling juga sama kayak batch sebelumnya. Aman.' Jadi saya tanda tangan. Lulus. Kirim."

"Tiga hari kemudian, telepon masuk. Dari distributor. Ada laporan. Konsumen yang minum obat itu... anak-anak, Mas. Beberapa diare. Beberapa muntah-muntah. Satu masuk rumah sakit."

Binto merasa seluruh badannya dingin.

"Saya nggak bisa tidur seminggu, Mas. Nggak bisa makan. Nggak bisa mikir. Setiap nutup mata, saya kebayang muka anak-anak itu. Yang sakit. Yang dirawat. Cuma gara-gara..."

Suaranya mulai pecah.

"Cuma gara-gara saya pikir... ah, paling juga sama."

"Hasil investigasi menemukan apa, Mbak?"

"Ada kontaminasi kecil di salah satu bahan baku. Harusnya ketangkap di step yang saya lewatin. Tapi karena tidak ketangkap, produk lolos. Sampai ke konsumen."

Mbak Rara mengusap matanya.

"Saya mundur seminggu setelah itu, Mas. Bukan dipecat. Saya yang mundur. Karena saya malu. Sama diri sendiri. Sama pabrik. Sama semua orang."

Binto hanya bisa diam.

"Makanya, Mas Binto..." Mbak Rara menatap Binto. Kali ini matanya jelas. Tegas. "Kalau saya kirim dua belas defect ke kamu, itu bukan karena saya tidak suka kode kamu. Tapi karena..."

Dia jeda.

"Satu kelalaian kecil bisa bikin anak masuk rumah sakit."

Kalimat itu menancap.

"Di dunia software, mungkin tidak ada anak yang masuk rumah sakit. Tapi ada pengguna yang kecewa. Ada klien yang marah. Ada bisnis yang rugi. Ada orang yang dipecat. Semua cuma gara-gara kita pikir, 'Ah, paling juga nggak apa-apa.'"

Binto melihat kertas laporan defect yang tadi pagi dia terima. Dua belas butir. Yang tadi pagi dia anggap remeh. Yang tadi pagi dia komplain.

Sekarang dia melihatnya berbeda.

---

## 9.11 Memandang Ulang

Malam itu, Binto tidak langsung pulang.

Dia buka lagi laptop. Buka lagi aplikasi. Buka lagi laporan defect.

Satu per satu.

Defect #1: Input tanggal tidak divalidasi. Binto lihat kodenya. Kalau user masukkan 30 Februari, sistem tidak mengecek. Padahal perbaikannya gampang. Cuma satu fungsi validasi. Kenapa aku tidak kepikiran?

Defect #4: Warna indikator tidak sesuai guideline. Binto pakai merah untuk normal. Harusnya hijau. Kesalahan kecil. Tapi user lihat merah, mereka panik. Mengira ada error. Padahal tidak.

Defect #7: Pesan error terlalu teknis. "Error 500: NullPointerException at line 247." Bagaimana kalau yang lihat Bu Sari? Atau klien UMKM yang tidak ngerti teknis? Mereka pasti makin panik.

Binto ingat analogi Mas Alin: API itu kontrak. Harus jelas.

Tapi ini bukan cuma soal API. Ini soal komunikasi ke manusia.

Jam sepuluh malam. Binto masih di kantor. Sudah memperbaiki tujuh defect. Masih lima lagi. Mata perih. Punggung pegal. Tapi dia terus.

Bukan karena takut dimarahi. Bukan karena mengejar target. Tapi karena... Satu kelalaian kecil bisa bikin anak masuk rumah sakit.

Bukan anak beneran. Tapi mungkin kepercayaan. Reputasi. Karir seseorang. Dan itu hampir sama sakitnya.

---

## 9.12 Perbaikan dan Unit Test Pertama

Keesokan harinya, Binto memperbaiki satu per satu celah yang ditemukan Mbak Rara.

Pertama, validasi di endpoint pesanan: jumlah minimal 1, tidak boleh melebihi stok. Jika tidak valid, kembalikan 422 dengan pesan jelas.

Kedua, pengecekan token: API memverifikasi keabsahan, bukan hanya keberadaan. Token palsu atau kadaluarsa langsung ditolak 401.

Ketiga, penanganan error global: setiap exception ditangkap dan diubah menjadi respons JSON standar. Tidak ada lagi error 500 misterius.

Keempat, validasi input tanggal: format, rentang, dan logika dicek sebelum masuk database.

Kelima, warna indikator sesuai guideline: hijau untuk normal, kuning untuk perlu perhatian, merah hanya untuk error.

Satu per satu. Sampai semua dua belas.

Mas Alin mendampingi. "Sekarang coba tulis unit test untuk endpoint login."

Binto membuka folder `tests/Feature`. Membuat file `AuthTest.php`. Menulis test case:

- test_login_with_valid_credentials_returns_token
- test_login_with_invalid_credentials_returns_401
- test_login_with_missing_fields_returns_422

Ia menjalankan `php artisan test`. Titik-titik hijau. Semua test lulus.

"Lihat, Mas. Hijau semua."

Mas Alin tersenyum. "Nah, itu rasanya aman. Setiap kali kamu ubah kode, jalankan test ini. Kalau ada yang merah, berarti kamu tidak sengaja merusak sesuatu."

---

## 9.13 Permintaan Maaf

Pagi berikutnya, Binto datang lebih pagi lagi.

Kali ini dia tidak ke mejanya dulu. Tapi langsung ke meja Mbak Rara.

Mbak Rara sedang menyalakan laptop. Masih memegang cangkir teh hangat.

"Eh, Mas Binto. Pagi."

"Mbak Rara..."

"Ya?"

Binto menarik napas. "Saya minta maaf."

"Lho, maaf kenapa?"

"Beberapa hari lalu. Saya komplain soal defect. Saya pikir itu kecil. Saya pikir Mbak terlalu perfeksionis. Padahal..." Dia jeda. "Padahal saya yang nggak ngerti."

Mbak Rara diam. Lalu senyum. Tipis.

"Nggak apa-apa, Mas. Saya juga dulu kayak gitu. Sebelum kejadian."

"Saya sudah perbaiki semuanya, Mbak. Semalam. Semua dua belas. Tolong dicek lagi."

"Wah. Semalam? Jam berapa pulangnya?"

"Nggak papa, Mbak." Binto nyengir. "Biar saya tahu rasanya jadi QA."

Mbak Rara ketawa kecil. "Nah, gitu dong."

"Tapi Mbak... saya jadi belajar sesuatu."

"Apa, Mas?"

"Testing itu bukan buat mencari kesalahan. Tapi buat memastikan tidak ada yang sakit."

Mbak Rara menatap Binto. Lama. Kali ini matanya tidak penuh beban. Tapi hangat.

"Makasih, Mas Binto."

"Sama-sama, Mbak."

Senyum tipis Mbak Rara pagi itu terasa menenangkan, seperti uap teh hangat yang memudar di udara sejuk Srengat.

---

## 9.14 Refleksi: Kita Semua Punya Luka

Siang harinya, terik matahari yang mulai menyengat diredam oleh rimbunnya dedaunan pohon rambutan di teras. Binto duduk bersisian dengan Wawan di bangku kayu.

"Wan."

"Ya, Mas?"

"Aku sudah tahu."

"Tahu apa?"

"Soal Mbak Rara."

Wawan menoleh. "Oh... dia cerita?"

"Dia cerita."

Mereka berdua diam. Melihat pohon rambutan yang daunnya goyang kena angin.

"Berat ya, Mas."

"Berat."

"Makanya saya dulu tidak berani cerita ke Mas. Itu bukan cerita saya."

Binto mengangguk. "Aku ngerti."

"Tapi sekarang Mas sudah tahu, kan? Kenapa Mbak Rara tuh teliti banget."

Binto ketawa kecil. "Iya. Dan aku merasa malu. Aku pikir aku paling benar. Paling ngerti. Cumlaude segala. Tapi soal ketelitian... aku kalah sama Mbak Rara."

Wawan menyender di tembok. "Mas Binto tahu tidak... di tim ini, ada satu pelajaran yang paling penting?"

"Apa?"

"Kita semua punya luka masing-masing."

Binto menoleh.

"Mas Alin... near-death experience. Saya... bapak saya. Mbak Rara... batch obat. Semua di sini punya cerita. Punya alasan kenapa mereka jadi kayak sekarang."

"Terus aku?"

"Mas Binto juga pasti punya. Entah apa. Nanti suatu saat Mas bakal cerita."

Binto diam.

Luka aku apa? Mungkin lulusan PTN top tapi tidak bisa apa-apa. Mungkin IPK cumlaude tapi di dunia kerja cuma jadi beban. Mungkin merasa superior, padahal inferior.

Dan di sinilah ia sekarang. Di sebuah kantor kecil di belakang pasar tradisional. Dikelilingi orang-orang yang—seperti pohon rambutan di depannya—pernah patah dan tumbuh dari luka. Namun pada akhirnya, mereka tetap sanggup berbuah pada waktunya. Tetap ranum dan manis.

*Mungkin itu intinya*, batin Binto menghela napas panjang. *Bukan tentang seberapa dalam luka yang kita bawa. Tapi seberapa lapang dada kita membiarkannya mengakar, lalu menjadikannya tempat untuk tumbuh.*

Di atas kepala mereka, sisa angin kemarau menggoyang pelan dahan-dahan rambutan. Menggugurkan satu persatu daun yang memang waktunya dilepaskan, untuk kelak akan berganti dengan daun-daun baru.

Seperti tim ini. Seperti baris-baris kode yang baru ia perbaiki semalam. Dan tentu saja, seperti dirinya sendiri.