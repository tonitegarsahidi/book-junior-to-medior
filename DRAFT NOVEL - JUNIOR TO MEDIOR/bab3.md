# **Bab 3: Waterfall, Agile, dan Sticky Notes Bebek**

## **3.1 Hantu Masa Lalu**

Hari kedua Binto di Garda Teknologi Nusantara dimulai dengan aroma kopi tubruk dan suara rintik hujan di atas genteng kodok.

Pagi ini Blitar mendung. Awan kelabu menggantung rendah di atas pohon rambutan depan kantor. Buah-buahnya yang masih hijau basah oleh gerimis, tampak lebih segar. Binto datang lebih pagi dari seharusnya—mungkin karena semangat, mungkin karena belum terbiasa dengan irama kantor desa yang santai.

Ia duduk di kursi plastik dekat jendela, menyeruput kopi pahit buatan Bu Sari. Pikirannya melayang ke masa lalu. Tepatnya, ke enam bulan paling menyiksa dalam hidupnya: Skripsi.

Dulu, ia dan teman-temannya diwajibkan menyusun proposal skripsi dengan metodologi Waterfall. Bab 1: Pendahuluan. Bab 2: Tinjauan Pustaka. Bab 3: Analisis dan Perancangan. Semua harus rinci, detail, dan yang paling penting: beku. Sekali disetujui dosen pembimbing, tidak boleh ada perubahan signifikan.

Binto ingat betul. Ia menghabiskan dua bulan pertama hanya untuk membuat *use case diagram*, *activity diagram*, dan *entity relationship diagram* yang konon katanya "penting untuk fondasi". Lalu empat bulan berikutnya *ngoding* sendirian di kos, bertarung dengan *bug* dan revisi kecil. Di akhir semester, ia mempresentasikan aplikasi manajemen inventaris berbasis desktop di hadapan dosen penguji.

"Menurut Bapak, aplikasi ini sudah *outdated*," kata salah satu dosen penguji waktu itu, sambil menatap layar laptop Binto dengan ekspresi datar. "Sekarang zamannya *mobile*. Kenapa tidak dibuat versi Android?"

Binto ingin menjawab: *"Karena di proposal yang Bapak setujui enam bulan lalu, tidak ada kata 'Android'\!"* Tapi tentu saja ia hanya bisa tersenyum pahit dan berjanji akan "menjadikan masukan".

*Enam bulan*, batin Binto. *Enam bulan kerja keras, dan akhirnya cuma jadi pajangan di rak perpustakaan. Bahkan kode-nya gak pernah dipakai siapa-siapa.*

Itulah Waterfall. Indah di atas kertas. Menyakitkan di dunia nyata.

## **3.2 Dua Proyek, Dua Nasib**

Lamunan Binto buyar ketika suara motor Mas Alin terdengar di halaman. Tidak lama kemudian, sang mentor masuk dengan jaket jeans basah dan rambut yang agak lepek kena gerimis.

"Pagi, *Le*. Tumben pagi banget," sapa Mas Alin sambil menggantung jaketnya di sandaran kursi.

"Belum bisa tidur, Mas. Kepikiran soal kode Koperasi Sekar Patria."

Mas Alin terkekeh. "Bagus. Itu tanda kamu mulai jatuh cinta sama pekerjaan. Atau mulai stress. Pilih aja."

Ia berjalan ke meja pojokannya, menyalakan monitor, lalu menoleh ke Binto. "Ngomong-ngomong soal Koperasi Sekar Patria, kamu sudah lihat *source code*\-nya?"

"Sudah, Mas. Tadi malam saya *clone* dari Git. Lumayan rapi."

"Itu proyek pertama kami yang pakai Waterfall."

Binto mengerutkan dahi. "Lho? Kirain di sini semua proyek pakai Agile, Mas. Kemarin Mas Alin cerita soal *Sprint* dan *Scrum*."

"*Iya*, sebagian besar iya. Tapi Koperasi Sekar Patria itu pengecualian." Mas Alin duduk, meraih cangkir enamel animenya yang—entah kenapa—selalu terisi kopi panas setiap pagi. "Kamu tahu kenapa?"

Binto menggeleng.

"Karena semua sudah jelas sejak awal."

Mas Alin menjelaskan. Proyek aplikasi simpan pinjam untuk Koperasi Sekar Patria itu datang dari Pak Lurah yang juga ketua koperasi. Kebutuhannya sudah sangat spesifik: ada aturan baku dari Dinas Koperasi tentang bagaimana pencatatan keuangan harus dilakukan, ada formulir-formulir standar, ada laporan bulanan yang formatnya tidak boleh diubah-ubah.

"Jadi kami tinggal eksekusi. Gak ada ruang buat 'tiba-tiba minta fitur baru' atau 'ganti alur bisnis di tengah jalan'. Kalau berubah, melanggar aturan dinas. Makanya Waterfall cocok: analisis di depan total, *ngoding*\-nya lurus, *testing* di akhir. Hemat waktu, hemat biaya, semua pihak puas."

Binto manggut-manggut. *Jadi Waterfall gak sepenuhnya jahat*, pikirnya.

"Tapi proyek Pabrik pakan ternak Garum?" Mas Alin melanjutkan. "Itu beda cerita."

## **3.3 Ketika Pabrik pakan ternak Berubah Pikiran**

Tepat saat Mas Alin menyebut nama itu, pintu depan terbuka. Wawan masuk dengan wajah kusut. Di tangannya, sebuah *tumbler* besar dan sebungkus nasi pecel.

"*Mboten* kuat, Mas," keluhnya sambil menjatuhkan diri di kursi. "Pak Bambang dari Garum *telpon* tadi subuh. Katanya fitur *inventory tracking*\-nya minta diubah. Katanya 'kurang greget'. Padahal desain UI-nya udah aku kerjain dua minggu."

Binto melirik Mas Alin, berharap melihat ekspresi frustrasi. Tapi pria itu malah tersenyum tipis.

"*Wes*, biasane ngono iku," katanya santai. "Dunia manufaktur itu dinamis, Wawan. Harga bahan baku naik-turun, permintaan pasar berubah, mesin kadang rusak. Mereka butuh aplikasi yang bisa ikut berubah."

Ia menatap Binto. "Nah, *Le*. Di sinilah Agile main. Proyek Garum itu kita kerjakan pakai Scrum. Setiap dua minggu kita *deploy* versi baru ke server *staging* mereka. Mereka coba, kasih masukan, kita ubah lagi. Gak ada istilah 'nunggu enam bulan baru kelihatan hasilnya'. Setiap dua minggu ada *progress*."

Binto mulai paham. Di kampus, ia diajari bahwa perubahan adalah musuh. *Scope creep*. Ancaman bagi *timeline*. Tapi di sini, di dunia nyata, perubahan justru dirayakan. Diantisipasi.

"Tapi Mas," Binto menyela, "kalau berubah terus, kapan selesainya?"

Mas Alin tertawa. "Pertanyaan klasik anak Waterfall. Di Agile, kita gak ngejar 'selesai' dalam arti 'aplikasi sudah sempurna dan gak akan berubah lagi'. Yang kita kejar adalah nilai. Setiap dua minggu, kita pastikan apa yang kita kirim itu sudah bisa dipakai dan berguna buat klien. Masalah nanti ada fitur tambahan? Ya sudah, masuk ke *sprint* berikutnya."

Wawan menimpali sambil mengunyah pecel. "Intinya, Mas Binto. Di sini kita *ikhlas*."

Ruangan tertawa kecil.

## **3.4 Tiga Peran di Panggung Scrum**

Binto masih penasaran. "Mas, tadi Mas Alin bilang proyek Garum pakai Scrum. Tapi Scrum itu sebenarnya apa sih? Selain *daily meeting* yang tadi pagi?"

Mas Alin meneguk kopinya, lalu mengarahkan pandangan ke arah pintu depan. "Nah, itu datang orang yang paling tepat buat jelasin."

Seorang pria berusia lima puluhan melangkah masuk. Rambutnya mulai memutih, tapi posturnya masih tegap. Wajahnya teduh ramah bersahabat. Ia memakai kaos berkerah, sebuah smart watch melingkar di tangan kanannya yang sedang memegang seikat map coklat. Ini Pakde Suhar, pemilik Garda Teknologi Nusantara.

"*Monggo*, Pakde," sapa Mas Alin membuyarkan lamunan Binto. "Ini lho, Binto lagi belajar Scrum. Mungkin Pakde bisa bantu jelasin."

Pakde Suhar tersenyum lebar. Ia meletakkan map-nya, lalu duduk di kursi dekat Binto. "Scrum itu simpel, *Le*. Cuma ada tiga peran utama. Pertama, Product Owner. Itu saya."

Binto mengernyit. "Product Owner?"

"Iya. Tugas saya cuma satu: mewakili suara klien. Saya yang ngobrol sama Pak Bambang dari Garum, atau pimpinannya Koperasi Sekar Patria. Saya yang ngumpulin *requirement*, bikin daftar keinginan, dan tentuin mana yang paling penting. Nanti daftar itu jadi Product Backlog." Ia menunjuk kolom paling kiri di papan dekat dispenser. "Itu lho, gudang ide."

Pakde Suhar melanjutkan. "Saya gak ngoding, saya gak tes. Tapi saya yang tentuin: fitur A dulu, fitur B nanti. Biar hasilnya sesuai yang diinginkan klien, dan gak buang-buang tenaga *programmer*."

Mas Alin menambahkan. "Pakde ini *jembatan*. Kalau Wawan ngamuk karena klien minta revisi aneh-aneh, Pakde yang ngerem. Kalau klien minta fitur gak masuk akal, Pakde yang negosiasi. Tanpa *Product Owner* yang kuat, tim bisa jungkir balik."

"Terus peran kedua?" tanya Binto.

"Itu saya," kata Mas Alin sambil menepuk dada. "Saya Scrum Master."

Binto menatap Mas Alin dengan ragu. "Scrum Master? Kayak *boss*-nya Scrum?"

"*Oh bukan*," Mas Alin menggeleng keras. "Secara teori, Scrum Master itu pelayan, bukan bos. Tugas utamanya memastikan proses Scrum berjalan lancar tanpa ngatur-ngatur teknis kerjaan orang. Cuma bantu hilangkan hambatan. Misal, Wawan butuh lisensi *font* yang mahal, saya bantu cari alternatif gratis. Atau kalau *daily meeting* mulai molor jadi 30 menit, saya ingetin biar balik ke 15 menit. Saya jagain ritme tim."

Mbak Rara yang sejak tadi menyimak tiba-tiba menimpali. "Mas Alin itu kayak *wasit*. Dia harusnya gak ikut main bola, cuma mastiin pertandingan adil dan gak curang."

"*Nah*, itu idealnya," Mas Alin terkekeh pelan. "Tapi di dunia nyata, apalagi di *startup* atau tim kecil kayak kita ini, peran itu sering campur aduk. Di sini saya juga merangkap jadi *Tech Lead*. Jadi ya, selain jadi wasit, kadang saya juga ikut turun tangan nendang bola, *ngoding*, sampai ngambil keputusan teknis. Praktik di lapangan sering gak sebersih buku teks, *Le*."

"Dan peran ketiga?" tanya Binto.

"Development Team," jawab Mas Alin sambil melingkarkan tangannya ke seluruh ruangan. "Itu kita semua: saya, Wawan, Mbak Rara, Mas Andik, dan sekarang kamu. Kita yang *ngoding*, *ngetes*, *ngedesign*. Kita yang ubah *sticky note* jadi kode beneran."

Pakde Suhar menambahkan. "Di Scrum, *development team* itu swakelola. Gak ada yang ngatur-ngatur detail teknis. Kalian yang paling tahu berapa lama ngerjain satu fitur. Kalian yang bagi-bagi tugas sendiri. Saya cuma kasih *prioritas*, Mas Alin cuma jagain proses. Selebihnya, kalian yang pegang kendali."

Binto merenung. Di kampus, struktur tim selalu hierarkis: ada ketua, ada anggota. Di sini, semuanya setara. Masing-masing punya peran jelas, tapi tidak ada yang merasa lebih tinggi.

## **3.5 Ritual Dua Mingguan: Sprint Planning**

Sambil menyeruput teh hangat, Binto kembali bertanya. "Terus, Mas. Gimana caranya *sticky note* di kolom Backlog bisa pindah ke To Do? Apa tiba-tiba aja?"

Mas Alin nyengir. "Nah, itu terjadi di Sprint Planning. Setiap dua minggu sekali, biasanya hari Senin pagi. Semua kumpul: Pakde, saya, Wawan, Mbak Rara, Mas Andik. Kita lihat Product Backlog—daftar fitur yang udah disusun Pakde. Lalu kita pilih mana yang mau dikerjain di *sprint* ini."

"Caranya milih gimana?"

"Pakde yang tentuin prioritas. Dia bilang, *'Fitur A harus selesai karena klien udah nunggu. Fitur B bisa nanti.'* Tapi yang menentukan berapa banyak yang bisa diambil, itu tim *development*. Kita yang bilang, *'Sanggupnya cuma 5 fitur, Pakde. Kalau 6 nanti gak kelar.'*"

Pakde sempat menambahkan satu catatan kecil. "Untuk fitur ini, pastikan datanya tidak bisa diakses sembarang orang ya."

Binto langsung menoleh. 

Mas Alin cuma mengangguk. "Iya, nanti kita masukin juga ke *acceptance criteria*."

Mbak Rara menimpali. "Nah, di sinilah pentingnya estimasi. Kita pakai *story points*—bukan jam, bukan hari. Angka relatif aja: 1 untuk gampang, 5 untuk susah. Biar kita tahu kapasitas tim."

Mas Alin menunjuk papan. "Hasil *Sprint Planning* itu ya ini: kolom To Do yang udah penuh *sticky note* terpilih. Semua orang tahu apa yang harus dikerjakan dua minggu ke depan. Gak ada lagi tiba-tiba disuruh ngerjain ini-itu di luar rencana."

Binto mengangguk paham. "Jadi *planning*\-nya cuma dua mingguan, bukan setahun?"

"*Hooh*. Karena kita tahu, dua minggu lagi dunia bisa berubah. Lebih baik rencana pendek tapi pasti, daripada rencana panjang tapi ilusi."

## **3.6 Lari Cepat 15 Menit (Daily Scrum)**

Tepat pukul 09.45, Mbak Rara berdiri dan bertepuk tangan dua kali. "Woy\! *Daily*\! Ayo kumpul\!"

Binto menoleh bingung. Wawan menghentikan kunyahannya. Mas Alin bangkit dari kursi sambil membawa cangkirnya. Bahkan Pakde Suhar, yang biasanya hanya datang siang, ikut berjalan ke arah *whiteboard*.

"*Daily Scrum*, *Le*," bisik Mas Alin. "Ikut. Berdiri aja."

Binto menurut. Ia berdiri di dekat dinding, memperhatikan.

Lima orang—Mas Alin, Wawan, Mbak Rara, Pakde Suhar, dan Mas Andik—membentuk setengah lingkaran di depan *whiteboard*. Tidak ada yang duduk. Semua berdiri.

Mbak Rara yang memandu. "Oke, *sprint* hari ke-7. Gas. Aku mulai ya."

Ia menunjuk satu *sticky note* di kolom In Progress—kertas kecil berwarna kuning dengan stiker kelinci di sudutnya. "Kemarin aku ngerjain *test case* buat fitur *login* KUD. Hari ini lanjut *testing* integrasi sama *backend*\-nya. Hambatan: *staging server* agak lemot, mungkin perlu dicek sama Mas Andik."

Rara ikut menambahkan, "Aku nanti pas testing juga coba akses tanpa login ya. Kadang yang kayak gini suka lolos."

Binto baru sadar, testing ternyata bukan cuma soal fitur jalan atau tidak.

Mas Andik mengacungkan dua jempolnya. "Mantep mbak!."

Giliran Wawan. *Sticky note* monyet. "Kemarin revisi UI Pabrik Garum, sesuai masukan Pak Bambang. Hari ini mau *finishing prototype* baru, terus serah ke Mas Alin buat di-*implement*. Hambatan: *font* yang diminta klien *license*\-nya mahal, aku cari alternatif dulu."

Mas Alin. *Sticky note* bebek. "Kemarin *debugging* modul *inventory*, udah *deploy* ke *staging*. Hari ini bantu Wawan *integrasi* UI baru. Hambatan: *Nggih* cuma satu... kopi habis."

Tawa kecil.

Pakde Suhar. "Saya kemarin follow up *invoice* Pabrik Garum, udah dibayar. Hari ini mau kirim *invoice* Koperasi Sekar Patria. Hambatan: Pak Lurah susah dihubungi. Tapi *InsyaAllah* besok ketemu."

Semua berlangsung cepat. Tidak lebih dari lima belas menit. Setelah Pakde Suhar selesai, Mbak Rara menutup dengan "Oke, lanjutkan. Semangat\!" dan semua kembali ke meja masing-masing.

Binto masih berdiri, tercengang.

"Ini... meeting atau laporan tentara? Cepat banget," tanyanya pelan ke Mas Alin.

Mas Alin nyengir. "Itu versi idealnya *Daily Scrum*. Tiap pagi, maksimal 15 menit, cuma jawab tiga pertanyaan: kemarin ngapain, hari ini ngapain, ada hambatan apa. Tujuannya murni buat sinkronisasi, bukan buat *ngalor-ngidul*."

"Terus kalau ada masalah yang butuh diskusi panjang?"

"Idealnya, ditunda setelah *daily*. Ngobrol berdua atau bertiga aja biar yang lain bisa lanjut kerja." Mas Alin menghela napas pelan. "Tapi jujur aja, *Le*, realitanya gak selalu semulus tadi. Sering kali *daily* itu molor karena tiba-tiba malah bahas *bug* dan keterusan jadi ajang *problem solving*. Kadang ada juga yang *skip* karena telat bangun atau terjebak macet. Tugas saya sebagai Scrum Master buat narik mereka balik ke relnya, walau kadang saya sendiri yang kebablasan bahas teknis."

Binto tersenyum. Di kampus, rapat proyek bisa berjam-jam, sering kali berakhir dengan *scroll* TikTok bareng. Di sini, mereka berusaha mati-matian mengejar efisiensi, sambil tetap menyadari bahwa realita tak pernah sesempurna teori di buku.

## **3.7 Papan Ajaib di Dekat Dispenser**

Setelah *daily* selesai, Binto menghampiri *whiteboard* yang tadi jadi pusat perhatian. Ia baru sadar, papan itu penuh dengan kolom-kolom vertikal yang digambar pakai spidol permanen:

| Backlog | To Do | In Progress | Testing | Done |
| :---- | :---- | :---- | :---- | :---- |

Di setiap kolom, menempel *sticky notes* warna-warni. Masing-masing punya stiker karakter lucu di sudutnya—bebek, kelinci, monyet, bunga, dan beberapa karakter lain.

"Ini Sprint Backlog," suara Mas Alin tiba-tiba di belakangnya. "Tempat kita memantau pekerjaan selama dua minggu ke depan."

Binto mendekat, membaca salah satu *sticky note* di kolom Backlog:

text

\[KUD-004\] Laporan Laba Rugi Bulanan

Mulai: (kosong)

🐤 (stiker bebek)

"KUD itu kependekan dari apa, Mas?"

"Koperasi Unit Desa. KUD-004 itu kode unik buat identifikasi fitur. Detail lengkapnya ada di Google Drive kita. Setiap *sticky note* di sini cuma ringkasan. Biar gak penuh tulisan."

Binto memperhatikan lagi. Setiap *sticky note* memang hanya berisi tiga hal: kode fitur, judul singkat, dan tanggal mulai (kalau sudah dikerjakan). Tidak lebih.

"Kenapa pakai *sticky notes* beneran, Mas? Bukannya sekarang banyak aplikasi kayak Jira atau Notion?"

Mas Alin tersenyum. "Dulu kami pakai Notion. Bahkan sempat nyoba Jira waktu ada klien dari Surabaya yang minta. Tapi..."

Ia menunjuk papan itu. "Di *retrospective*—nanti kamu akan belajar apa itu *retro*—anak-anak komplain. Katanya, kalau *online* gitu, 'kurang greget'. Mereka lebih suka lihat fisik. Lebih puas kalau bisa mindahin kertas dari In Progress ke Done pakai tangan sendiri."

"Greget?"

"*Nggih*. Ada sensasi tersendiri. Mbak Rara bilang, 'Rasanya kayak *game* menyelesaikan misi.' Wawan bilang, 'Enak dilihat, gak bikin mata kering kayak layar terus.' Lagipula," Mas Alin menunjuk ke sudut ruangan, "papan ini deket dispenser galon. Setiap kali orang mau ngisi air, dia lihat papan ini. Jadi inget terus sama pekerjaannya."

Binto nyengir. *Simple, tapi efektif*.

"Terus, kapan *sticky note*\-nya dipindah-pindah?"

"Bagus. Itu workflow kita."

Mas Alin menunjuk kolom pertama. "Backlog. Ini gudang ide. Fitur-fitur yang sudah disetujui tapi belum masuk jadwal *sprint*. Setiap awal *sprint*—setiap dua minggu sekali—kita pilih beberapa fitur dari sini, pindah ke To Do."

"Terus To Do?"

"Ini daftar pekerjaan untuk *sprint* ini. Belum dikerjakan, tapi sudah ditentukan siapa *PJ*\-nya. Lihat stikernya? Bebek itu saya. Kelinci Mbak Rara. Monyet Wawan."

"Lalu In Progress?"

"Pas kamu mulai *ngoding* atau *ngetes*, kamu pindahin ke sini. Aturan mainnya: maksimal dua *sticky note* per orang di kolom ini. Biar fokus. Jangan sampai kerjaan numpuk gak kelar-kelar."

Binto mengangguk. Masuk akal.

"Testing. Ini wilayahnya Mbak Rara. Setelah kamu selesai *ngoding*, kamu pindahin *sticky note*\-nya ke sini. Mbak Rara yang akan *test*. Kalau ada *bug*, dia lempar balik ke In Progress."

"Terakhir Done?"

"Kalau sudah lolos *testing* dan sudah di-*deploy* ke server, baru pindah ke sini. Di sinilah kita merasa jadi *pahlawan*." Mas Alin terkekeh. "Kertas di kolom Done itu yang bikin kita semangat tiap hari. Bukti nyata kalau kita gak cuma main-main."

Binto memandang papan itu lama. Di kampus, ia mengukur progres dengan *checklist* di aplikasi *notes*. Tapi ini berbeda. Ini visual. Ini kolektif. Ini... hidup.

## **3.8 Showtime: Sprint Review**

Siang menjelang, hujan sudah reda. Matahari mulai mengintip di balik awan. Tiba-tiba Pakde Suhar berjalan ke tengah ruangan dan bertepuk tangan.

"Semuanya, siap-siap. Jam 2 siang nanti kita ada Sprint Review dengan Pak Bambang dari Garum. Via Zoom."

Binto menoleh ke Mas Alin. "Sprint Review?"

"Iya. Ini ritual di akhir setiap *sprint*. Kita tunjukin hasil kerja dua minggu ke *stakeholder*. Pak Bambang lihat langsung aplikasinya, nyobain fitur baru, kasih masukan. Bukan presentasi PowerPoint, tapi demo aplikasi beneran."

"Terus kalau dia gak suka?"

"Justru itu gunanya. Masukan dari *review* jadi bahan buat *sprint* berikutnya. Dia bilang, 'Tombolnya kurang gede,' ya udah, masuk *backlog* buat *sprint* depan. Agile itu soal umpan balik cepat. Jangan nunggu aplikasi 'jadi' baru dikasih lihat. Nanti kecewa."

Jam 2 siang, seluruh tim berkumpul di depan laptop besar. Pak Bambang muncul di layar, wajahnya ramah tapi tatapannya tajam. Mas Alin memandu demo: menunjukkan fitur *inventory tracking* terbaru yang sudah direvisi sesuai permintaan dua minggu lalu.

Pak Bambang mengangguk-angguk. "Ini sudah lebih bagus. Tapi coba nanti ditambahin grafik tren stok per bulan. Biar saya tahu barang apa yang cepat habis."

Lalu Pak Bambang menambahkan dengan antusias. "Oh iya, sekalian bisa gak ditambahin fitur prediksi penjualan? Yang pakai AI gitu. Biar kelihatan canggih pas demo ke rekanan."

Binto melirik Mas Alin. Ekspresi mentor-nya tenang, tapi Binto bisa melihat alis kirinya sedikit terangkat—tanda ia sedang menahan respons.

Pakde Suhar yang justru menjawab. Suaranya ramah, tanpa sedikitpun nada menolak. "Grafik tren stok *InsyaAllah* bisa kita kerjakan di *sprint* depan, Pak Bambang. Kalau yang prediksi pakai AI, itu kita perlu riset dulu biar hasilnya bener-bener akurat. Jangan sampai prediksinya meleset, malah bikin bingung. Gimana kalau kita matangkan dulu fitur-fitur dasarnya, nanti AI-nya menyusul di tahap berikutnya?"

Pak Bambang manggut-manggut. "Iya juga ya, Pak Suhar. Yang penting dasarnya kuat dulu."

Binto tertegun. *Pakde gak bilang 'tidak'. Pakde bilang 'belum'. Dan Pak Bambang justru setuju. Ini bukan menolak. Ini mengatur ekspektasi.* Ia mencatat gaya komunikasi itu dalam hati.

Pakde Suhar cepat mencatat di buku kecilnya. "Siap, Pak Bambang. Nanti kita masukkan ke rencana *sprint* depan."

Setelah Zoom ditutup, Mas Alin menatap Binto. "Lihat? Gak ada drama. Semua jelas. Klien senang karena didengar. Tim senang karena kerjaannya dihargai."

## **3.9 Ngopi Sambil Evaluasi: Sprint Retrospective**

Usai *review*, Mas Alin mengajak Binto duduk lagi di teras depan, di bawah pohon rambutan.

"Tadi kita lihat *Sprint Review* buat *stakeholder*. Sekarang, ada satu ritual lagi yang lebih penting buat kita sendiri."

"Apa, Mas?"

"Sprint Retrospective."

Binto menunggu.

"Setiap akhir *sprint*—setelah *review*—kita ngobrol internal. Satu jam aja. Semua duduk, ngopi, dan jawab dua pertanyaan: *Apa yang berjalan baik selama sprint ini?* dan *Apa yang bisa diperbaiki?*"

"Kayak evaluasi?"

"*Nggih*. Tapi bukan buat nyalahin. Ini ruang aman. Siapa pun boleh ngomong apa pun. Dulu, gara-gara *retro* inilah kami pindah dari Notion ke *sticky notes* beneran. Gara-gara *retro* juga kami sadar kalau *daily* jam 09.30 itu kepagian buat Wawan. Makanya sekarang jam 09.45."

Binto tersenyum. "Hal-hal kecil gitu didiskusikan?"

"Justru itu intinya, *Le*. Agile itu bukan cuma soal *coding*. Agile itu soal manusia. Bagaimana kita kerja bareng tanpa bikin satu sama lain gila. *Retro* itu kayak... *service* motor rutin. Kalau gak pernah dicek, tiba-tiba mogok di jalan."

Mas Alin menyesap kopinya, lalu menatap pohon rambutan.

"Kita ini bukan cuma tukang kode, Binto. Kita ini tukang bangunan yang harus siap kalau pemilik rumah tiba-tiba minta jendela dipindah, pintu diperlebar, atau tembok dicat ulang. Waterfall itu bagus kalau pemilik rumah udah kasih gambar detail dan gak akan berubah pikiran. Tapi kalau dia masih galau? Agile jawabannya."

Binto mengangguk. Pelan-pelan, semua mulai masuk ke tempatnya.

## **3.10 Sticky Note Pertama**

Sore hari, sebelum pulang, Mas Alin memanggil Binto ke dekat papan *Backlog*.

"Sekarang giliranmu, *Le*."

"Giliran apa, Mas?"

"Menulis *sticky note* pertamamu."

Binto bingung. "Tapi saya belum ngapa-ngapain, Mas. Baru belajar Git kemarin."

"Justru itu. Tugas pertamamu sebagai *engineer* di sini adalah belajar. Itu juga pekerjaan. Jadi, tulis."

Mas Alin menyodorkan satu lembar *sticky note* kuning dan spidol hitam.

Binto berpikir sejenak. Lalu ia menulis:

text

\[KUD-000\] Pelajari Codebase Koperasi Sekar Patria

Mulai: 15 Jan

🐣 (stiker anak ayam?)

"Stikernya nanti aja," kata Mas Alin sambil tersenyum. "Besok kamu cari di toko alat tulis. Pilih karakter yang mewakili dirimu. Itu identitasmu di papan ini."

Binto menempel *sticky note* itu di kolom To Do. Rasanya aneh. Hanya secarik kertas kuning. Tapi ada kepuasan tersendiri. Seolah-olah ia baru saja menandatangani kontrak dengan dirinya sendiri.

"Ini," gumamnya pelan. "Greget."

Mas Alin tertawa. "*Nah*, mulai paham kamu."

Di luar, pohon rambutan bergoyang pelan. Buah-buahnya yang masih hijau basah oleh sisa hujan. Tapi satu dua mulai menunjukkan semburat kuning di ujungnya.

Januari belum berakhir. Dan perjalanan Binto baru saja dimulai.