# **Bab 9: Satpam Kualitas**

## **9.1 Mbak Rara Kembali dan Godaan Pakde**

Pagi itu, kantor Garda Teknologi Nusantara terasa lebih hidup. Binto baru saja menyalakan laptopnya ketika suara motor matik terdengar berhenti di halaman. Tidak lama kemudian, seorang perempuan berkerudung cokelat muda melangkah masuk dengan tote bag besar di bahunya.

"Mbak Rara\!" Wawan berseru dari balik iMac-nya. "Cuti panjang banget, Mbak. Kita sampe kangen."

Mbak Rara meletakkan tasnya di meja, lalu mengeluarkan bungkusan kresek. "Ini oleh-oleh dari Tulungagung. Tahu krispi sama keripik gadung. Pada mau?"

Belum sempat yang lain menjawab, Pakde Suhar muncul dari ruang depan. Wajahnya langsung sumringah melihat Mbak Rara.

"Wah, Rara. Akhirnya balik. Tadi pas kamu gak ada, aku ketemu tetangga. Anaknya masih sendiri lho. Kerja di bank, mapan. Kapan nih aku kenalin?"

Mbak Rara hanya nyengir sambil membuka kresek oleh-oleh. "*Nggih*, Pakde. Doakan saja. Yang penting sekarang saya fokus kerja dulu. Nanti kalau sudah waktunya, pasti ketemu sendiri."

Pakde tertawa. "Iya, iya. Tapi jangan kelamaan. Umur terus jalan, Ra."

Binto tersenyum melihat interaksi itu. Ia baru tahu kalau Mbak Rara juga seperti dirinya—balik kampung setelah merantau. Bedanya, Mbak Rara bukan lulusan IT. Ia lulusan Manajemen dari sebuah universitas di Surabaya, sempat bekerja di sana selama dua tahun sebelum memutuskan pulang ke Blitar. Di kantor ini, ia bukan cuma QA. Ia juga bantu Bu Sari urus administrasi, kadang ikut menyusun proposal proyek, dan jadi tempat curhat semua orang.

"Mas Binto," suara Mbak Rara menyadarkannya. "Aku denger kalian lagi bikin API buat Kalimantan. Gimana progresnya?"

Binto menegakkan duduknya. "Sudah jadi, Mbak. Endpoint login, produk, pesanan. Semua jalan."

"Oh ya? Coba tunjukkan."

## **9.2 "Udah Beres, Mbak"**

Dengan semangat, Binto membuka Postman dan mendemokan API-nya. Ia tunjukkan endpoint login: kirim email dan password, dapat token. Ia tunjukkan endpoint produk: kirim token di header, dapat daftar produk lengkap dengan harga dan stok. Ia tunjukkan endpoint pesanan: kirim data produk dan jumlah, dapat respons sukses.

"Lihat, Mbak. Lancar semua."

Mbak Rara memperhatikan dengan tenang. Tangannya sibuk mencatat di buku kecil bersampul cokelat yang selalu ia bawa ke mana-mana. Setelah Binto selesai, ia tersenyum tipis.

"Oke, Mas. Aku coba tes ya. Tapi aku pinjam laptopmu dulu. Biar aku yang operasikan."

Binto mengangguk, sedikit penasaran. *Mau diapakan lagi? Kan udah jelas semua berfungsi.*

## **9.3 Uji Coba: Input Aneh, Token Kadaluarsa, Stok Minus**

Mbak Rara mengambil alih laptop Binto. Ia membuka Postman dan mulai "bermain".

Pertama, ia membuka endpoint Login. Ia mengisi email dengan " ' OR '1'='1 dan password kosong. Klik Send.

Error 500\. Internal Server Error.

Binto mengernyit. "Lho?"

Mbak Rara tidak berkomentar. Ia mencoba lagi. Kali ini, ia isi email dengan sales1@tokobangun.com dan password yang salah. Responsnya: "Email atau password salah". Itu sudah benar.

Lalu ia pindah ke endpoint Produk. Ia mengambil token yang valid, lalu mengirim request. Daftar produk muncul. Normal.

Kemudian ia masuk ke endpoint Buat Pesanan. Ia mengirim data produk yang ada, dengan jumlah \-5. Klik Send.

Error 500\. Internal Server Error.

"Jumlah minus harusnya ditolak, Mas. Kasih tahu pengguna bahwa jumlah tidak valid. Jangan error 500," komentarnya pelan.

Binto mulai gelisah.

Mbak Rara melanjutkan. Ia membuat pesanan dengan produk yang stoknya 0\. API Binto memprosesnya. Stok produk itu menjadi minus 1\.

"Nah, ini bahaya. Stok minus bisa bikin laporan kacau. Harusnya ada validasi: kalau stok tidak cukup, tolak pesanan."

Belum selesai. Mbak Rara mencoba masuk ke endpoint daftar pesanan menggunakan token milik *sales* B. Ia sengaja mengganti parameter ID pesanan menjadi ID pesanan milik *sales* A.

Data pesanan *sales* A muncul utuh di layarnya.

Mbak Rara menoleh ke Binto. "Mas, ini datanya kok muncul yang bukan punya user ini ya?"

Mas Alin yang sedang berdiri di dekat dispenser langsung mendekat. Wajahnya berubah serius.

"Ini bukan cuma *bug*," katanya pelan. "Kalau salah *user* bisa lihat data orang lain... itu sudah masuk masalah keamanan. Celah otorisasi yang fatal."

Suasana ruangan mendadak lebih hening. Kipas angin Ufo yang berputar pelan kini terdengar jelas.

Untuk pertama kalinya, Binto merasa ini bukan sekadar error kecil yang bisa ditertawakan.

"Debugging itu bukan cuma bikin error hilang," lanjut Mas Alin dengan nada yang tidak menggurui, tapi tegas. "Tapi memastikan sistem kita tidak melakukan hal yang seharusnya tidak boleh terjadi."

Setelah ditelusuri bersama, ternyata *query* untuk melihat detail pesanan tidak memfilter berdasarkan kepemilikan *user* yang sedang aktif. Binto rupanya lupa menaruh filter pengecekan di fungsi *detail*-nya.

Binto menarik napas panjang. Hal kecil... tapi dampaknya bisa besar sekali.

"Lanjut ya. Satu lagi," kata Mbak Rara. Ia mengirim request ke endpoint Produk dengan token yang sudah kadaluarsa—ia sengaja menunggu beberapa menit setelah login. API Binto tidak memberi respons yang jelas. Bukannya 401 Unauthorized, malah error aneh.

Mbak Rara menutup laptop dan menatap Binto dengan tenang. "Ini belum apa-apa, Mas. Aku cuma coba beberapa skenario dasar. Bayangin kalau ini sudah dipakai sales di lapangan. Mereka bisa input angka minus. Stok jadi kacau. Orang iseng bisa ngintip data sales lain. Reputasi kita hancur."

## **9.4 Kuliah Mbak Rara: Kenapa QA Itu Penting**

Alih-alih marah, Mbak Rara malah duduk di sebelah Binto. Ia membuka buku catatannya.

"Aku ini lulusan Manajemen, Mas. Gak ngerti coding dalem-dalem. Tapi aku ngerti gimana pengguna berpikir. Mereka bisa pencet apa aja. Bisa isi form dengan emoji, angka minus, huruf di field yang harusnya angka. Mereka gak peduli sama logika di balik layar. Yang mereka tahu: aplikasi harus jalan."

Ia menunjuk catatannya. "Tugasku cuma satu: jadi satpam kualitas. Aku jagain gerbang biar gak ada yang aneh lolos ke production."

Binto mendengarkan dengan seksama.

"Waktu aku kerja di Surabaya dulu," Mbak Rara melanjutkan, "tim kami gak punya QA. Developer langsung rilis fitur ke production. Suatu hari, ada bug kecil—input tanggal lahir bisa tahun 3000\. Klien marah besar. Mereka bilang: 'Kalian gak punya QA?' Sejak itu, aku sadar. QA itu bukan beban. QA itu tameng."

Mas Alin yang sedari tadi mendengarkan dari pojokannya ikut bersuara. "Betul, Ra. Di tim kecil kayak kita, QA itu investasi. Kita gak mau klien kita yang jadi QA."

Mbak Rara mengangguk. "Ada prinsip yang selalu aku pegang: Lebih baik error di sini, di tangan QA, daripada error di tangan pengguna. Di sini, error bisa diperbaiki diam-diam. Di sana, error jadi tontonan."

## **9.5 ISO 29119 dan Standar Profesional**

Mas Alin bangkit dan berjalan mendekat. "Omong-omong soal testing profesional, sebenarnya ada standar internasional. Namanya ISO 29119\. Versi terbarunya 2022."

Binto menoleh. "ISO? Kayak standar mutu pabrik?"

"*Nggih*. ISO 29119 itu standar untuk *software testing*. Isinya panduan proses testing yang sistematis: dari perencanaan, desain test, eksekusi, sampai pelaporan. Kita gak harus saklek ikuti semua—namanya juga standar, bisa disesuaikan. Tapi bagus buat jadi referensi biar testing kita gak asal-asalan."

Mbak Rara menambahkan. "Aku pernah baca ringkasannya. Intinya: testing harus direncanakan, didokumentasikan, dan dilakukan secara independen. Independen artinya: jangan developer yang ngetes kodenya sendiri. Harus ada mata lain. Makanya ada aku."

Binto manggut-manggut. Ia baru tahu ada standar internasional untuk hal yang selama ini ia anggap remeh.

## **9.6 Kalau Gak Ada QA Gimana?**

"Terus, Mbak," Binto penasaran. "Kalau tim kecil kayak kita gak punya QA, gimana?"

Mas Alin menjawab. "Ya terpaksa peer review. Temen sesama developer ngecek kode dan testing sederhana. Tapi tetap ada *blind spot*. Karena sama-sama developer, cara berpikirnya mirip. Apa yang luput dari kamu, bisa jadi luput juga dari temenmu. Makanya adanya Mbak Rara itu aset."

Mbak Rara menimpali. "Peer review itu lebih baik daripada gak ada. Tapi idealnya tetap ada QA. Karena QA punya *mindset* yang beda. Aku gak mikirin *gimana caranya bikin fitur ini jalan*. Aku mikirin *gimana caranya fitur ini rusak*. Itu perbedaan mendasar."

## **9.7 Shift-Left: Kualitas Sejak Awal**

"Tapi," Mas Alin menambahkan, "bukan berarti developer lepas tangan soal kualitas. Ada konsep namanya Shift-Left."

"Shift-Left?"

"Iya. Ibaratnya, kualitas itu digeser ke kiri—ke tahap development. Jangan nunggu di akhir baru testing. Developer juga harus nulis unit test untuk kodenya sendiri. Jadi sebelum sampai ke Mbak Rara, kode sudah lolos pengecekan dasar."

Mbak Rara mengangguk setuju. "Aku senang kalau developer nulis unit test. Pekerjaanku jadi lebih ringan. Aku bisa fokus ke skenario yang lebih kompleks, bukan ngecek validasi dasar yang seharusnya sudah ditangani sejak awal."

## **9.8 Test Plan: Peta Perang Mbak Rara**

Mbak Rara membuka buku catatannya dan menunjukkan satu halaman penuh coretan ke Binto.

"Ini test plan sederhana buat API Kalimantan. Aku bikin sebelum kamu mulai *ngoding* kemarin. Harusnya aku kasih lihat dari awal, tapi aku keburu cuti."

Binto melihat halaman itu. Tercantum daftar skenario uji:

* Login: email valid \+ password benar (200), email valid \+ password salah (401), email tidak terdaftar (401), email kosong (422), password kosong (422).  
* Produk: dengan token valid (200), tanpa token (401), token palsu (401), token kadaluarsa (401).  
* Pesanan: produk tersedia \+ jumlah valid (201), jumlah 0 (422), jumlah minus (422), melebihi stok (422), produk tidak ditemukan (404).

"Harusnya tiap kali ada backlog naik ke sprint, aku bikin test plan kayak gini. Developer bisa lihat, jadi tahu nanti API-nya akan diuji dari sisi mana. Jadi bukan jebakan. Ini kolaborasi."

Binto mengangguk. Ia baru sadar, testing bukan sekadar mencari-cari kesalahan. Tapi proses yang terencana dan transparan.

## **9.9 Risk-Based Testing: Memilih Pertempuran**

"Omong-omong soal ISO 29119," Mbak Rara melanjutkan, "salah satu konsep penting di dalamnya adalah Risk-Based Testing."

"Risk-Based Testing?" Binto mengulang.

"Iya. Kita gak mungkin menguji semua kemungkinan. Waktu dan resource kita terbatas. Jadi kita harus pintar memilih: fitur mana yang paling berisiko? Fitur yang kalau rusak dampaknya paling besar? Nah, itu yang kita prioritaskan untuk diuji lebih dalam."

Ia menunjuk test plan-nya. "Contoh, fitur pesanan. Kalau ada bug di sini, stok bisa minus, laporan keuangan kacau, klien marah. Risikonya tinggi. Makanya aku buat banyak skenario untuk pesanan. Sementara fitur lihat produk, risikonya lebih rendah—paling hanya tidak muncul. Aku tetap uji, tapi tidak sedalam pesanan."

Mas Alin menimpali. "Itu kenapa di ISO 29119, risk-based testing jadi fondasi. Kita tidak mengejar 100% coverage—itu tidak realistis. Tapi kita pastikan bagian paling kritis dapat perhatian paling besar."

Binto mulai melihat gambaran besarnya. QA bukan hanya soal teknis, tapi juga soal manajemen risiko.

## **9.10 Otomatisasi vs Manual: Kapan Pakai Senjata Berat?**

"Terus, Mbak. Apa semua testing harus manual kayak tadi? Bolak-balik klik Postman?" tanya Binto.

Mbak Rara menggeleng. "Enggak. Itu cuma buat eksplorasi awal. Untuk test yang berulang—kayak login, validasi form—kita bisa pakai automated testing."

Ia mencontohkan. "Misalnya, setiap kali kamu nambah fitur, kamu harus pastiin fitur lama gak rusak. Itu namanya *regression testing*. Kalau manual, bisa habis waktu. Mending pakai script otomatis. Di Laravel ada PHPUnit buat unit test dan feature test. Di Postman juga bisa bikin collection yang di-run otomatis."

"Tapi gak semua harus otomatis?" Binto memastikan.

"Gak semua. Untuk eksplorasi, UX, atau kasus-kasus aneh yang susah diprediksi, tetap perlu manual. ISO juga gak maksa semuanya otomatis. Pilih sesuai kebutuhan dan risiko. Otomatisasi itu investasi: butuh waktu nulis script, tapi jangka panjang hemat waktu."

## **9.11 Perbaikan dan Unit Test Pertama**

Setelah sesi panjang itu, Binto kembali ke laptopnya dengan semangat baru. Ia perbaiki satu per satu celah yang ditemukan Mbak Rara.

Pertama, ia tambahkan validasi di endpoint pesanan: jumlah harus minimal 1, tidak boleh melebihi stok. Jika tidak valid, kembalikan 422 dengan pesan jelas.

Kedua, ia perbaiki pengecekan token. Kini API benar-benar memverifikasi keabsahan token, bukan hanya keberadaannya. Token palsu atau kadaluarsa langsung ditolak dengan 401.

Ketiga, ia tambahkan penanganan error global. Setiap exception ditangkap dan diubah menjadi respons JSON yang sesuai standar. Tidak ada lagi error 500 misterius.

Mas Alin mendampingi. "Sekarang coba tulis unit test untuk endpoint login."

Binto membuka folder tests/Feature. Ia membuat file AuthTest.php. Dibantu Mas Alin, ia menulis beberapa test case:

* test\_login\_with\_valid\_credentials\_returns\_token  
* test\_login\_with\_invalid\_credentials\_returns\_401  
* test\_login\_with\_missing\_fields\_returns\_422

Ia menjalankan perintah php artisan test. Beberapa saat kemudian, layar menampilkan titik-titik hijau. Semua test lulus.

"Lihat, Mas. Hijau semua."

Mas Alin tersenyum. "Nah, itu rasanya aman. Setiap kali kamu ubah kode, jalankan test ini. Kalau ada yang merah, berarti kamu tidak sengaja merusak sesuatu."

## **9.12 Refleksi: QA adalah Partner, Bukan Musuh**

Sore hari, kantor mulai sepi. Binto duduk di teras, menikmati teh hangat. Mbak Rara keluar membawa baskom kecil berisi rambutan yang baru dipetik dari pohon depan.

"Ini, Mas. Panen sore ini. Manis-manis."

Binto mengambil sebutir. "Mbak, saya baru sadar. Selama ini saya pikir QA itu tukang cari kesalahan. Ternyata lebih dari itu."

Mbak Rara duduk di bangku sebelah, mengupas sebuah rambutan dengan kuku telunjuknya. "Aku senang kamu bilang gitu. Aku gak pernah niat nyari-nyari kesalahan. Aku cuma mau kita semua bisa tidur nyenyak."

Mbak Rara menerawang sejenak, melihat ke arah jalanan desa yang lengang. "Dulu aku kerja di perusahaan logistik di Surabaya, Mas. Ritmenya gila. Tiap hari buru-buru, kejar target, sikut-sikutan. Aku capek. Akhirnya milih pulang ke Blitar pas diajak nikah sama suamiku sekarang."

Binto menyimak sambil mengunyah daging buah yang manis. 

"Di sini aku nemu ketenangan," lanjut Mbak Rara. "Kerja sama Pakde dan Mas Alin itu rasanya kayak kerja sama keluarga. Makanya, aku mau lindungi ketenangan ini. Bayangin kalau bug tadi lolos ke production. Pak Haji telepon marah-marah. Pakde stres. Kamu lembur benerin. Ketenangan kita semua hancur."

"Testing itu kayak milih rambutan," Mbak Rara menyodorkan sebuah rambutan yang kulitnya merah sempurna namun agak busuk di ujung. "Kalau kita petik asal-asalan, bisa dapat yang busuk. Tapi kalau kita periksa satu-satu—kulitnya merah, teksturnya kenyal, gak ada bekas ulat—baru kita sajikan. Hasilnya manis."

Mas Alin yang sejak tadi menyimak dari dalam ikut keluar. "Nah, itu analogi yang pas. Kualitas itu budaya, bukan sekadar proses. QA bukan musuh developer. QA itu partner yang bantu kamu jadi engineer lebih baik."

Mbak Rara menimpali. "Dan ingat ya, Mas. Lebih baik error di sini daripada di tangan pengguna. Di sini, kita masih bisa ketawa-ketiwi sambil makan rambutan. Di sana? Bisa-bisa kontrak diputus."

Mereka bertiga tertawa.

Di atas mereka, pohon rambutan bergoyang pelan. Buah-buahnya yang merah sudah banyak yang dipetik, tapi masih banyak yang bergelantungan, menunggu giliran untuk diuji kualitasnya.

Binto menatap langit Blitar yang mulai jingga. Pelajaran hari ini bukan cuma tentang validasi atau unit test. Tapi tentang *mindset*. Kualitas bukan beban. Kualitas adalah tameng. Dan Mbak Rara adalah satpam yang menjaga gerbang.