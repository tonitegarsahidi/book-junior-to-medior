# Sinopsis Novel — From Junior to Medior

## Sinopsis Global

Binto, lulusan Ilmu Komputer dari sebuah PTN ternama, sempat bekerja dua tahun di Jakarta sebelum akhirnya pulang ke Blitar karena ayahnya jatuh sakit. Dengan ijazah di tangan dan kepala tegak — yakin ilmunya sudah cukup untuk dunia kerja — ia melamar ke GTN, sebuah software house kecil yang berkantor di gang sempit perkampungan. Di sana ia bertemu Mas Alin, seorang Tech Lead yang bicaranya pelan tapi selalu menusuk tepat ke titik buta.

Sambutan pertama Mas Alin bukan pujian, melainkan pertanyaan-pertanyaan yang meruntuhkan kepercayaan diri Binto: "Kamu bisa Git?" "Kamu tahu Scrum?" "Kamu pernah deploy?" Jawaban Binto selalu "belum." Di situlah perjalanan sebenarnya dimulai.

Selama satu tahun, Binto belajar bahwa menjadi software engineer bukan sekadar bisa ngoding cepat. Ia belajar version control dari Git, kerja tim dari Scrum, menulis kode bersih dari Service-Repository Pattern, membangun API dari analogi Restoran Padang, menahan serangan dari QA yang teliti, membaca log seperti detektif, hingga memahami keamanan, scaling, dan CI/CD. Setiap pelajaran datang melalui proyek nyata: tombol laporan untuk klien minimarket di Kalimantan, database berantakan dari klien Tulungagung, aplikasi mobile untuk tim sales lapangan, hingga sistem yang mulai lemot karena pengguna bertambah.

Di sepanjang jalan, Binto tidak hanya belajar teknologi. Ia belajar rendah hati — bahwa lulusan SMK seperti Wawan bisa lebih jago darinya, bahwa anak magang seperti Cahyo berhak mendapat bimbingan yang sama, bahwa pertanyaan "kenapa" lebih penting daripada "bagaimana." Ia juga belajar bahwa software engineer tidak menulis kode untuk mesin; mereka menulis kode untuk manusia — pengguna di pelosok Kalimantan, pemilik toko kelontong di Tulungagung, atau siapa pun yang hidupnya tersentuh oleh sebuah tombol di layar.

Novel ini adalah kisah tentang transformasi: dari seorang "single fighter" yang hanya tahu teori, menjadi seorang engineer yang paham bahwa kode adalah warisan, tim adalah fondasi, dan pembelajaran tidak pernah selesai — selalu setengah matang, seperti tumbler ½ M yang menemani harinya.

---

## Sinopsis Per Bab

### Bab 1 — Kepala Tegak di Bawah Pohon Rambutan

Binto pulang ke Blitar setelah empat tahun kuliah dan dua tahun bekerja di Jakarta. Ayahnya — seorang pensiunan — kini terbaring dengan diabetes, tubuhnya melemah. Dengan ijazah sarjana ilmu komputer di tangan, Binto percaya diri melamar ke GTN, sebuah software house yang beralamat di gang sempit di pinggir desa. Ia membayangkan kantor modern, ruangan ber-AC, dan rekan-rekan yang akan kagum pada prestasinya.

Kenyataan berkata lain. Kantor GTN adalah rumah sederhana dengan pohon rambutan rindang di halaman. Suara jangkrik dan burung lebih keras daripada suara keyboard. Mas Alin — Tech Lead berbadan kurus, rambut mulai memutih di usia akhir 30-an — tidak memberinya sambutan hangat. Ia malah melontarkan pertanyaan-pertanyaan yang tidak pernah diajarkan di kampus: "Kamu bisa Git?" "Tahu Scrum?" "Pernah deploy ke production?" Setiap jawaban Binto adalah "belum."

Di bawah pohon rambutan itu, kepala tegak Binto mulai runtuh. Ia menyadari bahwa kampus telah mengajarinya menjadi *single fighter* — mengerjakan semuanya sendiri, mengejar deadline skripsi, tidak pernah benar-benar berkolaborasi. Sementara dunia industri menuntut sesuatu yang sama sekali berbeda: kerja tim, version control, metodologi pengembangan, dan kerendahan hati untuk terus belajar. Mas Alin menutup percakapan dengan kalimat yang menjadi fondasi perjalanan Binto: "Kampusmu ngajarin kamu jadi single fighter. Tapi di sini, kami kerja bareng."

### Bab 2 — Mesin Waktu Bernama GIT

Hari pertama Binto di GTN dimulai dengan rasa canggung. Ia belum diberi tugas, hanya diminta "mempelajari repositori." Mas Alin memberinya akses ke repo Git dan memberinya misi pertama: memahami kode yang sudah ada.

Binto mendapati dirinya tidak tahu harus mulai dari mana. Ia terbiasa mengerjakan tugas kuliah sendirian — satu folder, satu file, paling banter dikirim via ZIP. Mas Alin kemudian memberinya kuliah singkat tentang Git: `git init`, `git status`, `git add`, `git commit`, `git log`. Binto mulai memahami bahwa Git adalah mesin waktu — setiap commit adalah snapshot yang bisa dikunjungi kembali kapan saja.

Pelajaran berlanjut ke `git branch` dan `git checkout`. Mas Alin menjelaskan cabang sebagai "versi paralel" dari kode, memungkinkan banyak orang bekerja bersamaan tanpa saling menginjak. `git stash` diajarkan sebagai "laci darurat" untuk menyimpan pekerjaan setengah jadi. Puncaknya, Mas Alin mendemonstrasikan `git merge` dan konflik — apa yang terjadi ketika dua cabang mengubah baris yang sama.

Di sela-sela pelajaran, Binto menemukan sesuatu yang mengejutkan: Wawan, rekannya yang lulusan SMK, ternyata sedang kuliah online S1. Ia menjalaninya selepas jam kantor — kadang di kantor sepulang kerja, kadang di rumahnya. Wawan tidak pernah menyombongkan diri. Ia bekerja sambil belajar, membiayai kuliahnya sendiri. Binto yang tadinya merasa "lebih tinggi" karena lulusan PTN top mulai merasa malu — ijazah bukan ukuran. Menjelang Ashar, Mas Alin menutup sesi dengan pesan: "Kode adalah warisan. Kamu menulis hari ini, orang lain yang nerusin besok. Git adalah caramu memastikan warisan itu utuh."

### Bab 3 — Waterfall, Agile, dan Sticky Notes Bebek

Di hari keduanya, Binto dihadapkan pada istilah "Sprint Planning" dan trauma lamanya langsung kambuh. Skripsi di kampus dulu dikerjakan dengan Waterfall — enam bulan waktu yang diberikan, tapi empat bulan pertama habis hanya untuk revisi Bab 1. Bab 2, 3, dan seterusnya harus dikebut dalam dua bulan tersisa, sering begadang sampai subuh. Hasilnya? "Lulus, tapi rasanya kayak abis perang."

Mas Alin membandingkan dua proyek yang pernah ia tangani: proyek pabrik pakan ternak yang menggunakan Waterfall — setahun pengembangan, begitu selesai, klien bilang "maaf, bisnis saya sudah berubah" — dan proyek GTN yang menggunakan Scrum. Di Scrum, setiap dua minggu ada sesuatu yang bisa dilihat dan diuji klien. Klien tidak perlu menunggu setahun untuk tahu hasilnya.

Pakde Suhar — pemilik GTN — mengumpulkan tim di depan papan fisik yang penuh sticky notes. Ia memperkenalkan tiga peran Scrum: Product Owner (dirinya sendiri, "yang tahu apa yang harus dibuat"), Scrum Master (Mas Alin, "yang memastikan proses berjalan"), dan Development Team (semuanya, "yang mengeksekusi"). Binto menyaksikan Sprint Planning pertama: Pakde menjelaskan fitur-fitur prioritas, tim memecahnya menjadi tugas-tugas kecil, sticky notes berpindah dari kolom "Backlog" ke "To Do."

Selama sprint, Binto mengikuti Daily Scrum — rapat 15 menit setiap pagi, berdiri, menjawab tiga pertanyaan: apa yang sudah dikerjakan kemarin, apa yang akan dikerjakan hari ini, apa hambatannya. Ia kagum pada kesederhanaannya. Tidak ada laporan panjang, tidak ada presentasi PowerPoint. Hanya sticky notes yang bergerak: To Do → In Progress → Testing → Done.

Sprint diakhiri dengan Sprint Review via Zoom bersama Pak Bambang, kepala Puskesmas. Pak Bambang antusias melihat progress, tapi juga minta fitur tambahan yang belum direncanakan. Pakde Suhar — dengan seni diplomasi khas pemilik usaha kecil — tidak mengatakan "tidak," tapi "belum." "Ini kita masukin ke sprint berikutnya ya, Pak. Yang sekarang fokus ke antrian dulu." Binto belajar bahwa mengelola ekspektasi klien sama pentingnya dengan menulis kode.

Setelah review, tim berkumpul untuk Sprint Retrospective. Ngopi bersama, mengevaluasi: apa yang berjalan baik, apa yang harus diperbaiki. Tidak ada yang saling menyalahkan. Suasana seperti keluarga, bukan seperti ruang sidang.

### Bab 4 — Perjalanan Sebuah Tombol

Pagi yang cerah di GTN dipecahkan oleh telepon dari Kalimantan. Pak Haji Hamid — pemilik minimarket di Balikpapan yang sudah menjadi klien setia — butuh satu fitur mendesak: tombol laporan. Hanya satu tombol. Klik, muncul laporan pendapatan bulanan. Tapi harus selesai besok lusa karena minggu depan ada rapat dengan investor.

Mas Alin memanggil tim untuk rapat kilat di depan papan sticky notes. Ini bukan fitur biasa — ini fitur "sisipan" yang harus dikerjakan tanpa mengganggu sprint yang sedang berjalan. Binto belajar menulis PRD (Product Requirement Document) sederhana: apa yang diinginkan klien, siapa penggunanya, apa kriteria berhasilnya. Dari PRD, tim menulis acceptance criteria — daftar kondisi konkret yang harus terpenuhi agar fitur dianggap "selesai."

Binto membuat branch baru dari main, menulis kode untuk tombol laporan, dan membuka Pull Request. Ia pikir tugasnya sudah selesai — toh kodenya sudah jalan. Tapi Mas Alin punya pendapat lain. Code review bukan formalitas. Ia membaca kode Binto baris per baris.

"`$tmp`, ini apaan?" tanya Mas Alin, menunjuk nama variabel. Binto tersipu. Di kampus, nama variabel tidak pernah dipermasalahkan — yang penting program jalan. Mas Alin menjelaskan bahwa kode dibaca lebih sering daripada ditulis. `$tmp` tidak berarti apa-apa. `$total_pendapatan` — itu baru nama yang bermakna. Binto belajar memberi nama yang "jujur" pada setiap variabel dan fungsi.

Setelah revisi, giliran Mbak Rara — QA GTN — menguji fitur. Tangannya lincah memasukkan input-input aneh: tanggal 30 Februari, angka negatif, field kosong. Binto mendengus — siapa juga yang akan menginput tanggal 30 Februari? Ternyata programnya menerima input itu dan menghasilkan laporan ngawur. Mbak Rara menemukan bug kabisat — tahun kabisat tidak ditangani dengan benar. Binto belajar bahwa QA bukan mencari-cari kesalahan; QA adalah tameng terakhir sebelum pengguna sungguhan menemukan bug.

Setelah perbaikan, tombol akhirnya meluncur ke production. Sore harinya, Mas Alin mengirim pesan di grup: Pak Haji sudah pakai tombol laporannya. "Katanya rapat sama investor lancar. Terima kasih." Binto tersenyum. Satu tombol. Satu klik. Di ujung sana, seorang pemilik minimarket di Balikpapan bisa mempresentasikan bisnisnya dengan percaya diri. Inilah makna menjadi software engineer — bukan tentang kode, tapi tentang dampak.

### Bab 5 — No Silver Bullet

Seminggu pertama di GTN membuat Binto keranjingan mengamati. Ia melihat struktur repo, membaca kode demi kode, dan menemukan satu pola: semuanya PHP. Tidak ada Go, tidak ada Rust, tidak ada Node.js. Hanya PHP. Pikirannya kembali ke forum-forum pemrograman di internet yang selalu bilang "PHP is dead," "PHP itu bahasa masa lalu," "kalau mau serius, pake Go atau Rust."

Suatu sore, ia memberanikan diri bertanya pada Mas Alin. Kenapa GTN hanya pakai PHP? Mas Alin tidak langsung menjawab. Ia malah bercerita tentang proyek pemerintah yang pernah ia kerjakan di startup sebelumnya. Startup itu memilih *bleeding-edge stack* — framework terbaru, bahasa paling hype, arsitektur paling keren. Hasilnya? Development cepat di awal, tapi begitu masuk production: server klien tidak support, library yang dipakai tiba-tiba abandoned, developer susah dicari. Startup itu tutup dalam dua tahun.

Kemudian Mas Alin menceritakan proyek yang sama, versi yang ia kerjakan sekarang di GTN. PHP, framework Laravel, database MySQL. Bukan teknologi paling keren. Tapi server shared hosting murah bisa pakai. Developer mudah dicari. Ekosistem mature. "Mobil Alphard itu mewah," kata Mas Alin, "tapi coba masukkin ke gang sempit depan kantor ini. Gak bakal muat. Agya memang kecil, tapi dia bisa masuk, bisa putar balik, gak nyangkut."

Binto mulai memahami. Pemilihan teknologi bukan soal "keren" atau "basi." Ini soal konteks. Klien GTN adalah pengusaha UMKM — mereka butuh solusi yang berfungsi, bukan arsitektur yang kompleks. Server mereka shared hosting, bukan Kubernetes cluster. Tim kecil, proyek banyak. Di sinilah PHP dan monolith bersinar — satu codebase, deploy sekali, selesai.

Mas Alin juga bercerita tentang "hantu-hantu yang masih hidup" — sistem-sistem legacy yang dibangun puluhan tahun lalu dengan COBOL, masih berjalan di bank-bank besar. Gaji programmer COBOL selangit karena yang bisa makin sedikit. Binto tercenung. Ia yang mengira teknologi baru selalu lebih baik, kini sadar bahwa setiap teknologi punya tempat dan waktunya.

Bab ini ditutup dengan pengenalan konsep "No Silver Bullet" — esai legendaris Fred Brooks dari 1986 yang menyatakan bahwa tidak ada satu teknologi pun yang bisa menyelesaikan semua masalah software engineering. Tidak ada peluru sakti. Yang ada hanyalah *the right tool for the right job*.

### Bab 6 — Membangun Rumah yang Bersih

Pakde Suhar memberi Binto tugas "santai": aplikasi inventaris untuk Bu Warsiti, pemilik toko kelontong di Srengat. Kebutuhannya sederhana — catat barang masuk, barang keluar, stok tersisa. "Gampang," pikir Binto. Ia mengerjakannya dengan gaya kampus: satu file controller, semua logika di sana, query SQL mentah bercampur HTML, tidak ada struktur yang jelas. Dalam dua jam, aplikasi jadi. Bangga, ia pulang.

Keesokan paginya, Binto membuka kembali kodenya. Dan ia tidak mengerti apa yang ia tulis. Variabel-variabel dengan nama seperti `$x1`, `$tmp2`, `$ar`. Logika bisnis bercampur query database bercampur tampilan HTML. Dua jam ia menatap layar, mencoba memahami pikiran "Binto yang kemarin."

Mas Alin datang dan tersenyum melihat tampang frustrasi Binto. Ia tidak memarahi. Ia malah memberikan analogi: "Kamu pernah lihat rumah tanpa sekat?" Rumah tanpa sekat — ruang tamu, dapur, kamar mandi, semua jadi satu. Mau masak, baunya ke mana-mana. Mau tidur, terganggu tamu. Mau pipis, tidak ada privasi.

Kode yang baik juga butuh sekat. Mas Alin memperkenalkan Service-Repository Pattern: Controller menerima request dan memberi respons, Repository berurusan dengan database, Service berisi logika bisnis. Masing-masing punya tanggung jawab jelas, tidak saling mencampuri. Ia juga mengajarkan DRY (Don't Repeat Yourself) — kalau ada kode yang sama di dua tempat, pindahkan ke satu fungsi.

Binto melakukan "operasi plastik" pada kodenya sendiri. Ia memisahkan controller menjadi service dan repository. Ia mengganti nama variabel. Ia membuang kode duplikat. Ia menambahkan komentar — bukan komentar yang menjelaskan *apa* (kode sudah cukup jelas), tapi *kenapa* — alasan di balik keputusan desain tertentu. "Tulis komentar untuk dirimu sendiri enam bulan dari sekarang," kata Mas Alin.

Mbak Rara — yang biasanya galak saat testing — kali ini memuji. "Nah, gini enak bacanya," katanya sambil tersenyum. Binto belajar bahwa kode yang baik tidak hanya berfungsi, tapi juga "enak dibaca" — oleh kolega, oleh QA, dan terutama oleh dirinya sendiri di masa depan.

### Bab 7 — Tulang Punggung Sistem

Hari Sabtu. Harusnya libur, tapi Binto datang ke kantor karena penasaran dengan proyek klien dari Tulungagung. Mas Andik — DevOps GTN yang biasanya pendiam — sudah dulu datang, ditemani segelas kopi tubruk.

Di halaman, pohon rambutan sedang panen raya. Bu Sari dan Pakde Suhar memetik rambutan sambil bercanda. Binto, Mas Alin, dan Mas Andik ikut membantu. Di bawah pohon, di antara tawa dan manisnya rambutan, Binto teringat masa kecilnya: memanjat pohon rambutan di belakang rumah, ditemani Bapak yang masih sehat. Sekarang Bapak — seorang pensiunan — terbaring lemah karena diabetes, dan Binto di sini — bekerja di bawah pohon rambutan yang mengingatkannya pada kenangan itu.

Suasana berubah serius begitu Mas Alin membuka kode dari klien Tulungagung. Binto terkejut melihat struktur tabel database-nya: `barang1`, `barang2`, `barang3`… sampai `barang10`. Sepuluh kolom untuk menyimpan barang dalam satu tabel. Begitu toko butuh menambah barang ke-11, program tidak bisa menanganinya. "Ini yang terjadi kalau database tidak dinormalisasi," kata Mas Alin.

Pelajaran dimulai. Mas Alin menjelaskan normalisasi dengan analogi pohon rambutan: cabang yang terlalu rimbun harus dipotong. First Normal Form (1NF) — setiap kolom hanya berisi satu nilai, tidak boleh ada pengulangan grup seperti `barang1` sampai `barang10`. Second Normal Form (2NF) — setiap kolom harus bergantung pada primary key secara penuh, bukan sebagian. Third Normal Form (3NF) — tidak boleh ada ketergantungan antar kolom non-key. Binto mempraktikkannya langsung: memecah tabel menjadi beberapa tabel yang lebih kecil dan terhubung dengan foreign key.

Tapi Mas Alin segera mengingatkan: normalisasi bukan tujuan akhir. "Ada saatnya kamu justru sengaja melanggar normalisasi — namanya denormalisasi — kalau performa lebih penting daripada konsistensi."

Mas Andik kemudian angkat bicara. Ia bercerita tentang transaksi yang gagal setengah: uang nasabah terdebet, tapi saldo penerima tidak bertambah. "Kalau transfer gagal di tengah jalan, harus balik semua. Gak boleh setengah-setengah." Dari cerita ini, Mas Alin memperkenalkan konsep transaksi database dan ACID: Atomicity (semua atau tidak sama sekali), Consistency (data harus tetap valid setelah transaksi), Isolation (transaksi berjalan seolah-olah sendiri), Durability (sekali commit, datanya permanen — meskipun server mati).

Pelajaran dilanjutkan dengan perbandingan SQL vs NoSQL. Mas Alin menggunakan analogi yang brilian: SQL adalah lemari arsip. Setiap dokumen punya tempat pasti, dengan label, kategori, dan relasi yang ketat. NoSQL (seperti MongoDB) adalah gudang — barang bisa dilempar ke mana saja, cepat menyimpan, cepat mencari, tapi tidak cocok untuk data yang punya relasi rumit.

Sore harinya, Binto merenung di bawah pohon rambutan. Database yang baik adalah tulang punggung sistem. Seburuk apa pun UI-nya, kalau data tetap konsisten, sistem masih bisa diperbaiki. Tapi kalau database kacau — seluruh sistem runtuh. Seperti rumah tanpa pondasi.

### Bab 8 — Kontrak Komunikasi

Berita dari Kalimantan kembali datang. Pak Haji Hamid — pemilik minimarket yang dulu minta tombol laporan — kini ingin ekspansi. Bisnisnya berkembang ke rantai pasok grosir. Ia butuh aplikasi mobile untuk tim sales lapangan: mereka bisa input pesanan dari lapangan, cek stok, kirim laporan. Tidak perlu yang rumit — yang penting berfungsi.

Mas Alin mengadakan rapat di bawah pohon rambutan — sudah menjadi tradisi di GTN, rapat penting selalu di bawah pohon, bukan di ruang tertutup. Kali ini topiknya serius: arsitektur. Selama ini GTN membangun aplikasi monolitik — semua dalam satu codebase. Tapi untuk aplikasi mobile, butuh pendekatan berbeda. Backend harus bisa melayani banyak jenis frontend — web, Android, iOS.

Mas Alin memperkenalkan REST API dengan analogi yang jenius: Restoran Padang. Frontend (web/mobile) adalah pembeli yang duduk di meja. Backend adalah dapur — tempat semua logika dan data berada. API adalah pelayan. Pembeli tidak perlu tahu bagaimana dapur bekerja. Ia cukup pesan pada pelayan. Pelayan mencatat pesanan dalam bahasa yang dipahami dapur (JSON), pergi ke dapur, kembali membawa makanan (response). Kalau ada yang salah, pelayan kembali dengan penjelasan (status code).

Binto belajar komponen-komponen REST API melalui analogi ini: endpoint adalah nomor meja, HTTP method adalah jenis permintaan (GET = minta lihat menu, POST = pesan makanan baru, PUT = ganti pesanan, DELETE = batalkan pesanan), header adalah catatan tambahan pada pesanan, body adalah detail pesanan. Status code dijelaskan sebagai respons khas pelayan Padang: 200 OK (pesanan sukses), 201 Created (makanan baru berhasil dibuat), 400 Bad Request (pesanan tidak jelas), 401 Unauthorized (belum bayar tidak bisa pesan), 403 Forbidden (sudah bayar tapi tidak boleh pesan menu VIP), 404 Not Found (menu tidak ada), 422 Unprocessable Entity (pesanan lengkap tapi sambel ijo sedang habis), 500 Internal Server Error (kompor dapur meledak).

Mas Alin menekankan bahwa REST API harus stateless — setiap request harus membawa semua informasi yang diperlukan, tidak boleh bergantung pada request sebelumnya. "Setiap kali pelayan datang ke dapur, dia harus bawa pesanan lengkap. Gak bisa bilang 'itu lho, yang tadi.'" Token autentikasi dijelaskan sebagai kunci kamar hotel: sekali check-in, kamu dapat kunci yang berlaku selama menginap. Itu Bearer token — siapa pun yang pegang kunci, bisa masuk.

Binto juga belajar perbedaan autentikasi (siapa kamu? — login dengan username/password) dan otorisasi (apa yang boleh kamu lakukan? — role-based access). API key untuk mesin, Bearer token untuk manusia. Dokumentasi API contract — seperti menu restoran yang disepakati bersama antara koki dan pelayan — dibuat dengan Postman, sehingga Mas Andik bisa langsung mengerti endpoint apa saja yang tersedia dan bagaimana menggunakannya.

Bab ini diakhiri dengan Binto mulai ngoding API-nya sendiri — dan refleksi bahwa API adalah "wajah perusahaan." Seburuk apa pun internal sistem, API yang baik membuat integrasi menjadi mulus.

### Bab 9 — Satpam Kualitas

Mbak Rara kembali dari cuti. Tiga hari ia tidak masuk, dan Binto sudah menyelesaikan API untuk aplikasi Kalimantan. Dengan percaya diri, ia melapor ke Mbak Rara: "Udah beres, Mbak."

Mbak Rara tersenyum. "Beres menurut siapa?" Ia membuka laptop, menjalankan API Binto, dan dalam hitungan menit, menemukan lubang-lubang menganga. Pertama, SQL Injection — Mbak Rara memasukkan `' OR '1'='1` di field username, dan sistem menerimanya begitu saja. Kedua, input stok negatif — `-999` diterima tanpa validasi. Ketiga, otorisasi bocor — dengan mengubah ID di URL, user biasa bisa melihat data user lain. Keempat, token kadaluarsa masih bisa dipakai — tidak ada penanganan expiry. Binto pucat.

Mbak Rara tidak memarahi. Ia malah "kuliah" — menjelaskan kenapa QA itu penting dengan pendekatan yang membuat Binto berpikir ulang. QA bukan polisi yang mencari-cari kesalahan. QA adalah satpam kualitas — penjaga gerbang terakhir sebelum produk sampai ke pengguna. Mbak Rara memperkenalkan ISO 29119 — standar internasional untuk software testing — sebagai bukti bahwa QA adalah disiplin serius, bukan sekadar "asal klik-klik."

Ia juga menjelaskan tiga pendekatan testing. Risk-based testing: tidak semua fitur harus diuji sama rata, fokus pada area yang paling berisiko. Shift-left testing: testing jangan menunggu di akhir — libatkan QA sejak awal, bahkan sejak tahap desain. Automated vs manual testing: otomatisasi untuk test yang berulang-ulang (seperti login, logout), manual untuk test yang butuh penilaian manusia (seperti "apakah UI ini nyaman dilihat?").

Mbak Rara menunjukkan test plan-nya — di buku catatan kecilnya, tertulis rapi skenario-skenario pengujian, data input, hasil yang diharapkan, dan status. Binto tercengang melihat betapa detailnya. Ia baru sadar bahwa "beres" yang ia maksud ternyata masih jauh dari standar profesional.

Dengan bimbingan Mbak Rara, Binto memperbaiki semua celah keamanan: parameterized query untuk mencegah SQL injection, validasi input ketat untuk mencegah stok negatif, pengecekan kepemilikan data untuk mencegah otorisasi bocor. Ia juga menulis unit test pertamanya dengan PHPUnit — test otomatis yang akan menangkap regresi di masa depan. Bab ini ditutup dengan refleksi Binto: QA adalah partner, bukan musuh. Mbak Rara tidak mencari-cari kesalahannya; ia mentransfer pengetahuannya agar Binto menjadi engineer yang lebih baik.

### Bab 10 — Menenangkan Sistem yang Menangis

Sore yang tenang di GTN tiba-tiba berubah mencekam. Mas Andik — yang biasanya kalem — datang dengan laptop terbuka dan wajah tegang. "Ada yang aneh di production." Ia memutar layar. Di sana, di halaman aplikasi klien, terpampang pesan error mentah: `SQLSTATE[23000]: Integrity constraint violation: 1062 Duplicate entry`. Lengkap dengan stack trace, nama file, nomor baris, dan potongan kode.

Binto ngeri. Error semacam ini tidak boleh muncul di production. Mas Alin langsung mengambil alih. "Ini error yang menangis," katanya. "Dan semua orang bisa lihat. Termasuk klien. Termasuk kompetitor." Mereka bergegas memperbaiki, tapi Mas Alin menggunakan momen ini untuk mengajarkan sesuatu yang lebih dalam.

Kenapa error harus "ramah"? Bayangkan kamu tarik uang di ATM, lalu mesinnya nampilin kode error teknis dan restart. Apakah kamu akan percaya pada bank itu? Error di aplikasi sama persis. Pengguna tidak butuh tahu `SQLSTATE[23000]`. Mereka hanya perlu tahu: "Maaf, transaksi gagal. Silakan coba lagi. Kalau berlanjut, hubungi kami di nomor ini."

Mas Alin membedakan dua konsep kunci: **exception** dan **failure**. Exception adalah kesalahan yang bisa ditebak dan ditangani — seperti validasi input gagal, format tanggal salah, atau email sudah terdaftar. Exception harus ditangkap dengan `try-catch`, diberi pesan yang jelas, dan sistem tetap berjalan normal. Failure adalah kegagalan total — database mati, server down, third-party service timeout. Untuk failure, strateginya adalah "graceful degradation": sistem tetap berfungsi meskipun beberapa komponen mati. Seperti pesawat yang kehilangan satu mesin — tetap bisa terbang dan mendarat dengan selamat.

Mas Alin memperkenalkan logging sebagai "buku harian sistem." Setiap error dicatat: kapan terjadinya, di mana, apa penyebabnya, data apa yang sedang diproses. Tapi log ini untuk developer, bukan untuk pengguna. Log disimpan di file — bukan ditampilkan di browser. Binto kemudian mempraktikkan exception handler global: satu tempat yang menangkap semua exception di seluruh aplikasi, mencatatnya ke log, dan mengembalikan respons yang ramah ke pengguna.

Bab ini diakhiri dengan momen emosional. Wawan — yang selama ini menjalani kuliah online S1 selepas jam kantor — akhirnya wisuda. Orang tuanya datang ke kantor membawa nasi kotak untuk seluruh tim. Di bawah pohon rambutan, mereka makan bersama, mata Wawan berkaca-kaca. Binto melihat orang tua Wawan — sederhana, tidak mengerti apa itu kode — tapi bangga luar biasa pada anaknya. Binto teringat Bapaknya sendiri, yang kini terbaring di rumah, belum sempat melihat anaknya menjadi engineer sungguhan.

### Bab 11 — Panggung Gladi Resik

Cahyo datang. Anak SMK berusia 17 tahun dengan seragam putih-abu-abu yang masih dipakainya — karena langsung dari sekolah. Ia PKL di GTN selama sebulan. Matanya berbinar-binar, penuh semangat. Hari pertama, ia langsung diberi tugas kecil: memperbaiki bug tombol di salah satu aplikasi klien.

Cahyo berhasil memperbaiki dalam waktu satu jam. Dengan bangga, ia mengumumkan: "Udah beres, Mas. Tinggal ganti file di cPanel, kan?"

Satu kalimat itu membuat seisi ruangan berhenti. Mas Alin menoleh. Mbak Rara menghela napas. Mas Andik tersenyum getir. Binto — yang dulu juga pernah berada di posisi Cahyo — kini mengerti apa yang salah. Tapi ia membiarkan Mas Alin yang menjelaskan.

"Gak boleh langsung production, Cahyo." Mas Alin berkata pelan tapi tegas. Ia mengajak Cahyo ke Mbak Rara untuk belajar tentang staging environment. Mbak Rara — dengan kesabarannya yang legendaris — memberikan analogi yang sempurna: gladi resik.

"Kamu pernah lihat pertunjukan drama di sekolah? Sebelum tampil di depan penonton, pemain latihan dulu di panggung yang sama — pakai kostum lengkap, lighting, musik. Itu gladi resik. Kalau ada yang salah, masih bisa diperbaiki. Bayangkan kalau langsung tampil di depan penonton, tanpa gladi resik, terus lupa dialog? Malu. Production itu panggungnya. Penonton itu pengguna. Staging itu gladi resik."

Cahyo mengangguk, mulai paham. Mas Alin memperkuat dengan aturan branching: fitur baru harus dibuat dari branch production, lalu di-merge ke staging untuk diuji. Kalau lulus uji, baru di-merge ke production. Jangan pernah merge staging ke production! "Kamu gak mau kode setengah matang masuk ke production."

Mbak Rara mendemonstrasikan ritual testing-nya di staging: ia membuka aplikasi, menguji perbaikan Cahyo, tapi tidak hanya di laptop. Ia mengeluarkan tiga ponsel berbeda — Samsung, Xiaomi, iPhone. Di Android yang layar kecil, tombol yang diperbaiki Cahyo malah kepotong. Bug lain. Cahyo terkejut — ia hanya menguji di laptop. Mbak Rara menjelaskan bahwa testing harus mencakup berbagai device, terutama di Indonesia di mana banyak orang masih pakai ponsel lawas.

Cahyo kembali ke meja, memperbaiki bug device-nya, dan mengulang siklus: deploy ke staging → Mbak Rara testing → lolos → merge ke production. Hari itu, di bawah pohon rambutan sambil es dawet serabi, Cahyo belajar pelajaran paling penting: jangan pernah sentuh production langsung.

### Bab 12 — Meluncurkan Roket ke Bulan

Hari Sabtu. Bukan di kantor, tapi di Gelato Stasiun — kafe kecil dekat stasiun Blitar yang jadi tempat nongkrong favorit tim GTN. Pakde Suhar memesan gelato untuk semua. Ia juga — seperti biasa — tidak pernah berhenti "berburu." Kali ini ia ngobrol dengan pemilik kafe, dan sebelum gelato habis, sudah dapat prospek klien baru.

Cahyo — yang semakin kritis — bertanya pada Mas Alin: "Mas, kemarin aku git push, terus langsung muncul di production. Kok bisa?"

Pertanyaan itu membuka pintu ke pelajaran tentang CI/CD. Mas Alin memulai dari sejarah — bagaimana deployment berevolusi dari masa ke masa. Era disket: programmer membawa kode dalam disket fisik, mengantarkannya ke server. Era FTP/cPanel: upload file satu per satu via FTP client seperti FileZilla. Era Git Pull manual: SSH ke server, `git pull`, restart service. Semua manual. Semua rawan kesalahan manusia — lupa upload satu file, salah konfigurasi, dan production down berjam-jam.

Sekarang: CI/CD. Begitu Binto `git push` ke branch production, GitHub Actions langsung memicu pipeline otomatis. Tahapannya: (1) test — semua unit test dijalankan, kalau ada yang gagal, pipeline berhenti, (2) code checker — tools seperti PHPStan memeriksa kualitas kode, (3) security scan — memeriksa dependensi yang rentan, (4) build — mengkompilasi asset frontend, (5) deploy — mendorong kode yang sudah terverifikasi ke server production, (6) notify — kirim notifikasi ke Discord atau Slack bahwa deployment berhasil.

"Jadi CI itu Continuous Integration — setiap perubahan langsung dicek. CD itu Continuous Delivery atau Continuous Deployment — setiap perubahan yang lolos langsung terkirim," jelas Mas Alin. Binto membayangkan pipeline sebagai ban berjalan di pabrik: kode masuk, melewati serangkaian pemeriksaan, dan keluar sebagai aplikasi yang siap pakai. Tidak ada lagi "lupa upload file."

Tapi Mas Alin segera menekankan: CI/CD adalah *best practice*, bukan keharusan. Untuk proyek kecil dengan satu developer, git pull manual masih cukup. Untuk tim seperti GTN? CI/CD menghemat waktu dan mengurangi kesalahan. Ia juga menjelaskan peran DevOps — orang seperti Mas Andik yang mengelola pipeline, server, dan infrastruktur. Di tim besar, DevOps adalah peran terpisah. Di GTN, semua orang sedikit-sedikit DevOps.

Bab ini ditutup dengan refleksi: "Dari disket ke robot." Teknologi deployment telah berevolusi drastis, tapi esensinya tetap sama — memastikan kode sampai ke pengguna dengan aman.

### Bab 13 — Buku Harian Sistem

Pagi yang normal berubah panik ketika Mas Andik melapor: "Ada error di production. Gagal menyimpan data." Tapi kali ini, error-nya aneh — pesannya cuma "Gagal menyimpan data." Tidak ada stack trace, tidak ada detail. Hanya pesan samar yang tidak membantu siapa pun.

Mas Alin tidak panik. Ia membuka terminal, SSH ke server, dan mulai mencari. "Log ada di mana-mana," gumamnya. Ia membuka file `laravel.log`, menggulir ke timestamp terbaru, dan menemukan baris ini: `Disk quota exceeded`. Server kehabisan ruang disk. Log-lah yang memberitahu mereka apa yang sebenarnya terjadi — bukan pesan "Gagal menyimpan data" yang tidak berguna.

Dari insiden ini, Mas Alin mengembangkan pelajaran Bab 10 tentang logging. Logging bukan sekadar mencatat error — logging adalah buku harian sistem yang mencatat *semua hal penting*. Ia menjelaskan level severity: **Info** (kejadian normal — "user login," "laporan berhasil dibuat"), **Warning** (hal yang mencurigakan tapi belum error — "percobaan login gagal 3x"), **Error** (kesalahan yang perlu perhatian — "gagal menyimpan data karena disk penuh"), **Critical** (sistem down — "database connection timeout").

Mas Alin juga memperkenalkan tools logging profesional. Sentry: menangkap exception secara real-time dan memberikan notifikasi ke developer. ELK Stack (Elasticsearch, Logstash, Kibana): untuk tim besar yang perlu mencari dan memvisualisasikan log dari banyak server. Seq dan SigNoz: alternatif yang lebih ringan. Untuk GTN, file-based logging masih cukup — tapi Binto belajar bahwa seiring pertumbuhan, log harus dikelola dengan lebih serius.

Sebuah prinsip penting ditanamkan: "Log itu untuk debugging. Database untuk data bisnis. Jangan campur." Jangan mencatat log transaksi di tabel log — transaksi di database. Jangan menyimpan data bisnis di file log — itu bukan tempatnya. Log rotation juga diperkenalkan: file log harus dirotasi secara berkala (harian, mingguan) dan yang lama dikompres atau dihapus. Jangan sampai log memakan seluruh disk dan mengulangi insiden "Disk quota exceeded."

Bab ini ditutup dengan refleksi bahwa log ada di mana-mana — access log server, error log aplikasi, query log database. Engineer yang baik bukan hanya jago ngoding; ia juga jago membaca jejak.

### Bab 14 — Benteng yang Tak Terlihat

Hari terakhir Cahyo PKL di GTN. Sebulan berlalu cepat. Ia datang dengan membawa nasi kenduri — dimasak ibunya sendiri sebagai ucapan terima kasih. Seisi kantor berkumpul. Tapi sebelum pulang, Cahyo minta satu hal: "Satu pelajaran terakhir, Mas."

Mas Alin mengangguk. Ia memilih topik yang belum pernah dibahas secara formal: keamanan. "Keamanan itu kayak benteng yang tak terlihat," ia membuka. "Waktu berfungsi, gak ada yang sadar. Tapi begitu jebol, semua panik."

Ia memperkenalkan CIA Triad — tiga pilar keamanan informasi: **Confidentiality** (kerahasiaan — hanya yang berhak yang bisa melihat data), **Integrity** (keutuhan — data tidak boleh diubah oleh yang tidak berhak), **Availability** (ketersediaan — data harus bisa diakses saat dibutuhkan). Binto mulai menghubungkan dengan pelajaran-pelajaran sebelumnya: password hashing melindungi confidentiality, validasi input melindungi integrity, graceful degradation melindungi availability.

Kemudian serangan nyata. Mbak Rara bercerita tentang temannya yang jadi korban SQL Injection. Seorang hacker memasukkan kode SQL melalui field login dan berhasil mengakses seluruh database — nama, email, password, bahkan data finansial. Kerugiannya? Jutaan, dan kepercayaan pengguna yang tidak bisa dibeli kembali. Mas Alin menambahkan contoh XSS (Cross-Site Scripting): penyerang menyuntikkan JavaScript berbahaya ke halaman web yang dilihat pengguna lain.

Password menjadi bahasan serius. "Password itu bukan dienkripsi, tapi di-hash," tegas Mas Alin. Enkripsi bisa dibalik — hashing tidak. Bcrypt dan Argon2 adalah algoritma hashing modern yang lambat secara sengaja — untuk mempersulit brute-force. "Jangan bikin sistem sendiri. Pakai yang sudah terbukti aman."

Tapi keamanan bukan cuma urusan kode. Mas Andik menjelaskan keamanan infrastruktur: firewall yang memblokir akses tidak sah, VPN untuk koneksi jarak jauh yang aman, fail2ban yang otomatis memblokir IP yang mencurigakan. Mbak Rara — yang diam-diam juga belajar ISO 27001 — menjelaskan bahwa perusahaan besar wajib punya sertifikasi ini, dan QA berperan penting dalam memastikan standar keamanan terpenuhi.

Shift-left security menjadi mantra terakhir: keamanan tidak boleh dipikirkan belakangan. Dari awal desain, dari awal ngoding, dari awal testing — keamanan harus selalu ada di pikiran. Seperti benteng yang dibangun bata demi bata, bukan dipasang setelah musuh di depan gerbang.

Cahyo pamit. Ia meninggalkan stiker burung hantu — simbol kebijaksanaan — yang ia tempel di laptopnya sendiri. "Buat Mas Binto. Biar inget aku." Binto tersenyum getir. Dulu ia datang ke GTN dengan kepala tegak, tidak tahu apa-apa. Sekarang ia melihat dirinya di Cahyo — dan menyadari seberapa jauh ia sudah berjalan.

### Bab 15 — Seni Menahan Laju

Aplikasi Kalimantan mulai menunjukkan gejala. Dengan 20 tim sales yang simultan mengakses API, produk yang kini mencapai puluhan ribu, dan transaksi yang terus bertambah — response time melambat. Dari yang tadinya 200ms, kini hampir 4 detik. Pak Haji Hamid mulai mengeluh; ia bahkan mengancam kembali ke cara lama: pesan lewat WhatsApp.

Binto panik. Ia menghadap Mas Alin. "Harus gimana, Mas? Upgrade server?"

Mas Alin tersenyum. "Itu satu jawaban. Tapi ada banyak jawaban lain." Ia mulai dengan queue — analogi antrian di supermarket. Daripada semua transaksi diproses bersamaan dan membuat semua orang menunggu, masukkan transaksi ke antrian. Kasir (worker) proses satu per satu. Pengguna tidak perlu menunggu — mereka dapat notifikasi setelah transaksi selesai.

Kemudian cache — "warung dekat rumah." Daripada setiap kali butuh data produk harus "pergi ke supermarket" (baca dari database), simpan data yang sering diakses di cache — penyimpanan cepat di memori. Tapi cache harus dikelola hati-hati: kalau data di database berubah, cache harus dihapus atau diperbarui.

Vertical vs horizontal scaling dijelaskan dengan analogi kuda. Vertical scaling: "kudanya diperbesar" — upgrade server, tambah RAM, tambah CPU. Mahal, ada batasnya. Horizontal scaling: "kudanya ditambah" — tambah server, bagi beban ke banyak server. Lebih murah per unit, lebih elastis, tapi lebih kompleks.

Database scaling mendapat perhatian khusus. Tahap pertama: vertical scaling database. Tahap kedua: read replication — satu server untuk write (primary), beberapa server untuk read (replica). Tahap ketiga: sharding — memecah data ke banyak database berdasarkan kriteria tertentu (misalnya, pengguna A-F di database 1, G-M di database 2). Tapi Mas Alin memperingatkan: "Jangan sharding kecuali kamu benar-benar butuh. Kompleksitasnya gila-gilaan."

Monolith vs microservices kembali dibahas, kali ini dari perspektif scaling. Tapi Mas Alin konsisten dengan pesan dari Bab 5: "Jangan terburu-buru pindah ke microservices." Mulai dari monolith yang rapi. Kalau suatu saat butuh scale komponen tertentu, ekstrak jadi service terpisah. Arsitektur yang baik tumbuh secara organik, bukan dipaksakan dari awal.

Rate limiting juga diperkenalkan: membatasi jumlah request dari satu IP dalam periode tertentu. Bukan untuk mengganggu pengguna, tapi untuk melindungi sistem dari abuse — termasuk serangan DDoS sederhana dari bot. Mbak Rara senang — ini lapisan keamanan tambahan.

Bab ini ditutup dengan Binto melakukan performance testing menggunakan k6 — tools open-source untuk simulasi beban. Ia mengetes API dengan ribuan request virtual dan melihat titik mana yang pertama kali ambruk. Pelajaran dari Bab 5 kembali bergema: tidak ada silver bullet. Queue, cache, scaling — masing-masing adalah alat dengan tradeoff sendiri. "Seni menahan laju" adalah memilih alat yang tepat pada waktu yang tepat.

### Bab 16 — Pulang

Setahun kemudian. Pohon rambutan di halaman GTN kembali berbuah lebat, tapi banyak hal yang berubah. Wawan — yang selama ini kuliah online S1 sambil bekerja — diterima CPNS di Pemerintah Kabupaten Kediri. Di hari terakhirnya, ia membawa nasi kotak lagi, kali ini untuk perpisahannya sendiri. Tidak ada yang sedih — semua bangga. Wawan adalah bukti bahwa ijazah memang penting, tapi yang lebih penting adalah kemauan belajar.

Binto merenungkan perjalanannya. Setahun yang lalu ia datang dengan kepala tegak dan kosong. Kini kepalanya penuh — Git, Scrum, REST API, Clean Code, database, keamanan, CI/CD, scaling, logging — tapi kepalanya tidak lagi tegak. Kepalanya tertunduk, rendah hati, sadar bahwa selalu ada yang belum ia tahu. Tumbler ½ M (Setengah Mateng) di meja kerjanya adalah simbol: selalu setengah matang, selalu ada ruang untuk belajar.

Seorang junior baru datang. Aini, fresh graduate, mata berbinar seperti Binto setahun yang lalu. Binto ingat bagaimana Mas Alin dulu menyambutnya — bukan dengan pujian, tapi dengan pertanyaan yang meruntuhkan. Kini ia harus melakukan hal yang sama. "Kamu bisa Git?" tanyanya pada Aini. "Belum," jawab Aini. Dan Binto tersenyum — siklus pembelajaran dimulai lagi, kali ini dengan dirinya sebagai mentor.

Kabar tentang Cahyo: ia sekarang kuliah jurusan Informatika di Malang. Sebulan sekali ia masih mampir ke GTN, membawa cerita dari kampus. Binto melihat Cahyo dan melihat dirinya sendiri — dulu polos, sekarang mulai paham. Bapak Binto juga membaik; ia bahkan bisa pergi umroh bersama Ibu, sesuatu yang setahun lalu terasa mustahil.

Di akhir bab, Mas Alin membagikan refleksi yang dalam. Menjadi software engineer bukan tentang menulis kode tercepat atau menguasai framework terkini. Ini tentang cara berpikir. Tentang memahami masalah sebelum menulis solusi. Tentang mempertimbangkan dampak setiap baris kode — pada pengguna, pada tim, pada bisnis, pada masyarakat. "Kode bisa diubah, tapi dampaknya bisa permanen."

Novel ditutup dengan nada puitis. Binto berdiri di bawah pohon rambutan, memandang jalanan Blitar yang mulai temaram. Setahun yang lalu ia pulang karena terpaksa — ayah sakit, tidak ada pilihan. Kini ia sadar bahwa "pulang" bukan berarti mundur. Pulang adalah awal dari perjalanan yang sebenarnya. Dan di atas meja kerjanya, tumbler ½ M masih ada — selalu setengah, selalu siap diisi lagi.

---

## Tema Sentral

1. **Gap Pendidikan vs Industri** — Kampus mengajarkan teori dan kerja individu, industri menuntut kolaborasi, tooling, dan soft skills.
2. **Rendah Hati dan Pembelajaran Berkelanjutan** — "Setengah Mateng" sebagai filosofi: tidak pernah merasa cukup tahu, selalu ada ruang untuk tumbuh.
3. **Mentorship dan Siklus Pengetahuan** — Binto yang tadinya dibimbing Mas Alin, pada akhirnya menjadi mentor bagi Aini. Pengetahuan adalah warisan yang harus diteruskan.
4. **Pragmatisme Teknologi** — Tidak ada "bahasa pemrograman terbaik," yang ada hanyalah alat yang tepat untuk konteks yang tepat (No Silver Bullet).
5. **Kode untuk Manusia** — Di balik setiap fitur ada pengguna sungguhan: pemilik minimarket di Kalimantan, pemilik toko di Tulungagung, tim sales di lapangan.
6. **Budaya Kerja Perusahaan Kecil** — GTN bukan startup unicorn; ia software house di gang desa. Tapi di sanalah pembelajaran paling autentik terjadi — semua orang melakukan segalanya, tidak ada sekat antara "developer" dan "manusia."
