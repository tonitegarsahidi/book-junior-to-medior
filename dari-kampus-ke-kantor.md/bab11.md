# **Bab 11: Panggung Gladi Resik**

## **11.1 Si Anak Magang**

Pagi itu, kantor Garda Teknologi Nusantara kedatangan satu penghuni baru. Bukan karyawan tetap, bukan juga klien. Seorang anak laki-laki berbadan kurus, berkacamata tebal, dan membawa tas ransel lusuh yang penuh tempelan stiker band indie.

"Mas Binto, ini Cahyo. Keponakannya Pakde. Lagi PKL sebulan di sini," kata Bu Sari sambil menepuk bahu anak itu.

Cahyo menyalami Binto dengan canggung. "Saya Cahyo, Mas. SMK RPL. Mohon bimbingannya."

Binto tersenyum. *Gue dulu juga kayak gini*, pikirnya. Canggung, polos, dan tidak tahu apa-apa tentang dunia kerja sesungguhnya. Bedanya, dulu Binto masuk ke perusahaan besar di Jakarta dan langsung diceburkan ke pekerjaan administrasi tanpa bimbingan. Cahyo lebih beruntung.

"Ini minggu ketiga kamu, ya, Dik?" tanya Binto.

"*Nggih*, Mas. Dua minggu pertama saya banyak belajar Git sama Mas Alin. Sekarang Mas Alin bilang, minggu ini saya dibimbing Mas Binto."

Binto mengangguk. Ia ingat Mas Alin berpesan kemarin: *"Kamu sudah cukup matang, Le. Sekarang giliranmu ngajarin orang lain. Itu bagian dari jadi medior."*

"Oke. Sekarang lagi ngerjain apa?"

Cahyo membuka laptop tuanya. "Saya diminta perbaiki tampilan laporan di modul Minimarket Kalimantan, Mas. Kemarin ada keluhan dari sales, tombol 'Cetak' di aplikasi mobile terlalu kecil, susah ditekan."

"Itu tugas kecil tapi penting," komentar Binto.

"Sudah selesai, Mas. Tinggal *upload*." Cahyo membuka terminal, sudah siap menjalankan perintah Git untuk *push* langsung ke branch main.

## **11.2 "Jangan Langsung Production"**

"Eh, Dik\! Jangan\! Nanti dulu\!"

Cahyo terlonjak. Tangannya menjauh dari keyboard. "Lho, kenapa, Mas? Kan cuma gedein tombol?"

Binto menarik napas. Ia tahu harus mencegah Cahyo. Tapi saat Cahyo menatapnya dengan mata penuh tanda tanya, Binto sadar: ia sendiri tidak benar-benar paham *kenapa* harus dicegah.

*Gue tahu harus lewat staging dulu. Tapi kenapa? Apa bedanya?*

"Anu, Dik. Harus lewat server *staging* dulu. Nanti kalau Mbak Rara sudah tes dan bilang OK, baru naik ke *production*."

"Server *staging*? Itu yang mana, Mas?"

Binto menoleh ke sudut ruangan. Di sana, sebuah PC tower tua tanpa monitor tergeletak di atas meja kecil. Kabel power terpasang, kabel LAN menyala berkedip hijau.

"Itu lho, yang di pojok," tunjuk Binto.

"Lho, Mas. Katanya itu buat program Koperasi? Yang offline itu?"

Binto terdiam. Benar juga. PC itu adalah server staging untuk proyek Koperasi Sekar Patria—aplikasi yang diinstal offline di komputer klien. Staging-nya pun offline, berupa replika kecil dari setup mereka.

"Kalau proyek Kalimantan, staging-nya di cloud, Dik," suara Mas Andik tiba-tiba dari belakang. Ia lewat sambil membawa gelas kopi. "Servernya di Jakarta. Speknya mirip production, cuma lebih kecil. Alamatnya staging.minimarket-kalimantan.com."

Cahyo mengangguk. "Oh, di cloud. Terus kenapa harus lewat situ dulu, Mas? Kan sama aja. Sama-sama server. Kenapa gak langsung aja biar cepet?"

Pertanyaan sederhana itu menusuk Binto. Ia membuka mulut, tapi tidak ada kata yang keluar.

## **11.3 Bertanya pada Mbak Rara**

"Sebentar, Dik." Binto berdiri. "Kita tanya Mbak Rara dulu."

Mereka berdua berjalan ke meja Mbak Rara yang sedang serius mengetik di laptop. Di depannya, setumpuk kertas *test case* dan pulpen warna-warni berserakan.

"Mbak, maaf ganggu."

Mbak Rara mendongak, melepas kacamatanya. "Ada apa, Mas?"

Binto menghela napas. "Ini Cahyo mau langsung *deploy* ke *production*. Saya bilang jangan, harus lewat *staging* dulu. Tapi dia tanya kenapa. Saya... bingung jelasinnya."

Mbak Rara tersenyum. "Sini, Dik. Duduk dulu."

## **11.4 Panggung Gladi Resik**

Mbak Rara mengambil selembar kertas kosong dan pulpen. Ia mulai menggambar tiga kotak.

"Bayangin, Dik. Kamu mau pentas drama di sekolah."

Cahyo mengangguk. "Pernah, Mbak."

"Nah. Sebelum pentas beneran, kamu pasti latihan dulu di kelas, kan? Itu development. Salah ngomong gak apa-apa. Terus, seminggu sebelum pentas, ada gladi resik di panggung asli, pakai kostum asli, lighting asli. Tapi penontonnya cuma guru dan panitia. Itu staging. Kalau ada yang salah, masih bisa diperbaiki sebelum hari H. Nah, hari H pentas di depan semua orang. Itu production. Salah dikit, malu satu sekolah."

Cahyo manggut-manggut. "Jadi staging itu gladi resik?"

"Persis. Server staging itu panggung gladi resik. Di sana aplikasi berjalan dengan konfigurasi yang sama persis seperti production—database mirip, server mirip, koneksi mirip. Aku bisa uji semua skenario di sana tanpa takut merusak data asli atau bikin pengguna bingung."

Binto mendengarkan dengan seksama. Analogi ini membantunya sendiri memahami.

## **11.5 Server Staging yang Berbeda-beda**

Mas Andik yang masih berdiri ikut menjelaskan. "Biar jelas, Dik. Di kantor ini, setiap proyek punya *environment* yang beda-beda. Proyek Koperasi Sekar Patria itu aplikasinya di-install offline di komputer mereka sendiri. Jadi staging-nya ya komputer di pojok itu tadi—itu replika kecil dari setup mereka."

"Tapi untuk proyek Kalimantan," lanjut Mas Alin yang tiba-tiba muncul dari meja pojoknya, "servernya di cloud. Production di cloud, staging juga di cloud. Hanya beda alamat dan spek. Staging speknya lebih kecil, tapi konfigurasi server-nya sama. Jadi kalau ada bug yang cuma muncul di lingkungan cloud, kita bisa tangkap di staging."

Binto mencatat dalam hati. *Jadi staging itu gak selalu fisik. Bisa di mana saja, asal terpisah dari production.*

## **11.6 Ritual Mbak Rara**

Mbak Rara melanjutkan. "Setiap ada fitur baru—baik dari Mas Binto, Mas Alin, atau kamu, Dik—aku pasti tes dulu di staging. Aku coba semua skenario yang ada di *test plan*\-ku. Aku coba input kosong, karakter aneh, sampai *input* yang gak masuk akal ya."

"Kenapa harus sampai yang gak masuk akal, Mbak?" tanya Cahyo.

"Soalnya biasanya *bug*... atau celah keamanan, justru muncul dari situ," jelas Mbak Rara. 

Binto ikut mengangguk di sebelahnya. Ia teringat bagaimana dulu fitur pesanannya rontok hanya karena Mbak Rara memasukkan stok minus. 

"Ini contohnya," tambah Mbak Rara sambil menunjuk layar. "Kalau aku kasih karakter aneh di *form* pencarian, error-nya beda. Kadang sistem nangkap itu sebagai perintah kode. Hal-hal kecil seperti ini... ternyata bisa berarti banyak buat *hacker*."

Cahyo melongo. Ia mulai paham bahwa peran QA bukan cuma sekadar ngeklik tombol jalan atau tidak. QA adalah penjaga gerbang.

"Terus kalau sudah diuji dan dipastikan oke?" tanya Cahyo lagi.

"Aku bilang 'OK'. Seringnya aku kirim pesan di grup: *'Staging OK. Bisa naik production.'* Baru setelah itu Mas Alin atau Mas Binto *deploy* ke production."

"Itu aturan gak tertulis di sini," tambah Binto. "Aku dulu juga sempat ngeyel. Tapi sekarang paham."

Cahyo mengangguk. "Jadi Mbak Rara yang menentukan layak tidaknya naik?"

"Iya. Aku ini *gatekeeper* kualitas." Mbak Rara terkekeh. "Tapi enak, kan? Kamu jadi tenang. Ada yang ngecek sebelum dilihat orang banyak."

## **11.7 Branching yang Benar: Jangan Campur Sejarah**

Mas Alin berjalan mendekat. "Sekarang saya tunjukkan alur *branching* yang benar. Ini penting, Dik. Banyak yang salah kaprah."

Ia membuka laptop dan menggambar alur sederhana di papan tulis kecil.

"Ada yang pakai cara begini: bikin branch staging, semua fitur di-merge ke staging, kalau sudah OK, staging di-merge ke production. Itu sah, tapi tidak *best practice*."

"Kenapa, Mas?" tanya Cahyo.

"Karena branch staging itu jadi 'kotor'. Isinya campuran dari banyak fitur. Suatu hari, bisa jadi ada fitur yang sudah lolos QA, tapi ditunda deployment-nya karena klien belum mau rilis. Fitur itu tetap nempel di branch staging. Begitu staging di-merge ke production, fitur yang ditunda itu ikut terbawa. Bisa kacau."

Binto membayangkan. "Wah, iya juga."

"Makanya, kami pakai cara ini." Mas Alin menggambar alur baru.

"Setiap ada backlog baru, kita bikin branch fitur dari PRODUCTION—biasanya main atau master. Misal: fitur/tombol-cetak-besar. Kita kerjain di situ. Mau di-test sendiri, silakan."

"Begitu mau di-test oleh Mbak Rara, branch fitur itu kita merge ke staging. Staging hanya berisi kode yang sedang diuji *saat ini*. Bisa satu fitur, bisa beberapa fitur yang siap diuji bersamaan."

"Setelah Mbak Rara kasih lampu hijau, kita merge branch fitur itu langsung ke production. Bukan staging ke production. Jadi yang masuk ke production adalah branch fitur yang bersih, bukan staging yang campur aduk."

Cahyo manggut-manggut. "Jadi staging itu cuma tempat singgah sementara?"

"Persis. Staging adalah panggung gladi resik. Setelah gladi resik selesai, pemain yang tampil di production adalah pemain yang sudah siap, bukan seluruh isi panggung."

"Terus kalau ada fitur yang ditunda?" tanya Binto.

"Branch fitur itu tetap ada. Tapi dia tidak kita merge ke production sampai waktunya tiba. Staging bisa kita reset atau kita bersihkan setelah selesai testing. Production tetap bersih."

Binto mengangguk. "Rapi sekali."

"Ini yang namanya *clean history*. Production hanya berisi kode yang benar-benar sudah *release*. Staging hanya tempat uji. Fitur-fitur yang belum siap tidak akan mencemari production."

## **11.8 Deploy ke Staging Bareng Cahyo**

"Baik," kata Binto. "Sekarang kita praktik. Cahyo, kamu sudah buat branch fitur?"

"Sudah, Mas. Tadi saya buat fitur/tombol-cetak-besar dari main."

"Sekarang *push* ke staging."

Binto memandu Cahyo. Mereka menjalankan perintah Git sederhana untuk menggabungkan branch fitur ke branch staging. Beberapa saat kemudian, notifikasi dari pipeline CI/CD muncul: *Deployment to staging successful*.

"Nah, sudah naik ke staging. Sekarang Mbak Rara coba."

Mbak Rara membuka browser, mengetik alamat staging server—sebuah URL dengan subdomain staging.minimarket-kalimantan.com. Ia masuk ke aplikasi, membuka halaman laporan, dan mencoba tombol cetak.

"Tombolnya sudah lebih besar. Enak ditekan." Ia mengangguk puas.

Lalu ia membuka dari ponselnya. "Lho, ini di iPhone tombolnya bagus. Tapi di Android yang layar kecil, kok malah kepotong?"

Cahyo panik. "Waduh, saya kira aman. Tadi saya coba di laptop saja."

"Nah, ini gunanya staging," kata Mbak Rara. "Di sini aku bisa cek dari berbagai perangkat. Bayangin kalau tadi langsung production, sales yang pakai HP kecil gak bisa pencet tombol."

## **11.9 Perbaiki dan Ulangi**

Cahyo buru-buru membuka file CSS-nya. Ia tambahkan pengaturan untuk layar kecil. Setelah selesai, ia commit ulang, dan *push* lagi ke branch fiturnya. Lalu ia merge ulang ke staging.

Mbak Rara menguji lagi. Kali ini dari tiga jenis ponsel berbeda.

"OK. Sekarang aman."

"Jadi bisa naik production, Mbak?"

"Bisa."

Binto memandu Cahyo. "Sekarang kita merge branch fiturmu langsung ke main. Bukan staging ke main." Cahyo menjalankan perintah Git untuk menggabungkan branch fiturnya ke production. Beberapa menit kemudian, notifikasi sukses muncul.

Cahyo tersenyum lega. "Ternyata panjang juga prosesnya, Mas. Kirain tinggal upload."

"Itulah bedanya *programmer* sama *engineer*," kata Binto, mengutip Mas Alin. "*Programmer* cuma mikirin kode jalan. *Engineer* mikirin dampaknya ke pengguna."

## **11.10 Es Dawet Serabi dan Pelajaran Siang**

Siang itu, matahari bersinar terik. Pakde Suhar muncul dari ruangannya dengan beberapa bungkusan plastik di tangan.

"Wes, jam istirahat. Pada panas-panas gini enaknya yang seger-seger. Tadi aku belikan es dawet serabi."

Sorak kecil menyambut. Mbak Rara buru-buru membersihkan mejanya. Mas Andik mengambil gelas-gelas plastik dari dapur. Pakde membuka bungkusannya: dawet hijau kenyal dalam santan kental, gula merah cair, dan es batu mulai mencair. Di bungkus terpisah, serabi hangat—kue tradisional berbahan tepung beras dan santan, dimasak di atas tungku tanah liat, siap dicocol ke kuah gula merah.

Mereka berlima—Pakde, Mas Alin, Mbak Rara, Binto, dan Cahyo—duduk mengelilingi meja panjang. Sendok plastik beradu dengan gelas.

"Enak tenan iki," gumam Mas Alin.

Cahyo menyesap dawetnya. "Segar, Mas. Di sekolah gak ada yang kayak gini."

Obrolan kembali mengalir ke topik tadi. Mbak Rara, sambil menikmati serabi, berkata, "Nah, Dik. Tadi kamu sudah lihat kan alur branching yang benar? Itu yang bikin kerjaanku enak. Aku bisa tes di staging sepuasnya tanpa takut ngacak production."

Binto menambahkan. "Kamu beruntung, Dik. Di sini kamu diajarin alur kerja yang benar sejak awal. Saya dulu... sebelum kerja di sini, gak tahu apa-apa soal *staging*. Saya kira semua programmer langsung *upload* ke internet, langsung *live*."

Cahyo menatapnya. "Terus gimana, Mas?"

"Untung pas saya masuk sini, Mas Alin langsung kasih tahu: 'Jangan testing di production.' Saya masih ingat muka panik saya waktu itu." Binto terkekeh. "Padahal saya belum pernah *deploy* aplikasi beneran sebelumnya. Cuma ngebayangin aja udah deg-degan."

Mas Alin menimpali. "Justru itu, Dik. Di sini kami udah nemu alur yang pas. Branch fitur dari production, merge ke staging buat tes, kalau OK langsung merge branch fitur ke production. Jadi production tetap bersih. Gak ada fitur setengah matang yang nyempil."

Cahyo mengangguk. "Jadi kuncinya: jangan campur aduk."

"Persis."

Pakde Suhar yang sedari tadi diam ikut berkomentar. "Makanya, Cahyo. Kamu belajar yang bener di sini. Gak semua tempat ngajarin kayak gini. Banyak yang langsung *production*, begitu error malah saling lempar kesalahan."

Cahyo mencatat dalam hati. Pelajaran hari ini bukan cuma soal teknis. Tapi soal *mindset*.

## **11.11 Penutup**

Sore harinya, setelah es dawet habis dan serabi tinggal remah, Binto dan Cahyo kembali ke meja masing-masing. Cahyo merekap pelajaran hari ini di buku catatannya: *Staging adalah gladi resik. Jangan testing di production. Branch fitur dari production, merge ke staging, merge fitur ke production.*

"Mas," panggil Cahyo. "Terima kasih, ya. Hari ini saya belajar banyak."

Binto menepuk bahunya. "*Sami-sami*, Dik. Nanti kalau kamu sudah jadi *engineer* beneran, jangan lupa ngajarin yang lain."

Cahyo mengangguk mantap.

Di luar, sinar matahari sore mulai miring. Suara adzan ashar dari masjid desa desa sayup terdengar, menandakan pukul empat sore telah tiba. Binto menatap ruangan yang mulai sepi. Beberapa bulan lalu, ia datang ke kantor ini dengan kepala tegak dan jiwa "sombong" lulusan PTN ternama. Kini, ia justru belajar dari sebuah tim kecil di gang desa tentang hal-hal yang tak pernah diajarkan di kampus.

*Staging. Git flow. Clean history.*

Dan ia tahu, ini baru satu langkah lagi menuju *medior*.