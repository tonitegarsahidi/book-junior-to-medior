# Bab 2: Mesin Waktu Bernama Git

## 2.1 Warisan Kode

Hari belum berganti. Ini masih hari pertama Binto di Garda Teknologi Nusantara.

Setelah sesi *reality check* yang menghancurkan kepala tegaknya tadi pagi, Binto diberi waktu oleh Mas Alin untuk "berkenalan dengan suasana". Ia berkeliling ruangan, melihat Wawan yang sedang merapikan *padding* dan *margin* di Figma, melirik Mbak Rara yang tampak serius membaca dokumen sambil sesekali mencoret-coret, dan mengamati Bu Sari yang sedang menelepon klien dari Kalimantan dengan suara ramah khas Jawa Timuran.

Tapi pikirannya tidak bisa lepas dari meja pojok itu. Meja Mas Alin. Dengan tiga monitor menyala, *terminal* hitam penuh teks-teks misterius, dan cangkir enamel wayang yang entah sudah berapa hari tidak dicuci.

*Aku kudu belajar dari nol*, batin Binto. *Tapi mulai dari mana?*

Tepat saat adzan Dzuhur berkumandang dari masjid desa sebelah, Mas Alin bangkit dari kursinya. Ia meregangkan badan, menguap lebar, lalu menoleh ke arah Binto.

"Binto, sini, *Le*."

Binto mendekat, menggeser kursinya. Di monitor kanan Mas Alin, sebuah *file explorer* terbuka. Tampak susunan folder: koperasi-sekar-patria/, pabrik-pakan-ternak-garum/, sekolah-alhikmah-malang/, dan beberapa folder lain.

"Ini kode kita," kata Mas Alin sambil menyeruput kopinya yang pasti sudah dingin. "Aplikasi-aplikasi yang tadi pagi saya sebut. Pabrik pakan ternak, koperasi, minimarket, sekolah swasta. Semua disimpan di sini."

Binto mengangguk. "Di laptop Mas Alin sendiri?"

"*Yo enggak to*. Ini cuma tempat saya *ngakses*. Kode aslinya disimpan di... server."

"Server? Maksudnya *cloud*?"

"*Hooh*. Tapi jangan dibayangkan kayak Google Drive atau Dropbox. Ini beda. Ini tempat khusus buat programmer."

Mas Alin membuka aplikasi dengan ikon kucing—bukan kucing asli, tapi ikon hitam putih dengan bentuk geometris.

"Namanya Git."

Mas Alin menatapnya dari pojokan. Mungkin dia lihat Binto yang murung. Mungkin dia lihat remasan di ujung kemeja putih itu. Entahlah. Tapi yang pasti, dia bangkit. Membawa laptop tuanya. Menarik kursi ke dekat meja Binto.

"Sini, Le. Kita mulai dari yang paling dasar."

Binto menelan ludah. "Git, Mas?"

"Git."

---

## 2.2 Mesin Waktu

Mas Alin membuka terminal. Layar hitam. Teks putih. Binto selalu merasa asing sama tampilan kayak gini. Di kampus, mereka diajarin coding pakai IDE warna-warni. Terminal cuma dipakai kalau ada masalah. Itu pun lebih sering minta tolong teman.

"Aku nggak akan banyak ceramah," kata Mas Alin. "Kita langsung coba aja."

Dia membuat folder baru. `belajar-git`.

"Bayangin folder ini proyek kamu. Sekarang, kamu mau Git mengawasi semua yang terjadi di folder ini. Caranya..."

Dia mengetik:

```
git init
```

"Itu... udah?" Binto melongo.

"Udah. Sekarang folder ini jadi *repository*. Git akan nyatet semua perubahan yang terjadi. Setiap file yang kamu tambah. Setiap baris yang kamu ubah. Setiap file yang kamu hapus."

Mas Alin menatap Binto. Matanya sayu, tapi ada kilat kecil di sana. Kilat orang yang excited sama sesuatu.

"Git itu... mesin waktu, Le."

Binto mengerutkan dahi. "Mesin waktu?"

---

## 2.3 Skripsi yang Hilang

"Coba inget-inget. Waktu kamu ngerjain skripsi dulu. Gimana caranya kamu nyimpen file?"

Binto berpikir. Skripsi. Ah. Itu masa-masa yang...

"Saya bikin folder *backup*, Mas. Tiap kali ada perubahan besar, saya *copy-paste* folder proyek. Kasih nama: `Project_Backup_12_Juni_FINAL`."

Mas Alin menyeringai. "Terus?"

"Terus... besoknya ada revisi lagi. Jadi `Project_Backup_12_Juni_FINAL_REV1`."

"Terus?"

"Terus... `Project_Backup_12_Juni_FINAL_REV2_FIX`."

Mas Alin tertawa. Bukan mengejek. Lebih mirip... nostalgia.

"Kamu tahu nggak, Le. Itu yang saya lakukan juga waktu awal-awal. Sepuluh tahun lalu. Dua belas tahun lalu. Semua programmer pemula begitu. Bikin folder *backup* dengan nama yang makin lama makin panjang dan makin nggak jelas."

Dia menyesap kopinya.

"Tapi masalahnya... suatu hari kamu lupa *backup*. Atau *backup*-nya ketimpa. Atau kamu nggak inget *backup* yang mana yang isinya fitur terbaru. Dan tiba-tiba... kerjaan seminggu hilang. Cuma karena kamu salah *copy-paste* folder."

Binto terdiam. Itu persis yang pernah terjadi padanya. Semester lima. Tugas besar. Begadang tiga malam. File-nya corrupt. Dia nangis di kosan.

"Git itu... *backup* yang jauh lebih canggih," kata Mas Alin. "Setiap perubahan yang kamu lakukan... Git nyimpen. Kapan aja kamu mau balik ke versi sebelumnya... tinggal panggil. Gak perlu *copy-paste* folder. Gak perlu nama file kayak `FINAL_REV2_FIX_BENERAN`. Semua rapi. Semua tercatat."

---

## 2.4 Absen dan Buku Harian

Mas Alin membuat file baru. `halo.txt`. Isinya cuma satu baris: "Halo Dunia".

"Sekarang kita lihat status."

```
git status
```

Terminal menampilkan sesuatu. Ada tulisan *Untracked files*. Di bawahnya: `halo.txt`.

"Lihat. Git tahu ada file baru. Tapi belum dicatat secara resmi. Kayak orang baru datang ke kantor... belum absen. Dia ada. Tapi belum masuk daftar kehadiran."

Binto manggut-manggut. Analogi sehari-hari. Mas Alin memang selalu begitu. Nggak pernah pakai jargon yang bikin pusing.

"Biar ke-track, kita pakai `git add`."

```
git add halo.txt
```

"Git add itu kayak kamu bilang ke Git: 'Hei, catat perubahan di file ini.' Tapi ini baru setengah jalan. File ini baru masuk ke *staging area*. Kayak kamu udah tanda tangan absen... tapi belum masuk database HRD."

Binto nyengir. "Ini HRD-nya galak nggak, Mas?"

"Nggak. Tapi teliti." Mas Alin melanjutkan. "Kalau udah yakin sama perubahannya... baru kita `commit`."

```
git commit -m "Pesan pertama: halo dunia"
```

"Commit itu kayak simpan permanen. Masuk ke buku harian Git. Setiap *commit* punya... nomor unik. Penulis. Tanggal. Dan pesan. Ini yang bikin Git jadi mesin waktu. Kamu bisa balik ke *commit* mana pun... kapan aja."

Mas Alin menunjukkan log-nya:

```
git log
```

Layar menampilkan satu baris. Kode acak. Nama "alin". Tanggal. Dan pesan: "Pesan pertama: halo dunia".

"Kode acak ini namanya *hash*. Itu alamat di mesin waktu. Kalau kamu mau balik ke sini... kamu tinggal panggil alamat ini."

Binto menatap layar. Matanya mulai berbinar. *Ini... keren juga.*

---

## 2.5 Jangan Kayak Gini

Tapi Mas Alin belum selesai. Dia membuka terminal lagi. Mengetik sesuatu.

"Sekarang lihat ini."

```
commit a1b2c3d4...
Author: prog_baru <progbaru@mail.com>
Date:   Thu Apr 16 10:14:22 2026 +0700

    perbaiki dikit
```

Binto membaca. "Apa yang diperbaiki, Mas?"

"Nah. Itu dia. Kamu aja bingung. Apalagi temenmu yang lain." Mas Alin menatapnya serius. "Coba bayangin. Tiga bulan lagi kamu balik baca log ini. Kamu inget nggak... 'dikit' yang mana? Ngubah warna tombol? Nambah validasi? Hapus *bug* yang bikin server down? Kamu nggak akan tahu."

Dia mengetik lagi.

"Sekarang bandingkan sama ini:"

```
commit e5f6g7h8...
Author: alin <alinsholeh@gmail.com>
Date:   Thu Apr 16 10:18:45 2026 +0700

    fix: perbaiki validasi tanggal lahir kosong di form registrasi

    Sebelumnya user bisa submit form tanpa mengisi tanggal lahir,
    menyebabkan error 500 di server.
```

"Ini baru *commit* yang baik. Judulnya jelas. Ada penjelasannya. Jadi orang lain — termasuk kamu sendiri tiga bulan lagi — langsung paham apa yang diubah. Dan kenapa."

Binto membaca lagi log `perbaiki dikit`. Lalu melihat folder *backup* skripsinya di memori: `Project_Backup_12_Juni_FINAL_REV2_FIX`.

*Sama aja*, pikirnya. *Sama kacau dan nggak jelasnya.*

---

## 2.6 Cabang-Cabang

Mas Alin meregangkan lehernya. Matanya melirik ke luar jendela.

"Coba lihat pohon rambutan itu."

Binto menoleh. Pohon rambutan di depan kantor. Batangnya kokoh. Dari batang itu... tumbuh lima cabang besar. Masing-masing punya ranting sendiri. Daun sendiri. Buah sendiri — masih hijau, masih kecil.

"Dulu waktu saya pertama datang ke sini... pohon itu cuma punya satu batang utama. Kecil. Sekarang lihat. Lima cabang. Masing-masing cabang hidup sendiri-sendiri. Kalau satu cabang patah kena angin... cabang lain tetap hidup."

Mas Alin kembali menatap terminal.

"Di Git, kita bisa bikin *branch*. Cabang. Setiap cabang itu salinan dari kode utama. Tapi kamu bisa ubah sesukamu... tanpa merusak yang utama. Nanti kalau udah yakin... baru digabung lagi."

Dia mengetik:

```
git branch fitur-pinjaman
```

"git branch bikin cabang baru. Untuk pindah ke cabang itu... checkout."

```
git checkout fitur-pinjaman
```

Sekarang Binto lihat di terminal ada indikator `(fitur-pinjaman)`. "Jadi sekarang saya ada di cabang baru?"

"Iyo. Di cabang ini... kamu bebas ngubah apa pun. Kode di cabang utama — biasanya namanya `main` atau `master` — tetap aman."

Mas Alin mengubah file `halo.txt`. Menambahkan baris: "Selamat datang di Blitar". Lalu commit.

"Sekarang balik ke utama."

```
git checkout main
```

File `halo.txt` kembali ke versi semula. Baris "Selamat datang di Blitar"... hilang.

Binto melongo. "Lho? Kok hilang?"

"Karena perubahan tadi ada di cabang fitur-pinjaman. Di cabang main... belum ada perubahan apa-apa. Makanya cabang itu aman. Kamu bisa eksperimen di cabang sendiri... tanpa takut merusak yang utama."

Binto mulai melihat gambaran besarnya. Ini kayak punya *save file* di game. Sebelum lawan *boss*... *save* dulu. Kalau mati... tinggal *load* lagi.

---

## 2.7 Penyelamat di Saat Genting

Mas Alin tiba-tiba berhenti. Menatap Binto dengan ekspresi serius.

"Ada satu perintah lagi yang sering nyelametin nyawa programmer. Namanya `git stash`."

"Stash? Kayak simpenan?"

"Tepat. Bayangin kamu lagi asyik ngoding di cabang fitur-pinjaman. Belum selesai. Belum rapi. Belum siap di-commit. Tiba-tiba..."

Dia menjentikkan jari.

"...Mbak Rara teriak dari depan. 'Koperasi Sekar Patria error!' Kamu harus segera pindah ke cabang utama buat perbaiki bug. Tapi kamu belum mau commit kode yang berantakan itu. Gimana?"

Binto menggaruk kepala. "Ya... commit aja paksa?"

"Jangan." Mas Alin menggeleng keras. "Commit setengah jadi itu dosa. Nanti *history*-nya kotor. Solusinya..."

```
git stash
```

Mas Alin mendemonstrasikan. Dia membuat perubahan acak di `halo.txt`. Lalu `git stash`. Perubahan menghilang. File kembali bersih.

"Stash itu kayak kamu taruh pekerjaanmu di laci. Aman. Nanti kalau bug darurat udah beres... kamu bisa ambil lagi dari laci."

```
git stash pop
```

Perubahan acak tadi muncul kembali. Seperti sulap.

Binto terkagum. "Ini sih kayak..."

"Bukan sulap," potong Mas Alin. "Ini penyelamat. Kamu akan sering pakai ini."

---

## 2.8 Ketika Dua Dunia Bertabrakan

Sesi berlanjut. Di luar, suara anak-anak sekolah mulai terdengar. Wawan, yang dari tadi sibuk dengan Figma-nya, melirik ke arah Binto dan Mas Alin yang serius di depan laptop. Tapi dia nggak ikut nimbrung. Mungkin ngerti ini sesi penting.

"Sekarang... bagian paling mendebarkan," kata Mas Alin. Senyum misterius. "Merge conflict."

Binto meneguk ludah. "Konflik? Kayak perang?"

"Nggih. Perang kecil. Tapi bisa diselesaikan dengan kepala dingin."

Mas Alin membuat dua cabang dari main. `cabang-a` dan `cabang-b`. Di `cabang-a`, dia mengubah baris pertama `halo.txt` jadi "Halo Blitar". Di `cabang-b`, dia mengubah baris yang sama jadi "Halo Indonesia".

Lalu dia gabungkan `cabang-a` ke main. Berhasil. Tidak ada masalah.

"Tapi... coba sekarang kita gabung `cabang-b`."

```
git merge cabang-b
```

Terminal menampilkan pesan merah:

```
CONFLICT (content): Merge conflict in halo.txt
Automatic merge failed...
```

" Nah, ini dia. Git bingung. Di main... baris pertama isinya 'Halo Blitar'. Di cabang-b... isinya 'Halo Indonesia'. Git nggak tahu mana yang benar. Jadi Git minta bantuan manusia."

Mas Alin membuka file `halo.txt`. Isinya sekarang aneh:

```
<<<<<<< HEAD
Halo Blitar
=======
Halo Indonesia
>>>>>>> cabang-b
```

"Lihat. Git nunjukin dua versi yang bertabrakan. Tugasmu: pilih salah satu. Atau bikin versi gabungan. Lalu hapus tanda-tanda ini."

Dia menghapus tanda konflik. Memilih: "Halo Blitar dan Indonesia". Simpan. Lalu:

```
git add halo.txt
git commit -m "Selesaikan konflik: gabungkan salam"
```

"Berhasil. Konflik selesai."

Binto menghela napas lega. "Ternyata nggak serem-serem amat."

"Loh iya sekarang. Kalau konflik di sepuluh file... baru kamu ngerti rasanya hidup, Le."

---

## 2.9 Wawan dan Pekerjaan Sebenarnya

Sesi selesai menjelang dzuhur. Mas Alin kembali ke pojokannya. Ada notifikasi dari server Kalimantan. *Error* lagi.

Binto menatap layarnya. Terminal masih terbuka. `git log` masih menampilkan *commit-commit* barusan. Kepalanya penuh. Tapi ada rasa puas yang aneh.

*Aku baru tau ternyata kayak gini.*

---

Wawan lewat. Tumbler jumbo-nya ditaruh di meja. Dia melirik layar Binto.

"Wih, Mas Binto udah belajar Git? Cepet juga."

Binto tersenyum kikuk. "Baru mulai, Wan. Masih banyak yang nggak ngerti."

"Ah, biasa. Dulu aku juga gitu." Wawan duduk di kursi sebelah. "Waktu pertama kali Mas Alin ngajarin Git... aku sampe pusing tiga hari. Branch? Merge? Konflik? Kepalaku rasanya mau meledug, Mas."

Dia ketawa kecil.

"Tapi Mas Alin sabar banget. Nggak pernah marah. Nggak pernah ngejek. Dia cuma bilang: 'Wes, Le. Aku juga dulu kayak kamu. Malah lebih parah. Laptopku pernah kebanting gara-gara git reset.'"

Binto tertawa. "Serius?"

"Serius. Tanya aja sendiri." Wawan menunjuk Mas Alin dengan dagunya. "Itu orang, Mas. Ilmunya banyak. Tapi dia nggak akan kasih tahu... kecuali kamu nanya. Atau... kecuali kamu ngelakuin kesalahan dulu."

Dia berhenti. Menatap Binto.

"Jadi... santai aja. Salah itu biasa. Nanti juga bisa sendiri."

---

Binto menatap Wawan. Anak ini... lulusan SMK. Belajar HTML dan CSS dari YouTube. Dan sekarang dia duduk di sini... ngasih semangat ke lulusan PTN top.

*Aku yang seharusnya kasih semangat ke dia*, pikir Binto. *Kenapa malah kebalik?*

Tapi entah kenapa... kata-kata Wawan tadi ngena. *Salah itu biasa. Nanti juga bisa sendiri.*

Mungkin karena dia ngomongnya nggak kayak dosen. Nggak kayak motivator. Dia ngomong kayak... temen.

---

## 2.10 Wawan dan Kuliah Malam

Azan Ashar mulai terdengar dari kejauhan. Di desa sini, adzan memang dikumandangkan jam empat sore — menunggu para petani pulang dari sawah.

Jam kerja di kantor GTN pun ikut ritme itu. Jam empat sore, selesai.

Mas Alin menggeliat meregangkan tubuhnya, lalu mematikan komputernya.

"Untuk hari pertama, itu dulu, *Le*. Kamu sudah belajar *init*, *status*, *add*, *commit*, *branch*, *checkout*, *stash*, *merge*, dan *konflik*. Itu bekal utama."

Binto mengangguk. Kepalanya penuh dengan istilah baru, tapi ada rasa puas yang aneh. Di kampus, ia tidak pernah menyentuh hal-hal ini. Semua serba instan: *download ZIP*, *copy-paste folder*, atau kirim lewat WA.

"Besok," lanjut Mas Alin sambil meraih kunci motor, "kita akan lihat kode asli punya Koperasi Sekar Patria. Kamu akan *clone* dari *cloud* ke laptopmu. Nanti kamu lihat sendiri, berapa banyak branch yang sudah dibuat Wawan sama aku. Berapa banyak *commit* yang sudah kami tulis. Git itu bukan sekadar *tools*. Git itu budaya. Budaya kolaborasi."

Binto bangkit, meraih helm-nya. "Mas, satu pertanyaan lagi."

"Apa?"

"Tadi Mas Alin bilang Git itu mesin waktu. Tapi kok perintahnya banyak banget?"

"Kayak pertama kali bawa motor, Le. Gasnya nyentak-nyentak, remnya dadakan." Mas Alin tertawa kecil. "Tapi percayalah. Begitu kamu terbiasa, kamu akan heran kenapa dulu bisa hidup tanpa Git. Kayak motor tadi — begitu udah hafal, dia kayak perpanjangan badanmu."

Binto tersenyum. "Siap, Mas. *Matur suwun*."

Mas Alin menyalakan Astrea Grand-nya, melambaikan tangan singkat, lalu melesat pergi diiringi suara knalpot yang menderu pelan.

Binto berbalik untuk mengambil jaketnya di dalam. Kantor sudah sepi. Mbak Rara sudah pulang sejak setengah jam lalu. Bu Sari yang tinggal di sebelah kantor juga sudah tidak terlihat. Namun, saat melewati deretan meja, ia melihat Wawan masih duduk termenung di depan komputernya, tampak serius mengetik sesuatu, keningnya berkerut rapat.

"Belum balik, Wan? Lagi lembur kah?" sapa Binto sambil memakai jaketnya.

Wawan mendongak, terkejut sesaat sebelum tersenyum canggung. Ia buru-buru meminimalkan jendela browser-nya, tapi Binto sempat melihat sekilas logo universitas dan deretan teks berformat makalah.

"Eh, Mas Binto. Enggak kok, ini bukan kerjaan kantor," jawab Wawan sambil menggaruk tengkuknya. "Lagi ngerjain tugas kuliah."

"Kuliah?" Binto mengangkat alis. Setahunya, Wawan lulusan SMK dan sudah bekerja *full-time* di GTN sejak lulus.

Wawan menghela napas pelan. "Iya, Mas. Aku nyambi ambil kuliah online, jurusan IT. Sudah masuk semester tujuh sekarang."

"Wah, keren dong. Jarang loh orang bisa kerja sambil kuliah"

"Aku ngerasa beruntung banget bisa kerja di sini, Mas. Pakde Suhar sama Mas Alin percaya sama kemampuanku meski ijazahku cuma SMK. Tapi di luar sana... Mas tahu sendirilah gimana orang mandang lulusan SMK. Sering diremehin. Dianggap cuma tukang gambar atau teknisi kabel."

Binto terdiam. Ia tiba-tiba teringat kesombongannya sendiri tadi pagi—merasa superior hanya karena membawa ijazah PTN ternama. Di hadapannya kini, seorang lulusan SMK yang jauh lebih jago bekerja secara diam-diam berjuang mendapatkan ijazah sebuah PTS online yang selama ini Binto anggap "biasa saja".

"Semangat, Wan. Nggak gampang lho kerja *full-time* sambil kuliah," ucap Binto tulus. "Kalau butuh bantuan soal tugas-tugas teori, algoritma, atau apalah, bilang aja. Aku bantu sebisa mungkin."

Mata Wawan berbinar. "Serius, Mas? Beneran ya? Aku rada pusing nih soal program skripsiku."

"Santai. Anggap aja barter. Ntar kamu ajarin aku *layout*, aku bantu program."

Wawan tersenyum lebar, lalu membalik layarnya ke arah Binto. Di layar iMac-nya, Figma terbuka dengan puluhan *artboard* berjejer rapi. Binto sempat terpana melihat betapa banyaknya.

"Ini proyek Pabrik Garum, Mas. Dua puluh *screen*. Setiap *screen* harus konsisten—warnanya, *spacing*-nya, *icon*-nya, ukuran fontnya. Kalau satu aja beda sendiri, klien langsung ngeluh: *'Kok ini beda ya?'* Ribet juga lho ternyata bikin yang kelihatan 'simpel'."

Binto menatap layar itu. *Dua puluh screen. Konsisten semua. Dan orang bilang desainer cuma "tukang gambar"?*

Keduanya tertawa kecil. Binto menepuk bahu Wawan sekilas sebelum melangkah keluar.

Ia menyalakan motor Beat-nya. Di depan, pohon rambutan bergoyang pelan ditiup angin sore. Buah-buahnya yang masih hijau bergelantungan, sabar menunggu waktunya memerah.

*Besok*, pikir Binto. *Aku akan belajar lagi. Bukan cuma belajar coding, tapi belajar menghargai proses orang lain. *

Motor beat-nya melaju pelan melewati gang desa, menuju rumah Bapak yang hanya dua puluh menit jauhnya.

---

## 2.11 Mesin Waktu untuk Diri Sendiri

Di atas motor, pikirannya kembali ke sesi Git tadi. *Mesin waktu.* Mas Alin bilang Git bisa balikin kode ke versi sebelumnya. Tahu siapa yang ubah apa. Kapan. Kenapa.

*Bukan cuma buat kode*, pikir Binto.

*Tapi mungkin... juga buat aku.*

*Biar aku bisa balik ke masa lalu. Liat aku yang dulu. Aku yang sombong. Aku yang ngerasa paling pinter cuma gara-gara ijazah.*

*Dan aku bisa bilang ke dia... "Hei. Kamu belum jadi apa-apa."*

---

Di perjalanan, dia ingat sesuatu. Waktu semester lima. Ada dosen yang nyebut Git sekilas. Cuma sekilas. "Nanti kalian bisa pakai Git buat ngumpulin tugas." Itu aja. Nggak ada praktik. Nggak ada penjelasan. Dosennya sendiri mungkin juga nggak terlalu ngerti.

*Kenapa kampus nggak ngajarin ini dari awal?* pikirnya. *Kenapa aku harus nunggu kantor kecil di belakang pasar... buat belajar sesuatu yang sebenernya basic banget?*

Tapi kemudian dia ingat kata-kata Mas Alin. "Ini bukan salahmu."

Dan Wawan tadi siang. *"Salah itu biasa. Nanti juga bisa sendiri."*

Dan untuk pertama kalinya... dia nggak nyalahin siapa-siapa. Bukan nyalahin kampus. Bukan nyalahin dosen. Bukan nyalahin dirinya sendiri.

Cuma... menerima.

Bahwa ternyata... ada banyak hal yang nggak dia tahu. Dan itu... nggak apa-apa.

Yang penting... dia mau belajar.

---

Motor Beat-nya berbelok ke jalan berpaving, menuju rumah Bapak.

Dua puluh menit. Seperti biasa.

Tapi hari ini... dua puluh menit itu terasa lebih ringan.

Mungkin karena di dalam kepalanya... ada sesuatu yang baru. Sesuatu yang mulai tumbuh.

Seperti pohon rambutan itu.

Cabangnya masih sedikit. Buahnya masih hijau.

Tapi dia tahu...

suatu hari...

buahnya akan merah.

Dan manis.

