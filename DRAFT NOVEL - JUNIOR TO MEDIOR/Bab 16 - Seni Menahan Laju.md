# Bab 16: Seni Menahan Laju

## 16.1 Foto Lama

Malam di Srengat selalu membawa keheningan yang panjang. Di halaman depan kantor, angin malam berembus dingin, membuat dedaunan pohon rambutan yang mulai meranggas bergesekan lambat. Sisa-sisa daun yang gugur telah menyatu dengan tanah basah, meninggalkan aroma khas yang samar di bawah temaram lampu jalan. Di dalam ruang tengah yang sunyi, Binto masih duduk di depan laptopnya, ditemani segelas teh hangat yang mulai mendingin.

Belakangan ini, Binto punya kebiasaan baru: membuka kode-kode lamanya sendiri.

Bukan untuk dibanggakan. Justru sebaliknya.

Suatu malam yang tenang, tanpa notifikasi klien dan tanpa deadline mepet, ia membuka repo lama—proyek presensi QR pertama yang dulu ia kerjakan dengan dada penuh percaya diri. Lima menit kemudian, dia menutup wajahnya sendiri.

"Ya Tuhan..." bisiknya.

Nama variabelnya `data1`, `data2`, `temp`, `result`. Satu fungsi panjang seperti kereta tanpa stasiun. Tidak ada validasi input. Tidak ada error handling. Tidak ada pagar. Pokoknya jalan.

Dan justru itu yang bikin dia tersenyum geli.

*Dulu aku nulis ini sambil merasa keren banget,* pikirnya. *Sekarang kok rasanya kayak lihat foto zaman SMP.*

Tapi rasa malu itu tidak sepenuhnya pahit. Ada sedikit bangga di sana. Kode buruk itu tetap bukti: dia pernah mulai dari titik itu. Pernah tidak tahu. Pernah asal jalan. Dan dari situlah dia tumbuh.

Sekarang dia paham, kode yang bisa jalan dan kode yang bisa diandalkan... tidak selalu hal yang sama.

---

## 16.2 Aplikasi Mulai Lemot

Pagi itu, Binto duduk di depan laptop dengan wajah sedikit mengernyit. Di layarnya, dashboard monitoring sederhana yang baru seminggu dipasang Mas Andik menampilkan grafik yang tidak biasa. Garis response time API proyek Kalimantan perlahan naik—dari biasanya 200 milidetik, kini menyentuh 800 milidetik, bahkan kadang menembus satu detik.

"Tumben," gumamnya.

Mbak Rara yang lewat membawa gelas teh hangat ikut nimbrung. "Mas Binto, kok staging-nya Kalimantan agak lemot ya? Aku tadi tes tambah pesanan, loading-nya lama. Biasanya cepet."

Binto menatap layarnya lagi. "Di production juga, Mbak. Saya barusan cek."

Belum sempat mereka berdua menyimpulkan apa-apa, Mas Alin datang dengan cangkir enamel wayangnya. "Tumben pada serius lihat grafik. Ada apa?"

"Ini, Mas. Response time API Kalimantan naik. Padahal kode gak ada yang berubah."

Mas Alin melirik dashboard, lalu duduk di kursi sebelah Binto. "Kode gak berubah, tapi bebannya berubah, *Le*."

Belum sempat Mas Alin menjelaskan lebih lanjut, Pakde Suhar muncul dari ruang depan. Wajahnya serius. "Lin, Pak Haji barusan telepon. Katanya sales-nya pada ngeluh, aplikasinya lemot. Loading lama. Ada yang sampai gagal input pesanan karena keburu *timeout*. Pak Haji bilang: '*Kalau kayak gini terus, mending balik pakai WhatsApp aja.*'"

Kalimat terakhir itu menusuk. Binto merasakan beratnya. Ini bukan sekadar grafik yang naik di dashboard. Ini soal kepercayaan klien yang bisa hilang kapan saja.

Mas Alin mengangguk tenang. "Saya paham, Pakde. Kita tangani hari ini."

## 16.3 Pertanyaan ke Mas Alin

"Maksudnya beban berubah, Mas?" tanya Binto.

"Coba ingat. Waktu kita pertama kali deploy API Kalimantan, sales-nya berapa orang?"

"Lima," jawab Binto.

"Sekarang?"

Binto terdiam. Ia teringat kabar terakhir dari Pakde Suhar: tim sales sudah dua puluh orang, dan jumlah produk di database sudah menembus puluhan ribu item. Belum lagi transaksi harian yang dulu hanya puluhan, kini mencapai ratusan.

"Dua puluh sales," kata Binto pelan. "Dan produknya udah puluhan ribu."

"Nah. Kode kita tetap. Tapi jumlah pengguna dan data bertambah. Itu namanya masalah *scaling*—bagaimana sistem kita bisa terus berfungsi dengan baik meski bebannya naik."

"Selain itu," lanjut Mas Alin. "Kalau sistemnya makin besar, yang pakai bukan cuma *user*... tapi juga orang-orang yang penasaran nyari celah."

Binto langsung teringat momen-momen *debugging* bersama Mbak Rara.

"Di *cloud* itu memang enak, tinggal *deploy*," Mas Alin menambahkan. "Tapi ingat, salah konfigurasi sedikit saja, *port* database atau *dashboard admin* bisa kebuka ke publik tanpa sadar."

Binto menelan ludah. Keamanan ternyata bukan cuma fitur yang dikerjakan sekali, tapi konsekuensi logis dari *scale*. Semakin besar sistem, semakin besar ruang serangnya.

Mbak Rara ikut duduk. "Jadi yang sekarang ini murni beban server ya, Mas? Bukan *bug*?"

"Bukan bug. Ini tanda bahwa aplikasi kita mulai serius dipakai. Dan kita harus siapkan fondasi biar gak ambruk."

## 16.4 Queue: Jangan Kerjain Semua Sekarang

Mas Alin menaruh cangkirnya. "Saya kasih contoh kecil. Waktu sales bikin pesanan, di kode kita sekarang, selain nyimpan data pesanan, kita juga langsung kirim email notifikasi ke manager. Betul?"

Binto mengangguk. "Iya, Mas. Biar manager tahu ada order baru."

"Proses kirim email itu butuh waktu. Koneksi ke server email, antrian di provider, kadang lemot. Selama email belum terkirim, sales nunggu. Respons API kita jadi lambat."

Mbak Rara menimpali. "Terus solusinya?"

"Queue. Antrian." Mas Alin menggambar di kertas. "Bayangin kasir di supermarket. Kalau setiap pembeli harus nunggu kasir membereskan belanjaan, antrian bakal panjang. Tapi kalau kasir cuma terima uang, dan ada petugas lain yang membereskan belanjaan di ujung, antrian cepat jalan."

"Itu queue?"

"*Nggih*. Pesanan masuk antrian. Ada *worker*—petugas di belakang—yang mengerjakan tugas berat: kirim email, generate PDF, update laporan. Sales langsung dapat respons 'Pesanan berhasil'. Aplikasi terasa cepat."

Binto mengangguk paham. "Jadi kita gak perlu ngerjain semua di satu waktu."

"Persis. Di Laravel, kita bisa pakai fitur *queue* dan *job*. Tinggal kirim tugas ke antrian, biar worker yang kerjakan."

## 16.5 Cache: Gudang Kecil Dekat Rumah

"Contoh kedua," Mas Alin melanjutkan. "Setiap sales buka daftar produk, kita ambil dari database. Data produk jarang berubah—harga mungkin berubah seminggu sekali, nama produk hampir gak pernah. Kenapa kita bolak-balik ke database setiap kali ada yang lihat?"

Binto membayangkan. "Iya juga. Boros."

"Makanya kita pakai cache. Ibaratnya, kita punya gudang besar di pusat kota—itu database. Tapi di dekat rumah, kita buka warung kecil yang nyimpan barang-barang yang paling sering dicari. Mau beli gula, kopi, mie instan? Gak usah ke gudang pusat. Ke warung dekat rumah aja."

Mbak Rara menimpali. "Tapi gimana kalau barang di warung belum di-update? Misal harga berubah?"

"Nah, itu *trade-off*\-nya," kata Mas Alin. "Cache itu salinan. Ada kemungkinan data di cache sedikit ketinggalan—istilahnya *stale*. Tapi untuk data yang jarang berubah, itu gak masalah. Kita bisa atur masa berlaku cache—misal 10 menit. Setelah itu, cache dihapus, ambil lagi dari database yang terbaru."

"Jadi ada plus minusnya."

"Selalu. Di dunia *scaling*, gak ada solusi tanpa konsekuensi."

Wawan yang lewat membawa gelas kopi mendengar kata "cache" dan nyeletuk. "Di *frontend* juga ada cache lho, Mas. *Browser* nyimpen gambar, CSS, JavaScript biar gak *download* ulang setiap kali buka halaman. Makanya kadang klien bilang: *'Tampilannya belum berubah, Wan!'* padahal aku sudah *update*. Itu *cache browser* yang belum *expire*. Harus suruh mereka *hard refresh* atau *clear cache* dulu."

Mas Alin mengangguk. "*Nah*. Cache itu ada di mana-mana. *Backend*, *frontend*, bahkan di *database*. Prinsipnya sama: simpan salinan biar cepat, tapi harus pintar atur kapan diperbarui."

## 16.6 Memperbesar Tiang atau Menambah Pilar

"Sekarang," Mas Alin mengambil kertas baru, "kita bahas cara bikin sistem lebih kuat. Ada dua jalur."

Ia menggambar satu kotak besar. "Vertical scaling. Artinya kita upgrade server yang sekarang. Tambah RAM, ganti CPU lebih kencang, ganti hardisk ke SSD. Ibarat punya kuda beban, kita ganti jadi kuda yang lebih besar dan kuat."

"Kelebihannya?" tanya Binto.

"Gampang. Gak perlu ubah arsitektur. Tinggal beli server lebih gede, pindahin aplikasi. Selesai."

"Kekurangannya?"

"Ada batasnya. Setinggi apa pun, kuda tetap punya batas kekuatan. Server paling mahal pun ada limitnya. Dan biayanya gak linear—begitu nyentuh batas atas, harganya melonjak gila-gilaan."

Mas Alin menggambar tiga kotak kecil sejajar. "Horizontal scaling. Kita gak ganti kuda, tapi tambah kuda. Bikin beberapa server, bagi beban ke semuanya."

"Kelebihannya?"

"Bisa terus tumbuh. Mau tambah sepuluh server? Bisa. Mau seratus? Bisa, asal arsitektur mendukung. Gak ada batas fisik seperti vertical scaling."

"Kekurangannya?"

"Kompleks. Butuh *load balancer*—alat yang membagi trafik ke server-server itu. Kode juga harus siap dijalankan di banyak server. Database juga harus dipikirkan: bagaimana kalau semua server baca-tulis ke database yang sama?"

Binto mencatat dalam hati. *Tambah kuda atau ganti kuda? Dua-duanya punya tempat.*

## 16.7 Perlahan Membagi Beban

"Ngomong-ngomong soal database," Mas Alin melanjutkan, "scaling database itu perjalanannya panjang. Tapi mulainya dari yang paling sederhana."

"Apa, Mas?"

"Vertical scaling dulu. Tambah RAM server database. Ganti ke SSD. Optimasi query—pakai index, hindari query N+1. Itu sering kali sudah cukup untuk waktu yang lama."

"Kalau masih kurang?"

"Baru pikirkan replication. Database utama buat nulis data. Database salinan—satu atau lebih—buat baca data. Jadi beban baca gak numpuk di satu server." Mas Alin menggambar panah dari satu kotak ke dua kotak lain. "Tapi ingat, replikasi ada *lag*—data di salinan mungkin sedikit terlambat. Itu *trade-off* lagi."

"Dan kalau replikasi masih kurang?"

"Sharding. Data dipotong-potong berdasarkan kriteria tertentu—misal data toko A di server 1, toko B di server 2\. Ini solusi untuk data yang sangat besar. Tapi kompleksitasnya tinggi. Aplikasi harus tahu data mana di server mana. *Join* antar shard susah."

Mas Alin menatap Binto. "Intinya: jangan langsung lompat ke sharding kalau vertical scaling atau replikasi masih cukup. Itu *over-engineering*. Buang-buang tenaga."

## 16.8 Rate Limiting: Satpam di Pintu

"Satu lagi yang jarang dipikirkan," Mas Alin menambahkan. "Rate limiting."

"Itu apa, Mas?" tanya Binto.

"Batasan jumlah request dari satu IP atau satu user dalam jangka waktu tertentu. Misal: maksimal 60 request per menit."

"Buat apa?"

"Pertama, cegah *abuse*. Ada orang iseng yang nge-spam API kita? Rate limiting bikin dia gak bisa banjiri server. Kedua—dan ini penting—lindungi form login. Orang jahat bisa coba-coba password pakai *brute force*—nyoba ribuan kombinasi password sampai ketemu. Dengan rate limiting, setelah beberapa kali gagal, IP-nya diblokir sementara. Jadi serangan gak efektif."

Mbak Rara mengangguk. "Ini penting banget buat keamanan."

"*Nggih*. Rate limiting itu benteng pertama. Banyak yang mikir ini cuma buat cegah DDoS besar. Padahal untuk hal kecil kayak *brute force* juga ampuh."

## 16.9 Jangan Pecah Rumah Terlalu Cepat

Binto teringat bacaan-bacaan online-nya. "Mas, banyak yang bilang *microservices* itu lebih baik buat scaling. Apa kita harus ubah arsitektur?"

Mas Alin tersenyum tipis. "Pertanyaan bagus. Jawabannya: belum tentu."

"Kenapa, Mas?"

"*Microservices* itu arsitektur di mana aplikasi dipecah jadi layanan-layanan kecil yang independen. Tim A urus layanan pesanan. Tim B urus layanan produk. Masing-masing bisa di-scale sendiri-sendiri. Keren, kan?"

"Tapi..."

"Tapi kompleksitasnya tinggi. Kamu harus urus komunikasi antar layanan. Harus tangani kegagalan jaringan. Harus siapin infrastruktur yang lebih rumit. Debugging lebih susah. Butuh tim yang matang dan banyak."

Mas Alin menunjuk sekeliling. "Kita tim kecil. Untuk skala kita sekarang, *monolith* yang di-*scale* horizontal—beberapa server jalankan kode yang sama—sudah lebih dari cukup."

"Jadi gak perlu buru-buru pindah?"

"*Mboten*. Jangan bongkar rumah cuma karena butuh tambah kamar. *Monolith* bukan dosa. Banyak perusahaan besar juga mulai dari *monolith* dan tetap pakai *monolith* sampai bertahun-tahun. Pindah ke *microservices* itu keputusan besar, bukan *upgrade* biasa."

## 16.10 Performance Testing: Ukur Sebelum Jebol

Mas Andik yang sedari tadi mendengarkan dari mejanya ikut bersuara. "Ngomong-ngomong soal scaling, sebelum kita nambah server, kita perlu tahu batas sistem kita sekarang."

"Maksudnya, Mas?" tanya Binto.

"Performance testing. Kita bikin simulasi beban. Misal, seratus pengguna akses bersamaan. Kita ukur responsenya. Seribu pengguna? Kita ukur lagi. Dari situ kita tahu: di titik mana sistem mulai lambat? Berapa *request per second* maksimal?"

Mas Alin menimpali. "Betul. Jangan nunggu pengguna komplain baru sadar. Ukur dulu, rencanakan scaling sebelum terlambat."

"Tools-nya?" tanya Binto.

"Banyak. Bisa pakai k6, Apache JMeter, atau Locust. Yang penting paham konsepnya."

Udara terik Blitar pelan-pelan meredup, tergantikan oleh semburat senja yang mulai melingkupi pekarangan kantor. Dari kejauhan, sayup-sayup terdengar lengkingan klakson kereta api barang yang melintas lambat menembus kota, menarik gerbong-gerbong panjang yang sarat muatan. Sebuah pengingat visual bahwa seberat apa pun beban yang ditarik, selama lokomotifnya melaju dengan ritme yang terukur, semuanya akan sampai di tujuan.

Pelajaran tentang skala dan beban hari itu terasa sangat padat dan menuntut konsentrasi tinggi. Namun anehnya, melihat rimbun dedaunan rambutan yang bergoyang pelan tertiup angin sore, pikiran Binto justru terasa jauh lebih lapang.

## 16.11 Refleksi: Tidak Ada Peluru Sakti

Sore merunduk pelan di Srengat. Binto duduk santai di teras. Pohon rambutan di depannya kini hanya tinggal rimbun dedaunan dan ranting kokoh yang berayun tenang. Musim buah memang sudah berlalu, tapi rimbun teduhnya masih setia memayungi beranda.

Mas Alin keluar membawa dua cangkir enamel. Satu kopi untuknya, satu teh untuk Binto.

"Gimana, *Le*?" tanyanya.

Binto memutar cangkirnya pelan. "Saya baru sadar, Mas... scaling itu bukan soal bikin sistem kelihatan hebat. Tapi bikin dia tetap waras waktu hidupnya makin ramai."

Mas Alin tersenyum kecil. "Nah. Itu kalimat yang lebih berguna daripada hafal sepuluh istilah." Ia menyesap kopi, lalu menambahkan, "Besok kita mulai dari yang paling masuk akal dulu. Cache. Habis itu queue. Pelan-pelan."

Binto mengangguk.

Tidak ada kalimat besar sesudah itu. Tidak ada petuah tambahan. Cuma suara sendok yang beradu tipis dengan gelas, dan angin sore yang lewat sebentar lalu hilang.

Di kepalanya, semua istilah tadi—cache, queue, replication, rate limiting, microservices—akhirnya duduk di tempat masing-masing. Bukan sebagai daftar konsep untuk dipamerkan, tapi sebagai pilihan-pilihan yang harus dipakai dengan hati-hati.

Binto menatap halaman depan yang perlahan mulai berselimut sepi. Siluet daun rambutan bergetar tipis menangkap sisa cahaya, seolah mengangguk membenarkan ritme kehidupan yang senantiasa meminta jeda.

*Menjadi lebih matang dan dewasa*, batinnya sembari meresapi hembusan napas yang mengisi penuh paru-parunya, *ternyata bukanlah perihal memaksakan diri berlari lebih kencang agar bisa mengungguli yang lain.* Membangun sistem yang bisa menampung ribuan orang bukan tentang mempercepat putaran mesin hingga terbakar, melainkan tentang membangun fondasi yang bisa menopang beban tanpa harus berteriak.

Seringkali, kedewasaan sejati—baik bagi sebuah perangkat lunak maupun seorang manusia—justru tumbuh di saat kita tahu persis kapan harus berhenti sejenak, mengambil napas panjang yang tenang, dan dengan penuh kesadaran berani menahan laju diri sendiri di tengah dunia yang terus mendesak kita untuk berlari.

---
