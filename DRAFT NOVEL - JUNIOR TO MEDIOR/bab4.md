# **Bab 4: Perjalanan Sebuah Tombol**

## **4.1 Telepon dari Kalimantan**

Pagi itu, kantor Garda Teknologi Nusantara masih lengang. Hanya suara kipas angin Ufo yang berputar pelan dan aroma kopi tubruk dari dapur kecil. Binto datang lebih awal—entah karena semangat atau karena belum terbiasa tidur setelah subuh seperti orang Blitar pada umumnya.

Ia duduk di kursi plastik dekat jendela, menatap pohon rambutan di depan. Buahnya masih hijau, tapi satu dua sudah mulai menunjukkan semburat kuning di ujungnya. *Tinggal nunggu waktu*, pikir Binto.

Tiba-tiba, suara dering telepon kantor memecah keheningan. Bu Sari yang baru saja datang mengangkatnya.

"Garda Teknologi Nusantara, selamat pagi... Oh, Pak Haji Hamid\! *Nggih*, *nggih*... Sebentar, saya sambungkan ke Pakde Suhar."

Binto menajamkan telinga. *Pak Haji Hamid?* Itu klien minimarket dari Balikpapan yang sering disebut-sebut Mas Alin. Klien satu-satunya dari luar Jawa.

Tidak lama kemudian, Pakde Suhar muncul dari ruang depan. Wajahnya serius, tangannya masih memegang ponsel yang menempel di telinga.

"*Nggih*, Pak Haji. *Monggo*... Fitur cetak laporan harian? *Nggih*, bisa... Besok lusa? *Waduh*, mepet *nggih*... Tapi *InsyaAllah* kita usahakan... *Nggih*, untuk calon investor? *Alhamdulillah*, selamat... *Nggih*, nanti saya kabari lagi."

Pakde menutup telepon, menghela napas panjang, lalu menatap sekeliling ruangan. Mas Alin baru saja datang, masih dengan jaket jeans basah karena gerimis pagi. Wawan menyusul di belakangnya, membawa *tumbler* besar dan bungkusan nasi pecel seperti biasa.

"Ada apa, Pakde?" tanya Mas Alin sambil menggantung jaketnya.

Pakde Suhar berjalan ke tengah ruangan. "Pak Haji Hamid dari Balikpapan. Dia minta fitur cetak laporan penjualan harian. *Deadline*\-nya besok lusa. Katanya mau didemoin ke calon investor."

Wawan nyaris tersedak pecelnya. "Besok lusa?\! Gila, Pakde. Itu kan mepet banget."

Mas Alin tidak langsung bereaksi. Ia berjalan ke meja pojokannya, menyalakan monitor, lalu menyeruput kopi dari cangkir enamel wayangnya. "Prioritas, Pakde. Kalau kita ambil ini, harus ada yang dikorbankan."

Pakde mengangguk. Ia sudah menduga pertanyaan itu. "Iya, saya paham. Makanya saya mau diskusi dulu sama kalian."

## **4.2 Rapat Kilat di Depan Papan**

Seluruh tim berkumpul di depan *whiteboard* dekat dispenser. Papan itu masih penuh dengan *sticky notes* warna-warni—bekas *Sprint Planning* awal pekan. Di kolom In Progress, ada beberapa kertas: punya Wawan (revisi UI Pabrik Garum), punya Mbak Rara (testing fitur Koperasi), dan punya Mas Alin sendiri.

Mas Alin menunjuk satu *sticky note* di kolom In Progress dengan stiker bebek: \[MMK-010\] Optimasi Query Stok.

"Ini pekerjaan saya untuk minggu ini. Optimasi *query* laporan stok minimarket Kalimantan. Sebenarnya penting, tapi tidak *urgent*. Kalau kita butuh *slot* kosong, saya rela ini dipindah balik ke Backlog."

Pakde Suhar menatap Mas Alin. "Yakin, Lin? Ini kan sudah setengah jalan."

"Baru mulai analisis, Pakde. Belum ada kode yang ditulis. Aman." Mas Alin tersenyum. "Lagipula, kalau Pak Haji dapat investor baru, itu bagus buat kita juga. Siapa tahu dia tambah cabang, kita tambah proyek."

Pakde Suhar manggut-manggut. "Baik. Kalau gitu, MMK-010 kita tunda. Fitur cetak laporan harian kita masukkan ke *sprint* ini." Ia menatap Binto. "Binto, kamu ikut bantu Mas Alin di fitur ini ya. Biar sekalian belajar *flow*\-nya."

Binto mengangguk cepat. "Siap, Pakde."

Dalam hati, ia gugup. *Ini pertama kalinya gue ngerjain fitur beneran. Bukan tugas kuliah. Dipakai orang beneran. Dan deadlinenya besok lusa.*

## **4.3 Dari Obrolan ke Kertas Kecil**

Setelah rapat kilat, Mas Alin, Binto, dan Wawan duduk mengelilingi meja panjang. Pakde Suhar berdiri di dekat mereka, tangannya memegang buku catatan kecil.

"Jadi gini," Pakde memulai. "Pak Haji butuh tombol di halaman laporan. Dia bisa pilih tanggal, klik cetak, lalu keluar PDF yang siap print. Biar pas demo keliatan profesional."

Wawan mengangguk. "Aku bisa bantu bikin *layout* PDF-nya. Biar gak polos-polos amat. Ada logo minimarket, alamat, garis-garis rapi."

Mas Alin menatap Pakde. "Formatnya PDF atau *thermal print* langsung? Karena di minimarket biasanya pakai printer *thermal* buat struk."

Pakde berpikir sejenak. "PDF saja. Soalnya ini buat demo ke investor. Bukan buat operasional harian. Nanti kalau sudah deal, baru kita pikirkan *thermal print*."

"Data yang ditampilkan per hari atau per *shift*?" tanya Mas Alin lagi. "Karena minimarket biasanya buka 24 jam, tapi *shift* kasir ganti-ganti."

"Per hari dulu. Yang penting total penjualan tanggal itu."

Mas Alin mencatat di buku kecilnya. "Satu lagi, perlu logo minimarket di PDF? Atau cukup kop teks saja?"

Pakde tersenyum. "Logo. Pasti. Investor kan lihat *branding*."

Binto hanya mendengarkan. Pikirannya sibuk mencerna. *Gue kira cuma "bikin tombol cetak". Ternyata banyak banget yang harus dipikirin.*

Tapi yang lebih menarik perhatiannya bukan jawaban-jawabannya, melainkan pertanyaan-pertanyaannya. *Pakde gak nanya "mau fitur apa". Mas Alin gak nanya "pakai teknologi apa". Mereka nanya: buat siapa, kapan dipakainya, apa yang mau dicapai, dan seperti apa konteks penggunanya.* Pertanyaan-pertanyaan yang tidak pernah Binto pikirkan ketika mengerjakan tugas kuliah.

Mas Alin seolah membaca pikirannya. "Inilah bedanya bikin fitur buat tugas kuliah sama buat klien beneran, *Le*. Di kampus, dosen cuma nilai 'fungsinya jalan apa enggak'. Di sini, kita harus mikirin siapa yang pakai, buat apa, dan gimana *experience*\-nya."

## **4.4 Menulis Tiket Sisipan**

Mas Alin bangkit, mengambil satu lembar *sticky note* kuning dari tumpukan dekat papan. Ia menulis dengan spidol hitam:

text

\[MMK-012\] Cetak Laporan Penjualan Harian

Mulai: 17 Jan

🐤 (stiker bebek)

"Kode MMK itu Minimarket Kalimantan," jelas Mas Alin sambil menempel *sticky note* di kolom To Do. "Nomor 012 karena ini fitur kedua belas yang kita kerjain buat mereka."

Binto memperhatikan. "Terus detailnya di mana, Mas? Kan di *sticky note* cuma judul."

Mas Alin kembali ke mejanya, membuka laptop. "Kita simpan di Google Drive. Namanya PRD—*Product Requirement Document*. Simpel aja."

Ia membuka file baru di Google Docs, lalu mulai mengetik. Binto melihat di layar:

---

MMK-012: Cetak Laporan Penjualan Harian

Deskripsi:  
Pengguna dapat mencetak laporan penjualan harian dalam format PDF untuk keperluan dokumentasi dan presentasi.

Acceptance Criteria:

* Pengguna dapat memilih tanggal dari *date picker*  
* Sistem menampilkan data penjualan tanggal tersebut (total transaksi, total item, total pendapatan)  
* Tombol "Cetak" tersedia dan berfungsi  
* PDF yang dihasilkan memuat logo minimarket, tanggal laporan, dan ringkasan data  
* Format tanggal di PDF sesuai dengan pilihan pengguna

Prioritas: High (mendadak, *deadline* 19 Jan)

PJ: Alin, Binto (Wawan bantu desain PDF)

---

"*Acceptance criteria* ini penting," kata Mas Alin. "Ini jadi patokan kapan fitur dianggap 'selesai'. Kalau semua kotak sudah centang, baru boleh pindah ke Testing."

Binto mengangguk. *Ini rapi banget. Gak kayak tugas kelompok gue dulu yang cuma modal "nanti aja lihat jadinya".*

"Tapi gak semua *acceptance criteria* sama, *Le*," Mas Alin menambahkan. Ia membuka kembali laptopnya dan mengetik cepat. "Coba lihat ini."

Ia menunjukkan dua versi *acceptance criteria* di layar:

Versi buruk (yang sering saya temui di lapangan):
* Sistem bisa cetak laporan
* Laporan bisa dilihat user
* Desain rapi

"Lihat? Ini terlalu umum. 'Bisa cetak laporan' — cetak dari mana? Format apa? Data apa yang muncul? 'Desain rapi' — rapi menurut siapa? Ini subjektif. Nanti Mbak Rara test, dia bilang belum rapi. Kamu bilang udah rapi. Debat gak jelas."

Versi baik (yang kita tulis):
* Pengguna dapat memilih tanggal dari *date picker*
* Sistem menampilkan data penjualan tanggal tersebut (total transaksi, total item, total pendapatan)
* Tombol "Cetak" tersedia dan berfungsi
* PDF yang dihasilkan memuat logo minimarket, tanggal laporan, dan ringkasan data

"Lihat bedanya, *Le*. *Acceptance criteria* yang baik itu spesifik dan *testable*. Bisa diuji dengan jelas: 'Apakah logo muncul? Ya atau tidak.' Bukan 'Apakah desainnya bagus?' — itu pertanyaan yang gak akan selesai-selesai."

Binto memperhatikan perbedaan itu. "Jadi *acceptance criteria* itu kayak kontrak kecil, Mas? Hitam di atas putih, gak bisa debat?"

"Persis. Semakin jelas kontraknya, semakin sedikit drama antara *developer*, QA, dan klien. Semuanya punya ekspektasi yang sama."

Binto merenung lagi, lalu bertanya: "Mas, ini namanya PRD ya? Saya sering dengar juga istilah *user story*. Beda gimana?"

Mas Alin tersenyum. "Pertanyaan bagus. PRD itu dokumen lengkap satu fitur — kayak yang barusan kita tulis. Ada deskripsi, *acceptance criteria*, prioritas, penanggung jawab. Cocok buat proyek yang kliennya butuh kepastian dan kontrak jelas — kayak klien-klien kita di GTN."

Ia mencondongkan badan. "*User story* lebih ringkas. Formatnya cuma satu kalimat: 'Sebagai [pengguna], saya ingin [fitur], supaya [manfaat].' Contoh: 'Sebagai pemilik minimarket, saya ingin mencetak laporan penjualan harian, supaya bisa presentasi ke investor.' Itu aja. Detailnya nanti didiskusikan saat *Sprint Planning*."

"Jadi PRD lebih formal, *user story* lebih fleksibel?"

"*Nggih*. Di GTN kita pakai PRD karena klien kita rata-rata orang bisnis biasa — mereka butuh dokumen yang jelas, bisa dibaca ulang, bisa jadi pegangan kalau ada dispute. Di *startup* produk, biasanya mereka pakai *user story* karena timnya lebih kecil, lebih sering diskusi, dan produknya berubah cepat."

Binto mengangguk paham. *Dunia software engineering ternyata gak cuma ngoding. Ada seni nulis spesifikasi juga.*

## **4.5 Ngoding Cepat tapi Rapi**

Setelah PRD disetujui Pakde, Mas Alin membuka terminal.

"Kita mulai. Saya bikin *branch* baru dari main."

bash

git checkout \-b feature/MMK-012

"*Branch* ini khusus buat fitur cetak laporan. Kamu nanti *ngoding* di sini. Jangan langsung di main, bahaya."

Binto membuka laptopnya, melakukan git pull dan git checkout ke *branch* yang sama. Mereka mulai bekerja.

Mas Alin mengambil bagian *backend*: menulis *endpoint* API baru untuk mengambil data penjualan berdasarkan tanggal. 

"Tanggalnya dari input user kan?" tanya Mas Alin.

Binto mengangguk.

"Jangan langsung kamu tempel ke query. Minimal validasi dulu. Yang kayak gitu bisa jadi pintu masuk SQL Injection kalau gak hati-hati."

"Oh ya," tambah Mas Alin lagi, "Pastikan juga endpoint ini cuma bisa diakses user yang berhak. Jangan sampai orang lain bisa lihat laporan toko cuma karena tahu URL-nya."

Binto mencatat itu dalam hati. Ia lalu kebagian menulis logika untuk menghasilkan PDF dari data tersebut. Wawan sibuk di laptopnya, membuat *template* HTML sederhana dengan CSS yang akan dikonversi jadi PDF.

"*Commit* yang kecil-kecil, *Le*," Mas Alin mengingatkan. "Jangan nunggu semua selesai baru di-*commit*. Nanti susah *tracking*\-nya kalau ada masalah. Dan satu lagi — *commit message*\-nya yang jelas."

Binto menuruti. Setiap kali satu fungsi kecil selesai, ia mengetik:

bash

git add .

git commit \-m "feat: tambah endpoint API /api/laporan/penjualan"

git commit \-m "feat: buat struktur dasar PDF dengan header logo"

git commit \-m "feat: integrasi template HTML dari Wawan ke PDF generator"

Mas Alin mengangguk melihat pesan *commit* Binto. "Nah, ini sudah lebih baik dari kemarin. Lihat polanya? Awalan 'feat:' buat fitur baru. Nanti kalau ada perbaikan *bug*, pakai 'fix:'. Kalau ada perubahan yang gak nambah fitur tapi memperbaiki struktur kode, pakai 'refactor:'. Ini namanya *conventional commits*."

Binto memperhatikan. "Jadi kayak label gitu ya, Mas?"

"Persis. Bayangin beberapa bulan lagi kita lihat `git log`. Dengan label ini, kita langsung tahu *commit* mana yang nambah fitur, mana yang perbaikan bug, mana yang bersih-bersih kode. Tanpa harus baca detail isinya satu per satu. Ini kebiasaan kecil yang dampaknya besar."

Rasanya berbeda dengan cara lamanya dulu. Dulu ia hanya *copy-paste* folder kalau mau *backup* — itupun dengan nama folder `Project_Backup_12_Juni_FINAL_REV2_FIX`. Sekarang setiap langkah tercatat rapi dengan label yang jelas.

Sekitar pukul dua siang, fitur sudah mulai terbentuk. Di layar Binto, sebuah file PDF sederhana berhasil di-generate. Ada logo minimarket, tanggal, tabel data penjualan, dan total.

"Wah, lumayan," Wawan melirik. "Nanti tak kasih *padding* dikit biar gak mepet."

## **4.6 Pull Request: Kenapa Gak Bisa Langsung Merge?**

Menjelang sore, semua kode sudah selesai. Binto merasa lega.

"Langsung gabung ke main aja, Mas?" tanyanya sambil membuka Git di terminal.

Mas Alin menggeleng sambil tersenyum. "*Mboten*. Coba aja sendiri. Ketik git push."

Binto mengetik git push origin feature/MMK-012. Kode terkirim ke GitHub. Lalu ia mencoba pindah ke *branch* main dan mengetik git merge feature/MMK-012.

Error.

*"You don't have permission to merge to 'main'. Request a pull request."*

Binto menatap layar dengan bingung. "Lho? Kok gak bisa?"

Mas Alin terkekeh. "Karena kamu belum punya akses *maintainer*. Itu sengaja. Di tim yang sehat, gak semua orang bisa langsung *merge* ke main. Harus lewat Pull Request dan *review* dulu."

Ia mendekat ke laptop Binto, membuka GitHub di browser. "Sini, saya tunjukin caranya."

Mas Alin mengklik tombol New Pull Request, memilih *branch* feature/MMK-012 sebagai sumber, dan main sebagai target. Di halaman PR, ia mulai mengetik deskripsi. Binto memperhatikan dari samping.

"Deskripsi PR itu penting, *Le*. Ini yang pertama kali dilihat *reviewer* sebelum buka kode kamu," kata Mas Alin sambil terus mengetik. "PR yang baik itu kasih konteks. Gak cuma judul 'Tambah fitur cetak laporan'."

Ia menunjukkan dua versi deskripsi yang ditulisnya:

text
### Deskripsi Singkat (Buruk):
Tambah fitur cetak laporan.

### Deskripsi Singkat (Baik):
## Apa yang dikerjakan
- Menambahkan endpoint API `/api/laporan/penjualan` untuk mengambil data penjualan berdasarkan tanggal
- Membuat PDF generator dengan logo minimarket dan ringkasan data
- Menambahkan validasi tanggal (format Y-m-d)

## Kenapa
Untuk demo ke calon investor Pak Haji Hamid

## Cara testing
1. Buka halaman laporan
2. Pilih tanggal, klik Cetak
3. PDF harus muncul dengan logo dan data yang sesuai
4. Coba tanggal 29 Februari 2024 (tahun kabisat)

"Lihat bedanya? Deskripsi baik langsung kasih tahu *reviewer* apa yang harus dicek, kenapa fitur ini dibuat, dan bagaimana cara mengetesnya. *Reviewer* gak perlu nebak-nebak. Kalau semua PR ditulis kayak gini, tim gak buang-buang waktu."

Binto mengangguk. *Ternyata nulis deskripsi PR juga ada seninya. Bukan sekadar "ini lho kode gue, review ya."*

Mas Alin menekan Create Pull Request.

"Nah, sekarang PR sudah dibuat. Tapi belum bisa di-*merge* sebelum ada yang *approve*. Saya sebagai *maintainer* yang punya hak *approve*. Nanti saya *review* dulu kodenya."

Binto mengangguk paham. "Jadi *Pull Request* itu semacam... izin dulu gitu, Mas?"

"Lebih dari sekadar izin, *Le*. PR itu jantung kolaborasi di industri," Mas Alin menjelaskan dengan serius. "Di sini tempatnya *code review*, diskusi, dan *approval*. Saya bisa lihat perubahan kodemu baris demi baris, kasih komentar kalau ada yang kurang efisien, atau minta perbaikan. Kalau saya merasa kodenya sudah *clean* dan bener, baru saya *approve* dan klik Merge."

Mas Alin men-scroll kode Binto di layar. Matanya teliti menyusuri setiap baris. Ia lalu menyorot satu blok kode dan mengetikkan komentar langsung di antarmuka GitHub.

"Ini contohnya," kata Mas Alin. "Logikamu sudah benar. Coba lihat komentar saya." Ia memutar layar laptop agar Binto bisa membaca:

text
### Komentar dari Mas Alin:
Halo, To. Logikanya udah bener. Hasil akhirnya udah sesuai acceptance criteria. Aku kasih catatan kecil ya:

### 1. Nama variabel `tmp` (BarangController.php:27)
Saran: ganti jadi `total_pendapatan`.
Alasan: `tmp` terlalu generik. Seminggu lagi kamu buka kode ini, kamu sendiri bisa lupa `tmp` itu isinya apa. Nama variabel harus menjelaskan isinya, bukan tipe-nya.

### 2. Pemanggilan fungsi duplikat (BarangService.php:42-45)
Fungsi `hitungTotal()` dipanggil dua kali — di baris 42 dan 45. Ini boros karena query database bisa jalan dua kali.
Saran: Simpan hasilnya di variabel dulu.
```php
$total = $this->hitungTotal($tanggal);
$this->setRingkasan($total);
$this->setPendapatan($total);
```

### 3. Validasi tanggal (BarangService.php:18)
Ini oke, tapi coba dipastiin juga ngecek tahun kabisat ya. Februari 2024 punya 29 hari, jangan cuma 28.

Overall: Kode udah rapi. Dua catatan di atas minor, tapi perbaiki dulu ya biar makin clean. Good job buat PR pertama!

"Lihat formatnya, *Le*," kata Mas Alin. "Saya gak cuma bilang 'ini salah'. Saya kasih tahu: apa masalahnya, di mana lokasinya, kenapa jadi masalah, dan gimana cara perbaikinya — lengkap dengan contoh kode. Itu bedanya *code review* yang konstruktif dengan yang cuma nyalahin."

Binto mengangguk cepat. "Ini enak banget, Mas. Saya langsung tahu apa yang harus diperbaiki. Gak perlu nebak-nebak."

"Prinsipnya, *Le*: *review* itu tujuannya buat ngebantu, bukan buat ngerendahin. Pujilah yang sudah benar. Kasih saran yang spesifik untuk yang perlu perbaikan. Dan selalu pisahkan antara kritik ke kode dengan kritik ke orangnya. Kode bisa jelek, itu wajar — namanya juga belajar. Tapi orangnya jangan direndahkan."

Binto mencatat dalam hati. *Code review beneran kayak gini. Bukan ajang nyalahin, tapi diskusi dan ngebantu. Ada pujian, ada saran, ada contoh konkret.*

"Tapi, Mas," Binto bertanya. "Apakah aturan *review* dan *approve* ini kaku banget? Kalau misalnya ada *bug* darurat tengah malam dan Mas Alin lagi tidur, gimana?"

Mas Alin tersenyum tipis. "Nah, ini dunia nyata. Dalam kondisi tertentu—misal darurat butuh perbaikan detik itu juga, atau yang bikin PR adalah *engineer* senior yang sudah sangat terpercaya—proses formal kayak *approval* dan *code review* bisa dilewati. Di GTN kadang kita juga gitu kalau lagi krisis. Tapi dalam kondisi normal, apalagi buat *feature* baru, saya gak akan *approve* kalau kode belum *clean* atau kerjanya masih ngawur."

Binto segera memperbaiki kodenya di laptop, lalu melakukan *commit* ulang dan *push*. Secara otomatis, tampilan Pull Request di GitHub ikut ter-update.

"Nah, sekarang kodenya sudah rapi dan *clean*." Mas Alin menekan tombol Approve, lalu mengklik tombol hijau Merge Pull Request. Beberapa detik kemudian, kode Binto resmi bergabung dengan `main`.

"Selamat, *Le*. Kode kamu sudah jadi bagian dari proyek."

Binto tersenyum lega. Tapi perjalanan belum selesai.

## **4.7 Mbak Rara dan Hantu Kabisat**

Keesokan paginya, *sticky note* \[MMK-012\] berpindah dari In Progress ke Testing.

"Tak *testing* dulu ya, To," kata Mbak Rara sambil tersenyum manis. Tapi Binto tahu, di balik senyum itu ada ketelitian yang tajam.

Mbak Rara duduk di mejanya, membuka laptop, dan mengakses server *staging*. Ia mencoba fitur cetak laporan.

Pertama, ia pilih tanggal 15 Januari. Muncul PDF. Rapi.

Kedua, ia pilih tanggal 1 Februari. Muncul PDF. Rapi.

Ketiga, ia pilih tanggal 29 Februari 2024\.

Error.

Layar menampilkan pesan merah: *"Invalid date."*

Mbak Rara menoleh ke Binto dengan senyum yang lebih lebar. "Wah, Mas Binto. Lupa ya kalau 2024 itu tahun kabisat? Februari 2024 punya 29 hari lho."

Binto menepuk jidatnya sendiri. "Aduh. Iya, Mbak. Saya cuma ngecek maksimal tanggal 28 buat Februari. Lupa tahun kabisat."

"Ya sudah, tak balikin dulu ya *sticky note*\-nya." Mbak Rara dengan santai memindahkan kertas kuning itu dari Testing kembali ke In Progress. "Nanti kalau udah bener, kabari aku."

Binto menghela napas. *Gue kira udah beres. Ternyata masih ada jebakan.*

Mas Alin yang mendengar dari pojokannya hanya terkekeh. "Nah, kan. *Testing* itu penting. Developer sering *bias*. Kita pikir kode kita sudah sempurna, padahal ada kasus-kasus yang bisa jadi kelewat. Mbak Rara itu *quality gate* kita."

## **4.8 Belajar dari Kabisat**

Binto kembali membuka kodenya. Ia mencari bagian validasi tanggal dan menemukan bahwa ia hanya memeriksa batas 28 hari untuk Februari, tanpa memperhitungkan tahun kabisat.

Dengan sedikit riset dan bantuan Mas Alin yang menjelaskan logika tahun kabisat, Binto memperbaiki fungsinya. Ia menambahkan pengecekan: jika tahun habis dibagi 4 dan bukan kelipatan 100, atau habis dibagi 400, maka Februari punya 29 hari.

Setelah diuji sendiri dengan berbagai tanggal—29 Februari 2024 lolos, 29 Februari 2025 ditolak—Binto *commit* perbaikannya dan *push*.

"Mbak, sudah saya perbaiki. Bisa di-*test* lagi."

Mbak Rara mencoba lagi. Tanggal 29 Februari 2024, 2028, 2032... semua lolos. Tanggal 29 Februari 2025, 2026, 2027... ditolak dengan pesan error yang ramah.

"*Nah*, gini dong," Mbak Rara tersenyum puas. Ia memindahkan *sticky note* dari In Progress ke Testing, lalu—setelah semua *acceptance criteria* terpenuhi—ke Done.

Kertas kuning dengan stiker bebek itu kini bertengger manis di kolom paling kanan.

Binto merasa lega sekaligus belajar sesuatu yang berharga. *Tanggal itu gak sesederhana 1 sampai 31\. Ada bulan, tahun kabisat, bahkan zona waktu. Ini gak diajarin di kampus.*

## **4.9 Tombol di Tangan Pak Haji**

Hari itu juga, Mas Alin melakukan Release.

"Fitur MMK-012 sudah di main. Sekarang kita *deploy* ke *production*."

Ia membuka satu aplikasi di komputernya—semacam *dashboard* dengan tombol-tombol dan grafik. Binto belum paham betul apa itu, tapi ia melihat Mas Alin mengklik satu tombol bertuliskan Deploy to Production.

Beberapa menit kemudian, layar menunjukkan status Success.

"Selesai," kata Mas Alin santai. "Sekarang fitur cetak laporan sudah bisa dipakai di minimarket Pak Haji."

Binto melongo. "Segampang itu, Mas?"

"Segampang itu. Tapi itu karena kita sudah siapin *pipeline*\-nya dari dulu. Nanti kamu akan belajar soal CI/CD. Untuk sekarang, cukup tahu bahwa kode kita sudah *live*."

Sore harinya, telepon kantor berdering lagi. Pakde Suhar yang mengangkat.

"*Nggih*, Pak Haji... *Alhamdulillah*, sudah bisa? *Syukur*... Calon investornya suka? *Alhamdulillah*... *Nggih*, *sami-sami*. Siap, nanti kalau ada perlu apa-apa kabari lagi."

Pakde menutup telepon dengan senyum lebar. Ia menatap Binto dan Mas Alin.

"Pak Haji bilang terima kasih. Tadi demo ke investor, tombol cetaknya dipakai. Investor terkesan. Katanya, 'Wah, minimarket di Kalimantan sudah pakai sistem canggih.'"

Wawan bersorak kecil. Mbak Rara mengacungkan jempol. Mas Alin hanya tersenyum tipis sambil menyeruput kopinya.

Binto terdiam. Ada rasa aneh di dadanya. *Fitur kecil yang gue bikin... dipakai orang di Kalimantan. Dan itu membantu bisnis mereka.*

Rasanya berbeda dengan tugas kuliah yang hanya dilihat dosen lalu disimpan di rak.

## **4.10 Alur Itu Tidak Selalu Sama**

Sore itu, Binto dan Mas Alin duduk di bangku kayu teras depan. Pohon rambutan di hadapan mereka bergoyang pelan, buahnya mulai merah merona.

"Mas," Binto membuka suara. "Apa alurnya selalu seperti ini? Di semua perusahaan?"

Mas Alin menyesap kopinya, lalu terkekeh. "Ya enggaklah, *Le*. Tiap tempat beda."

Ia menatap langit sore yang mulai jingga. "Sekarang kita enak. Ada Wawan yang bantu desain UI, ada Mbak Rara yang jadi QA. Kamu dan saya fokus di *backend* dan logika."

"Kalau dulu?"

"Dulu?" Mas Alin tersenyum nostalgia. "Waktu saya pertama kali kerja di Surabaya, lima belas tahun lalu, saya sendirian. *Fullstack* beneran. Saya yang bikin *database*, *backend*, *frontend*, sampai desain tombolnya. QA-nya? Ya saya sendiri. *Testing* sendiri. Kalau ada *bug*, ya saya yang malu sendiri di depan klien."

Binto membayangkan betapa beratnya.

"Terus di tempat lain bisa lebih lengkap lagi," lanjut Mas Alin. "Saya pernah kontrak di perusahaan *startup* Jakarta. Di sana timnya gede. Ada *frontend engineer* khusus React, *backend engineer* khusus Node.js, ada *database engineer* yang ngurusin *query* dan *index*, ada *DevOps* yang ngurusin server. Lengkap banget. Tiap orang cuma megang bagian kecil."

"Enak dong, Mas?"

"Enak sih. Tapi kita jadi gak tahu *gambaran besar*. Kalau ada masalah, suka lempar-lemparan. 'Ah itu *backend*\-nya yang error.' 'Bukan, itu *database*\-nya lambat.'"

Mas Alin menoleh ke Binto. "Intinya, *Le*, tim itu dinamis. Gak ada struktur yang sempurna. Di sini kita kecil, semua serba *fullstack*. Kamu belajar dari hulu ke hilir. Itu bagus buat fondasi. Nanti kalau kamu pindah ke tempat yang lebih besar dan lebih terspesialisasi, kamu gak akan kaget. Kamu paham konteks."

Binto mengangguk pelan.

"Jadi kita adaptasi aja," Mas Alin menyimpulkan. "Pakai yang ada, sesuai kebutuhan. Agile itu bukan cuma soal *framework* atau *role*. Agile itu *mindset*. Fleksibel."

Binto merenung. *Berarti alur kerja yang gue lihat dua hari ini bukan satu-satunya kebenaran. Tapi ini fondasi yang kuat.*

Ia menatap pohon rambutan. Beberapa buah sudah merah sempurna, siap dipetik. Seperti ilmunya yang mulai matang, satu per satu.

"*Matur suwun*, Mas," katanya tulus.

Mas Alin mengangkat cangkirnya, memberi hormat kecil. "*Sami-sami*, *Le*. Besok kita lanjut lagi. Masih banyak yang harus dipelajari."

Di langit Blitar, burung-burung gereja terbang pulang ke sarangnya. Hari hampir berakhir, tapi perjalanan Mas Binto masih panjang.

---