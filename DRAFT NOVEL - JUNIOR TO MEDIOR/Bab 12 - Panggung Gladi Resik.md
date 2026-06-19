# Bab 12: Panggung Gladi Resik

## 12.1 Tidak Bisa Tidur

Seminggu sebelum deploy.

Binto nggak bisa tidur lagi.

...

Bukan karena nggak ngantuk. Matanya udah perih dari jam sembilan. Tapi setiap kali kepala nempel bantal... otaknya malah muter.

*Load testing udah bener belum?*

*Database migration-nya udah dicek?*

*Kalau production error gimana?*

*Kalau user nggak bisa login?*

*Kalau...*

*Kalau...*

*Kalau...*

...

Dia bangkit. Nyalain lampu. Buka laptop.

Jam setengah satu malam.

...

Staging environment masih nyala. Dashboard monitoring masih kebuka. Angka-angka CPU, memory, response time — semua normal.

Tapi Binto nggak tenang.

Kayak... ada sesuatu yang kurang. Sesuatu yang dia lupa. Sesuatu yang nanti pas udah deploy ke production... baru ketauan.

*Ini cuma staging.*

*Production itu beda.*

*Traffic-nya lebih gede. Usernya lebih banyak. Error-nya lebih...*

...

Dia nutup laptop.

Tarik napas. Helaan napas panjang. Dalam. Kayak yang diajari Mas Alin.

*"Kalau udah mentok, Bin. Jangan dipaksa. Tidur. Besok lanjut lagi."*

Tapi Mas Alin nggak ngerti.

Besok... tinggal enam hari.

---

## 12.2 Pagi dan Si Anak Magang

Pagi harinya, Binto dateng dengan muka yang... yah, cukup jelasin semuanya.

Mata panda. Rambut agak acak-acakan. Ujung kemejanya — seperti biasa — kusut karena diremas.

"Waduh, Mas." Wawan nyamperin sambil bawa dua gelas kopi. "Tidur jam berapa?"

"Nggak tidur."

"Gila. Deadline masih seminggu, Mas. Santai."

...

Binto ngeliat Wawan. "Kamu bisa santai?"

"Bisa."

"Gimana caranya?"

Wawan nyengir. "Saya mah pasrah, Mas. Kalau error ya error. Namanya juga manusia. Kecuali saya robot."

"Tapi ini deploy pertama aku, Wan. Dari nol. Sendiri."

"Sendiri?"

"Ya maksudnya... backend-nya saya yang handle."

"Frontend-nya saya. QA-nya Mbak Rara. DevOps-nya Andik. Itu namanya bukan sendiri, Mas."

...

Binto diem.

...

"Kita tim, Mas. Deploy ini tanggung jawab bareng. Bukan cuma Mas Binto."

...

*Aku tau itu.*

*Tapi...*

*Kenapa rasanya tetap kayak beban di pundak aku sendiri?*

...

"Udah. Minum dulu kopinya." Wawan nyodorin gelas. "Hari ini gladi resik kan?"

"Iya."

"Nah. Gladi resik itu bukan buat ngecek kesempurnaan, Mas. Tapi buat ngecek kesiapan."

...

Binto nyeruput kopi. Pahit. Tapi entah kenapa... pas.

---

Belum sempat Binto menikmati kopinya lebih lama, Bu Sari muncul dari arah dapur. Di belakangnya, seorang anak laki-laki berbadan kurus, berkacamata tebal, membawa tas ransel lusuh penuh tempelan stiker band indie.

"Mas Binto, ini Cahyo. Keponakannya Pakde. Lagi PKL sebulan di sini."

Cahyo menyalami Binto dengan canggung. "Saya Cahyo, Mas. SMK RPL. Mohon bimbingannya."

Binto tersenyum. *Aku dulu juga kayak gini*, pikirnya. Canggung, polos, dan tidak tahu apa-apa tentang dunia kerja sesungguhnya. Bedanya, dulu Binto masuk ke perusahaan besar dan langsung diceburkan ke pekerjaan administrasi tanpa bimbingan. Cahyo lebih beruntung.

"Ini minggu ketiga kamu, ya, Dik?"

"*Nggih*, Mas. Dua minggu pertama kemarin saya masih remote dari rumah, ngerjain tugas Git sama Mas Alin. Baru minggu ini disuruh masuk kantor, terus Mas Alin bilang sekarang saya dibimbing Mas Binto."

Binto mengangguk, tapi dalam hati... *Minggu ini? Minggu deploy?*

Ia ingat Mas Alin berpesan kemarin: *"Kamu sudah cukup matang, Le. Sekarang giliranmu ngajarin orang lain. Itu bagian dari jadi medior."*

"Oke. Sekarang lagi ngerjain apa?"

Cahyo membuka laptop tuanya. "Saya diminta perbaiki tampilan laporan di modul Minimarket Kalimantan, Mas. Kemarin ada keluhan dari sales, tombol 'Cetak' di aplikasi mobile terlalu kecil."

"Itu tugas kecil tapi penting."

"Sudah selesai, Mas. Tinggal *upload*." Cahyo membuka terminal, jarinya udah siap menjalankan perintah Git untuk *push* langsung ke production.

---

## 12.3 "Jangan Langsung Production"

"Eh, Dik! Jangan! Nanti dulu!"

Cahyo terlonjak. "Lho, kenapa, Mas? Kan cuma gedein tombol?"

Binto menarik napas. *Aku tahu harus lewat staging dulu. Tapi kenapa? Apa bedanya? Selama ini aku cuma ngikutin apa kata Mas Alin tanpa benar-benar paham alasannya. Dan sekarang, ada orang yang nanya, dan aku nggak bisa jawab.*

Rasa malu itu familiar. Persis seperti hari pertamanya di kantor ini, ketika Mas Alin bertanya soal Git dan ia hanya bisa diam. Bedanya, kali ini ia bukan junior. Ia mentor. Dan mentor yang tidak bisa menjelaskan alasannya sama saja dengan guru yang cuma menyuruh hafalan.

"Anu, Dik. Harus lewat server *staging* dulu. Nanti kalau Mbak Rara sudah tes dan bilang OK, baru naik ke *production*."

"Server *staging*? Itu yang mana, Mas?"

Binto menoleh ke sudut ruangan. Di sana, sebuah PC tower tua tanpa monitor tergeletak di atas meja kecil.

"Itu lho, yang di pojok."

"Lho, Mas. Katanya itu buat program Koperasi? Yang offline itu?"

Binto terdiam. Benar juga.

"Kalau proyek Kalimantan, staging-nya di cloud, Dik," suara Mas Andik tiba-tiba dari belakang. Ia lewat sambil membawa gelas kopi. "Servernya di Jakarta. Speknya mirip production, cuma lebih kecil."

Cahyo mengangguk. "Oh, di cloud. Terus kenapa harus lewat situ dulu, Mas? Kan sama aja. Sama-sama server. Kenapa nggak langsung aja biar cepet?"

Pertanyaan sederhana itu menusuk Binto. Ia membuka mulut, tapi tidak ada kata yang keluar.

"Sebentar, Dik." Binto berdiri. "Kita tanya Mbak Rara dulu."

---

## 12.4 Panggung Gladi Resik

Mbak Rara sedang serius mengetik di laptop. Di depannya, setumpuk kertas *test case* dan pulpen warna-warni.

"Mbak, maaf ganggu."

Mbak Rara mendongak, melepas kacamatanya. "Ada apa, Mas?"

"Ini Cahyo mau langsung *deploy* ke *production*. Saya bilang jangan, harus lewat *staging* dulu. Tapi dia tanya kenapa. Saya... bingung jelasinnya."

Mbak Rara tersenyum. "Sini, Dik. Duduk dulu."

Ia mengambil selembar kertas kosong dan pulpen, mulai menggambar tiga kotak.

"Bayangin, Dik. Kamu mau pentas drama di sekolah."

Cahyo mengangguk. "Pernah, Mbak."

"Nah. Sebelum pentas beneran, kamu pasti latihan dulu di kelas, kan? Itu development. Salah ngomong nggak apa-apa. Terus, seminggu sebelum pentas, ada gladi resik di panggung asli, pakai kostum asli, lighting asli. Tapi penontonnya cuma guru dan panitia. Itu staging. Kalau ada yang salah, masih bisa diperbaiki sebelum hari H. Nah, hari H pentas di depan semua orang. Itu production. Salah dikit, malu satu sekolah."

Cahyo manggut-manggut. "Jadi staging itu gladi resik?"

"Persis. Server staging itu panggung gladi resik. Di sana aplikasi berjalan dengan konfigurasi yang sama persis seperti production — database mirip, server mirip, koneksi mirip. Aku bisa uji semua skenario di sana tanpa takut merusak data asli atau bikin pengguna bingung."

Binto mendengarkan dengan seksama. Analogi ini... membantunya sendiri memahami.

---

## 12.5 Gladi Resik: Checklist

Jam sepuluh pagi. Seluruh tim ngumpul di ruang tengah — Mas Alin, Mbak Rara, Andik, Wawan, Binto. Dan Cahyo, duduk di pojok dengan buku catatan, matanya bolak-balik dari satu orang ke orang lain.

Mas Alin berdiri di depan. "Oke. Hari ini gladi resik. Kita simulasiin proses deploy dari awal sampe akhir. Semua step harus dicek. Semua skenario harus dicoba. Termasuk worst-case scenario."

"Termasuk kalau server kebakar?" Wawan nyeletuk.

"Termasuk kalau server kebakar," Mas Alin jawab, tanpa senyum. "Saya serius. Kita harus siap."

...

Suasana berubah. Biasanya meeting di GTN selalu ada tawa. Tapi gladi resik ini... beda.

"Binto, kamu lead-nya. Silakan."

...

Binto maju. Tenggorokannya kering. Tapi dia inget kata-kata Mas Alin: *"Gladi resik itu bukan buat mastiin nggak ada yang salah. Tapi buat mastiin kalau ada yang salah, kamu tahu harus ngapain."*

"Oke. Kita mulai. Step satu: database migration. Andik?"

Andik ngangguk. "Siap. Script migration siap. Staging tested, production ready. Rollback plan juga udah ada."

"Rollback plan-nya gimana?"

"Kalau migration gagal di tengah jalan, script otomatis nge-restore backup terakhir. Downtime maksimal... sepuluh menit."

"Sepuluh menit?"

"Estimasi aman. Realistisnya lima."

...

Binto nulis di checklist: *DB migration ✓ rollback plan ✓*

"Step dua: environment variables. Semua terpisah? Production, staging, development?"

"Udah, Mas." Andik buka tabletnya. "Saya double-check tadi pagi. Nggak ada yang bocor. API keys semua pake environment variable."

...

*Good. Good.* Binto mulai ngerasa sedikit tenang. Dikit.

"Step tiga: load testing."

Mbak Rara angkat tangan. "Skenario seratus user, seribu, lima ribu. Di seribu masih aman. Response time di bawah dua detik."

"Memory?"

"Ada spike. Tapi masih dalam batas."

...

Binto nulis lagi. Tangannya udah nggak sedingin tadi.

---

## 12.6 Branching yang Benar

Mas Alin berjalan ke depan. "Sekarang saya tunjukkan alur *branching* yang benar. Ini penting, Dik — dan penting buat semuanya."

Ia membuka laptop dan mulai menggambar alur.

"Ada yang pakai cara begini: bikin branch staging, semua fitur di-merge ke staging, kalau sudah OK, staging di-merge ke production. Itu sah, tapi tidak *best practice*."

"Kenapa, Mas?" tanya Cahyo.

"Karena branch staging itu jadi 'kotor'. Isinya campuran dari banyak fitur. Suatu hari, bisa jadi ada fitur yang sudah lolos QA, tapi ditunda deployment-nya karena klien belum mau rilis. Fitur itu tetap nempel di branch staging. Begitu staging di-merge ke production, fitur yang ditunda itu ikut terbawa. Bisa kacau."

Binto membayangkan. "Wah, iya juga."

"Makanya, kami pakai cara ini." Mas Alin menggambar alur baru. "Setiap fitur baru, kita bikin branch dari PRODUCTION — biasanya main. Misal: fitur/tombol-cetak-besar. Kita kerjain di situ. Begitu mau di-test oleh Mbak Rara, branch fitur itu kita merge ke staging. Setelah Mbak Rara kasih lampu hijau, kita merge branch fitur itu LANGSUNG ke production. Bukan staging ke production."

Cahyo manggut-manggut. "Jadi staging itu cuma tempat singgah sementara?"

"Persis. Staging adalah panggung gladi resik. Setelah gladi resik selesai, pemain yang tampil di production adalah pemain yang sudah siap — bukan seluruh isi panggung."

"Ini yang namanya *clean history*," tambah Binto. "Production hanya berisi kode yang benar-benar sudah *release*. Fitur-fitur yang belum siap tidak akan mencemari production."

---

## 12.7 Skenario Terburuk

"Oke. Sekarang... worst-case scenario."

Mas Alin ngambil alih.

"Ini bagian yang paling penting. Kita harus mikir: apa hal terburuk yang bisa terjadi? Dan gimana kita nanggepinnya?"

...

"Server down?" Wawan nebak.

"Server down. Gimana, Andik?"

"Ada auto-scaling. Kalau server pertama down, server kedua langsung take over. Downtime maksimal... tiga menit."

"Tiga menit itu lama."

"Iya, Mas. Tapi itu worst-case. Normalnya di bawah satu menit."

...

"Database corrupt?" Mbak Rara.

"Backup tiap jam. Point-in-time recovery. Maksimal data loss... satu jam."

...

"User nggak bisa login?" Wawan lagi.

"Kita punya fallback authentication. Manual reset password by admin. Emergency only."

...

"Data transaksi hilang?"

Semua diem.

"Itu nggak boleh terjadi." Suara Mas Alin tegas. "Makanya, setiap transaksi harus ada log. Double entry. Sekali masuk database... harus ada di dua tempat."

...

Binto nulis. Tangannya udah bener-bener stabil sekarang.

"Oke. Satu lagi..." Mas Alin ngeliatin semua orang. "Ini bukan skenario teknis. Tapi skenario manusia."

"Maksudnya, Mas?" Mbak Rara tanya.

"Gimana kalau... di hari deploy, Binto sakit?"

Semua natap Binto.

"Atau Mbak Rara sakit. Atau Wawan. Atau saya. Gimana? Siapa yang backup siapa?"

...

Pertanyaan yang nggak pernah kepikiran.

...

"Saya..." Wawan mulai. "Kalau Mas Binto sakit, saya bisa handle backend dulu. Nggak jago-jago amat. Tapi cukup buat emergency fix."

"Kalau saya sakit," Mbak Rara nyaut, "test case saya udah didokumentasiin. Wawan bisa ngejalanin. Atau Andik."

"Kalau saya sakit," Andik ngomong pelan, "semua script deployment udah automated. Tinggal klik."

...

Dan kalau Mas Alin...?

"Kalau saya sakit," Mas Alin senyum, "kalian semua udah lebih dari cukup. Saya cuma tidur aja di rumah."

...

Tawa kecil. Tapi di balik tawa itu... ada kepercayaan.

Cahyo mencatat semuanya di buku tulisnya. Hari ini ia belajar lebih dari sekadar coding.

---

## 12.8 Deploy Bareng Cahyo

"Baik," kata Binto setelah sesi selesai. "Cahyo, sekarang kita praktik. Kamu sudah buat branch fitur?"

"Sudah, Mas. Tadi saya buat fitur/tombol-cetak-besar dari main."

"Sekarang *push* ke staging."

Cahyo menjalankan perintah Git. Beberapa saat kemudian, notifikasi muncul: *Deployment to staging successful*.

"Nah, sudah naik ke staging. Sekarang Mbak Rara coba."

Mbak Rara membuka browser, mengetik alamat staging server. Ia masuk ke aplikasi, membuka halaman laporan, dan mencoba tombol cetak.

"Tombolnya sudah lebih besar. Enak ditekan." Ia mengangguk puas.

Lalu ia membuka dari ponselnya. "Lho, ini di iPhone tombolnya bagus. Tapi di Android yang layar kecil, kok malah kepotong?"

Cahyo panik. "Waduh, saya kira aman. Tadi saya coba di laptop saja."

"Nah, ini gunanya staging," kata Mbak Rara. "Di sini aku bisa cek dari berbagai perangkat. Bayangin kalau tadi langsung production, sales yang pakai HP kecil nggak bisa pencet tombol."

Cahyo buru-buru membuka file CSS-nya. Ia tambahkan pengaturan untuk layar kecil. Commit ulang, push lagi ke branch fiturnya, merge ulang ke staging.

Mbak Rara menguji lagi. Kali ini dari tiga jenis ponsel berbeda.

"OK. Sekarang aman."

"Jadi bisa naik production, Mbak?"

"Bisa."

Binto memandu Cahyo. "Sekarang kita merge branch fiturmu langsung ke main. Bukan staging ke main." Cahyo menjalankan perintah Git. Beberapa menit kemudian, notifikasi sukses muncul.

Cahyo tersenyum lega. "Ternyata panjang juga prosesnya, Mas. Kirain tinggal upload."

"Itulah bedanya *programmer* sama *engineer*," kata Binto, mengutip Mas Alin. "*Programmer* cuma mikirin kode jalan. *Engineer* mikirin dampaknya ke pengguna."

---

## 12.9 Es Dawet Serabi

Siang itu, matahari bersinar terik. Pakde Suhar muncul dari ruangannya dengan beberapa bungkusan plastik.

"Wes, jam istirahat. Panas-panas gini enaknya yang seger-seger. Tadi aku belikan es dawet serabi."

Sorak kecil menyambut. Mbak Rara buru-buru membersihkan mejanya. Andik mengambil gelas-gelas plastik dari dapur. Pakde membuka bungkusannya: dawet hijau kenyal dalam santan kental, gula merah cair, dan es batu mulai mencair. Di bungkus terpisah, serabi hangat — kue tradisional berbahan tepung beras dan santan, siap dicocol ke kuah gula merah.

Mereka berenam — Pakde, Mas Alin, Mbak Rara, Andik, Binto, dan Cahyo — duduk mengelilingi meja panjang.

"Enak tenan iki," gumam Mas Alin.

Cahyo menyesap dawetnya. "Segar, Mas. Di sekolah nggak ada yang kayak gini."

Pakde Suhar menatap keponakannya. "Makanya, Cahyo. Kamu belajar yang bener di sini. Nggak semua tempat ngajarin kayak gini. Banyak yang langsung *production*, begitu error malah saling lempar kesalahan."

Cahyo mengangguk. Pelajaran hari ini bukan cuma soal teknis. Tapi soal *mindset*.

---

## 12.10 Malam Sebelum

Enam hari kemudian. Malam sebelum deploy.

Binto duduk di teras rumah Bapak. Sendiri.

Langit Blitar cerah. Bintang-bintang keliatan. Bulan sabit. Angin dingin.

...

Besok...

Besok adalah hari yang udah dia tunggu — dan takutin — selama tiga bulan.

Dari pertama kali dia ngerjain proyek ini. Dari first commit. Dari diskusi requirement bareng klien. Dari ratusan kali debug. Dari puluhan defect Mbak Rara. Dari malam-malam nggak tidur.

Semua... mengerucut ke besok.

...

HP-nya bergetar.

---

**Wawan** [22:30]:
Mas, udah tidur?

---

**Binto** [22:30]:
Belum. Kenapa?

---

**Wawan** [22:31]:
Nggak.
Cuma mau bilang.
Good luck buat besok.
Kita pasti bisa.

---

Binto senyum.

---

**Binto** [22:32]:
Makasih, Wan.
Kamu juga.

---

Lima menit kemudian.

---

**Mbak Rara** [22:37]:
Mas Binto.
Saya udah cek ulang test case.
Semua siap.
Besok kita tempur.

---

**Binto** [22:38]:
Siap, Mbak.
Tempur.

---

Sepuluh menit kemudian.

---

**Andik** [22:48]:
Mas, server udah saya warming up.
Harusnya nggak ada cold start besok.

---

**Binto** [22:49]:
Makasih, Dik.
Kamu emang jago.

---

**Andik** [22:50]:
Biasa aja, Mas. 😊

---

Dan terakhir...

---

**Mas Alin** [23:05]:
Bin.
Besok kamu yang lead.
Saya cuma nonton di belakang.
Percaya sama diri sendiri.
Kamu udah siap.

---

## 12.11 Saya Siap

Binto baca pesan itu berulang-ulang.

*Kamu udah siap.*

...

*Aku... udah siap?*

...

Dia inget pertama kali masuk GTN. Pertama kali liat kode Mas Alin. Merasa inferior. Merasa cumlaude-nya nggak ada artinya.

Tapi sekarang...

Dia inget analogi API sebagai kontrak. Dia inget cerita Wawan: *siapa tahu ada*. Dia inget cerita Mbak Rara: *satu kelalaian kecil*. Dia inget Mas Alin: *kode bisa nunggu, ayahmu nggak*. Dia inget bapaknya: *anak yang baik selalu inget jalan pulang*.

Semua pelajaran itu...

Bukan dari textbook. Bukan dari kampus.

Tapi dari sini. Dari GTN. Dari timnya.

...

Dia bales chat Mas Alin.

---

**Binto** [23:10]:
Siap, Mas.
Saya siap.

---

Dia naruh HP. Ngelihat langit lagi.

...

*Besok.*

*Besok aku deploy ke production.*

*Besok aku... launching.*

...

Jantungnya deg-degan.

Tapi anehnya... nggak cuma takut. Ada excitement juga.

Kayak... roller coaster. Naik pelan-pelan ke puncak. Menakutkan. Tapi di saat yang sama...

...nggak sabar pengen turun.

---

Jam tujuh pagi.

Binto udah di kantor. Padahal deploy baru jam sembilan. Tapi dia nggak bisa diem di rumah.

Kantor masih sepi. Cuma Bu Sari. Seperti biasa.

"Pagi, Mas. Tumben pagi banget?"

"Nggak bisa tidur, Bu."

Bu Sari nyengir. "Deg-degan?"

"...Iya."

"Wajar, Mas." Bu Sari nyodorin segelas teh hangat. "Tapi Mas Binto pasti bisa. Saya lihat sendiri Mas Binto berubah dari pertama kali masuk sini."

...

Binto nyeruput tehnya. Hangat.

...

Di luar, matahari mulai naik. Pohon rambutan di halaman bergoyang pelan kena angin pagi. Buahnya udah merah semua sekarang. Sebagian udah mulai berjatuhan — siap dipanen.

Dan di dalam kantor, Binto nungguin jam sembilan.

Dengan teh hangat di tangan. Dengan tim di belakangnya. Dengan satu kata di kepala:

*Siap.*
