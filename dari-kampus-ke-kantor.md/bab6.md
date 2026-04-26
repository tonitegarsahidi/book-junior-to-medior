# **Bab 6: Membangun Rumah yang Bersih**

## **6.1 Tugas Santai**

Pagi itu, kantor Garda Teknologi Nusantara terasa lebih tenang dari biasanya. Wawan sedang *remote* dari rumah karena ibunya sakit, Mbak Rara sibuk dengan setumpuk *test case* untuk proyek Pabrik Garum, dan Mas Alin asyik dengan *headset*\-nya, tampak serius menatap layar yang penuh log server.

Binto duduk di mejanya, menyesap teh hangat buatan Bu Sari. Pikirannya melayang ke fitur cetak laporan yang sudah *live* di Kalimantan. Ada rasa bangga yang masih tersisa.

"Mas Binto," suara Pakde Suhar tiba-tiba dari arah pintu.

Binto menoleh. Pakde berjalan mendekat, di tangannya ada selembar kertas kecil.

"Saya mau minta tolong. Adik saya, Bu Warsiti, punya toko ATK di Pasar Besar Kota Blitar. Dia butuh program kecil buat catat barang masuk dan keluar. Yang simpel aja. Bisa tambah barang, lihat stok, edit, hapus. Gak usah rumit-rumit."

Binto mengangguk. "Buat tokonya langsung, Pakde?"

"Iya. Tapi ini lebih kayak uji coba dulu. Dia mau lihat apakah sistem kayak gini berguna. Kalau cocok, nanti bisa kita kembangkan lebih serius."

Mas Alin yang sedari tadi diam tiba-tiba membuka suara. "*Nggih*, Pakde. Biar Binto aja yang kerjain sendiri. Saya mau lihat caranya *ngoding* dari nol."

Binto menoleh ke Mas Alin. Ada nada penasaran dalam suara mentornya itu. Bukan nada menguji, tapi lebih seperti... ingin tahu.

"Siap, Mas. Saya kerjain sendiri."

Dalam hati, Binto bersemangat. *Akhirnya gue bisa unjuk gigi. Ini proyek kecil, tapi dari nol. Bukan lanjutan kode orang lain.*

## **6.2 Gaya Kampus**

Binto memutuskan memakai Laravel—*framework* PHP yang mulai ia kenal saat magang dulu. Ia membuat proyek baru di laptopnya: inventory\_atk.

Ia bekerja seharian penuh.

Pertama, ia membuat database sederhana: satu tabel barang dengan kolom id, nama, stok, harga, dan keterangan. Lalu ia membuat satu *controller*: BarangController. Di sanalah semuanya bercampur.

Semua logika ia tulis di dalam *controller* itu. Fungsi index() untuk menampilkan daftar barang: di dalamnya ada *query* ke database, pengolahan data, dan pemanggilan *view*. Fungsi tambah() untuk menyimpan data: di dalamnya ada validasi manual, *query* insert, dan *redirect*. Fungsi edit(), hapus()—semua di *controller* yang sama.

Untuk *view*\-nya, Binto membuat satu file Blade: index.blade.php. Di dalamnya ada HTML header, sidebar, konten tabel, footer—semua dalam satu file. Tidak ada pemisahan *layout*. Tidak ada @extends. Tidak ada @section. Semua utuh seperti satu halaman HTML raksasa.

Binto bahkan tidak menulis komentar. *Ngapain? Kan gue yang nulis. Pasti inget.*

Sore harinya, ia mencoba aplikasinya. Tambah barang: berhasil. Edit: berhasil. Hapus: berhasil. Stok berkurang otomatis saat ada barang keluar? Ia belum membuat fitur itu, tapi untuk sekarang, fungsionalitas dasar sudah jalan.

"Beress," gumamnya puas. Ia *push* kodenya ke Git.

## **6.3 Review Pagi: Bingung Sendiri**

Keesokan paginya, Mas Alin mendatangi meja Binto sambil membawa cangkir enamel animenya.

"Gimana, *Le*? Sudah bisa dilihat?"

Binto mengangguk percaya diri. "Sudah, Mas. Jalan semua." Ia membuka laptop, menjalankan aplikasi, dan mendemokan fitur-fitur dasarnya.

Mas Alin memperhatikan tanpa banyak komentar. Setelah demo selesai, ia berkata, "Sekarang coba buka kodenya. Jelaskan ke saya alurnya."

Binto membuka BarangController.php. Layar menampilkan ratusan baris kode.

"Jadi di sini ada fungsi index, Mas. Ini ngambil data dari database, terus dikirim ke *view*..."

Ia *scroll* ke bawah.

"Ini fungsi tambah, buat nyimpan data..."

Ia *scroll* lagi.

"Ini fungsi edit..."

Ia berhenti. Jarinya menunjuk satu bagian, lalu terdiam.

"Mas, tadi saya taruh validasi stok di mana ya?"

Ia *scroll* naik-turun. Matanya mencari-cari. "Ini kan harusnya ada pengecekan kalau stok kurang dari batas minimal... Tadi saya taruh di mana..."

Mas Alin hanya tersenyum tipis. Ia tidak membantu. Ia membiarkan Binto berjuang dengan kodenya sendiri.

Butuh waktu hampir dua menit bagi Binto untuk menemukan potongan kode validasi stok. Ternyata ada di dalam fungsi index, terselip di antara logika pengambilan data dan pemanggilan *view*.

"*Nah*, ini, Mas. Di sini."

Ia membaca kode yang ia tulis sendiri kemarin:

php

foreach ($barangs as $barang) {

    if ($barang-\>stok \< 10\) {

        $barang-\>status \= 'Menipis';

    }

}

Mas Alin mengangguk pelan. "Kenapa harus 10? Bukan 5? Atau 15?"

Binto membuka mulut, lalu menutupnya lagi. Ia tidak ingat alasan memilih angka 10\.

"Saya... kurang ingat, Mas."

"Tapi ini kode kamu sendiri, *Le*. Baru kemarin kamu tulis."

Binto terdiam. *Iya juga. Kenapa gue sendiri lupa?*

## **6.4 Rumah Tanpa Sekat**

Mas Alin bangkit. "Sini, ikut saya."

Mereka berjalan ke teras depan. Pohon rambutan di halaman kini buahnya semakin merah. Beberapa sudah bisa dipetik, tapi Bu Sari bilang menunggu akhir pekan biar panen bareng-bareng.

"Lihat pohon rambutan itu," kata Mas Alin sambil menunjuk. "Bayangin kamu punya rumah. Tapi rumahmu gak punya sekat. Dapur, kamar mandi, ruang tamu, kamar tidur—semua jadi satu ruangan besar."

Binto mencoba membayangkan.

"Sekarang kamu mau ganti wastafel di dapur. Gampang, kan? Tinggal bongkar, pasang baru. Tapi karena gak ada sekat, begitu kamu bongkar wastafel, tiba-tiba atap kamar mandi ikut bocor. Tembok ruang tamu retak. Lantai kamar tidur ikut rusak."

Binto mulai menangkap arah analoginya.

"Kode kamu tadi kayak rumah tanpa sekat, *Le*. Mau ubah dikit di bagian validasi stok, eh malah tampilan tabelnya ikut kacau. Mau ganti warna tulisan, eh logika *query*\-nya malah error. Itu karena semua campur jadi satu. Namanya Separation of Concerns—pisahkan urusan."

Mas Alin duduk di bangku kayu. Binto ikut duduk.

"Dalam aplikasi, setidaknya ada tiga urusan besar. Pertama, tampilan: bagaimana data ditampilkan ke pengguna. Kedua, logika bisnis: aturan-aturan seperti 'stok di bawah 10 harus kasih peringatan'. Ketiga, akses data: cara ngambil dan nyimpan data dari database. Kalau tiga ini dicampur, kamu bikin *spaghetti code*. Lezat sih, tapi kusut."

"Kode yang berantakan itu bukan cuma bikin pusing," tambah Mas Alin. "Kadang juga bikin *bug*... dan *bug* itu bisa jadi celah keamanan kalau lolos."

Binto manggut-manggut. "Jadi harus dipisah-pisah, Mas?"

"*Nggih*. Minimal di file terpisah. Atau kalau mau lebih rapi, pakai pola seperti yang kita pakai di proyek Garum."

## **6.5 Membedah Contoh Rapi**

Mereka kembali ke dalam. Mas Alin membuka laptopnya, menampilkan kode proyek Pabrik Garum.

"Lihat ini."

Ia menunjukkan struktur folder:

text

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

"Ini bukan aturan baku, *Le*. Cuma pola yang bantu kita tetap waras. *Controller* tugasnya cuma satu: terima *request* dari browser, terus panggil *Service*. *Service* isinya logika bisnis—aturan main kayak validasi stok minimal, hitung total, dan sebagainya. *Repository* tugasnya ngurusin database—*query*, simpan, hapus. *Model* itu representasi data. Dan *view*\-nya juga dipisah: ada *layout* utama, lalu setiap halaman cuma isi kontennya aja."

Binto memperhatikan. "Jadi kalau saya mau ubah logika validasi stok, saya tinggal buka *Service*? Gak perlu sentuh *Controller* atau *Repository*?"

"Tepat. Dan kalau suatu hari kamu ganti database dari MySQL ke PostgreSQL, kamu cuma perlu ubah di *Repository*. *Service* dan *Controller* tetap aman. Itulah kekuatan pemisahan."

Mas Alin menunjuk folder *views*. "Dan lihat *layout*\\-nya. Ini buatan Wawan. Dia pisah *header*, *sidebar*, dan *footer* di file *layout* utama. Setiap halaman cuma isi kontennya aja, gak perlu tulis ulang *header* di setiap halaman. Kalau Wawan mau ganti logo atau warna *navbar*, cukup edit satu file. Semua halaman ikut berubah. Prinsip yang sama: *Don't Repeat Yourself*. DRY. Berlaku di *backend* maupun *frontend*."

"Lagipula," lanjut Mas Alin. "Kalau validasi kamu taruh di satu tempat yang jelas, lebih susah buat orang 'lupa' ngecek input. Dan di dunia nyata, banyak masalah keamanan justru muncul karena hal-hal kecil yang kelupaan kayak gitu."

## **6.6 Operasi Plastik Sendiri**

"Sekarang," kata Mas Alin sambil menutup laptopnya, "kamu yang kerjakan."

"Maksudnya, Mas?"

"Saya tidak akan sentuh kode kamu. Kamu sendiri yang akan merapikannya. Saya cuma duduk di sini, kamu tanya kalau buntu."

Binto menatap layarnya. Ratusan baris kode di BarangController.php menatap balik. *Rumah tanpa sekat.*

Ia menarik napas panjang, lalu mulai.

Pertama, ia membuat folder baru: app/Services dan app/Repositories. Ia membuat file BarangRepository.php dan mulai memindahkan semua *query* SQL ke sana. Ia membuat BarangService.php dan memindahkan logika bisnis—termasuk validasi stok minimal.

Kedua, ia memangkas BarangController.php. Kini *controller* hanya bertugas menerima *request*, memanggil *service*, dan mengembalikan *view*. Tidak ada lagi *query* mentah di dalamnya.

Ketiga, ia membongkar index.blade.php. Ia membuat file *layout* utama: layouts/app.blade.php yang berisi header, sidebar, dan footer. Lalu ia ubah index.blade.php menjadi hanya berisi konten tabel, me-*extends* *layout* utama.

Proses ini memakan waktu hampir dua jam. Setiap kali selesai satu bagian, Binto menjalankan ulang aplikasi. *Masih jalan? Alhamdulillah.* Masih jalan? *Lanjut.*

Mas Alin hanya duduk di sampingnya, sesekali memberi petunjuk kecil: "Nah, itu fungsi cekStokMenipis taruh di *Service*, bukan di *Repository*." Atau: "*Repository* jangan pakai echo. Itu urusan *View*."

## **6.7 Pesan untuk Masa Depan**

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

## **6.8 Konstanta di Tempat Terpusat**

Saat Binto selesai menulis komentar, Mas Alin menunjuk ke nilai 10 yang masih tertulis di dalam *Service*.

"Satu lagi, *Le*. Angka 10 ini kamu taruh di sini. Sudah lumayan, karena sekarang terpusat di satu kelas. Tapi bagaimana kalau nanti ada fitur lain yang juga butuh nilai 10 ini? Atau suatu hari Bu Warsiti minta batas minimalnya diubah jadi 5?"

Binto berpikir. "Saya tinggal ubah di sini, Mas?"

"Iya, kalau cuma satu tempat. Tapi di aplikasi yang lebih besar, bisa jadi ada banyak konstanta seperti ini. Batas stok minimal, biaya pengiriman, persentase pajak, dan lain-lain. Kalau tersebar di berbagai *Service*, kamu harus mencari satu per satu saat ada perubahan."

Mas Alin membuka proyek Pabrik Garum di laptopnya. Ia menunjukkan folder config/.

"Di Laravel, ada folder config khusus buat konfigurasi. Semua nilai yang sifatnya konstan dan mungkin berubah suatu hari, taruh di sini. Misalnya bikin file config/constants.php."

Ia menunjukkan contoh isinya:

php

return \[

    'stok\_minimal' \=\> 10,

    'biaya\_pengiriman' \=\> 15000,

    'pajak\_ppn' \=\> 0.11,

\];

"Kalau begini, semua orang di tim tahu di mana mencari nilai-nilai ini. Mau ubah? Tinggal buka satu file. Bahkan bisa pakai *helper* config('constants.stok\_minimal') di mana saja."

Binto mengangguk paham. "Jadi lebih rapi lagi."

"*Nggih*. Ini *best practice* sederhana. Nilai yang bisa berubah, taruh di tempat terpusat. Jangan *hardcode* di tengah-tengah logika. Nanti susah *maintenance*\-nya."

Binto segera membuat file config/constants.php dan memindahkan nilai 10 ke sana. Ia mengganti kode di *Service* menjadi config('constants.stok\_minimal').

Mas Alin melanjutkan. "Tapi tidak semua konstanta taruh di constants.php. Ada yang lebih cocok di file .env. Misalnya nama toko, alamat, atau *credentials* database. Itu karena tiap *environment* bisa beda. Di lokal kamu namanya 'Toko ATK Warsiti', tapi di *production* nanti bisa jadi 'Warsiti ATK'."

Binto mengangguk. Ia paham sekarang: nilai yang bersifat bisnis dan sama di semua *environment* taruh di config/constants.php. Nilai yang berbeda antar *environment* taruh di .env.

"Sekarang lebih rapi," gumamnya puas.

## **6.9 Testimoni Mbak Rara**

Sore harinya, Mbak Rara selesai dengan tumpukan *test case*\-nya. Ia berjalan ke meja Binto untuk mengisi air di dispenser. Matanya melirik layar Binto.

"Wah, Mas Binto bikin apa ini?"

"Ini program inventaris buat toko ATK adiknya Pakde, Mbak."

Mbak Rara berhenti sejenak. "Boleh lihat kodenya?"

Binto mengangguk, sedikit gugup. Mbak Rara dikenal teliti dan kritis.

Mbak Rara duduk di sebelah Binto. Ia membuka file BarangService.php dan membaca. Matanya bergerak cepat.

"Ini bagus. Ada komentarnya. Jadi aku gak perlu tanya-tanya lagi."

Ia *scroll* ke bawah.

"Ooh, cekStokMenipis di sini. Aku langsung paham alurnya. Jadi kalau ada *bug* di perhitungan stok, aku tinggal lihat *Service* ini aja, gak perlu buka file lain?"

"*Nggih*, Mbak. Logikanya semua di sini."

Mbak Rara tersenyum lebar. "Enak banget ini. Coba kemarin-kemarin kodenya kayak gini, aku gak perlu jungkir balik nyari *bug*."

Binto tersipu. Pujian dari Mbak Rara terasa seperti validasi bahwa ia berada di jalur yang benar.

## **6.10 Refleksi: Kode untuk Manusia**

Sore menjelang adzan ashar di masjid desa. Jam empat kurang sedikit, Binto dan Mas Alin kembali duduk di teras. Pohon rambutan di depan kini berwarna merah merona di banyak bagian. Beberapa hari lagi panen.

"Gimana rasanya?" tanya Mas Alin sambil menyesap kopi dari cangkir enamelnya.

Binto merenung sejenak. "Awalnya males, Mas. Masa cuma program kecil harus dipisah-pisah segala. Tapi setelah jadi... enak lihatnya. Rapi."

"Itulah bedanya *programmer* biasa sama level software *engineer*," Mas Alin meletakkan cangkirnya. "*Programmer* bikin kode biar mesin ngerti. Software *engineer* bikin kode biar manusia juga ngerti. Termasuk dirimu sendiri dua bulan lagi."

Binto mengangguk. Ia teringat bagaimana pagi tadi ia sendiri kesulitan membaca kodenya yang baru berumur satu hari.

"Dan soal komentar tadi," lanjut Mas Alin, "banyak yang males nulis komentar. Katanya: 'Kode yang bagus itu *self-documenting*, gak perlu komentar.' Itu betul, tapi hanya untuk kode yang benar-benar sederhana. Di dunia nyata, kode kita penuh dengan keputusan bisnis yang aneh. Kenapa stok minimal 10? Kenapa biaya kirim 15000? Kenapa pakai algoritma A, bukan B? Itu semua perlu dicatat. Komentar adalah surat cinta untuk dirimu di masa depan."

Binto tersenyum mendengar analogi itu.

"Dan satu lagi, *Le*," Mas Alin menatap Binto serius. "Kode yang kamu tulis hari ini, bisa jadi akan dibaca oleh orang lain bertahun-tahun setelah kamu pindah kerja. Bayangkan mereka buka kode kamu, lihat strukturnya rapi, ada komentarnya. Mereka akan berdoa: 'Semoga orang yang nulis ini selalu diberi kesehatan.' Itu warisan. Itu profesionalisme."

Binto terdiam. Ia tidak pernah berpikir sejauh itu. Selama ini ia hanya berpikir tentang membuat kode yang "jalan". Bukan kode yang "hidup" dan dirawat oleh orang lain.

Cahaya matahari sore mulai melembut. Suara adzan ashar terdengar sayup dari masjid desa, menandakan pukul empat sore telah tiba. Binto menatap pohon rambutan yang buahnya siap panen.

*Kayak kode gue*, pikirnya. *Butuh waktu buat matang. Tapi begitu matang, hasilnya manis.*

"*Matur suwun*, Mas. Hari ini saya belajar banyak."

Mas Alin mengangkat cangkirnya, memberi hormat kecil. "*Sami-sami*, *Le*. Besok kita lanjut lagi. Masih banyak kamar yang perlu disekat di rumahmu."

Mereka tertawa kecil. Burung-burung gereja terbang pulang. Hari hampir berakhir, tapi fondasi rumah kode Mas Binto baru saja dibangun.