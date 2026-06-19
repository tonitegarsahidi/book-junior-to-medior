# Bab 5: No Silver Bullet

Minggu keempat.

Binto mulai pede. Udah bisa Git. Udah ngerti Scrum. Udah pernah deploy fitur ke production. Udah ngerasain gimana kode-nya dipakai orang beneran di Kalimantan.

Tapi hari ini... dia mulai bertanya.

Bukan tentang kode. Bukan tentang framework. Tapi tentang sesuatu yang lebih besar.

## 5.1 Mengamati Repo

Sore itu, kantor Garda Teknologi Nusantara lumayan lengang. Wawan masih remote, Mbak Rara sedang keluar menemani Bu Sari belanja kebutuhan dapur kantor, dan Pakde Suhar ada rapat dengan klien dari Kediri. Hanya Binto dan Mas Alin yang tersisa, ditemani suara kipas angin Ufo dan aroma kopi yang mulai dingin.

Binto baru saja selesai melakukan deploy kecil untuk perbaikan bug di modul Koperasi Sekar Patria. Sambil menunggu proses deploy selesai, iseng ia membuka Git dan melihat daftar repositori proyek di organisasi kantor.

koperasi-sekar-patria. PHP.

pabrik-garum. PHP.

sekolah-alhikmah. PHP.

minimarket-kalimantan. PHP.

toko-atk-warsiti. PHP.

Semua PHP.

Binto mengernyit. Ia scrolling lagi. Semua proyek yang ia temui selama dua minggu terakhir ternyata ditulis dalam bahasa yang sama. PHP. Bahkan proyek untuk klien dari Surabaya yang katanya "lebih modern" juga PHP—hanya beda framework, pakai Laravel terbaru.

Ia jadi teringat sesuatu. Sesuatu yang sering ia lihat di linimasa sebelum ia pulang kampung.

## 5.2 Suara dari Internet

Malam-malam di kosannya dulu, Binto punya kebiasaan membuka forum-forum teknologi dan membaca utas-utas di media sosial. Sebagai lulusan PTN yang ingin tetap update, ia merasa perlu tahu apa yang sedang hype.

Dan hype itu punya pola yang jelas.

Setiap beberapa bulan, akan ada utas viral yang membandingkan bahasa pemrograman. Kebanyakan berupa meme, tapi ada kalanya grafik benchmark warna-warni ditampilkan. Di puncak, selalu ada nama-nama seperti Rust, Go, atau Zig. Grafik batangnya menjulang tinggi, menunjukkan kecepatan yang fantastis.

Dan di dasar grafik? Hampir selalu ada PHP. Tertinggal jauh. Disertai candaan: "PHP is dead." "PHP: the elephant that never dies." "Paling cocok buat bikin blog DoFollow."

Binto tidak pernah benar-benar ngoding pakai Rust atau Go. Ia hanya tahu bahwa bahasa-bahasa itu katanya cepat. Katanya modern. Katanya dipakai oleh perusahaan-perusahaan besar.

Sementara PHP? Itu bahasa jadul. Bahasa yang dipelajarinya di semester 6, lalu kemudian ia tinggalkan karena dosen beralih ke JavaScript dan Python.

*Kenapa kantor ini masih setia sama PHP?*

Ia membayangkan Raka, teman kuliahnya yang sekarang kerja di startup Jakarta. Minggu lalu Raka posting di LinkedIn: "Just migrated our entire backend to Go. 10x performance improvement!" Delapan ratus likes. Puluhan komentar kagum. Binto sempat meng-scroll postingan itu berkali-kali, perutnya terasa aneh. *Apa aku stuck di teknologi yang udah mati? Apa aku salah pilih?*

Pertanyaan itu mengendap di kepalanya sepanjang sore.

## 5.3 Pertanyaan di Sore Hari

Menjelang pukul empat sore, sesaat sebelum jam pulang, Mas Alin keluar ke teras membawa dua cangkir enamel—satu kopi hitam, satu teh hangat. Ia duduk di bangku kayu, memberi isyarat ke Binto untuk ikut.

"Tumben sepi," kata Mas Alin sambil menyesap kopinya. "Enak, ya. Bisa mikir tanpa suara Wawan yang lagi ngomel sama request klien."

Binto tersenyum tipis. Ia menerima cangkir tehnya, menyesap pelan. Pikirannya masih pada daftar repo tadi.

"Mas," akhirnya ia membuka suara. "Saya mau tanya."

"Monggo."

"Kenapa kita di sini pakai PHP terus? Semua proyek PHP."

Mas Alin tidak langsung menjawab. Ia hanya menyesap kopinya, menunggu Binto melanjutkan.

"Maksud saya... di internet itu katanya PHP lambat. Banyak yang bilang mending pindah ke Go atau Rust. Katanya lebih cepat, lebih modern. Teman-teman saya di Jakarta juga beberapa pada pindah ke situ. Kenapa kita gak ikut?"

Mas Alin meletakkan cangkirnya. Ia menatap pohon rambutan yang buahnya sudah merah merona. Senyum tipis muncul di wajahnya.

"Pertanyaan bagus, Le."

## 5.4 Kisah Proyek Pemerintah

"Kamu tahu," Mas Alin memulai, "dulu saya pernah pegang proyek di sebuah institusi pemerintah. Lumayan besar. Saya sudah siapkan arsitektur keren. Saya mau pakai Python waktu itu, karena lagi hype buat data processing."

Binto menyimak.

"Sudah saya pelajari framework-nya. Sudah saya siapin struktur foldernya. Saya semangat. Mau tunjukin ke klien kalau kita ini update."

"Lalu?"

"Lalu klien bilang: 'Mas, server kami cuma bisa deploy PHP dan NodeJS.'"

Binto mengerutkan dahi.

"Server mereka sudah ada. Dikelola oleh divisi IT internal. Mereka gak bisa—atau gak mau—nambah konfigurasi baru. Jadi pilihannya cuma dua: PHP atau NodeJS. Waktu itu NodeJS masih baru, ekosistemnya belum serame sekarang. Jadi ya sudah, saya pakai PHP."

Mas Alin menoleh ke Binto. "Itu pertama kalinya saya sadar, Le. Memilih teknologi itu gak cuma soal 'apa yang paling keren'. Tapi juga soal 'apa yang bisa jalan di sana'. Klien kita bukan cuma butuh kode. Mereka butuh solusi yang bisa hidup di ekosistem mereka."

Binto manggut-manggut pelan.

"Klien kita itu rata-rata orang biasa, To. Kayak temennya Pakde Suhar." Mas Alin menerawang, senyumnya sedikit memudar. "Kamu tahu kenapa kantor ini namanya Garda Teknologi Nusantara?"

Binto menggeleng.

Mas Alin menyesap kopinya lagi. "Dulu, sebelum bikin GTN, Pakde itu punya warnet namanya GardaNet. Lumayan ramai. Terus dia dapat pesanan bikin web toko. Karena nggak bisa coding, dia serahin uang DP-nya ke teman programmernya. Eh, uangnya dibawa kabur. Klien marah, Pakde terpaksa jual semua PC warnetnya buat ganti rugi. Hancur lebur."

Binto membelalak. "Serius, Mas? Pantesan Pakde nggak pernah mau pegang urusan teknis."

"Iya. Pakde trauma. Sama kayak saya waktu itu." Mas Alin tertawa sumbang. "Saya dulu CTO startup fintech di Jakarta. Keren, valuasinya miliaran. Tapi saya... saya kerja kayak orang kesurupan. Ngejar valuasi, ngejar investor. Anak buah saya benci saya — saya paksa mereka lembur tiap hari. Saya kira itu cara ngebangun perusahaan. Ternyata... saya cuma ngebangun monster."

Ia menarik napas panjang. "Usia 30... saya ambruk. Masuk rumah sakit. Kurang tidur kronis. Co-founder cuma jenguk sekilas. Anak buah... sebagian mungkin lega. Tapi orang tua saya — yang dua tahun nggak pernah saya jenguk — mereka naik kereta dari Kediri ke Jakarta. Duduk di samping ranjang saya. Nggak banyak ngomong. Cuma nemenin."

"Saya sadar: ambisi startup itu fatamorgana. Saya resign. Minta maaf satu-satu ke anak buah. Jual saham saya. Balik ke Kediri. Nunggu bus... di Terminal Bungurasih, Surabaya."

Mas Alin memutar cangkir enamel di tangannya perlahan. Cangkir dengan gambar wayang itu adalah merchandise dari startup fintech-nya yang gagal — satu-satunya yang dia simpan. "Di situlah saya ketemu Pakde. Masjid terminal, habis sholat."

Ia menoleh ke arah Binto. "Kantor ini dibikin bukan buat bersaing bikin aplikasi super canggih sekelas Silicon Valley. Kantor ini dibikin buat nampung programmer yang pengen kerja tenang di daerah, dan buat bantu orang-orang biasa di sekitar kita. Buat Koperasi Sekar Patria biar nggak salah hitung utang. Teknologi buat mereka itu bukan soal Rust atau Go yang bisa proses jutaan data per detik. Teknologi buat mereka itu cuma satu: programnya jalan, gampang dipakai, dan yang paling penting... nggak nipu."

Karena program terbaik itu bukan program yang mahal, dapat investor milyaran — bukan, bukan itu. Tapi software yang dipakai dan bermanfaat.

Binto terdiam. Kata-kata terakhir itu terasa sangat berat dan dalam. Tiba-tiba, PHP yang dianggapnya kuno itu terasa jauh lebih mulia daripada sekadar angka-angka di benchmark kecepatan.

## 5.5 Kecepatan yang Mana?

"Terus soal kecepatan," Mas Alin melanjutkan. "Kamu bilang PHP lambat?"

"Iya, Mas. Di benchmark kalah jauh sama Go atau Rust."

"Betul. Di benchmark, PHP memang kalah. Tapi coba lihat klien kita."

Mas Alin menunjuk ke arah kantor—ke papan sticky notes yang menempel di dekat dispenser.

"Koperasi Sekar Patria. Anggotanya cuma 100-an orang. Aplikasinya dipakai paling ramai seminggu sekali pas pencatatan simpanan."

"Pabrik Garum. Admin yang pakai cuma 5 orang. Itu pun cuma buka aplikasi pagi hari buat input stok, siang lihat laporan."

"Sekolah Al-Hikmah. Guru dan TU yang akses bareng paling 15 orang. Jam sibuk cuma pas pembagian rapor."

"Minimarket Kalimantan. Tiga cabang di Balikpapan. Transaksinya sekitar 200-300 per cabang per hari. Lumayan ramai—tapi tetap masih skala kecil."

Mas Alin menatap Binto. "Mau secepat apa, Le? Mau pakai Rust yang bisa proses jutaan request per detik, buat apa? PHP udah cukup buat skala segini. Yang penting aplikasi jadi, biaya murah, dan mudah dirawat."

"Tapi kecepatan bukan satu-satunya pertimbangan," Mas Alin melanjutkan. Ia menghitung dengan jari. "Ada banyak dimensi lain. Pertama, development speed — seberapa cepat fitur bisa jadi. Klien kita minta revisi tengah malam, pagi harus jadi. PHP dengan Laravel bisa ngebut. Kedua, hiring — cari programmer PHP di Blitar? Ada. Cari programmer Rust di Blitar? Mungkin nol."

"Ketiga, ekosistem. PHP punya WordPress, Laravel, Magento — ratusan ribu library, tutorial, forum. Error apa pun, solusinya sudah ada. Bahasa baru? Komunitasnya masih kecil. Satu error bisa bikin stuck berhari-hari."

"Keempat, biaya operasional. Hosting PHP murah — shared hosting Rp 50 ribu per bulan cukup buat kebanyakan klien kita. Mau deploy Go atau Rust? Minimal butuh VPS, itu sudah ratusan ribu per bulan. Buat minimarket tiga cabang? Gak masuk akal."

Binto mulai melihat celah di logikanya sendiri. *Selama ini aku cuma lihat kecepatan. Padahal ada banyak faktor lain yang gak pernah kepikiran.*

## 5.6 Analogi Mobil di Gang Sempit

"Kamu tahu mobil Alphard?" tanya Mas Alin tiba-tiba.

Binto mengangguk. "Tahu, Mas. Mobil mewah. Besar. Nyaman."

"Bayangin kamu punya Alphard. Keren, kan? Tapi rumahmu di gang sempit. Lebar gang cuma dua meter. Mobil cuma bisa lewat kalau spion dilipat. Mau parkir di rumah? Gak muat. Akhirnya parkir di pinggir jalan raya, kena panas, kena debu, setiap malam was-was takut digores orang."

Binto membayangkan. "Ribet juga ya, Mas."

"Sekarang bayangin kamu punya Agya atau Ayla. Mobil kecil. Muat di gang sempit. Parkir enak. Irit bensin. Gak bikin pusing."

Mas Alin menyesap kopinya. "Nah, Rust atau Go itu kayak Alphard. Keren, canggih, tapi belum tentu cocok buat jalanan di sini. PHP itu kayak Agya. Sederhana, tapi cukup. Masuk gang sempit bisa. Nanjak dikit bisa. Yang penting sampai tujuan."

Binto nyengir. Analogi itu sederhana, tapi mengena.

## 5.7 Ekosistem yang Mendukung

"Itu baru dari sisi kecepatan," Mas Alin melanjutkan. "Sekarang lihat dari sisi ekosistem."

Ia membuka laptop yang sejak tadi tergeletak di sampingnya. "PHP itu sudah ada sejak sebelum kamu lahir, Le. Hosting murah bertebaran. Dokumentasi melimpah. Komunitas besar. Kalau ada error, tinggal Googling, hampir pasti ketemu solusinya."

Ia scrolling. "Coba bandingkan dengan bahasa baru. Ekosistemnya masih kecil. Komunitasnya masih terbatas. Mau cari solusi error sepele aja bisa berjam-jam nyari di forum yang sepi. Itu gak efisien buat bisnis kita."

Binto teringat pengalamannya sendiri saat mencoba framework JavaScript modern untuk tugas akhir. Error kecil saja bisa bikin dia begadang karena dokumentasinya tidak lengkap.

"Waktu itu saya nyoba framework JS, Mas. Error undefined doang, saya nyari solusinya sampai subuh."

"Nah, itu dia. Bayangin kalau itu proyek klien. Deadline besok. Kamu stuck di error sepele karena dokumentasinya kurang. Klien marah, bos marah, kamu stress. Itu biaya yang gak kelihatan."

## 5.8 Monolith untuk yang Kecil

Binto ingat istilah lain yang sering berseliweran di linimasa teknologinya dulu. *Microservices*. Katanya arsitektur masa depan. Pisah-pisah aplikasi jadi layanan-layanan kecil yang berdiri sendiri. Kayak restoran food court: tiap tenant punya dapur sendiri, menu sendiri, kasir sendiri. Kalau tenant mie ayam tutup, tenant sate masih buka. Beda sama restoran biasa — satu dapur, satu menu, satu kasir. Kalau dapurnya kebakaran, semua tutup.

Dia juga sering lihat istilah lawannya: *monolith*. Satu aplikasi utuh. Semua fitur dalam satu codebase. Satu database. Satu server. Kayak warung Padang legendaris: semua lauk dalam satu etalase. Praktis, murah, cepat. Tapi kalau etalasenya penuh... susah nambah lauk baru.

*Kenapa kita gak pakai microservices?* pikirnya. *Katanya lebih scalable.*

"Mas," Binto membuka suara. "Saya sering baca soal microservices. Katanya lebih scalable, lebih modern. Kenapa kita gak pakai arsitektur itu?"

Mas Alin tertawa kecil. "Microservices buat Koperasi Sekar Patria?"

Ia menggeleng. "Koperasi cuma punya 100 anggota, Le. Mau di-scale sampai mana? Mau dipisah jadi berapa service? Nanti kita lebih sibuk urus jaringan antar-service daripada urus fitur buat klien."

Mas Alin mencondongkan badan. "Begini. Microservices itu bagus. Tapi dia punya harga. Kompleksitas. Biaya server lebih banyak. Butuh tim yang paham. Cocok buat perusahaan besar dengan jutaan pengguna. Tapi buat kita?"

Ia menunjuk ke sekeliling. "Tim cuma segini. Klien cuma segitu. Monolith itu cukup. Bahkan lebih dari cukup."

"Terus kapan microservices cocok, Mas?" tanya Binto.

Mas Alin berpikir sejenak. "Bayangin Tokopedia atau Gojek. Mereka punya jutaan pengguna, ribuan transaksi per detik. Tim engineer-nya ratusan orang, dibagi per tim kecil. Setiap tim megang satu domain — tim pencarian, tim pembayaran, tim notifikasi. Kalau mereka masih pakai satu monolith raksasa, tiap kali tim notifikasi mau deploy, mereka harus nunggu antrian. Tiap kali ada bug di modul pembayaran, bisa bikin seluruh aplikasi down."

"Di microservices, tiap tim bisa deploy sendiri-sendiri. Gak perlu nunggu tim lain. Modul pencarian rusak? Yang lain tetap jalan. Modul notifikasi butuh scale karena Hari tanggal kembar? Tinggal nambah server untuk notifikasi doang, gak perlu scale semua."

Mas Alin menyesap kopinya. "Jadi prinsipnya: monolith itu untuk tim kecil dengan kompleksitas rendah. Microservices untuk organisasi besar dengan tim banyak dan domain yang kompleks. Jangan pakai microservices cuma karena keren. Tapi jangan paksa monolith kalau tim dan sistemmu sudah terlalu besar untuk satu codebase."

"Pilih arsitektur sesuai ukuran masalah. Jangan bawa pedang ke perang pisau. Atau jangan bawa pisau ke perang pedang. Sesuaikan."

Wawan yang sejak tadi menyimak dari dalam—jendela teras terbuka lebar—tiba-tiba nimbrung. "Aku juga gitu, Mas. Di komunitas desain, tiap bulan ada framework CSS baru. Dulu main Bootstrap, lalu ada yang bilang Bootstrap jelek, mending pakai Tailwind. Styled-components, CSS Modules, Sass... Aku capek ngikutin. Akhirnya aku pakai yang aku kuasai dan yang klien gak komplain."

Mas Alin menunjuk Wawan. "Nah. Itu berlaku di semua lini. Backend, frontend, desain. Pilih yang masuk akal, bukan yang paling ramai dibicarakan."

## 5.9 Hantu-Hantu yang Masih Hidup

Mas Alin meraih ponselnya, membuka sesuatu. Bukan media sosial kali ini, tapi sebuah situs lowongan kerja.

"Sini, Le. Lihat ini."

Binto mendekat. Di layar, tampak daftar lowongan pekerjaan.

"COBOL Developer. Bank BUMN. Pengalaman minimal 3 tahun. Penempatan Jakarta."

Binto mengerutkan dahi. "COBOL? Itu kan bahasa kuno banget, Mas. Jaman kakek-kakek."

"Tahu dari mana kamu?"

"Ya... baca-baca di internet. Katanya bahasa itu udah mati. Gak ada yang pakai lagi."

Mas Alin tersenyum. "Mati? Coba lihat berapa gajinya."

Binto membaca angka yang tertera. Matanya membelalak.

"Gila. Segitu?"

"COBOL itu masih hidup, Le. Banyak bank dan asuransi tua di dunia yang sistem intinya masih pakai COBOL. Mereka gak berani ganti karena sistemnya kritis. Transaksi jutaan dolar per hari. Salah sedikit bisa kacau. Jadi mereka pertahankan."

Mas Alin menggulir layar. "Ini lagi. Java Developer. Perusahaan enterprise. Butuh 5 orang. Padahal di kampus-kampus sekarang Java sudah mulai jarang diajari, kalah sama Python dan JavaScript."

Ia menggulir lagi. "Nah, ini. .NET Developer. Perusahaan sawit di Kalimantan. Padahal coba sebutkan satu kampus di Indonesia yang ngajarin .NET secara serius. Langka."

Binto terdiam. Semua yang ia kira "kuno" dan "mati" ternyata masih bertahan, bahkan dibayar mahal.

"Punya teman saya di Jakarta," Mas Alin melanjutkan. "Kerja di sebuah vendor IT. Mereka dapat proyek dari perusahaan asuransi Jepang. Tahu apa yang dipakai? COBOL. Timnya isi bapak-bapak usia 50-an. Anak muda kayak kamu gak ada yang mau. Padahal gajinya selangit."

"Kenapa gak direkrut anak muda, Mas?"

"Karena anak muda maunya yang hype. React, Go, Rust. Begitu dengar COBOL, langsung mundur. Padahal di situlah duit beredar."

## 5.10 Fleksibel, Bukan Fanatik

Binto merenung. Pandangannya tentang "teknologi modern" mulai goyah.

"Jadi... gak ada bahasa yang benar-benar mati?"

"Selama masih ada sistem yang berjalan di atasnya, bahasa itu hidup. Mungkin gak seksi. Gak dibahas di Twitter. Tapi dia hidup. Diam-diam menghidupi banyak orang."

Mas Alin menatap Binto serius. "Makanya, Le. Jangan jadi fanatik satu bahasa. Jangan jadi orang yang cuma bisa PHP, atau cuma bisa JavaScript. Kamu harus fleksibel. Paham konsep dasarnya. Nanti tinggal adaptasi sintaks."

Ia menunjuk ponselnya. "Lihat COBOL tadi. Suatu hari bisa jadi kita dapat proyek yang butuh maintenance sistem COBOL. Kalau kita menutup diri, kita kehilangan kesempatan."

"Tapi kan kita gak bisa semua bahasa, Mas."

"Gak perlu semua. Tapi jangan membenci yang tidak kamu kenal. Buka pikiran. Pelajari mindset-nya. Nanti kalau ketemu di lapangan, kamu gak kaget."

## 5.11 Seni Migrasi: Kapan Harus Pindah

Binto teringat satu hal. "Mas, kalau misalnya suatu hari kita mau ganti stack. Dari PHP ke Go, misalnya. Itu gimana?"

Mas Alin mengangguk. "Pertanyaan bagus. Migrasi itu bukan dosa, Le. Asal dilakukan dengan sadar, bukan sekadar ikut-ikutan."

Ia menghitung dengan jari. "Pertama, lihat sumber daya. Apa kita punya orang yang bisa Go? Kalau gak ada, ya harus hire. Atau belajar dulu. Itu butuh waktu dan biaya."

"Kedua, lihat timeline. Migrasi itu gak instan. Proyek Koperasi Sekar Patria mungkin bisa selesai 2 minggu kalau pakai PHP. Kalau sambil belajar Go? Bisa 2 bulan. Klien mau nunggu segitu?"

"Ketiga, dan ini yang paling penting," Mas Alin menunjuk ke dalam kantor. "Manusia. Kode itu dipelihara oleh manusia. Bukan cuma kita yang sekarang. Tapi juga orang yang akan menggantikan kita kelak."

Ia menyesap kopinya. "Bayangin kita migrasi ke Go karena keren. Dua tahun kemudian kita pindah kerja. Tiba-tiba klien butuh perbaikan bug. Dia cari developer Go di Blitar? Susah. Bisa-bisa proyek terbengkalai."

"Jadi migrasi harus dipikirkan jangka panjang?"

"Persis. Jangan cuma mikir 'enak buat kita sekarang'. Tapi juga 'enak buat yang nerusin nanti'. Itu tanggung jawab profesional."

Binto manggut-manggut. Lalu ia teringat sesuatu. "Mas, saya sering dengar istilah technical debt. Itu apa sih? Apa hubungannya sama migrasi dan pilihan teknologi?"

Mas Alin tersenyum. "Pertanyaan lanjutan yang bagus, Le. Kamu mulai berpikir seperti engineer."

Ia menyesap kopinya. "Technical debt itu utang teknis. Setiap kali kita ambil jalan pintas demi kejar deadline, kita sebenarnya ngutang. Contoh: daripada bikin validasi lengkap, kita bikin validasi seadanya biar cepat rilis. Itu utang. Atau kita pakai library versi lama karena males upgrade. Itu juga utang."

"Terus suatu hari nanti kita harus bayar. Validasi seadanya tadi bikin user bisa masukin data sampah. Kita harus benerin — itu bayar utang. Library versi lama tadi tiba-tiba gak kompatibel sama server baru — kita harus upgrade darurat. Itu juga bayar utang, plus bunganya: stress, lembur, klien komplain."

Binto mengangguk pelan. "Jadi technical debt itu kayak utang di bank ya, Mas. Bunga-nya makin gede kalau gak segera dibayar."

"Persis. Tapi ini penting, Le: technical debt itu tidak selalu jahat," Mas Alin mencondongkan badan. "Kadang kita sengaja ngutang. Misalnya, klien butuh demo besok. Kita bikin fitur seadanya dulu, cepat — itu ngutang. Tapi setelah demo sukses, klien kasih kita waktu seminggu untuk merapikan. Kita bayar utangnya. Itu strategi yang valid."

"Yang bahaya itu kalau kita ngutang terus tanpa pernah bayar. Atau lebih parah lagi — ngutang tapi gak sadar kalau kita ngutang. Itu yang bikin proyek jadi legacy nightmare — kode yang semua orang takut sentuh, karena satu perbaikan kecil bisa bikin semuanya runtuh kayak rumah kartu."

Binto teringat proyek tugas akhir temannya yang sampai sekarang gak bisa di-maintenance karena kodenya terlalu ruwet. *Itu pasti technical debt yang sudah bertahun-tahun gak dibayar*, pikirnya.

"Jadi aturannya: ngutang boleh, asal dicatat. Dan harus ada rencana kapan bayarnya."

## 5.12 Berpikir Kritis pada Hype

Mas Alin membuka kembali aplikasi burung biru di ponselnya. Ia menunjukkan sebuah utas yang sedang viral.

"Ini. Lihat. 'PHP is dead.' Ribuan retweet. Yang nulis engineer dari startup unicorn."

Ia menggulir layar. "Tapi coba lihat siapa yang komentar. Kebanyakan anak startup Jakarta yang proyeknya high traffic. Mereka memang butuh teknologi high performance. Konteks mereka beda."

Mas Alin menutup ponselnya. "Setiap tahun ada yang bilang PHP mati. Tapi nyatanya WordPress, Magento, Laravel masih hidup. Toko online, website berita, aplikasi pemerintahan—banyak yang masih pakai PHP. Mereka gak peduli sama benchmark. Yang penting aplikasi jalan, bisnis jalan."

Ia menatap Binto serius. "Jangan telan mentah-mentah hype, Le. Tanya dulu: siapa yang bicara? Apa konteksnya? Apa kepentingannya? Bisa jadi mereka promosi bahasa baru karena ada insentif. Atau cuma pengen kelihatan keren."

Binto mengangguk. Pelajaran ini tidak pernah ia dapat di kampus.

"Tapi, Le," Mas Alin mencondongkan badan. Suaranya lebih pelan sekarang. "Bukan berarti kita tutup mata sama perkembangan zaman."

Binto menoleh.

"Tadi saya bilang jangan telan hype. Betul. Tapi kebalikannya juga bahaya: cuek total. Ngerasa PHP aja cukup, nggak perlu belajar yang lain. Ngerasa monolith aja cukup, nggak perlu ngerti microservices. Itu... juga jebakan."

Ia menyesap kopinya yang sudah mulai dingin. "Dunia IT itu bergerak cepet, Le. Bukan cuma soal teknologi. Tapi soal *market fit*. Klien kita hari ini cukup pakai PHP. Tapi lima tahun lagi? Mungkin mereka butuh aplikasi mobile. Atau butuh integrasi sama IoT. Atau butuh real-time dashboard. Kalau kita cuma bisa PHP... kita kehilangan mereka."

"Dan buat kamu sendiri," Mas Alin menatap Binto, "skill itu mata uang. Kamu mungkin nyaman di Blitar sekarang. Tapi suatu hari... siapa tahu kamu dapat tawaran di Jakarta. Atau remote buat perusahaan luar. Mereka cari Go, mereka cari Rust. Kamu mau bilang 'maaf, saya cuma PHP'?"

Binto terdiam. *Market fit.* Istilah yang belum pernah dia dengar sebelumnya. Tapi masuk akal.

"Jadi prinsipnya: *be where the market is, not where the hype is*," Mas Alin melanjutkan. "Hype itu suara. Market itu kenyataan. PHP masih besar market-nya sekarang. Tapi Go, Rust, Node.js... market-nya tumbuh. Python dengan AI-nya... meledak. Kamu nggak harus jago semua. Tapi setidaknya... tahu. Bisa baca. Bisa ngobrol. Bisa nilai kapan harus pindah."

"Kayak kamu tahu mobil Alphard walaupun nggak beli, kan?"

Mas Alin nyengir. "Persis. Kamu nggak harus punya Alphard. Tapi kamu harus tahu Alphard itu ada. Dan kenapa orang-orang pada ngomongin Alphard."

Binto nyengir balik. Analogi Mas Alin selalu sederhana, tapi ngena.

*Jangan fanatik PHP. Tapi jangan juga cuek sama dunia luar. Market yang nentuin.*

"Tapi, Mas," Binto berkata pelan. "Kadang justru karena banyak pilihan itu yang bikin bingung. Lihat aja: PHP, Go, Rust, Node.js, Python, Java... terus microservices, monolith, serverless... terus Laravel, Express, Gin, Actix... Pusing sendiri jadinya."

Mas Alin tertawa kecil. "Itu namanya paradox of choice, Le — paradoks pilihan. Ada istilah psikologi: semakin banyak pilihan, justru semakin susah memilih. Dan setelah memilih pun, kita jadi gampang menyesal. 'Ah, kenapa aku pilih PHP ya? Mending Go kali.'"

Ia menatap pohon rambutan. "Tapi coba pikir: apakah klien kita peduli pakai framework apa? Mereka cuma peduli satu hal: aplikasinya jalan. Solusi buat mereka sederhana: pakai yang sudah dikuasai, yang cocok buat masalahnya, dan yang bisa dikerjakan tepat waktu."

"Kamu gak perlu pusing memilih dari seratus opsi. Mulai aja dari yang kamu tahu. Buat di Blitar sini, PHP sudah cukup untuk sekarang. Nanti kalau ketemu masalah yang memang gak bisa diselesaikan PHP, saat itulah kamu cari alternatif. Jangan nyari masalah buat teknologi. Tapi cari teknologi buat masalah."

Binto menghela napas lega. Beban di kepalanya terasa lebih ringan. *Aku gak perlu jadi ahli semua teknologi. Cukup pilih yang tepat untuk masalah yang ada di depan mata.*

## 5.13 Penutup: Peluru Sakti

Sore mulai teduh. Matahari semakin condong ke barat. Suara adzan ashar ala pedesaan sebentar lagi akan berkumandang, menandakan pukul empat sore telah tiba.

"Ada istilah di dunia software engineering," kata Mas Alin sambil menyesap sisa kopinya yang sudah dingin. "No Silver Bullet."

Binto menoleh. "No Silver Bullet?"

"Iya. Istilah ini dipopulerkan oleh Fred Brooks tahun 1986. Intinya: tidak ada satu teknologi, satu metode, atau satu alat pun yang bisa menyelesaikan semua masalah software engineering."

Mas Alin menatap pohon rambutan yang buahnya siap panen.

"Di cerita siluman, peluru perak itu bisa membunuh semua monster. Tapi di dunia nyata, gak ada peluru sakti kayak gitu. PHP bukan peluru sakti. Rust juga bukan. COBOL juga bukan. Java, .NET, Go—semua punya tempatnya masing-masing."

Ia menoleh ke Binto. "Tugas kita sebagai engineer bukan cuma ngoding. Tapi memilih alat yang paling tepat untuk masalah yang ada. Bukan alat yang paling keren, paling hype, atau paling banyak dipuji di internet. Tapi yang paling sesuai."

Binto terdiam. Ia teringat meme-meme yang dulu ia lihat. Grafik benchmark warna-warni. Utas viral yang saling menjatuhkan. Semua itu terasa begitu jauh dari realitas kantornya yang tenang di Srengat ini.

"Jadi... kita pakai PHP bukan karena gak tahu yang lain?"

"Bukan. Kita pakai PHP karena itu yang paling masuk akal untuk klien kita. Murah, cepat development-nya, mudah dicari orang kalau kita butuh tambahan tim. Itu pilihan sadar, bukan keterpaksaan."

Mas Alin bangkit, meregangkan tubuh.

"Dan ingat, Le. Dunia IT itu luas. Ada yang sibuk bikin aplikasi high traffic pakai Go. Ada yang maintain sistem bank pakai COBOL. Ada yang bikin website toko online pakai PHP. Gak ada yang lebih rendah atau lebih tinggi. Semua punya peran."

Binto mengangguk. "Saya paham sekarang, Mas."

Suara adzan mulai terdengar sayup dari masjid desa. Jam 4 sore, waktunya mereka hendak pulang.

"Nggih, sudah. Ayo sholat dulu. Nanti kalau sudah dapat proyek yang memang butuh kecepatan tinggi, kita bisa explore Go atau Rust. Atau kalau dapat proyek maintenance COBOL, ya kita pelajari COBOL. Tapi untuk sekarang, PHP sudah cukup. Jangan sampai kita tinggal di gang sempit tapi malah mau beli Alphard yang gak muat."

Binto tersenyum. Ia bangkit, mengikuti Mas Alin ke masjid.

Di kepalanya, istilah "No Silver Bullet" terngiang-ngiang. Juga bayangan lowongan COBOL dengan gaji selangit. Pelajaran sore ini lebih berharga dari sekadar sintaks atau framework. Ini tentang cara berpikir. Cara memilih. Dan cara menghargai bahwa setiap teknologi punya tempatnya.

Dan ia tahu, ini baru permulaan.
