# Bab 6: Membangun Rumah yang Bersih

Pagi itu, Pakde Suhar kasih tugas baru. Fitur laporan stok barang untuk toko ATK Bu Warsiti, teman lama yang punya toko di Pasar Besar.

"Simpel aja, To. Tambah barang. Lihat stok. Edit. Hapus."

Binto mengangguk mantap. "Siap, Pakde. Saya kerjain sendiri."

Mas Alin melirik dari pojokan. "Yakin, Le? Mau dibantuin?"

"Nggak usah, Mas. Saya bisa."

Mas Alin mengangguk pelan. Tapi ada sesuatu di matanya. Sesuatu yang Binto nggak sadari.

*Dia pernah lihat ini sebelumnya*, mungkin begitu isi kepala Mas Alin. *Anak baru. Udah mulai pede. Udah ngerasa bisa.*

*Dan biasanya... itu pertanda akan ada yang jatuh.*

## 6.1 Gaya Kampus

Binto membuka laptop. Membuat proyek Laravel baru. `inventory_atk`.

Dia kerja seharian penuh.

Database? Satu tabel. `barang`. Kolom: id, nama, stok, harga, keterangan.

Controller? Satu file. `BarangController.php`. Semua fungsi numpuk di situ. `index()`. `tambah()`. `edit()`. `hapus()`. Semua campur jadi satu.

View? Satu file Blade. `index.blade.php`. HTML header. Sidebar. Tabel. Footer. Semua dalam satu file.

Validasi? Seadanya.

Komentar? Nggak ada.

*Ngapain? Kan aku yang nulis. Pasti inget.*

Sore harinya, dia coba. Tambah barang: berhasil. Edit: berhasil. Hapus: berhasil.

"Beress," gumamnya puas. Push ke Git. Selesai.

---

Malam itu, dia cerita ke Bapak. "Pak, aku udah bisa bikin aplikasi sendiri. Dari nol. Buat toko ATK."

Bapak cuma manggut-manggut. "Sing penting... wong jujur, yo."

Binto nyengir. *Bapak nggak ngerti IT. Tapi doanya selalu sama. "Yang penting... orang jujur."*

## 6.2 Review Pagi: Bingung Sendiri

Besoknya, Mas Alin datangi meja Binto. Bawa cangkir enamel wayangnya.

"Gimana, Le? Udah bisa dilihat?"

"Udah, Mas. Jalan semua."

Binto buka laptop. Demo. Tambah barang. Edit. Hapus. Jalan.

Mas Alin memperhatikan. Tanpa komentar.

"Oke. Sekarang... coba buka kodenya. Jelaskan ke saya alurnya."

Binto buka `BarangController.php`. Ratusan baris kode.

"Jadi di sini fungsi index, Mas. Ini ngambil data... terus dikirim ke view..."

Scroll.

"Ini fungsi tambah... buat nyimpan data..."

Scroll.

"Ini fungsi edit..."

Dia berhenti. Jarinya nunjuk satu bagian.

Lalu terdiam.

"Mas... tadi saya taruh validasi stok di mana ya?"

Scroll naik. Scroll turun.

"Ini harusnya ada pengecekan kalau stok kurang dari batas minimal..."

Scroll lagi.

"Tadi saya taruh di mana..."

Butuh hampir dua menit buat Binto nemuin potongan kode validasi stok. Ternyata ada di dalam fungsi `index`. Terselip di antara logika pengambilan data dan pemanggilan view.

"Nah, ini, Mas. Di sini."

```
foreach ($barangs as $barang) {
    if ($barang->stok < 10) {
        $barang->status = 'Menipis';
    }
}
```

Mas Alin mengangguk pelan. "Kenapa harus 10? Bukan 5? Atau 15?"

Binto buka mulut. Tutup lagi.

Dia... nggak inget.

"Tapi ini kode kamu sendiri, Le. Baru kemarin kamu tulis."

Binto terdiam.

*Iya juga. Kenapa aku sendiri lupa?*

## 6.3 Tiba-Tiba Hancur

Sorenya, Mbak Rara test aplikasi Binto. Dia buka di staging. Coba-coba.

Lima menit pertama... oke.

Sepuluh menit...

"Mas Binto. Sini deh."

Binto mendekat. Wajah Mbak Rara datar. Tapi matanya... matanya tajam.

"Coba lihat ini."

Dia input stok: -50. Sistem terima.

"Nggak ada validasi stok negatif, Mas?"

Binto kaget. "Eh... iya, Mbak. Kelewat."

Mbak Rara lanjut. Dia input harga: "abc". Sistem terima.

"Dan ini?"

Binto menelan ludah.

Terus Mbak Rara buka halaman edit. Dia hapus ID dari URL. Ketik manual ID yang nggak ada. Muncul error jelek. Pesan SQL langsung terpampang di layar.

"Dan ini... ini celah keamanan, Mas. SQL injection."

Binto merasakan perutnya mulas.

Dalam dua jam, Mbak Rara nemu dua belas bug. Dua belas. Bukan dua. Bukan tiga. Dua belas.

Sticky note di kolom Testing... pindah balik ke In Progress. Terus balik lagi. Terus balik lagi.

"Duh, Mas Binto," kata Mbak Rara sambil geleng-geleng. "Bikin kopi dulu deh. Capek aku bolak-balik."

Dia nyengir. Tapi Binto tahu... di balik senyum itu ada kekecewaan.

## 6.4 Runtuh

Binto duduk di mejanya. Nggak ngomong. Nggak gerak.

*Dua belas bug.*

*Aku kira aku udah bisa. Aku kira kodeku udah rapi. Aku kira aku...*

*Ternyata... nggak.*

Tangannya otomatis meremas ujung kemejanya. Jemarinya mencengkeram kain sampai ujungnya berkerut. Kebiasaan sejak kecil. Setiap kali gugup. Setiap kali merasa nggak cukup.

*Aku lulusan PTN top. Masa iya bikin aplikasi toko aja nggak becus?*

---

Mas Alin dateng. Duduk di sampingnya. Nggak ngomong apa-apa. Cuma diam.

Lama.

Akhirnya Binto yang buka suara. "Mas... saya payah ya?"

"Nggak."

"Tapi bug-nya..."

"Itu wajar, Le." Mas Alin menyesap kopinya. "Kamu baru pertama kali ngerjain fitur sendiri. Dari nol. Tanpa bantuan. Wajar kalau ada yang kelewat."

"Tapi dua belas..."

"Saya dulu... waktu pertama kali deploy ke production... dua puluh tiga bug. Dan itu di depan klien. Langsung. Saya disemprot satu jam."

Binto mendongak. "Serius?"

"Serius." Mas Alin nyengir. "Malu? Pasti. Tapi dari situ saya belajar. Testing sendiri sebelum kirim ke QA. Bikin acceptance criteria yang jelas. Minta review teman."

Dia menatap Binto. Matanya tenang.

"Bug itu bukan tanda kamu payah, Le. Bug itu... gurunya programmer. Dari bug kita belajar."

## 6.5 Rumah Tanpa Sekat

Mas Alin berdiri. "Sekarang... kita perbaiki. Sini, ikut saya."

Tapi dia nggak langsung buka kode. Dia malah berjalan ke teras depan. Binto mengikuti.

Pohon rambutan di halaman kini buahnya semakin merah. Beberapa sudah bisa dipetik.

"Lihat pohon rambutan itu," kata Mas Alin sambil menunjuk. "Bayangin kamu punya rumah. Tapi rumahmu gak punya sekat. Dapur, kamar mandi, ruang tamu, kamar tidur—semua jadi satu ruangan besar."

Binto mencoba membayangkan.

"Sekarang kamu mau ganti wastafel di dapur. Gampang, kan? Tinggal bongkar, pasang baru. Tapi karena gak ada sekat, begitu kamu bongkar wastafel, tiba-tiba atap kamar mandi ikut bocor. Tembok ruang tamu retak. Lantai kamar tidur ikut rusak."

Binto mulai menangkap arah analoginya.

"Kode kamu tadi kayak rumah tanpa sekat, Le. Mau ubah dikit di bagian validasi stok, eh malah tampilan tabelnya ikut kacau. Mau ganti warna tulisan, eh logika query-nya malah error. Itu karena semua campur jadi satu. Namanya Separation of Concerns—pisahkan urusan."

Mas Alin duduk di bangku kayu. Binto ikut duduk.

"Dalam aplikasi, setidaknya ada tiga urusan besar. Pertama, tampilan: bagaimana data ditampilkan ke pengguna. Kedua, logika bisnis: aturan-aturan seperti 'stok di bawah 10 harus kasih peringatan'. Ketiga, akses data: cara ngambil dan nyimpan data dari database. Kalau tiga ini dicampur, kamu bikin spaghetti code. Lezat sih, tapi kusut."

"Kode yang berantakan itu bukan cuma bikin pusing," tambah Mas Alin. "Kadang juga bikin bug... dan bug itu bisa jadi celah keamanan kalau lolos."

Binto manggut-manggut. "Jadi harus dipisah-pisah, Mas?"

"Nggih. Minimal di file terpisah. Atau kalau mau lebih rapi, pakai pola seperti yang kita pakai di proyek Garum."

## 6.6 Membedah Contoh Rapi

Mereka kembali ke dalam. Mas Alin membuka laptopnya, menampilkan kode proyek Pabrik Garum.

"Lihat ini."

Ia menunjukkan struktur folder:

```
app/
├── Http/
│   └── Controllers/
│       └── LaporanController.php
├── Services/
│   └── LaporanService.php
├── Repositories/
│   └── LaporanRepository.php
├── Models/
│   └── Penjualan.php
resources/
└── views/
    ├── layouts/
    │   └── app.blade.php
    └── laporan/
        └── index.blade.php
config/
├── constants.php
└── app.php
```

"Ini bukan aturan baku, Le. Cuma pola yang bantu kita tetap waras. Controller tugasnya cuma satu: terima request dari browser, terus panggil Service. Service isinya logika bisnis—aturan main kayak validasi stok minimal, hitung total, dan sebagainya. Repository tugasnya ngurusin database—query, simpan, hapus. Model itu representasi data. Dan view-nya juga dipisah: ada layout utama, lalu setiap halaman cuma isi kontennya aja."

Binto memperhatikan. "Jadi kalau saya mau ubah logika validasi stok, saya tinggal buka Service? Gak perlu sentuh Controller atau Repository?"

"Tepat. Dan kalau suatu hari kamu ganti database dari MySQL ke PostgreSQL, kamu cuma perlu ubah di Repository. Service dan Controller tetap aman. Itulah kekuatan pemisahan."

Mas Alin menunjuk folder views. "Dan lihat layout-nya. Ini buatan Wawan. Dia pisah header, sidebar, dan footer di file layout utama. Setiap halaman cuma isi kontennya aja, gak perlu tulis ulang header di setiap halaman. Kalau Wawan mau ganti logo atau warna navbar, cukup edit satu file. Semua halaman ikut berubah. Prinsip yang sama: Don't Repeat Yourself. DRY. Berlaku di backend maupun frontend."

"Lagipula," lanjut Mas Alin. "Kalau validasi kamu taruh di satu tempat yang jelas, lebih susah buat orang 'lupa' ngecek input. Dan di dunia nyata, banyak masalah keamanan justru muncul karena hal-hal kecil yang kelupaan kayak gitu."

## 6.7 Operasi Plastik Sendiri

"Sekarang," kata Mas Alin sambil menutup laptopnya, "kamu yang kerjakan."

"Maksudnya, Mas?"

"Saya tidak akan sentuh kode kamu. Kamu sendiri yang akan merapikannya. Saya cuma duduk di sini, kamu tanya kalau buntu."

Binto menatap layarnya. Ratusan baris kode di BarangController.php menatap balik. *Rumah tanpa sekat.*

Ia menarik napas panjang, lalu mulai.

Pertama, ia membuat folder baru: app/Services dan app/Repositories. Ia membuat file BarangRepository.php dan mulai memindahkan semua query SQL ke sana. Ia membuat BarangService.php dan memindahkan logika bisnis—termasuk validasi stok minimal.

Kedua, ia memangkas BarangController.php. Kini controller hanya bertugas menerima request, memanggil service, dan mengembalikan view. Tidak ada lagi query mentah di dalamnya.

Ketiga, ia membongkar index.blade.php. Ia membuat file layout utama: layouts/app.blade.php yang berisi header, sidebar, dan footer. Lalu ia ubah index.blade.php menjadi hanya berisi konten tabel, me-extends layout utama.

Proses ini memakan waktu hampir dua jam. Setiap kali selesai satu bagian, Binto menjalankan ulang aplikasi. *Masih jalan? Alhamdulillah.* Masih jalan? *Lanjut.*

Mas Alin hanya duduk di sampingnya, sesekali memberi petunjuk kecil: "Nah, itu fungsi cekStokMenipis taruh di Service, bukan di Repository." Atau: "Repository jangan pakai echo. Itu urusan View."

Saat Binto selesai memindahkan logika validasi stok ke Service, Mas Alin menunjuk nama fungsinya. "Soal penamaan, Le. Coba lihat lagi nama fungsi yang kamu buat."

Binto melihat. Fungsi-fungsi di BarangService.php: `cekStokMenipis`, `hitungTotal`, `simpanData`.

"Ini sudah lumayan," kata Mas Alin. "Tapi ada ruang untuk lebih baik. Aturan praktisnya gampang: nama variabel dan fungsi harus menjawab apa, bukan bagaimana. `cekStokMenipis` — jelas, langsung bisa ditebak fungsinya. Tapi `simpanData`? Data apa? Disimpan ke mana? Mending `simpanBarangKeDatabase` — meskipun agak panjang, tapi gak ambigu."

Binto mengangguk. "Terus `hitungTotal`... total apa, Mas?"

"Nah, itu pertanyaan yang bagus. `hitungTotal` itu ambigu. Total penjualan? Total stok? Total harga? Mending `hitungTotalNilaiStok` atau `hitungTotalPenjualanHarian`. Lebih panjang dikit, tapi satu tahun lagi kamu baca, langsung paham."

Mas Alin berdiri, meregangkan kakinya. "Ini bedanya clean code dan clever code, Le. Banyak programmer pemula pengen kelihatan pintar. Mereka bikin kode pendek-pendek, satu baris isinya banyak logic, namanya satu huruf semua: `x`, `y`, `tmp`, `fn`. Itu clever code — kode yang cuma dipahami sama penulisnya, itupun cuma saat dia nulis."

"Clean code beda. Nama fungsinya jelas meskipun panjang. Logikanya lurus, gak berbelit-belit — meskipun jadinya lebih banyak baris. Strukturnya terpisah rapi. Tujuannya: orang lain bisa baca kode kamu tanpa harus mikir keras. Itu yang tadi kita kerjakan."

Binto merenung. *Aku dulu sering banget bikin variabel satu huruf. Bangga kalau kodeku pendek dan susah dipahami. Kirain itu keren. Ternyata... itu cuma nyusahin diri sendiri.*

## 6.8 Pesan untuk Masa Depan

Setelah semua selesai dan aplikasi kembali berjalan normal, Binto meregangkan tubuhnya. "Selesai, Mas."

Mas Alin menggeser kursinya, melihat layar Binto. Ia membuka file BarangService.php dan menunjuk satu bagian.

"Bagus. Sekarang coba kamu baca lagi fungsi ini."

Binto membaca fungsi cekStokMenipis. Fungsinya sederhana: mengecek apakah stok di bawah nilai tertentu.

"Paham, Mas?"

"Coba jelaskan ke saya. Kenapa batas minimalnya 10? Bukan 5 atau 15?"

Binto terdiam lagi. Ia masih belum ingat alasan pastinya. "Saya... kurang yakin, Mas. Mungkin karena dulu di kampus sering pakai contoh 10."

"Nah. Dua minggu lagi, kalau kamu buka kode ini, kamu akan tanya lagi: 'Kenapa 10?' Bisa jadi waktu itu kamu punya alasan bagus, tapi karena tidak ditulis, alasan itu hilang."

Mas Alin menunjuk ke bagian atas file. "Tulis komentar. Bukan buat saya. Bukan buat Mbak Rara. Tapi buat kamu sendiri di masa depan."

Binto mengangguk. Ia mulai mengetik komentar di atas fungsi tersebut, menjelaskan bahwa batas minimal 10 berdasarkan diskusi dengan Bu Warsiti—beliau ingin peringatan dini karena waktu pengiriman ulang dari supplier sekitar dua sampai tiga hari.

Mas Alin tersenyum. "Nah, itu dia. Sekarang, dua tahun lagi kalau kamu lupa, kamu tinggal baca komentarmu sendiri. Langsung ingat."

Binto melanjutkan. Ia menambahkan komentar di setiap fungsi penting: apa fungsinya, parameter apa yang diterima, apa yang dikembalikan, dan—yang paling penting—mengapa keputusan tertentu diambil.

## 6.9 Konstanta di Tempat Terpusat

Saat Binto selesai menulis komentar, Mas Alin menunjuk ke nilai 10 yang masih tertulis di dalam Service.

"Satu lagi, Le. Angka 10 ini kamu taruh di sini. Sudah lumayan, karena sekarang terpusat di satu kelas. Tapi bagaimana kalau nanti ada fitur lain yang juga butuh nilai 10 ini? Atau suatu hari Bu Warsiti minta batas minimalnya diubah jadi 5?"

Binto berpikir. "Saya tinggal ubah di sini, Mas?"

"Iya, kalau cuma satu tempat. Tapi di aplikasi yang lebih besar, bisa jadi ada banyak konstanta seperti ini. Batas stok minimal, biaya pengiriman, persentase pajak, dan lain-lain. Kalau tersebar di berbagai Service, kamu harus mencari satu per satu saat ada perubahan."

Mas Alin membuka proyek Pabrik Garum di laptopnya. Ia menunjukkan folder config/.

"Di Laravel, ada folder config khusus buat konfigurasi. Semua nilai yang sifatnya konstan dan mungkin berubah suatu hari, taruh di sini. Misalnya bikin file config/constants.php."

Ia menunjukkan contoh isinya:

```php
return [
    'stok_minimal' => 10,
    'biaya_pengiriman' => 15000,
    'pajak_ppn' => 0.11,
];
```

"Kalau begini, semua orang di tim tahu di mana mencari nilai-nilai ini. Mau ubah? Tinggal buka satu file. Bahkan bisa pakai helper config('constants.stok_minimal') di mana saja."

Binto mengangguk paham. "Jadi lebih rapi lagi."

"Nggih. Ini best practice sederhana. Nilai yang bisa berubah, taruh di tempat terpusat. Jangan hardcode di tengah-tengah logika. Nanti susah maintenance-nya."

Binto segera membuat file config/constants.php dan memindahkan nilai 10 ke sana. Ia mengganti kode di Service menjadi config('constants.stok_minimal').

Mas Alin melanjutkan. "Tapi tidak semua konstanta taruh di constants.php. Ada yang lebih cocok di file .env. Misalnya nama toko, alamat, atau credentials database. Itu karena tiap environment bisa beda. Di lokal kamu namanya 'Toko ATK Warsiti', tapi di production nanti bisa jadi 'Warsiti ATK'."

Binto mengangguk. Ia paham sekarang: nilai yang bersifat bisnis dan sama di semua environment taruh di config/constants.php. Nilai yang berbeda antar environment taruh di .env.

"Sekarang lebih rapi," gumamnya puas.

## 6.10 Debugging Sistematis

Besoknya, Mas Alin nggak biarin Binto terpuruk dengan dua belas bug itu.

"Sekarang... kita perbaiki bareng. Satu per satu."

Dia buka laptop. Buka daftar bug dari Mbak Rara.

"Bug 1: validasi stok negatif. Gimana caranya?"

"Tambah pengecekan. Kalau stok kurang dari nol, tolak."

"Bener. Bug 2?"

"Validasi harga. Input harus angka."

"Lanjut."

"Bug 3: SQL injection. Harus pakai parameterized query."

Satu per satu. Dua belas bug.

Mas Alin nggak ngasih jawaban langsung. Dia tanya. "Menurutmu gimana?" "Coba mikir." "Inget pelajaran kemarin?"

Dia paksa Binto mikir sendiri.

Dan entah kenapa... cara ini lebih ngena.

---

Sorenya, semua beres. Mbak Rara test lagi. Kali ini lolos.

"Nah gini dong," katanya sambil pindahin sticky note ke Done. "Tapi jangan nunggu aku test lagi ya, Mas. Coba test sendiri dulu."

Binto mengangguk. "Siap, Mbak."

Dia belajar sesuatu. *Debugging itu bukan cuma nemuin error. Tapi mikir sistematis. Satu per satu. Analisis. Akar. Perbaiki. Verify. Bukan panik. Bukan ngawur.*

## 6.11 Testimoni Mbak Rara

Keesokan harinya, Mbak Rara selesai dengan tumpukan test case proyek Garum. Ia berjalan ke meja Binto untuk mengisi air di dispenser. Matanya melirik layar Binto.

"Wah, Mas Binto, kodenya udah beda sekarang."

"Ini habis dirombak total, Mbak."

Mbak Rara berhenti sejenak. "Boleh lihat?"

Binto mengangguk.

Mbak Rara duduk di sebelah Binto. Ia membuka file BarangService.php dan membaca. Matanya bergerak cepat.

"Ini bagus. Ada komentarnya. Jadi aku gak perlu tanya-tanya lagi."

Ia scroll ke bawah.

"Ooh, cekStokMenipis di sini. Aku langsung paham alurnya. Jadi kalau ada bug di perhitungan stok, aku tinggal lihat Service ini aja, gak perlu buka file lain?"

"Nggih, Mbak. Logikanya semua di sini."

Mbak Rara tersenyum lebar. "Enak banget ini. Coba kemarin-kemarin kodenya kayak gini, aku gak perlu jungkir balik nyari bug."

Binto tersipu. Pujian dari Mbak Rara terasa seperti validasi bahwa ia berada di jalur yang benar.

## 6.12 Dua Langkah Maju

Sore menjelang adzan ashar. Binto dan Mas Alin kembali duduk di teras. Pohon rambutan di depan kini berwarna merah merona di banyak bagian. Panen tinggal menghitung hari.

"Gimana rasanya?" tanya Mas Alin sambil menyesap kopi dari cangkir enamelnya.

Binto merenung sejenak. "Awalnya males, Mas. Masa cuma program kecil harus dipisah-pisah segala. Tapi setelah jadi... enak lihatnya. Rapi."

"Itulah bedanya programmer biasa sama software engineer," Mas Alin meletakkan cangkirnya. "Programmer bikin kode biar mesin ngerti. Software engineer bikin kode biar manusia juga ngerti. Termasuk dirimu sendiri dua bulan lagi."

Binto mengangguk.

"Dan soal komentar tadi," lanjut Mas Alin, "banyak yang males nulis komentar. Katanya: 'Kode yang bagus itu self-documenting, gak perlu komentar.' Itu betul, tapi hanya untuk kode yang benar-benar sederhana. Di dunia nyata, kode kita penuh dengan keputusan bisnis yang aneh. Kenapa stok minimal 10? Kenapa biaya kirim 15000? Kenapa pakai algoritma A, bukan B? Itu semua perlu dicatat. Komentar adalah surat cinta untuk dirimu di masa depan."

Binto tersenyum mendengar analogi itu.

"Dan satu lagi, Le," Mas Alin menatap Binto serius. "Kode yang kamu tulis hari ini, bisa jadi akan dibaca oleh orang lain bertahun-tahun setelah kamu pindah kerja. Bayangkan mereka buka kode kamu, lihat strukturnya rapi, ada komentarnya. Mereka akan berdoa: 'Semoga orang yang nulis ini selalu diberi kesehatan.' Itu warisan. Itu profesionalisme."

Binto terdiam. Ia tidak pernah berpikir sejauh itu.

---

Malam itu, di rumah. Bapak udah tidur.

Binto ingat bug-bug tadi. Ingat kata Mas Alin: *Bug bukan tanda kamu payah. Bug itu gurunya programmer.*

Dia ingat sesuatu yang dulu sering diomongin Bapak.

*"Ono rego ono rupo, To. Ada harga... ada bentuk."*

Bapak nggak pernah ngerti IT. Tapi kata-katanya... selalu nyambung.

*Semua butuh proses. Semua butuh harga.*

*Termasuk jadi engineer.*

---

Di luar, pohon rambutan di depan rumah bergoyang. Masih kecil, baru dua tahun. Ditanam Bapak tepat di hari kelulusan Binto. Masih belum berbuah.

Tapi akarnya... makin dalam.

Jatuh. Tapi nggak hancur. Gagal. Tapi belajar. Kode yang kemarin amburadul, sekarang rapi dengan sekat yang jelas. Dua belas bug yang bikin malu, kini jadi dua belas pelajaran.

*Dua langkah maju. Satu langkah mundur.*

*Tapi tetep... maju.*
