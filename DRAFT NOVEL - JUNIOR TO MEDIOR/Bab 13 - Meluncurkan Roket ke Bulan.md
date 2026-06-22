# Bab 13: Meluncurkan Roket ke Bulan

## 13.1 Sabtu di Kafe Gelato

Sabtu siang. Matahari Blitar bersinar cukup terik, tapi angin dari arah selatan membuat udara tidak terlalu gerah. Binto memarkirkan motornya di halaman sebuah kafe mungil bergaya industrial, tak jauh dari Stasiun Blitar. Papan namanya sederhana: *Gelato Stasiun*.

"Wah, tumben Pakde ngajak ke sini," gumam Binto sambil membuka helm.

Di dalam, Pakde Suhar sudah duduk di meja panjang dekat jendela. Di sebelahnya, seorang ibu berkerudung pastel—istri Pakde—sedang asyik mengobrol dengan beberapa ibu lain di sudut ruangan. Tampaknya mereka sedang arisan.

"Sini, *Le*," panggil Pakde. "Hari ini istri saya arisan di sini. Saya sekalian aja ngikut. Daripada bengong di rumah, mending ngopi sambil ngobrol sama kalian."

Mas Alin, Mbak Rara, dan Cahyo sudah duduk duluan. Cahyo tampak antusias memandangi etalase gelato warna-warni.

"Mas, itu es krim Italia ya? Boleh pesan?" tanyanya.

Pakde tertawa. "Pesan aja. Anggap aja bonus PKL."

Binto memesan es kopi susu. Saat disajikan, ia menyesapnya pelan. *Creamy. Bedanya jauh sama kopi tubruk di kantor.* Di kantor, kopi itu sederhana: hitam, pahit, kadang ada ampasnya. Tapi justru di situlah kenikmatannya. Di kafe ini, semuanya terasa lebih... *halus*.

Cahyo kembali dengan cup gelato stroberi. Matanya berbinar. "Enak, Mas. Lembut banget."

Sementara mereka menikmati pesanan, Binto memperhatikan Pakde Suhar yang sedang mengobrol ringan dengan pemilik kafe—seorang ibu muda berkacamata. Dari potongan percakapan yang terdengar, Pakde sedang bertanya soal operasional kafe.

"Masih pakai nota kertas, Bu? Gak pernah salah hitung?" tanya Pakde sambil menunjuk tumpukan bon di kasir.

"Sering, Pak. Apalagi kalau rame. Kadang lupa catat, kadang salah jumlah," jawab si pemilik.

"Nanti kapan-kapan saya kenalin sama tim saya. Siapa tahu bisa dibantu bikin sistem kasirnya. Yang simpel aja, gak ribet."

Binto tersenyum dalam hati. *Pakde gak pernah berhenti cari peluang. Bahkan di kafe gelato pun, naluri bisnisnya tetap jalan. Dan caranya halus—bukan jualan, tapi menawarkan bantuan.*

## 13.2 Pertanyaan Cahyo

Obrolan mengalir santai. Dari soal arisan, cuaca, sampai akhirnya kembali ke soal kerjaan.

"Mas Alin," Cahyo membuka suara. "Saya mau tanya. Kemarin kita *deploy* ke staging dan production cuma pakai git push. Kok bisa ya langsung muncul di internet? Dulu di sekolah, saya diajarinnya *upload* pakai FileZilla. Satu-satu. Ribet."

Binto ikut menoleh. Ia juga penasaran. Selama ini ia hanya mengikuti prosedur: *push* ke branch tertentu, tunggu notifikasi, selesai. Tapi apa yang sebenarnya terjadi di balik layar?

Mas Alin meletakkan cangkir kopinya. "Pertanyaan bagus, Dik. Sebelum jawab, saya cerita dulu ya. Biar kalian paham perjalanannya."

## 13.3 Era Pra-Internet: Deploy Pakai Disket

"Dulu," Mas Alin memulai, "sebelum internet merata seperti sekarang, orang *deploy* program itu pakai disket."

Cahyo mengernyit. "Disket? Itu yang bentuknya kotak pipih, Mas?" Ia berpikir sejenak. "Oh, yang jadi ikon *Save* itu ya?"

Mas Alin tertawa. "Betul. Kamu tiap hari klik ikon itu, tapi gak pernah pegang benda aslinya."

"*Nggih*. Disket. Atau CD. Jadi programmer bikin program di komputernya, lalu disalin ke disket. Terus disket itu dibawa langsung ke komputer klien. Bisa naik motor, naik angkot, atau kalau jauh ya dikirim lewat pos."

Binto membayangkan. "Ribet banget, Mas."

"Ribet. Itu pun cuma untuk aplikasi *offline*—kayak program Koperasi Sekar Patria yang kita kerjakan. Sampai sekarang, aplikasi yang cuma dipakai di jaringan lokal ya deploy-nya masih mirip-mirip begitu: install fisik, datang ke tempat, setup satu-satu. Gak bisa remote."

Mbak Rara menimpali. "Aku pernah baca, dulu perusahaan besar kayak bank, tim IT-nya keliling dari cabang ke cabang cuma buat *update* program. Bisa habis berhari-hari."

"*Nggih*. Dan disket itu sendiri gak selalu andal. Kadang sampai di tempat, disketnya rusak. Kena debu, kena panas, atau memang sudah aus. Programmer harus punya salinan cadangan. Kalau semua salinan rusak? *Wes*, pulang dengan tangan hampa."

Binto menggeleng pelan. Ia tidak bisa membayangkan betapa repotnya. Apalagi disket—ia bahkan tidak pernah melihat wujud aslinya. Hanya tahu dari cerita dan foto di internet. *Alangkah ribetnya*, pikirnya. *Betapa beruntungnya orang zaman sekarang.*

## 13.4 Era FTP dan cPanel: Upload Satu-Satu

"Terus internet mulai murah," Mas Alin melanjutkan. "Muncul hosting-hosting. Orang mulai *deploy* pakai FTP—*File Transfer Protocol*. Aplikasi kayak FileZilla, CuteFTP, atau langsung dari browser."

"Caranya?" tanya Cahyo.

"Edit file di komputer lokal. Kalau sudah jadi, buka FileZilla, login ke server, *upload* file satu per satu ke folder public\_html. Kalau ada revisi, *upload* lagi file itu. Kalau ada banyak file? Pilih satu-satu, atau *drag and drop* berharap gak ada yang putus di tengah."

Binto menimpali. "Saya dulu juga gitu, Mas. Sebelum kerja di sini. Upload lewat cPanel. Satu-satu. Kadang kalau koneksi lemot, bisa sejam cuma buat upload."

Mbak Rara menambahkan. "Aku ingat dulu waktu masih di Surabaya. Ada teman developer yang *deploy* pakai FTP. Suatu hari dia lupa *upload* file koneksi.php. Pas *production*, semua halaman error. Klien marah-marah. Dia panik, buru-buru *upload*, tapi klien sudah kecewa."

"Human error," Mas Alin mengangguk. "Itu risiko terbesar FTP. Belum lagi kalau *upload* ke folder salah. Atau tidak sengaja menimpa file penting. Atau koneksi internet putus di tengah *upload*. Semua bisa kacau."

## 13.5 Era Git Pull: Semi-Manual

"Lalu muncul Git," Mas Alin meneruskan. "Cara *deploy* mulai berubah. Kita bisa *SSH* ke server, lalu langsung git pull dari repository."

"Ini yang lebih rapi?" tanya Binto.

"Lebih rapi. Kita gak perlu *upload* satu-satu. Cukup git pull, semua perubahan terbaru langsung turun. Kalau proyek pakai Laravel, kita jalankan composer install buat *dependency*. Kalau Node.js, npm run build. Kalau ada migrasi database, php artisan migrate."

Cahyo mengangguk. "Tapi masih manual ya, Mas?"

"Masih semi-manual. Selama ini di kantor, cara ini yang kita pakai. Begitu ada *pull request* yang saya *approve*, saya yang login ke server, git pull, lalu jalankan perintah-perintah yang diperlukan. Di staging maupun di production. Butuh waktu sekitar 10 sampai 15 menit setiap kali deploy. Belum lagi kalau ada kesalahan kecil, harus ulangi."

Binto ingat. Selama beberapa bulan terakhir, setiap kali ia menyelesaikan fitur dan Mas Alin bilang "Sudah di-*deploy*", ia tidak pernah tahu proses di baliknya. Ternyata Mas Alin yang turun tangan langsung. *Pantas kadang ada jeda*, pikirnya.

"Itu lebih rapi dari FTP," kata Mas Alin. "Tapi tetap saja ada *human touch*. Kalau saya lupa composer install? Bisa error. Kalau saya lagi sibuk dan gak bisa deploy? Fitur numpuk di repository, gak sampai ke klien."

## 13.6 Saat Langkah Manual Menjadi Beban

"Makanya," Mas Alin menyesap kopinya, "untuk proyek Kalimantan ini, sekitar seminggu terakhir saya selesai setup CI/CD."

"Oh, ini yang baru ya, Mas?" Binto menimpali. "Pantesan kemarin pas saya push, tiba-tiba langsung muncul notifikasi sukses. Saya kira Mas Alin yang deploy cepat banget."

Mas Alin tertawa kecil. "Bukan saya. Robot yang kerja."

"Kenapa baru proyek Kalimantan, Mas?" tanya Cahyo.

"Karena pengalaman waktu itu. Waktu klien minta fitur cetak laporan dalam dua hari. Ingat, kan?"

Binto mengangguk. Ia ingat betul. Fitur pertamanya yang *live* ke production. Deg-degannya masih terasa.

"Waktu itu saya harus deploy beberapa kali dalam sehari. Bolak-balik login ke server, git pull, composer install, *build*, restart. Capek. Dari situ saya berpikir: kita perlu otomatisasi. Biar *deploy* gak jadi beban. Dan biar kalian juga bisa *deploy* sendiri tanpa nunggu saya."

"Tapi proyek lain belum ya, Mas?" tanya Binto.

"Belum. Proyek Koperasi versi lama kan offline. Yang versi baru ini nanti kita deploy ke VPS, tapi belum sempat saya pasang pipeline CI/CD. Proyek Pabrik Garum sama Sekolah Al-Hikmah juga masih pakai cara semi-manual. Nanti pelan-pelan kita migrasi. Yang penting kalian paham dulu konsepnya."

## 13.7 Robot Pengantar di Ujung Jalur

"Cahyo tadi tanya, apa itu CI/CD," Mas Alin mencondongkan badan. "CI itu *Continuous Integration*. CD itu *Continuous Delivery* atau *Continuous Deployment*."

Ia mencari analogi. "Bayangin pabrik roti modern. Ada mesin yang otomatis ngecek adonan—kekentalannya pas gak, raginya cukup gak. Terus mesin itu manggang. Terus mesin lain ngepak roti ke dalam plastik. Gak ada tangan manusia yang nyentuh. Hasilnya konsisten, cepat, dan minim kesalahan."

"Itu CI/CD. Setiap kali kita *push* kode ke repository, mesin itu langsung bekerja: ngecek kode kita, nge-*test*, nge-*build*, dan kalau lolos, langsung di-*deploy* ke server. Gak perlu login manual. Gak perlu ingat-ingat perintah. Robot yang kerjakan."

Cahyo melongo. "Jadi kita tinggal *push*, terus duduk manis?"

"Kurang lebih begitu. Untuk proyek Kalimantan, ya. Yang lain masih manual."

## 13.8 Aliran Air dalam Pipa Otomatis

Mas Alin mengambil selembar tisu dari meja. Ia mulai menggambar dengan pulpen.

"Ini alurnya. Namanya pipeline—kayak pipa air. Kode masuk dari ujung, keluar di ujung lain sebagai aplikasi *live*. Tapi di dalam pipa itu ada beberapa stasiun pemeriksaan."

Ia menggambar beberapa kotak berurutan.

"Pertama: Test. Robot jalankan unit test yang sudah kita tulis. Kalau ada yang merah, proses langsung berhenti. Robot kasih tahu: 'Test-mu gagal. Perbaiki dulu.' Gak akan ada kode rusak yang lolos."

"Kedua: Code Checker. Robot periksa gaya koding kita. Apakah ada kurung kurawal yang letaknya aneh? Apakah ada variabel yang tidak dipakai? Ini bikin kode kita tetap rapi dan konsisten."

"Ketiga: Static Security Check. Robot periksa apakah ada celah keamanan di kode kita. Misal, ada *hardcoded password*? Atau *library* yang sudah usang dan punya kerentanan? Robot kasih peringatan."

"Keempat: Build. Kalau semua pemeriksaan lolos, robot siapkan kode untuk *production*. Ibaratnya, adonan yang sudah lolos uji kualitas siap dipanggang."

"Kelima: Deploy. Kode yang sudah siap dikirim ke server tujuan. Bisa staging, bisa production. Tergantung *branch*\-nya."

Mas Alin menatap Binto dan Cahyo serius. "Tapi ingat, di lokal aman belum tentu di *production* aman. Di luar sana, siapa saja bisa coba akses sistem kita."

"Pastikan *config* sensitif seperti *password database* tidak ikut ke-*push* ke *repository*," lanjutnya tegas. "Banyak kebocoran data raksasa justru berawal dari hal sederhana kayak itu. Ingat pelajaran Git dulu?"

Binto mengangguk mengiyakan.

"Keenam: Notifikasi. Robot kirim pesan ke Telegram atau Slack. 'Deploy sukses' atau 'Deploy gagal'. Jadi kita bisa langsung tahu hasilnya tanpa harus buka laptop."

Mas Alin tersenyum tipis membayangkan proses akhirnya. "Setelah notifikasi sukses itu muncul, artinya sistem kita sudah *online*," katanya pelan. "Dan artinya... kita juga sudah 'terlihat'."

Kata-kata itu diucapkan dengan santai, tapi maknanya sangat kuat. Menjadi *online* bukan hanya soal fitur bisa dipakai, tapi juga membuka pintu bagi ribuan pasang mata—termasuk *hacker* iseng di seluruh dunia.

Binto memperhatikan coretan di tisu. "Wah, panjang juga prosesnya. Dan ternyata tanggung jawabnya berat."

"Panjang, tapi semua otomatis. Kita cuma perlu *push*. Robot yang kerja."

## 13.9 Macam-Macam Tools CI/CD

"Terus, robotnya pakai apa, Mas?" tanya Cahyo.

"Banyak pilihan. Kita di proyek Kalimantan pakai GitHub Actions, karena repository kita di GitHub. Tinggal bikin file konfigurasi di folder .github/workflows/. Gratis untuk tim sekecil kita."

Mas Alin melanjutkan. "Tapi ada juga yang lain. GitLab CI/CD kalau repository-nya di GitLab. Jenkins—ini tools legendaris, bisa diinstal di server sendiri, sangat fleksibel tapi agak ribet setup-nya. CircleCI, Travis CI. Prinsipnya sama: otomatisasi pipeline. Tinggal pilih yang paling cocok dengan kebutuhan dan *budget*."

"Jadi gak ada yang paling baik?" tanya Binto.

"Gak ada. Semua punya plus minus. Yang penting paham konsepnya. Nanti kalau pindah proyek atau pindah perusahaan, tinggal adaptasi."

## 13.10 Antara Pilihan dan Keharusan

"Tapi Mas," Binto bertanya. "Semua proyek harus pakai CI/CD?"

Mas Alin menggeleng. "Gak harus. Ini opsional. Lihat proyek Koperasi Sekar Patria. Aplikasinya offline, diinstal di komputer mereka. Buat apa pakai CI/CD? Gak relevan. Proyek Garum sama Sekolah masih pakai cara semi-manual juga gak masalah, karena frekuensi deploy-nya masih jarang."

"Tapi untuk proyek yang sering berubah, butuh rilis cepat, dan diakses banyak orang? CI/CD adalah standar *best practice*."

"Kenapa?" tanya Cahyo.

"Karena mengurangi *human error*. Robot gak akan lupa composer install. Robot gak akan salah *upload* folder. Robot gak akan capek. Selain itu, *feedback*\-nya cepat. Begitu *push*, kita langsung tahu apakah kode kita aman atau ada yang rusak. Gak perlu nunggu Mbak Rara tes manual dulu."

Mbak Rara menimpali. "Aku juga terbantu. Begitu ada *push* ke staging, aku langsung bisa tes. Gak ada lagi drama 'udah *deploy* belum, Mas?' Aku fokus nyari bug, bukan nungguin *deploy*."

## 13.11 Dirigen di Balik Layar Server

"Di tim kecil kayak kita," Mas Alin menambahkan, "kita semua rangkap. Saya yang setup pipeline. Binto yang nulis test. Andik yang urus server. Tapi di tim besar, biasanya ada role khusus: DevOps Engineer."

"DevOps?" Cahyo mengulang.

"*Development* dan *Operations*. Mereka yang jadi jembatan antara *developer* dan *server*. Tugas mereka: setup pipeline CI/CD, urus server, monitoring, logging, keamanan infrastruktur. *Developer* tinggal *push*, DevOps yang pastikan semuanya jalan mulus sampai ke *production*."

Binto membayangkan. "Enak juga ya. Fokus ngoding aja."

"Enak. Tapi jadi DevOps itu gak gampang. Harus paham dua dunia: kode dan infrastruktur."

## 13.12 Plus Minus CI/CD

Mbak Rara menimpali. "CI/CD memang keren. Tapi ada plus minusnya, lho."

"Apa minusnya, Mbak?" tanya Cahyo.

"Plus-nya jelas: cepat, konsisten, minim *human error*, *feedback* cepat, bisa *deploy* sambil tidur. Begitu *push*, robot kerja. Kita bisa lanjut ngopi."

"Minus-nya: butuh waktu setup di awal. Harus belajar cara bikin pipeline. Harus nulis unit test yang memadai. Kalau pipeline-nya terlalu kompleks, malah jadi beban. Dan kalau ada yang error di pipeline, kita harus bisa baca log-nya."

Mas Alin menambahkan. "Tapi untuk jangka panjang, investasinya sepadan. Sekali setup, selamanya tinggal pakai. Tim jadi lebih tenang, klien lebih puas."

## 13.13 Refleksi: Dari Disket ke Robot

Mas Alin menyandarkan punggungnya. Matanya menerawang ke luar jendela, ke arah Stasiun Blitar yang ramai.

"Dulu, *deployment* itu kayak meluncurkan roket ke bulan. Deg-degan. Banyak yang bisa salah. Sekali pencet, doa. Sekarang? Untuk proyek Kalimantan, tinggal *push*. Robot yang urus."

Ia menatap Binto dan Cahyo bergantian. "Tapi ingat. Secanggih apa pun pipeline, fondasinya tetap kode yang bersih dan *test* yang baik. Robot cuma bisa ngecek apa yang kita suruh. Kalau kita suruh ngecek hal yang gak penting, ya dia loloskan yang gak penting."

Binto mengangguk. "Jadi CI/CD itu akselerator. Bikin kita makin cepat. Tapi kalau mobilnya sendiri gak layak jalan, ya nabrak lebih cepat."

"Persis."

## 13.14 Penutup: Gelato dan Kode

Sore mulai turun. Istri Pakde dan rombongan arisan mulai beranjak. Pakde Suhar melirik jam.

"Wes, waktunya pulang. Pada mau nitip gelato lagi?"

Cahyo menggeleng. "Cukup, Pakde. Tadi sudah dua cup."

Mereka beranjak dari meja. Binto membawa sisa es kopinya. Di luar, suara kereta dari arah Malang lewat dengan klakson panjang yang memantul di dinding-dinding kafe.

Binto menatap stasiun yang ramai. Pikirannya melayang ke cerita Mas Alin tadi. *Dari disket, FTP, Git pull manual, sampai CI/CD.* Ia tidak bisa membayangkan alangkah repotnya orang IT zaman dulu. Harus bawa disket, datang ke lokasi fisik, instalasi atau update satu per satu. Apalagi disket katanya rawan rusak—terkena debu, panas, atau aus. Meski Binto tidak pernah tahu wujud disket seperti apa, ia bisa merasakan betapa merepotkannya.

*Betapa beruntungnya orang zaman sekarang*, pikirnya. Tinggal *push*, robot yang kerja. Semua serba cepat, serba otomatis—setidaknya untuk proyek Kalimantan. Proyek lain masih pakai cara semi-manual, tapi itu pun sudah jauh lebih baik daripada FTP.

"Mas," Cahyo tiba-tiba bersuara. "Nanti proyek lain bakal pakai CI/CD juga?"

"Pelan-pelan. Kalau sudah waktunya, pasti."

Cahyo tersenyum.

Motor dinyalakan. Satu per satu mereka meninggalkan kafe. Binto menatap spanduk *Gelato Stasiun* untuk terakhir kalinya. Hari ini ia belajar bahwa teknologi bukan cuma soal bahasa pemrograman atau *framework*. Tapi juga tentang bagaimana kode itu sampai ke pengguna.

Dari disket, FTP, Git pull manual, hingga robot-robot yang bekerja dalam sunyi di balik layar. Semua adalah bagian dari perjalanan panjang sebuah kode.
Dan ia tahu, ini satu langkah lagi menuju *medior*.

---

## 13.15 Hari Peluncuran

Seminggu setelah Sabtu di kafe Gelato.

Jam tujuh pagi, Binto sudah di kantor. Padahal deploy baru jam sembilan. Tapi dia tidak bisa diam di kontrakan.

Motor Beat-nya melaju lebih pelan dari biasanya tadi. Dua puluh menit. Tapi dua puluh menit ini terasa beda.

*Deg-degan*, pikirnya. *Wajar.*

Modul koperasi versi baru. Bukan lagi modul kecil. Bukan lagi tambalan. Ini versi dua. *Rewrite* total. Semua modul: anggota, simpanan, pinjaman, laporan, notifikasi. Semua terhubung. Semua harus berjalan.

Dan hari ini... dia akan *deploy* ke *production*.

Sendiri — tapi tidak sendirian.

Di kampus dulu, *production* adalah laptop sendiri. Kalau error... tinggal restart. Kalau gagal... tinggal ngomong ke dosen. Di sini... *production* berarti Koperasi Sekar Patria. Berarti seratus anggota yang tiap hari transaksi. Berarti data yang tidak boleh hilang. Berarti klien yang bayar.

Kantor masih sepi saat dia datang. Hanya Bu Sari, seperti biasa, menyapu teras yang mulai diguguri daun. "Pagi, Mas. Tumben pagi banget?"

"Tidak bisa tidur, Bu."

Bu Sari nyengir. "Deg-degan?"

"...Iya."

"Wajar, Mas." Bu Sari menyodorin segelas teh hangat. "Tapi Mas Binto pasti bisa. Saya lihat sendiri Mas Binto berubah dari pertama kali masuk sini."

Binto menyeruput tehnya. Hangat.

Jam delapan, kantor mulai penuh. Wawan sudah di meja — lebih pagi dari biasanya. Tumbler jumbo-nya penuh. Matanya melek. Dia ngerti ini hari penting. Mbak Rara juga sudah siap. *Test case*-nya sudah dicek ulang. Dua kali. Andik... baru datang. Tapi ThinkPad-nya sudah menyala. Terminal sudah terbuka. Dia sudah siap buat memantau server.

Dan Mas Alin. Di pojokan. Cangkir enamel wayangnya masih mengepul. Dia tidak berkata apa-apa. Hanya mengangguk kecil ke arah Binto.

Anggukan yang artinya: *Saya percaya.*

---

"Sebelum deploy... kita gladi resik."

Mas Alin berdiri di depan. Spidol di tangan. Kali ini bukan diagram arsitektur. Tapi... checklist.

"Gladi resik itu bukan buat memastikan tidak ada yang salah." Dia menulis. "Tapi buat memastikan... kalau ada yang salah, kamu tahu harus ngapain."

Daftar itu ditulis satu per satu: database backup ✅, staging tested ✅, semua test case lolos ✅, environment variable dicek ✅, rollback plan siap, tim siap siaga.

"Rollback plan." Mas Alin menunjuk nomor 5. "Ini paling penting. Kalau ada yang salah... kamu bisa balik ke versi sebelumnya dalam waktu lima menit. Gimana caranya?"

Binto mendemonstrasikan. Git revert ke tag sebelumnya. Database restore dari backup. Sistem kembali ke versi sebelumnya.

"Bagus." Mas Alin mengangguk. "Sekarang kamu tahu... bahkan kalau roket ini meledak... kamu bisa balik ke landasan."

---

Jam dua siang.

"Udah siap?" suara Andik dari mejanya. Grafik monitoring sudah terbuka — CPU, memory, disk, network — semua siap dipantau.

Binto menatap layarnya. Terminal terbuka. Satu perintah lagi.

```
git push production main
```

Satu baris. Delapan belas karakter. Tapi rasanya... seperti tombol peluncuran roket.

"Mas." Wawan berdiri di samping. "Santai. Dulu saya pertama deploy... sampai tangan gemeteran. Mau muntah. Tapi Mas Alin bilang: *Roket ini kamu yang bangun. Kamu yang paling tahu. Percaya sama dirimu sendiri.*"

Mbak Rara menimpali. "Testing saya sudah lolos semua. Saya jamin tidak ada bug fatal."

"Kalau ada error di server... saya sudah siap," tambah Andik. "Log sudah kebuka. Alert sudah aktif. Saya pantau."

Binto menatap mereka satu per satu.

*Aku tidak sendirian.*

Itu pemikiran yang aneh. Karena secara teknis... dia yang akan menekan tombol. Tangannya sendiri. Tapi entah kenapa... dia merasa ada empat pasang tangan lain di bahunya.

Mas Alin berdiri. Tidak mendekat. Tidak banyak bicara. Hanya mengangguk.

"Saya percaya, Le."

---

Binto mengetik.

```
git push production main
```

Enter.

Terminal mulai bergulir. `Enumerating objects... Counting objects... Compressing objects... Writing objects...` Binto menahan napas. `remote: Building... remote: Running migration... remote: Restarting server... remote: Deploy complete!`

Sunyi.

Lalu...

"BERHASIL!"

Wawan yang pertama teriak. Tumbler jumbo-nya hampir jatuh.

"Alhamdulillah..." Mbak Rara menghela napas panjang.

Andik cuma mengangguk. Tapi sudut bibirnya naik sedikit. Itu senyum paling lebar yang pernah Binto lihat dari dia.

Mas Alin... diam. Menyesap kopinya. Tapi Binto bisa lihat matanya. Ada sesuatu di sana. Sesuatu yang hangat. Sesuatu yang... bangga.

---

Binto membuka browser. Mengetik URL Koperasi Sekar Patria.

Aplikasi muncul. Versi baru. Lebih cepat. Lebih rapi. Modul-modul yang dulu terpisah... sekarang terhubung. Dia klik modul satu per satu. Anggota. Simpanan. Pinjaman. Laporan. Notifikasi.

Semua jalan.

*Aku... bikin ini. Aku deploy ini. Ini production. Dipakai orang beneran.*

Binto merasakan napasnya tertahan. Matanya tiba-tiba memanas, menatap layar yang kini memuat sebuah sistem bernyawa. Ribuan baris kode yang ia tulis berbulan-bulan, berhadapan dengan eror di tengah malam, perdebatan teknis dengan Wawan, hingga gladi resik panjang pagi ini—semuanya mengerucut pada layar di depannya. 

Ia buru-buru mengerjapkan mata dan menelan ludah lekat-lekat untuk meredam haru. Perasaan lega itu perlahan turun meluruh, menggantikan sisa-sisa adrenalin yang tadi sempat membuat jemarinya kebas. Di luar, matahari Srengat mulai merunduk membiaskan semburat jingga ke lantai paving. Angin kemarau yang tenang menyusup lewat ventilasi, menyapu peluh di dahi Binto, dan membawa serta aroma debu jalanan yang menenangkan. 

Roket itu telah meluncur dengan selamat. Dan ia masih berpijak kokoh di bumi.

---

## 13.16 Di Bawah Pohon Rambutan

Malam telah larut. Garasi kecil yang disulap menjadi kantor itu kini sudah sepi.

Wawan pulang duluan — mau jemput adiknya. Mbak Rara pamit — besok mau tes manual lagi. Andik masih di depan laptop, memantau server. Mas Alin entah ke mana.

Binto duduk di teras kantor. Di bawah pohon rambutan.

Pohon itu bergoyang pelan diterpa angin malam. Di atas sana, buah-buahnya sudah merah semua — sebagian sudah berjatuhan, siap dipanen. Puncak musim. Binto memandangnya dengan mata yang berbeda dari seminggu lalu. Mata seseorang yang baru saja meluncurkan roketnya sendiri.

"Binto."

Suara dari belakang. Bukan Mas Alin. Lebih berat. Lebih tua.

Pakde Suhar.

"Ini dia jagoan kita," katanya sambil tersenyum. Tangannya membawa dua cangkir kopi tubruk Bu Sari. Satu dia sodorkan ke Binto. Satu dia pegang sendiri.

Dia duduk di samping Binto. Di bawah pohon rambutan.

"Saya lihat tadi. Dari jendela. Kamu *deploy* sendirian."

"*Nggih*, Pakde."

"Hebat."

Satu kata. Tapi dari mulut Pakde Suhar... terasa berat. Mungkin karena Pakde jarang ngomong. Mungkin karena dia lebih sering di belakang layar. Atau mungkin karena... ada sesuatu di matanya.

"Saya dulu... juga pernah kayak kamu."

---

## 13.17 Cerita Pakde

Pakde menunjuk pohon rambutan. Batangnya yang kokoh. Cabang-cabangnya. Buahnya yang merah-ranum, lebat di antara dedaunan hijau.

"Dulu... tempat ini bukan kantor. Ini warnet. Warnet biasa. Anak-anak main Point Blank. Mahasiswa ngetik tugas. Bapak-bapak buka Facebook. Saya yang jaga."

Binto mendengarkan.

"Waktu itu saya sudah pensiun. Mantan PNS. Tapi saya lihat... IT ini masa depan. Saya mau belajar. Saya cari partner — anak muda, programmer, jago katanya. Saya percaya."

Pakde menyesap kopinya.

"Ternyata... dia nipu saya. Proyek pertama kami: sistem informasi UMKM. Saya yang cari klien. Saya yang nego. Dia yang ngerjain. Tapi waktu klien udah bayar DP... dia kabur. Bawa duitnya. Ninggalin kode yang cuma setengah jadi."

Binto terdiam.

"Saya dulu tidak ngerti IT. Tidak ngerti kode. Jadi saya tidak bisa bedain... mana programmer yang jujur, mana yang nipu. Itu yang bikin saya..."

Pakde berhenti. Menatap pohon rambutan.

"...bikin tempat ini. Garda Teknologi Nusantara. Supaya programmer tidak kayak saya dulu: ditipu. Dan supaya programmer... tidak jadi penipu."

---

Pakde menatap Binto. Matanya yang tua... ada sesuatu di sana. Bukan marah. Bukan sedih. Lebih ke... harapan.

"Saya tidak butuh programmer yang jago, Le. Saya butuh programmer yang jujur. Yang kalau salah... bilang salah. Yang kalau tidak bisa... bilang tidak bisa. Yang bisa diandalkan."

Dia menunjuk ke arah kantor. Ke meja Wawan yang berantakan. Ke laptop Andik yang masih menyala.

"Wawan itu anak SMK. Tidak kuliah. Tapi klien suka sama dia. Kenapa? Karena dia jujur. Dia tidak pernah janji muluk-muluk. Dia selalu bilang: 'Saya coba dulu ya, Pak. Kalau tidak bisa... saya bilang.'"

"Nah, itu. Itu yang saya cari."

Dia menatap Binto lagi.

"Kamu lulusan PTN top. Saya tahu. Tapi yang bikin saya bangga... bukan itu. Yang bikin saya bangga... kamu belajar dari nol. Kamu ngakuin apa yang kamu tidak tahu. Kamu terima masukan. Kamu tidak sombong."

Binto merasakan tenggorokannya tercekat.

"Itu yang penting, Le. Bukan jago. Bukan gelar. Tapi... bisa diandalkan."

---

## 13.18 Setengah Matang

Angin malam berembus. Buah rambutan yang merah-ranum bergoyang pelan.

Pakde bangkit. Menepuk bahu Binto.

"Kamu sudah jauh. Dari yang dulu... tidak tahu Git. Tidak tau deploy. Sekarang... deploy sendirian. Production."

Dia tersenyum.

"Tapi ingat, Le. Ini baru awal. Kamu masih setengah matang."

Binto mengangguk. "Saya tahu, Pakde."

"Bagus. Karena orang yang ngerasa sudah matang... biasanya busuk."

Pakde tertawa kecil. Lalu berjalan masuk ke kantor.

"Bu Sari! Kopi lagi, Le. Yang tubruk. Pahit."

---

Binto tetap duduk di bawah pohon rambutan. Menatap buah-buah merah yang bergoyang.

*Setengah matang.*

Dulu... mungkin dia akan tersinggung dibilang begitu. Dulu dia pikir gelar sarjana PTN top sudah cukup. Dulu dia pikir ijazah itu tanda kematangan.

Sekarang... dia tahu.

*Setengah matang itu... justru bagus. Berarti masih belajar. Masih tumbuh. Masih ada ruang buat jadi lebih baik.*

Dia ingat Mas Alin. Orang yang sudah hampir dua puluh tahun di dunia IT. Orang yang sudah jadi CTO startup. Dan bahkan dia... masih bilang "Saya masih belajar, Le."

*Ah. Jadi ini toh.*

*Engineer sejati... bukan yang paling tahu. Tapi yang paling sadar... betapa banyak yang belum dia tahu.*

---

Di dalam kantor, Andik masih di depan laptop. Grafik server stabil. CPU 18%. Memory 2.1 GB. Semua normal.

Di dapur, Bu Sari menyeduh kopi tubruk lagi. Satu untuk Pakde. Satu untuk Mas Alin — yang baru muncul entah dari mana. Satu lagi... untuk dirinya sendiri. Malam ini... dia butuh.

Di luar, bulan menggantung rendah di langit pekat. Di bawahnya, pohon rambutan itu bergoyang pelan tertiup angin malam yang dingin. Entah sudah berapa kali pohon rambutan itu panen. Binto juga pernah merasakannya. Dan mungkin akan merasakannya lagi di musim-musim berikutnya

Namun anehnya, sembari memeluk lutut di beranda yang mulai dingin, Binto tak lagi melihat panen rambutan sebagai titik akhir dari segalanya.

Musim panen bukanlah sebuah garis finish. Ia hanyalah sebuah perayaan kecil untuk membuktikan bahwa di bawah sana, dalam sunyi dan gelap, akar-akar pohon ini telah bekerja keras mencengkeram tanah. Dan segera setelah buah-buah ini habis dipetik, pohon itu tak lantas mati. Ia akan menggugurkan daun tuanya, memanjangkan ranting, dan menumbuhkan tunas-tunas baru. Memulai kembali fase berikutnya.

Binto tersenyum menatap bayangannya sendiri di kaca jendela kantor yang redup. *Setengah matang.* Ia mengulang kata-kata itu dalam kepalanya. 

Dulu, ia selalu berusaha keras menutupi ketidaktahuannya agar terlihat sempurna. Ia takut dianggap tidak kompeten. Namun malam ini, melihat sisa kopi bapaknya dan mengingat setiap jatuh-bangunnya di tempat ini, ia menyadari sebuah kebenaran baru: *menjadi matang berarti berhenti bertumbuh.* Buah yang telah matang sempurna, hanya memiliki satu takdir yang tersisa—menuju busuk.

Sedangkan menjadi setengah matang... itu berarti ia masih hidup. Ia masih akan belajar, masih akan berbuat salah, dan masih akan merambat tumbuh ke arah cahaya.

Ia memang masih setengah matang. Dan syukurlah, dalam dunia yang terus bergerak maju, itu adalah wujud eksistensi yang paling menjanjikan.