# Bab 3: Menari di Atas Arus yang Berubah

## 3.1 Hantu Skripsi

Hari kedua Binto di Garda Teknologi Nusantara dimulai dengan aroma pekat kopi tubruk hitam dan tabuhan rintik hujan di atas genteng kodok yang saling bersahutan.

Pagi ini Blitar berwajah muram. Awan kelabu menggantung rendah di atas pucuk dahan pohon rambutan di depan kantor, menumpahkan gerimis tipis yang membasahi buah-buah hijau kecil yang menggantung di sela dedaunan. Air hujan membuat warna hijaunya tampak lebih pekat, berkilau diterpa cahaya pagi yang samar. Binto datang lebih awal hari ini. Ia mulai memahami irama di tempat ini: kantor GTN tidak pernah terburu-buru, ia hidup perlahan dan hangat, seperti ampas kopi tubruk yang perlahan turun mengendap di dasar cangkir.

Ia duduk di kursi plastik dekat jendela, menyeruput teh hangat buatan Bu Sari.

Pagi ini, sesuatu menarik perhatiannya.

Whiteboard besar di dekat dispenser.

Dia udah lihat papan itu di hari pertama. Tapi cuma sekilas. Sekarang... dia berdiri di depannya. Memperhatikan.

Papan itu penuh coretan. Kolom-kolom vertikal yang digambar pakai spidol permanen. Di setiap kolom... tempelan kertas warna-warni. Sticky notes. Ada yang kuning. Ada yang hijau. Ada yang pink.

Masing-masing punya stiker karakter di sudutnya. Bebek. Kelinci. Monyet. Bunga. Dan satu... stiker anak ayam? Lucu.

Di atas kolom-kolom itu, ada tulisan dengan spidol hitam besar:

| Backlog | To Do | In Progress | Testing | Done |

Binto mengernyit. *Apaan nih?*

Dia membaca salah satu sticky note di kolom Backlog:

```
[KUD-004] Laporan Laba Rugi Bulanan
🐤
```

KUD? Laporan? Stiker bebek?

*Ini kantor software... atau taman kanak-kanak?*

---

Tapi sesuatu tentang papan ini... bikin dia penasaran. Ada yang rapi. Ada yang teratur. Ada yang... profesional.

Nggak kayak tugas kuliahnya dulu.

---

Pikirannya melayang ke masa lalu. Tepatnya, ke enam bulan paling menyiksa dalam hidupnya: Skripsi.

Dulu, ia dan teman-temannya diwajibkan menyusun proposal skripsi dengan metodologi Waterfall. Bab 1: Pendahuluan. Bab 2: Tinjauan Pustaka. Bab 3: Analisis dan Perancangan. Semua harus rinci, detail, dan yang paling penting: beku. Begitu disetujui di seminar proposal... nggak boleh ada perubahan signifikan. Mau sebagus apa pun ide baru yang muncul di tengah jalan. Nggak boleh.

Binto ingat betul. Ia menghabiskan dua bulan pertama hanya untuk membuat *use case diagram*, *activity diagram*, dan *entity relationship diagram*. Bulan ketiga: seminar proposal. Disetujui. Lalu empat bulan berikutnya *ngoding* sendirian di kos—bertarung dengan *bug* dan revisi kecil. Begadang. Kopi sachet. Mie instan. Nggak ada yang bantu. Nggak ada yang review.

Di akhir semester, ia mempresentasikan aplikasi manajemen inventaris berbasis desktop di hadapan dosen penguji. Bukan dosen pembimbingnya. Dosen yang baru pertama kali melihat aplikasinya hari itu juga.

"Menurut Bapak, aplikasi ini sudah *outdated*," kata salah satu dosen penguji waktu itu, sambil menatap layar laptop Binto dengan ekspresi datar. "Sekarang zamannya *mobile*. Kenapa tidak dibuat versi Android?"

Binto ingin menjawab. Ingin menjelaskan bahwa proposalnya disetujui empat bulan lalu. Bahwa saat itu "desktop" masih masuk akal. Bahwa dia nggak bisa tiba-tiba ganti platform karena... metodologinya nggak ngasih ruang buat itu. Tapi tentu saja ia hanya bisa tersenyum pahit.

*Enam bulan*, batin Binto. *Dari pengajuan judul sampai sidang. Enam bulan kerja keras... dan akhirnya cuma jadi pajangan di rak perpustakaan.*

---

*Itulah Waterfall*, pikir Binto sambil menatap papan sticky notes. *Indah di atas kertas. Menyakitkan di dunia nyata.*

Tapi papan ini... papan ini beda.

Ada apa dengan papan ini?

---

## 3.2 Dua Proyek, Dua Nasib

"Pagi, Le."

Suara Mas Alin membuyarkan lamunannya. Sang mentor baru datang. Jaket jeans-nya basah. Gerimis lagi.

"Pagi, Mas."

"Ngapain berdiri di depan papan kayak orang bingung?"

Binto nyengir malu. "Ini... saya cuma... baca-baca, Mas. Belum ngerti."

Mas Alin meletakkan cangkir enamelnya di meja. "Bagus. Berarti kamu penasaran. Orang yang penasaran itu... lebih gampang diajarin."

Dia menunjuk papan. "Itu Sprint Backlog. Tempat kita memantau pekerjaan selama dua minggu ke depan."

"Dua minggu?"

"Nggih. Itu bedanya sama skripsimu. Kamu dulu rencana enam bulan di depan kan? Dan itu pun berubah?"

Binto mengangguk pelan. *Kok Mas Alin tahu?*

"Di sini... kita cuma rencana dua minggu. Namanya Sprint. Kenapa dua minggu? Karena dua minggu lagi dunia bisa berubah. Klien bisa minta fitur baru. Pasar bisa geser. Regulasi bisa ganti. Lebih baik rencana pendek tapi pasti... daripada rencana panjang tapi ilusi."

Dia menunjuk ke luar jendela. "Koperasi Sekar Patria. Itu proyek pertama kami yang pakai Waterfall."

Binto menoleh. "Lho? Kirain di sini semua proyek pakai Agile, Mas."

"Iya. Sebagian besar iya. Tapi Koperasi Sekar Patria pengecualian. Kamu tahu kenapa?"

Binto menggeleng.

"Karena semua sudah jelas sejak awal. Pak Lurah yang juga ketua koperasi datang ke sini. Bawa map tebal. Isinya aturan baku dari Dinas Koperasi. Formulir standar. Laporan bulanan yang formatnya nggak boleh diubah. Nggak ada ruang buat 'tiba-tiba minta fitur baru'. Kalau berubah... melanggar aturan dinas."

"Jadi Waterfall cocok?"

"Cocok. Hemat waktu. Hemat biaya. Semua pihak puas." Mas Alin menyesap kopinya. "Tapi proyek Pabrik Pakan Ternak Garum... beda cerita."

Tepat saat itu, pintu depan terbuka. Wawan masuk. Wajah kusut. Di tangan kirinya, tumbler jumbo. Di tangan kanannya, sebungkus nasi pecel yang baru dibeli dari depan pasar. Ia menjatuhkan diri di kursi, meletakkan tumbler dengan bunyi gedebug, lalu mulai membuka bungkusan pecelnya—sambil tetap memasang wajah kusut.

"Mboten kuat, Mas," keluhnya, mulutnya setengah penuh sambal kacang. "Pak Bambang dari Garum nelpon Pakde Suhar kemarin sore. Katanya fitur inventory tracking-nya minta diubah. Katanya kurang greget. Pakde langsung WA aku habis subuh tadi—dikirimi screenshot coretan tangan yang difoto dari notes beliau. Tulisan tangannya miring-miring, Mas. Aku sampe mikir keras ini maksudnya apa."

Binto melirik Mas Alin. Berharap lihat ekspresi frustrasi. Tapi pria itu malah tersenyum tipis.

"Wes. Biasane ngono iku," katanya santai. "Pabrik itu dinamis, Wawan. Harga bahan baku naik-turun. Permintaan pasar berubah. Mesin kadang rusak. Mereka butuh aplikasi yang bisa ikut berubah."

Dia menatap Binto. "Nah, Le. Di sinilah Agile main. Proyek Garum kita kerjakan pakai Scrum. Setiap dua minggu kita deploy versi baru. Klien coba. Kasih masukan. Kita ubah lagi. Nggak ada istilah 'nunggu enam bulan baru keliatan hasilnya'."

"Tapi, Mas," Binto menyela. "Kalau berubah terus... kapan selesainya?"

Mas Alin tertawa. "Pertanyaan klasik anak Waterfall."

Dia meletakkan cangkirnya.

"Di Agile, kita nggak ngejar 'selesai' dalam arti 'aplikasi udah sempurna dan nggak akan berubah lagi'. Yang kita kejar... adalah nilai. Setiap dua minggu, kita pastikan apa yang kita kirim itu udah bisa dipakai. Udah berguna. Masalah nanti ada fitur tambahan? Ya udah. Masuk ke sprint berikutnya."

Wawan menimpali sambil mengunyah pecel. "Intinya gini, Mas Binto. Di sini kita... ikhlas."

Ruangan tertawa kecil.

---

## 3.3 Tiga Peran di Panggung

Pakde Suhar datang menjelang siang. Membawa map coklat tebal. Wajahnya teduh seperti biasa.

"Lho, pada ngumpul di sini?" tanyanya.

"Binto lagi belajar Scrum, Pakde," kata Mas Alin. "Mungkin Pakde bisa bantu jelasin."

Pakde Suhar tersenyum lebar. Dia meletakkan map-nya. Duduk di kursi dekat Binto.

"Scrum itu simpel, Le. Cuma ada tiga peran utama."

Dia mengacungkan satu jari. "Pertama. Product Owner. Itu saya."

"Product Owner?"

"Iya. Tugas saya cuma satu: mewakili suara klien. Saya yang ngobrol sama Pak Bambang dari Garum. Atau Pak Haji Hamid dari Kalimantan. Saya yang ngumpulin keinginan mereka. Saya yang tentuin... fitur mana yang paling penting."

Dia menunjuk kolom paling kiri di papan. "Itu Product Backlog. Gudang ide. Semua keinginan klien numpuk di situ. Bisa puluhan. Bisa ratusan."

Dua jari. "Kedua. Scrum Master. Itu Mas Alin."

Binto menatap Mas Alin. "Kayak boss-nya Scrum?"

"Oh, bukan." Mas Alin menggeleng. "Scrum Master itu... pelayan. Tugas saya mastiin semua proses Scrum berjalan lancar. Kalau Wawan butuh lisensi font yang mahal... saya bantu cari yang gratis. Kalau daily meeting mulai molor... saya ingetin biar balik ke 15 menit. Saya jagain ritme. Tapi saya nggak ngatur-ngatur kerjaan orang."

Mbak Rara yang sejak tadi menyimak tiba-tiba nimbrung. "Mas Alin itu kayak wasit. Dia nggak ikut main bola. Cuma mastiin pertandingan adil."

"Tapi di dunia nyata," Mas Alin nyengir, "peran itu sering campur aduk. Saya juga Tech Lead. Jadi selain jadi wasit... kadang saya ikut nendang bola juga."

Pakde Suhar melanjutkan. Tiga jari. "Ketiga. Development Team. Itu kalian semua. Wawan. Mbak Rara. Mas Andik. Mas Alin. Dan sekarang kamu, Binto. Kalian yang ngoding. Yang ngetes. Yang ngedesain. Yang ngubah sticky note jadi kode beneran."

"Dan yang paling penting," dia menatap Binto serius. "Development team itu swakelola. Nggak ada yang ngatur-ngatur detail teknis. Kalian yang paling tahu berapa lama ngerjain satu fitur. Kalian yang bagi-bagi tugas sendiri. Saya cuma kasih prioritas. Mas Alin cuma jagain proses. Selebihnya... kalian yang pegang kendali."

Binto merenung. Di kampus... struktur tim selalu hierarkis. Ada ketua. Ada anggota. Di sini... semua SEOLAH setara.

---

## 3.4 Menyusun Rencana Dua Pekan

Sambil menyeruput teh hangat, Binto kembali bertanya. "Terus, Mas. Gimana caranya *sticky note* di kolom Backlog bisa pindah ke To Do? Apa tiba-tiba aja?"

Mas Alin nyengir. "Nah, itu terjadi di Sprint Planning. Setiap dua minggu sekali, biasanya hari Senin pagi. Semua kumpul: Pakde, saya, Wawan, Mbak Rara, Mas Andik. Kita lihat Product Backlog—daftar fitur yang udah disusun Pakde. Lalu kita pilih mana yang mau dikerjain di *sprint* ini."

"Caranya milih gimana?"

"Pakde yang tentuin prioritas. Dia bilang, *'Fitur A harus selesai karena klien udah nunggu. Fitur B bisa nanti.'* Tapi yang menentukan berapa banyak yang bisa diambil, itu tim *development*. Kita yang bilang, *'Sanggupnya cuma 5 fitur, Pakde. Kalau 6 nanti gak kelar.'*"

Pakde sempat menambahkan satu catatan kecil. "Untuk fitur ini, pastikan datanya tidak bisa diakses sembarang orang ya."

Mas Alin cuma mengangguk. "Iya, nanti kita masukin juga ke *acceptance criteria*."

Mbak Rara menimpali. "Nah, di sinilah pentingnya estimasi. Kita pakai *story points*—bukan jam, bukan hari. Angka relatif aja: 1 untuk gampang, 5 untuk susah. Biar kita tahu kapasitas tim."

Mas Alin menunjuk papan. "Hasil *Sprint Planning* itu ya ini: kolom To Do yang udah penuh *sticky note* terpilih. Semua orang tahu apa yang harus dikerjakan dua minggu ke depan. Gak ada lagi tiba-tiba disuruh ngerjain ini-itu di luar rencana."

Binto mengangguk paham. "Jadi *planning*-nya cuma dua mingguan, bukan setahun?"

"*Hooh*. Karena kita tahu, dua minggu lagi dunia bisa berubah. Lebih baik rencana pendek tapi pasti, daripada rencana panjang tapi ilusi."

---

## 3.5 Lari Cepat Lima Belas Menit

Tepat pukul 09.45, Mbak Rara berdiri. Tepuk tangan dua kali.

"Woy! Daily! Ayo kumpul!"

Binto menoleh bingung. Wawan menghentikan kunyahannya. Mas Alin bangkit dari kursi sambil bawa cangkir. Bahkan Pakde Suhar ikut berdiri.

Binto menurut. Dia berdiri di dekat dinding. Memperhatikan.

Di atas meja rapat kayu jati, Disket—si kucing abu-abu bermata katarak juling—duduk tenang di dekat tumpukan spidol. Saat selembar *sticky note* pink bergoyang ditiup angin kipas, ia mendongak melihatnya, sebelum ia kembali melingkar tidur.

Kemarin, di hari pertamanya, dia juga melihat ritual ini. Cuma saat itu dia masih terlalu linglung—baru sejam duduk, masih shock dengan kenyataan bahwa ijazah S1-nya cuma bernilai sebungkus nasi pecel. Daily kemarin lewat begitu saja seperti kabut pagi. Hari ini, dia mulai bisa mencerna.

Lima orang — Mas Alin, Wawan, Mbak Rara, Pakde, dan satu lagi yang belum sempat dikenalkan: Mas Andik. Cowok kurus berkacamata yang duduk di pojok ruangan dekat server. DevSecOps—istilah yang baru pertama kali Binto dengar dua hari lalu.

Selama daily, Andik cuma diam. Tangannya sibuk menyilang di dada. Matanya fokus ke whiteboard, sesekali ke layar laptopnya yang penuh terminal hitam dengan teks hijau. Nggak ada yang bisa nebak apa yang ada di kepalanya.

Tapi anehnya... ketika dia bicara, semua orang berhenti dan dengar. Mungkin karena dia jarang bicara. Atau mungkin karena setiap kali dia buka mulut, selalu ada sesuatu yang berbahaya yang berhasil dia cegah.

Mbak Rara yang mulai. "Oke, sprint hari ke-7. Gas. Aku mulai ya."

Dia menunjuk satu sticky note di kolom In Progress. Kertas kuning dengan stiker kelinci. "Kemarin aku ngerjain test case buat fitur login Koperasi. Hari ini lanjut testing integrasi sama backend-nya. Hambatan: staging server agak lemot. Mungkin perlu dicek Mas Andik."

Mas Andik mengacungkan jempol. Nggak ngomong apa-apa. Cuma jempol.

Giliran Wawan. Sticky note monyet. "Kemarin revisi UI Pabrik Garum. Hari ini mau finishing prototype baru. Trus serah ke Mas Alin. Hambatan: font yang diminta klien licensenya mahal. Aku cari alternatif."

Mas Alin. Sticky note bebek. "Kemarin debugging modul inventory. Udah deploy ke staging. Hari ini bantu Wawan integrasi UI baru. Hambatan: cuma satu. Kopi habis."

Tawa kecil.

Pakde Suhar. "Saya kemarin follow up invoice Pabrik Garum. Udah dibayar. Hari ini mau kirim invoice Koperasi. Hambatan: Pak Lurah susah dihubungi."

Mbak Rara menoleh ke Binto. "Binto, mau coba setoran?"

Binto membeku. Setoran? Maksudnya laporan kayak tadi? Dia bahkan belum punya sticky note. Dia menoleh panik ke Wawan. Wawan—yang udah balik mengunyah pecel—nyenggol sikunya.

"Bilang aja lagi belajar," bisiknya, suara pelan tapi cukup keras buat bikin yang lain senyum kecil.

"Sa-ya... lagi belajar," Binto menelan ludah. "Kemarin... baca-baca codebase Koperasi. Hari ini... lanjut. Hambatan... masih banyak yang belum ngerti."

Mbak Rara manggut-manggut. "Oke, gas. Nanti tanya-tanya aja. Kita di sini saling bantu."

Semua berlangsung cepat. Nggak lebih dari lima belas menit. Setelah Pakde selesai, Mbak Rara tutup: "Oke, lanjutkan. Semangat!" Dan semua kembali ke meja masing-masing.

Binto masih berdiri. Tercengang.

"Ini... meeting atau laporan tentara? Cepet banget."

Mas Alin nyengir. "Itu Daily Scrum. Tiap pagi. Maksimal 15 menit. Cuma jawab tiga pertanyaan: kemarin ngapain? Hari ini ngapain? Ada hambatan apa?"

"Terus kalau ada masalah yang butuh diskusi panjang?"

"Ditunda. Ngobrol berdua atau bertiga aja setelah daily. Biar yang lain bisa lanjut kerja."

Mas Alin menghela napas pelan. "Tapi jujur aja, Le, realitanya gak selalu semulus tadi. Dulu pernah, Wawan nyinggung soal *bug* UI di Pabrik Garum. Terus Mas Andik nyamber bahas *query* database-nya. Terus saya ikut-ikutan buka terminal buat cek. Tau-tau udah 45 menit, yang lain pada duduk-duduk nungguin kita bertiga debat teknis."

Ia menggaruk kepalanya yang agak gondrong. "Itu salah saya. Saya yang harusnya motong diskusi, malah ikut nyemplung. Akhirnya di *retro*—nanti kamu belajar—anak-anak komplain. Mbak Rara bilang: '*Mas, kalau daily molor, test case-ku gak kelar. Nanti fiturnya telat di-review.*' Sejak itu kami belajar disiplin. Kalau ada diskusi teknis yang panjang, catat di papan, terus bahas setelah *daily* dengan yang berkepentingan aja."

Binto tersenyum. Di kampus... rapat kegiatan kemahasiswaan bisa berjam-jam. Seringkali berakhir dengan scroll TikTok bareng. Di sini, mereka berusaha mati-matian mengejar efisiensi, sambil tetap menyadari bahwa realita tak pernah sesempurna teori di buku.

---

## 3.6 Kanvas yang Berbicara

Setelah daily, Binto mendekati whiteboard lagi. Kali ini dengan pemahaman yang sedikit lebih baik.

Kolom Backlog. Gudang ide. Fitur-fitur yang udah disetujui tapi belum masuk jadwal.

Kolom To Do. Pekerjaan untuk sprint ini. Belum dikerjakan. Tapi udah ditentukan siapa yang ngerjain.

Kolom In Progress. Lagi dikerjakan. Maksimal dua sticky note per orang. Biar fokus.

Kolom Testing. Wilayahnya Mbak Rara. Dia yang test. Kalau ada bug... dilempar balik.

Kolom Done. Fitur yang udah lolos testing. Udah deploy. Aman. Inilah puncak kebahagiaan.

"Kenapa pakai sticky notes beneran, Mas?" tanya Binto. "Bukannya sekarang banyak aplikasi kayak Jira atau Notion?"

Mas Alin tersenyum. "Dulu kami pakai Notion. Bahkan sempet nyoba Jira. Tapi di retrospective — nanti kamu belajar — anak-anak komplain. Katanya... 'kurang greget'."

"Greget?"

"Nggih. Ada sensasi tersendiri. Mbak Rara bilang rasanya kayak game menyelesaikan misi. Wawan bilang... enak dilihat, nggak bikin mata kering kayak layar terus."

Dia menunjuk ke dispenser. "Lagipula... papan ini dekat galon. Setiap kali orang mau ngisi air... dia lihat papan ini. Jadi inget terus sama pekerjaannya."

Binto nyengir. Sederhana. Tapi efektif.

Di luar, gerimis yang sejak pagi mengguyur Srengat akhirnya reda, menyisakan wangi tanah basah dan dedaunan rambutan yang lembap. Matahari sore mulai mengintip tipis dari balik awan kelabu.

---

## 3.7 Sticky Note Pertama

Menjelang ashar, Mas Alin memanggil Binto.

"Sekarang giliranmu, Le."

"Giliran apa, Mas?"

"Menulis sticky note pertamamu."

Binto bingung. "Tapi saya belum ngapa-ngapain, Mas. Baru belajar Git kemarin."

"Justru itu." Mas Alin menyodorkan spidol dan satu lembar sticky note kuning. "Tugas pertamamu di sini adalah belajar. Itu juga pekerjaan. Jadi... tulis."

Binto berpikir sejenak. Lalu menulis:

```
[BIN-000] Pelajari Codebase Koperasi Sekar Patria
Mulai: 15 Jan
🐣
```

"Stikernya nanti aja," kata Mas Alin. "Besok kamu cari di toko alat tulis. Pilih karakter yang mewakili dirimu. Itu identitasmu di papan ini."

Binto menempel sticky note itu di kolom To Do.

Hanya secarik kertas kuning. Kecil. Ringan.

Tapi rasanya... ada kepuasan tersendiri. Seolah dia baru aja menandatangani kontrak. Dengan dirinya sendiri.

"Ini..." gumamnya pelan. "Greget."

Mas Alin tertawa. "Nah. Mulai paham kamu."

---

## 3.8 Pohon dan Tim

Sore itu, Binto duduk di teras depan. Sendirian. Menatap pohon rambutan yang bergoyang pelan.

Buah-buahnya masih hijau. Tapi satu dua sudah mulai menunjukkan semburat kuning di ujungnya.

Dia ingat kata-kata Mas Alin tentang pohon ini. Bagaimana batang utama bisa punya lima cabang besar. Masing-masing cabang hidup sendiri. Tapi tetap bagian dari pohon yang sama.

*Kayak tim ini*, pikirnya.

Wawan. UI/UX. Cabang paling kreatif. Bikin tampilan yang enak dilihat.

Mbak Rara. QA. Cabang paling teliti. Mastikan nggak ada yang cacat.

Mas Andik. Infra dan backend. Cabang paling teknis. Jagain server biar nggak tumbang.

Pakde Suhar. Product Owner. Cabang yang dekat sama klien. Nyambungin kebutuhan sama solusi.

Mas Alin. Tech Lead dan Scrum Master. Mungkin bukan cabang. Mungkin... batangnya?

Dan dia... Binto.

*Cabang baru. Masih kecil. Masih belajar tumbuh.*

---

Di dalam, dia masih ingat presentasi skripsinya dulu. Enam bulan kerja keras. Sendirian. Hasilnya cuma jadi pajangan di rak perpustakaan.

Di sini... dalam waktu tiga hari... dia udah lihat bagaimana tim ini kerja bareng. Bagaimana setiap orang punya peran. Bagaimana semua bergerak ke arah yang sama.

Bukan sendiri-sendiri.

Bukan single fighter.

Tapi tim.

Beneran.

---

"Mas Binto!"

Suara Wawan dari dalam. "Pulang bareng yuk. Aku laper, tadi ada yang bilang di depan pasar ada bakmi enak baru buka. Yang pake topping ayam suwir banyak itu lho."

Binto bangkit. Meraih helm-nya. Melirik pohon rambutan sekali lagi. Perutnya ikut keroncongan—baru sadar dari tadi cuma isi kopi tubruk.

*Aku belum ngerti semuanya*, pikirnya. *Masih banyak yang harus dipelajari.*

*Tapi... setidaknya sekarang aku tahu... kerja itu nggak harus sendirian.*

Dia menyalakan motor.

Dan entah kenapa... hari ini rasanya lebih ringan dari kemarin.

Mungkin karena di papan itu... di kolom To Do... ada satu sticky note dengan namanya.

Kecil. Kuning. Masih kosong stikernya.

Tapi itu punyanya.

Di perjalanan pulang, Binto nggak bisa berhenti mikir. Tentang Agile. Tentang Scrum. Tentang sticky notes dan daily meeting dan sprint.

*Dulu aku pikir... bikin software itu cuma soal ngoding bener*, pikirnya.

*Ternyata... banyak banget yang aku nggak tahu.*

*Ternyata... ada cara kerja tim yang bikin semuanya lebih teratur. Lebih jelas. Lebih... manusiawi.*

---

═══

Beberapa hari telah berlalu.

Blitar memasuki minggu kedua Januari. Pohon rambutan di depan kantor mulai menunjukkan lebih banyak semburat kuning di ujung buahnya.

Binto sudah tidak lagi datang kepagian. Ritme kantor sudah mulai ia pahami: kopi tubruk pagi, daily jam 09.45, kode dan diskusi sampai ashar. Sticky note kuningnya—[BIN-000] dengan stiker anak ayam yang ia beli di toko alat tulis dekat pasar—sudah berpindah dua kali: dari To Do ke In Progress, lalu ke Done. Ia sudah membaca seluruh codebase Koperasi Sekar Patria. Sudah mulai paham bagaimana Mas Alin menyusun kode. Sudah mulai berkontribusi di bug-bug kecil.

Hari ini, sesuatu yang berbeda.

## 3.9 Showtime: Sprint Review

Pagi itu, Pakde Suhar bertepuk tangan. "Semuanya. Jam 2 siang nanti kita ada Sprint Review dengan Pak Bambang dari Garum. Via Zoom."

Binto menoleh ke Mas Alin. "Sprint Review?"

"Iya. Ini ritual di akhir sprint. Kita tunjukin hasil kerja dua minggu ke klien. Pak Bambang lihat langsung. Nyobain fitur baru. Kasih masukan. Bukan presentasi PowerPoint... tapi demo aplikasi beneran."

"Terus kalau dia nggak suka?"

"Justru itu gunanya. Masukan dari review jadi bahan buat sprint berikutnya. Dia bilang, 'Tombolnya kurang gede.' Ya udah. Masuk backlog. Sprint depan dikerjain. Agile itu soal umpan balik cepat."

Jam 2 siang, seluruh tim berkumpul di depan laptop besar. Pak Bambang muncul di layar. Wajahnya ramah. Tapi tatapannya tajam.

Mas Alin yang demo. Nunjukin fitur inventory tracking terbaru.

Pak Bambang mengangguk-angguk. "Ini udah lebih bagus. Tapi coba nanti ditambahin grafik tren stok per bulan ya. Biar saya tahu barang apa yang cepat habis."

Lalu dia tambahin. "Oh iya, sekalian bisa nggak ditambahin fitur prediksi penjualan? Yang pakai AI gitu. Biar keliatan canggih pas demo ke rekanan."

Binto melirik Mas Alin. Ekspresi mentornya tenang. Tapi alis kirinya sedikit terangkat. Tanda dia lagi nahan respons.

Pakde Suhar yang menjawab. Suaranya ramah. "Grafik tren stok InsyaAllah bisa kita kerjakan sprint depan, Pak Bambang. Kalau yang prediksi pakai AI... itu kita perlu riset dulu. Biar hasilnya akurat. Gimana kalau kita matangkan fitur dasarnya dulu. AI-nya menyusul?"

Pak Bambang manggut-manggut. "Iya juga ya. Yang penting dasarnya kuat dulu."

Binto tertegun. *Pakde nggak bilang 'tidak'. Pakde bilang 'belum'. Dan Pak Bambang justru setuju.*

Ini bukan menolak. Ini mengatur ekspektasi.

---

## 3.10 Ngopi Sambil Evaluasi

Setelah Zoom ditutup, Mas Alin mengajak Binto ke teras depan. Di bawah pohon rambutan.

"Tadi kamu lihat Sprint Review. Sekarang ada satu ritual lagi yang lebih penting."

Binto menunggu.

"Sprint Retrospective."

"Apa itu, Mas?"

"Setiap akhir sprint — setelah review — kita ngobrol internal. Satu jam aja. Semua duduk. Ngopi. Dan jawab dua pertanyaan: *Apa yang berjalan baik selama sprint ini?* Dan *Apa yang bisa diperbaiki?*"

"Kayak evaluasi?"

"Nggih. Tapi bukan buat nyalahin. Ini ruang aman. Siapa pun boleh ngomong apa pun." Mas Alin menyesap kopinya. "Dulu, gara-gara retro inilah kami pindah dari Notion ke sticky notes beneran. Gara-gara retro juga... kami sadar daily jam 08.30 itu kepagian buat Wawan. Makanya sekarang jam 09.45."

Binto tersenyum. "Hal-hal kecil kayak gitu didiskusiin?"

"Justru itu intinya, Le. Agile bukan cuma soal coding. Agile itu soal manusia. Gimana kita kerja bareng... tanpa bikin satu sama lain gila. Retro itu kayak service motor rutin. Kalau nggak pernah dicek... tiba-tiba mogok di jalan."

Dia menatap Binto serius. "Tapi ada satu aturan sakral. Kamu nggak boleh nyalahin orang. Nggak boleh bilang: 'Wawan lambat ngerjain UI.' Yang boleh: 'Proses serah terima dari desain ke kode sering molor. Mungkin kita butuh checklist.' Fokus ke proses. Bukan ke orang."

Binto mengangguk. Dia ingat rapat kegiatan kemahasiswaan di kampus dulu. Kalau ada yang salah... selalu ujungnya saling tunjuk.

"Mungkin karena nggak ada aturan kayak gini," gumamnya.

---

Angin sore berhembus lembut, membawa serta aroma samar sisa hujan dari dedaunan. Pohon rambutan di depan mereka bergoyang pelan, mempertontonkan satu dua buahnya yang mulai menunjukkan semburat kuning di antara rimbun hijau.

"Kita ini bukan cuma tukang kode, Binto," kata Mas Alin, suaranya mengalun tenang menyamai ritme sore. "Kita ini tukang bangunan. Yang harus siap kalau pemilik rumah tiba-tiba minta jendela dipindah. Pintu diperlebar. Tembok dicat ulang."

"Waterfall itu bagus... kalau pemilik rumah udah kasih gambar detail dan nggak akan berubah pikiran."

"Tapi kalau dia masih galau?"

"Agile jawabannya."

Binto mengangguk. Pelan-pelan, seperti sisa tetes hujan yang mendarat lembut dari genteng ke genangan air, semua konsep itu mulai masuk ke tempatnya. Rencana yang pendek, ritme yang luwes, dan kerendahan hati untuk terus beradaptasi.

---
