# **Bab 2: Mesin Waktu Bernama GIT**

## **2.1 Warisan Kode**

Hari belum berganti. Ini masih hari pertama Binto di Garda Teknologi Nusantara.

Setelah sesi *reality check* yang menghancurkan kepala tegaknya tadi pagi, Binto diberi waktu oleh Mas Alin untuk "berkenalan dengan suasana". Ia berkeliling ruangan, melihat Wawan yang sedang merapikan *padding* dan *margin* di Figma, melirik Mbak Rara yang tampak serius membaca dokumen sambil sesekali mencoret-coret, dan mengamati Bu Sari yang sedang menelepon klien dari Kalimantan dengan suara ramah khas Jawa Timuran.

Tapi pikirannya tidak bisa lepas dari meja pojok itu. Meja Mas Alin. Dengan tiga monitor menyala, *terminal* hitam penuh teks-teks misterius, dan cangkir enamel anime yang entah sudah berapa hari tidak dicuci.

*Gue kudu belajar dari nol*, batin Binto. *Tapi mulai dari mana?*

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

## **2.2 Bukan Sekadar Download ZIP**

"Git?" Binto mengulang. "Itu yang buat *download* kode dari internet kan? Saya sering pakai. Tinggal klik tombol hijau, *Download ZIP*..."

Mas Alin mengangkat tangan, menghentikan Binto. Wajahnya antara geli dan miris.

"Git itu bukan cuma tempat nyimpen kode. Git itu mesin waktu."

Binto mengerutkan dahi. "Mesin waktu?"

"Gini lho, Le. Bayangin kamu baru selesai skripsi. ZIP itu ibarat file PDF skripsi yang sudah kamu *export* final. Kamu punya isinya lengkap, bisa kamu baca, bisa kamu kirim ke orang lain. Tapi, PDF itu 'mati'. Kamu gak bisa tahu kalau Bab 2 itu sebenarnya pernah direvisi lima kali karena dosenmu galak. Kamu gak bisa lihat paragraf mana yang kamu hapus minggu lalu tapi tiba-tiba sekarang kamu butuhkan lagi."

Binto manggut-manggut, mulai menangkap arah pembicaraan mentor barunya.

"Nah, Git itu bukan cuma file skripsinya, tapi seluruh buku draf dan rekaman bimbinganmu. Di dalam Git, tersimpan rapi catatan: 'Tanggal 10 Desember, Binto ganti judul karena disuruh dosen A'. Atau 'Tanggal 15 Desember, Binto hapus paragraf ini karena ternyata salah kutip'. Jadi kalau suatu saat kamu menyesal sudah menghapus sesuatu, kamu tinggal buka 'mesin waktu' itu dan ambil lagi datanya."

"ZIP itu cuma hasil akhir. Git itu adalah sejarah perjuangan di balik kode itu. Paham?"

"Kamu pernah ngerasa takut *ngedit* kode? Takut kalau rusak, terus kamu nggak bisa balikin lagi kayak semula?"

Binto mengangguk pelan. Selama kuliah, itulah ritualnya. Sebelum mengubah kode besar, ia selalu *copy-paste* folder proyek, memberi nama Project\_Backup\_12\_Juni\_FINAL atau Project\_Backup\_12\_Juni\_FINAL\_REV1. Kalau kodenya rusak, ia akan *copy-paste* lagi dari folder *backup*. Tapi kalau lupa *backup*? Mampus sudah. Begadang semalaman memperbaiki.

"Nah, Git ini *backup* yang jauh lebih canggih. Setiap perubahan yang kamu lakukan, Git nyimpen. Kapan aja kamu mau balik ke versi sebelumnya, tinggal pencet tombol. Gak perlu *copy-paste* folder gak jelas."

Mas Alin membuka *terminal*—layar hitam dengan teks putih. Binto sedikit bergidik. *Terminal* selalu terasa asing. Di kampus, mereka diajari *ngoding* pakai IDE berwarna-warni. *Terminal* cuma dipakai kalau ada masalah dengan *library* atau *path*.

"Tenang," kata Mas Alin seolah membaca pikirannya. "Kita cuma perlu beberapa perintah dasar. Nanti juga hafal sendiri."

## **2.3 Membuka Buku Harian Proyek**

"Kita mulai dari awal ya. Kamu belum punya proyek apa-apa. Kamu mau mulai bikin proyek baru. Langkah pertama?"

Binto berpikir. "Bikin folder baru?"

"Bener. Bikin folder. Tapi setelah itu, kamu harus bilang ke Git: 'Hei, folder ini akan aku awasi. Tolong catat semua perubahan yang terjadi.' Nah, caranya dengan perintah ini."

Mas Alin mengetik di terminal:

```bash
alin:~$ git init
```

"Aku lagi Inisialisasi. *Init*. Artinya, mulai sekarang Git akan memantau folder ini. Folder ini jadi repository."

Di layar, muncul teks:

```text
Initialized empty Git repository in ....
```

Binto memperhatikan.

"Gampang kan? Sekarang coba kita lihat statusnya."

Mas Alin membuat sebuah file teks sederhana bernama `halo.txt` berisi "Halo Dunia". Lalu ia mengetik:

```bash
alin:~$ git status
```

Terminal kini menampilkan sesuatu:

```text
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        halo.txt
```

"Lihat, Binto. Git bilang file halo.txt ini *untracked*. Artinya Git tahu ada file baru, tapi belum dicatat secara resmi. Kayak orang baru datang ke kantor, belum absen. Dia ada, tapi belum masuk daftar kehadiran."

Binto mengangguk. "Terus biar ke-*track*, gimana?"

"Pakai `git add`."

```bash
alin:~$ git add halo.txt
```

"git add itu seperti kamu bilang ke Git: 'Hei, catat perubahan di file ini.' Setelah di-*add*, file ini masuk ke staging area. Kayak kamu sudah tanda tangan absen, tapi belum masuk ke database HRD."

Binto tersenyum kecil. Penjelasan Mas Alin selalu pakai analogi sehari-hari.

"Kalau sudah yakin dengan perubahanmu, baru kamu `commit`."

```bash
alin:~$ git commit -m "Pesan pertama: halo dunia"
```

"commit itu seperti kamu simpan permanen ke buku harian Git. Setiap *commit* punya nomor unik, penulis, tanggal, dan pesan. Ini yang bikin Git jadi mesin waktu. Kamu bisa balik ke *commit* mana pun kapan saja."

"Nanti kalau sudah terbiasa, kamu bisa shortcut. Tapi penting ngerti konsepnya dulu," tambah Mas Alin.

Mas Alin menunjukkan *log*-nya:

```text
alin:~$ git log
commit 63bebb491218d6c72098... (HEAD -> master)
Author: alin <alinsholeh@gmail.com>
Date:   Wed Apr 15 21:32:05 2026 +0700

    Pesan pertama: halo dunia
```

Layar menampilkan satu baris *commit* dengan kode acak, nama "Alin", tanggal, dan pesan "Pesan pertama: halo dunia".

"Kode acak ini namanya *hash*. Itu alamat di mesin waktu. Kalau kamu mau balik ke sini, kamu tinggal panggil alamat ini."

"Hash ini kayak jejak di mesin waktu kita," lanjut Mas Alin. "Sebagai bukti perubahan. Kalau ada yang aneh di sistem, kita bisa lacak siapa ubah apa. Itu penting buat debugging... dan kadang buat keamanan juga."

Binto manggut-manggut. "Jadi tiap kali aku *ngoding*, aku harus *add* terus *commit*?"

"Ada sih *shortcut*-nya biar sekaligus, tapi sebagai awalan, idealnya begitu. Tapi jangan *commit* sembarangan. *Commit* itu buat perubahan yang bermakna. Misal: 'tambah fitur login', 'perbaiki bug perhitungan bunga', atau 'update warna tombol'. Bukan *commit* dengan pesan 'perbaiki dikit' atau 'lupa tadi'."

## **2.4 Cabang-Cabang Kehidupan**

Mas Alin meregangkan lehernya. Matanya melirik ke luar jendela.

"Coba Lihat pohon rambutan di depan."

Binto menoleh. Pohon rambutan itu masih hijau buahnya, bergelantungan di ujung-ujung ranting.

"Dulu waktu saya pertama pindah ke sini, pohon itu cuma punya satu batang utama. Kecil. Sekarang lihat. Ada lima cabang besar. Masing-masing cabang punya ranting sendiri, daun sendiri, buah sendiri. Kalau satu cabang patah kena angin, cabang lain tetap hidup. Kode kita juga harus begitu."

Mas Alin kembali menatap terminal.

"Di Git, kita bisa bikin branch—cabang. Setiap cabang itu salinan dari kode utama, tapi kamu bisa ubah sesukamu tanpa merusak yang utama. Nanti kalau sudah yakin, baru digabung lagi ke batang utama."

Ia mengetik:

```bash
alin:~$ git branch fitur-pinjaman
```

"`git branch` bikin cabang baru bernama 'fitur-pinjaman'. Untuk pindah ke cabang itu, pakai `checkout`."

```bash
alin:~$ git checkout fitur-pinjaman
```

"Atau bisa sekaligus: git checkout \-b fitur-pinjaman."

Sekarang Binto melihat di terminal ada indikator (fitur-pinjaman). "Jadi sekarang aku ada di cabang baru?"

"*Iyo*. Di cabang ini, kamu bebas ngubah apa pun. Kode di cabang utama—biasanya namanya main atau master—tetap aman."

Mas Alin membuka file halo.txt, menambahkan baris "Selamat datang di Blitar". Lalu ia *add* dan *commit* di cabang fitur-pinjaman.

"Sekarang coba kita balik ke cabang utama."

```bash
alin:~$ git checkout main
```

File halo.txt kembali ke versi semula. Baris "Selamat datang di Blitar" hilang.

Binto melongo. "Lho? Kok hilang?"

"Karena perubahan tadi ada di cabang fitur-pinjaman. Di cabang main, belum ada perubahan apa-apa. Makanya cabang itu aman. Kamu bisa eksperimen di cabang sendiri tanpa takut merusak yang utama."

Binto mulai melihat gambaran besarnya. Ini seperti punya *save file* di game RPG. Sebelum melawan *boss*, dia bisa *save* dulu. Kalau mati, tinggal *load* lagi.

## **2.5 Menyelamatkan yang Belum Jelas**

Mas Alin tiba-tiba berhenti. Ia menatap Binto dengan ekspresi serius.

"Ada satu perintah lagi yang sering nyalametin nyawa programmer. Namanya git stash."

"Stash? Kayak simpenan?"

"Tepat. Bayangin kamu lagi asyik *ngoding* di cabang fitur-pinjaman. Belum selesai, belum rapi, belum siap di-*commit*. Tiba-tiba ada *bug* darurat di cabang main. Mbak Yuni teriak dari depan: 'Koperasi Sekar Patria error\!' Kamu harus segera pindah ke main buat perbaiki *bug*. Tapi kamu belum mau *commit* kode yang berantakan itu. Gimana?"

Binto menggaruk kepala. "Ya... *commit* aja paksa?"

"Jangan. *Commit* setengah jadi itu dosa. Nanti *history*\-nya kotor. Solusinya: git stash."

Mas Alin mendemonstrasikan. Ia membuat beberapa perubahan acak di file `halo.txt` di cabang `fitur-pinjaman`. Lalu ia mengetik:

```bash
alin:~$ git stash
```

Perubahan menghilang. File kembali bersih seperti *commit* terakhir.

"stash itu kayak kamu taruh pekerjaanmu di laci. Aman. Nanti kalau *bug* darurat sudah beres, kamu bisa ambil lagi dari laci dengan git stash pop."

Ia mengetik git stash pop. Perubahan acak tadi muncul kembali.

"Mantap," Binto bergumam. "Ini sih kayak sulap."

"Bukan sulap. Ini penyelamat. Kamu akan sering pakai ini."

## **2.6 Ketika Dua Dunia Bertabrakan**

Sesi berlanjut hingga sore. Di luar, suara anak-anak pulang sekolah mulai terdengar. Wawan sudah membereskan tasnya, pamit duluan karena ada pesanan desain banner untuk acara desa. Mbak Rara masih sibuk dengan *spreadsheet*\-nya.

"Sekarang kita masuk ke bagian paling mendebarkan," kata Mas Alin sambil tersenyum misterius. "Merge conflict."

Binto meneguk ludah. "Konflik? Kayak perang?"

"*Nggih*. Perang kecil. Tapi bisa diselesaikan dengan kepala dingin."

Mas Alin membuat dua cabang dari main: cabang-a dan cabang-b. Di cabang-a, ia mengubah baris pertama halo.txt menjadi "Halo Blitar". Di cabang-b, ia mengubah baris yang sama menjadi "Halo Indonesia".

Lalu ia mencoba menggabungkan `cabang-a` ke `main`:

```bash
alin:~$ git checkout main
alin:~$ git merge cabang-a
```

Berhasil. Tidak ada masalah.

"Tapi coba sekarang kita gabungkan cabang-b ke main."

Mas Alin mengetik `git merge cabang-b`. Terminal menampilkan pesan merah:

```text
CONFLICT (content): Merge conflict in halo.txt
Automatic merge failed; fix conflicts and then commit the result.
```

"Nah, ini dia. Git bingung. Di main, baris pertama isinya 'Halo Blitar'. Di cabang-b, isinya 'Halo Indonesia'. Git tidak tahu mana yang benar. Jadi Git minta bantuan manusia."

Mas Alin membuka file `halo.txt`. Isinya sekarang:

```text
<<<<<<< HEAD  
Halo Blitar  
=======  
Halo Indonesia
>>>>>>> cabang-b
```

"Lihat. Git menunjukkan dua versi yang bertabrakan. Yang di antara \<\<\<\<\<\<\< dan \======= itu versi dari cabang saat ini (main). Yang di antara \======= dan \>\>\>\>\>\>\> itu versi dari cabang yang mau digabung (cabang-b). Tugasmu: pilih salah satu, atau buat versi gabungan, lalu hapus tanda-tanda itu."

Mas Alin menghapus tanda konflik dan memilih "Halo Blitar dan Indonesia". Ia simpan, lalu:

```bash
alin:~$ git add halo.txt
alin:~$ git commit -m "Selesaikan konflik: gabungkan salam"
```

"Berhasil. Konflik selesai."

Binto menghela napas lega. "Ternyata nggak serem-serem amat."

"Loh iya sekarang. Kalau konflik di 10 file, baru kamu ngerti rasanya hidup, *Le*," sahut Mas Alin.

"Kuncinya: jangan panik. Konflik itu biasa. Justru pertanda kalau kamu kerja bareng tim. Lebih baik konflik diketahui Git daripada kamu timpa kerjaan temanmu tanpa sadar."

## **2.7 Pesan Sebelum Ashar**

Azan Ashar mulai terdengar dari kejauhan, menandakan pukul empat sore telah tiba. Itu adzan masjid di desa, yang meski waktu ashar biasanya jam 3 an, namun di desa disini umumnya dikumandangkan jam 4 sore. Menunggu para petani pulang dari sawah mereka. Demikian pula jam kerja di kantor GTN. Rupanya disamakan dengan jam kerja kebanyakan kantor di daerah : jam 4 sore.  Mas Alin menggeliat meregangkan tubuhnya, lalu mematikan monitor.

"Untuk hari pertama, itu dulu, *Le*. Kamu sudah belajar *init*, *status*, *add*, *commit*, *branch*, *checkout*, *stash*, *merge*, dan *konflik*. Itu bekal utama."

Binto mengangguk. Kepalanya penuh dengan istilah baru, tapi ada rasa puas yang aneh. Di kampus, ia tidak pernah menyentuh hal-hal ini. Semua serba instan: *download ZIP*, *copy-paste folder*, atau kirim lewat WA.

"Besok," lanjut Mas Alin sambil meraih kunci motor, "kita akan lihat kode asli punya Koperasi Sekar Patria. Kamu akan *clone* dari *cloud* ke laptopmu. Nanti kamu lihat sendiri, berapa banyak branch yang sudah dibuat Wawan sama aku. Berapa banyak *commit* yang sudah kami tulis. Git itu bukan sekadar *tools*. Git itu budaya. Budaya kolaborasi."

Binto bangkit, meraih helm-nya. "Mas, satu pertanyaan lagi."

"Apa?"

"Tadi Mas Alin bilang Git itu mesin waktu. Tapi kok perintahnya banyak banget? Kayak nyetir mobil manual."

Mas Alin tertawa kecil. "Iya, memang. Awalnya ribet. Tapi percayalah, *Le*. Begitu kamu terbiasa, kamu akan heran kenapa dulu bisa hidup tanpa Git. Sama kayak kamu heran kenapa dulu naik angkot kalau sekarang punya motor sendiri."

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

*Besok*, pikir Binto. *Gue akan belajar lagi. Bukan cuma belajar coding, tapi belajar menghargai proses orang lain. *

Motor beat-nya melaju pelan melewati gang desa, menuju rumah Bapak yang hanya dua puluh menit jauhnya.