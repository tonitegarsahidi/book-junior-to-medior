# Bab 4: Perjalanan Sebuah Tombol

## 4.1 Telepon dari Kalimantan

Pagi itu kantor masih lengang.

Cuma suara kipas angin Ufo. Cuma aroma kopi tubruk dari dapur kecil.

Binto duduk di dekat jendela. Menatap pohon rambutan. Buahnya mulai ada yang kuning sekarang. Nggak banyak. Cuma satu dua. Tapi cukup buat bikin dia tersenyum.

*Mulai menguning juga akhirnya*, pikirnya. *Tanda-tanda mau matang.*

Tiba-tiba...

telepon kantor berdering.

Bu Sari mengangkat. Suaranya ramah seperti biasa. "Garda Teknologi Nusantara, selamat pagi... Oh, Pak Haji Hamid! Nggih, nggih... Sebentar, saya sambungkan ke Pakde Suhar."

Binto menajamkan telinga. Pak Haji Hamid? Itu klien minimarket dari Balikpapan. Satu-satunya klien dari luar Jawa.

Nggak lama kemudian, Pakde Suhar muncul. Wajahnya serius. Tangannya masih megang ponsel di telinga.

"Nggih, Pak Haji. Monggo... Fitur cetak laporan harian? Nggih, bisa... Besok lusa? Waduh, mepet nggih... Tapi InsyaAllah kita usahakan... Untuk calon investor? Alhamdulillah, selamat... Nggih, nanti saya kabari lagi."

Pakde menutup telepon. Menghela napas panjang.

Mas Alin baru datang. Jaket jeans-nya basah. Gerimis lagi.

"Ada apa, Pakde?"

Pakde Suhar berjalan ke tengah ruangan. "Pak Haji minta fitur cetak laporan penjualan harian. Deadline-nya besok lusa. Katanya mau didemoin ke calon investor."

Wawan — yang baru masuk sambil bawa nasi pecel — nyaris tersedak. "Besok lusa? Gila, Pakde. Mepet banget."

Mas Alin nggak langsung bereaksi. Dia berjalan ke meja pojokannya. Menyalakan monitor. Menyesap kopi.

"Prioritas, Pakde. Kalau kita ambil ini... harus ada yang dikorbankan."

Pakde mengangguk. Dia udah menduga.

---

## 4.2 Rapat Kilat

Semua berkumpul di depan whiteboard.

Mas Alin menunjuk satu sticky note di kolom In Progress. Stiker bebek. `[MMK-010] Optimasi Query Stok`.

"Ini pekerjaan saya minggu ini. Optimasi query laporan stok minimarket Kalimantan. Sebenernya penting. Tapi bukan urgent. Kalau kita butuh slot kosong... saya rela ini balik ke Backlog."

Pakde menatap Mas Alin. "Yakin, Lin? Ini kan udah setengah jalan."

"Baru mulai analisis. Belum ada kode yang ditulis. Aman." Mas Alin tersenyum. "Lagipula... kalau Pak Haji dapat investor baru, itu bagus buat kita juga. Siapa tahu dia tambah cabang. Kita tambah proyek."

Pakde manggut-manggut. "Baik. MMK-010 kita tunda. Fitur cetak laporan masuk sprint ini."

Dia menatap Binto. "Binto, kamu ikut bantu Mas Alin ya. Biar sekalian belajar flow-nya."

Binto mengangguk cepat. "Siap, Pakde."

Dalam hati... dia gugup setengah mati.

*Ini pertama kalinya aku ngerjain fitur beneran. Bukan tugas kuliah. Dipakai orang beneran. Dan deadlinenya... besok lusa.*

---

## 4.3 Dari Obrolan ke Kertas

Mas Alin, Binto, dan Wawan duduk mengelilingi meja panjang. Pakde berdiri di dekat mereka.

"Jadi gini," Pakde memulai. "Pak Haji butuh tombol di halaman laporan. Dia bisa pilih tanggal. Klik cetak. Keluar PDF yang siap print. Biar pas demo kelihatan profesional."

Wawan mengangguk. "Aku bantu bikin layout PDF-nya. Ada logo minimarket. Alamat. Garis-garis rapi."

Mas Alin menatap Pakde. "Formatnya PDF aja? Atau sekalian thermal print buat struk?"

"PDF aja. Ini buat demo ke investor. Bukan operasional harian."

"Data yang ditampilkan per hari? Atau per shift kasir?"

"Per hari dulu. Yang penting total penjualan tanggal itu."

"Satu lagi... perlu logo di PDF?"

"Logo. Pasti. Investor kan lihat branding."

Binto hanya mendengarkan. Pikirannya sibuk mencerna.

*Aku kira cuma "bikin tombol cetak". Ternyata... banyak banget yang harus dipikirin. Format. Data. Logo. Konteks pengguna.*

Tapi yang lebih menarik perhatiannya... bukan jawabannya. Melainkan pertanyaannya.

*Mas Alin nggak nanya "pakai teknologi apa". Dia nanya: buat siapa? Kapan dipakainya? Apa yang mau dicapai?*

Pertanyaan-pertanyaan yang nggak pernah Binto pikirkan waktu ngerjain tugas kuliah.

Mas Alin seolah membaca pikirannya. "Ini bedanya bikin fitur buat tugas kuliah... sama buat klien beneran, Le. Di kampus, dosen cuma nilai: fungsinya jalan apa nggak. Di sini... kita harus mikirin siapa yang pakai. Buat apa. Dan gimana experience-nya."

---

## 4.4 Tiket Sisipan

Mas Alin bangkit. Ambil spidol. Ambil sticky note kuning.

```
[MMK-012] Cetak Laporan Penjualan Harian
Mulai: 17 Jan
🐤
```

"MMK itu Minimarket Kalimantan. Nomor 012 karena ini fitur kedua belas."

Dia tempel di kolom To Do.

"Detailnya?" tanya Binto.

Mas Alin kembali ke laptop. Buka Google Docs. Mulai mengetik.

```
MMK-012: Cetak Laporan Penjualan Harian

Deskripsi:
Pengguna dapat mencetak laporan penjualan harian dalam format PDF.

Acceptance Criteria:
- Pengguna dapat memilih tanggal dari date picker
- Sistem menampilkan data penjualan tanggal tersebut
- Tombol "Cetak" tersedia dan berfungsi
- PDF memuat logo minimarket, tanggal, dan ringkasan data

Prioritas: High (deadline 19 Jan)
PJ: Alin, Binto (Wawan bantu desain PDF)
```

Binto membaca layar. "Acceptance criteria... ini maksudnya syarat-syaratnya ya, Mas?"

"Nah, pinter." Mas Alin menoleh. "Acceptance criteria ini penting. Ini patokan kapan fitur dianggap selesai. Kalau semua kotak udah centang... baru boleh pindah ke Testing."

Binto mengangguk. *Ini rapi banget. Nggak kayak tugas kelompok aku dulu yang cuma modal "nanti aja lihat jadinya".*

---

## 4.5 Nama yang Jelas

Mas Alin belum selesai. Dia mengetik lagi di layar. Menunjukkan dua versi acceptance criteria.

"Versi buruk:"

```
- Sistem bisa cetak laporan
- Laporan bisa dilihat user
- Desain rapi
```

"Lihat? 'Bisa cetak laporan' — cetak dari mana? Format apa? 'Desain rapi' — rapi menurut siapa? Ini subjektif. Nanti Mbak Rara test, dia bilang belum rapi. Kamu bilang udah rapi. Debat nggak jelas."

"Versi baik — yang tadi kita tulis — itu spesifik. Testable. Bisa diuji dengan jelas: 'Apakah logo muncul? Ya atau tidak.' Bukan 'Apakah desainnya bagus?' — itu pertanyaan yang nggak akan selesai-selesai."

Binto memperhatikan. "Jadi acceptance criteria itu kayak kontrak kecil ya, Mas?"

"Persis. Semakin jelas kontraknya... semakin sedikit drama antara developer, QA, dan klien."

---

## 4.6 Mulai Ngoding

Mas Alin buka terminal.

"Kita mulai. Saya bikin branch baru."

```
git checkout -b feature/MMK-012
```

"Branch ini khusus buat fitur cetak laporan. Kamu nanti ngoding di sini. Jangan langsung di main."

"Main itu kayak jalan utama," lanjut Mas Alin. "Semua kendaraan lewat situ. Kalau kamu bikin perbaikan di tengah jalan... macet. Bisa-bisa yang lain nggak bisa kerja. Makanya bikin jalur alternatif dulu. Branch. Nanti kalau udah yakin... baru gabung lagi ke main."

Binto mengikuti. Clone. Checkout. Siap.

Mas Alin ambil backend: endpoint API untuk ambil data penjualan berdasarkan tanggal.

"Tanggalnya dari input user kan? Jangan langsung kamu tempel ke query. Minimal validasi dulu. Yang kayak gitu bisa jadi pintu masuk SQL Injection kalau nggak hati-hati. Kayak ninggalin pintu rumah nggak dikunci — orang iseng bisa masuk dan ngacak-ngacak isinya."

"Oh ya," tambah Mas Alin, "Pastikan juga endpoint ini cuma bisa diakses user yang berhak. Jangan sampai orang lain bisa lihat laporan toko cuma karena tahu URL-nya."

Binto mencatat dalam hati. Dia kebagian logika generate PDF dari data. Wawan sibuk bikin template HTML yang nanti dikonversi jadi PDF.

"Commit yang kecil-kecil, Le," Mas Alin mengingatkan. "Jangan nunggu semua selesai baru commit. Nanti susah tracking-nya kalau ada masalah. Dan satu lagi — commit message-nya yang jelas."

Binto menuruti. Setiap kali satu fungsi kecil selesai:

```
git add .
git commit -m "feat: tambah endpoint API /api/laporan/penjualan"
git commit -m "feat: buat struktur dasar PDF dengan header logo"
git commit -m "feat: integrasi template HTML dari Wawan ke PDF generator"
```

Mas Alin mengangguk melihat pesan commit Binto. "Nah. Ini udah lebih baik dari kemarin. Lihat polanya? Awalan 'feat:' untuk fitur baru. Nanti kalau perbaikan bug, pakai 'fix:'. Kalau ada perubahan yang nggak nambah fitur tapi memperbaiki struktur kode, pakai 'refactor:'. Ini namanya conventional commits."

Binto memperhatikan. "Jadi kayak label gitu ya, Mas?"

"Persis. Bayangin beberapa bulan lagi kita lihat `git log`. Dengan label ini, kita langsung tahu commit mana yang nambah fitur, mana yang perbaikan bug, mana yang bersih-bersih kode. Tanpa harus baca detail isinya satu per satu. Ini kebiasaan kecil yang dampaknya besar."

Binto tersenyum tipis — lalu teringat sesuatu dan nyengir sendiri. *Dulu... aku cuma copy-paste folder kalau mau backup. Itupun dengan nama folder `Project_Backup_12_Juni_FINAL_REV2_FIX`. Sekarang... setiap langkah tercatat rapi dengan label yang jelas.*

---

## 4.7 Pull Request

Menjelang sore, semua kode selesai. Binto merasa lega.

"Langsung gabung ke main aja, Mas?"

Mas Alin menggeleng. "Coba aja sendiri."

Binto mencoba merge. Error.

*"You don't have permission to merge to 'main'."*

"Lho? Kok nggak bisa?"

"Karena kamu belum punya akses maintainer. Itu sengaja. Di tim yang sehat... nggak semua orang bisa langsung merge ke main. Harus lewat Pull Request. Dan review dulu."

Mas Alin buka GitHub. Klik New Pull Request. Mulai nulis deskripsi.

"PR yang baik kasih konteks, Le. Gak cuma judul 'Tambah fitur cetak laporan'."

Dia menunjukkan dua versi:

"Buruk:"

```
Tambah fitur cetak laporan.
```

"Baik:"

```
## Apa yang dikerjakan
- Endpoint API /api/laporan/penjualan
- PDF generator dengan logo minimarket
- Validasi tanggal

## Kenapa
Untuk demo ke calon investor Pak Haji Hamid

## Cara testing
1. Buka halaman laporan
2. Pilih tanggal, klik Cetak
3. PDF harus muncul dengan logo dan data
4. Coba tanggal 29 Februari 2024 (tahun kabisat)
```

"Lihat bedanya? Deskripsi baik langsung kasih tahu reviewer apa yang harus dicek, kenapa fitur ini dibuat, dan gimana cara ngetesnya. Reviewer nggak perlu nebak-nebak."

Binto manggut-manggut. *Ternyata nulis deskripsi PR juga ada seninya.*

Mas Alin buka kode Binto di GitHub. Matanya teliti menyusuri setiap baris. Lalu dia mulai mengetik komentar langsung di antarmuka GitHub.

"Sini, lihat."

Ia memutar layar laptop agar Binto bisa membaca:

```
Komentar dari Mas Alin:

Halo, To. Logikanya udah bener. Hasil akhirnya udah sesuai acceptance criteria.
Aku kasih catatan kecil ya:

### 1. Nama variabel `tmp` (LaporanController.php:27)
Saran: ganti jadi `total_pendapatan`.
Alasan: `tmp` terlalu generik. Seminggu lagi kamu buka kode ini, kamu sendiri
bisa lupa `tmp` itu isinya apa. Nama variabel harus menjelaskan isinya,
bukan tipe-nya.

### 2. Pemanggilan fungsi duplikat (LaporanService.php:42-45)
Fungsi `hitungTotal()` dipanggil dua kali — di baris 42 dan 45.
Ini boros karena query database bisa jalan dua kali.
Saran: Simpan hasilnya di variabel dulu.
  $total = $this->hitungTotal($tanggal);
  $this->setRingkasan($total);
  $this->setPendapatan($total);

### 3. Validasi tanggal (LaporanService.php:18)
Ini oke, tapi coba dipastiin juga ngecek tahun kabisat ya.
Februari 2024 punya 29 hari, jangan cuma 28.

Overall: Kode udah rapi. Dua catatan di atas minor, tapi perbaiki dulu
biar makin clean. Good job buat PR pertama!
```

"Lihat formatnya, Le," kata Mas Alin. "Saya nggak cuma bilang 'ini salah'. Saya kasih tahu: apa masalahnya, di mana lokasinya, kenapa jadi masalah, dan gimana cara perbaikinya — lengkap dengan contoh kode. Itu bedanya code review yang konstruktif dengan yang cuma nyalahin."

Binto mengangguk cepat. "Ini enak banget, Mas. Saya langsung tahu apa yang harus diperbaiki. Nggak perlu nebak-nebak."

"Prinsipnya, Le: review itu tujuannya buat ngebantu, bukan buat ngerendahin. Pujilah yang sudah benar. Kasih saran yang spesifik untuk yang perlu perbaikan. Dan selalu pisahkan antara kritik ke kode dengan kritik ke orangnya. Kode bisa jelek, itu wajar — namanya juga belajar. Tapi orangnya jangan direndahkan."

Binto baca ulang komentar Mas Alin. Dan sesuatu mencair di dadanya.

*Ini... code review beneran. Bukan ajang nyalahin. Tapi diskusi. Ngebantu. Ada pujian. Ada saran. Ada contoh konkret.*

"Tapi, Mas," Binto bertanya. "Apakah aturan review dan approve ini kaku banget? Kalau misalnya ada bug darurat tengah malam dan Mas Alin lagi tidur, gimana?"

Mas Alin tersenyum tipis. "Nah, ini dunia nyata. Dalam kondisi tertentu — misal darurat butuh perbaikan detik itu juga, atau yang bikin PR adalah engineer senior yang sudah sangat terpercaya — proses formal kayak approval dan code review bisa dilewati. Di GTN kadang kita juga gitu kalau lagi krisis. Tapi dalam kondisi normal, apalagi buat feature baru, saya nggak akan approve kalau kode belum clean."

Binto segera perbaiki kodenya. Commit ulang. Push.

Mas Alin klik Approve. Lalu Merge.

"Selamat, Le. Kode kamu udah jadi bagian dari proyek."

---

## 4.8 Hantu Kabisat

Keesokan paginya. Sticky note MMK-012 pindah dari In Progress ke Testing.

Mbak Rara duduk. Buka laptop. Akses staging server.

Pilih tanggal 15 Januari. Muncul PDF. Rapi.

Pilih 1 Februari. Muncul PDF. Rapi.

Pilih 29 Februari 2024.

Error.

Layar menampilkan pesan merah: *"Invalid date."*

Mbak Rara menoleh ke Binto dengan senyum lebar. "Wah, Mas Binto. Lupa ya kalau 2024 itu tahun kabisat? Februari 2024 punya 29 hari lho."

Binto menepuk jidat. "Aduh, Mbak. Saya cuma ngecek maksimal 28."

"Ya udah. Tak balikin dulu ya sticky note-nya." Mbak Rara pindahin kertas kuning itu dari Testing balik ke In Progress. "Nanti kalau udah bener kabari aku."

Binto menghela napas.

*Aku kira udah beres. Ternyata masih ada jebakan.*

Mas Alin yang denger dari pojokan cuma terkekeh. "Testing itu penting, Le. Developer sering bias. Kita pikir kode kita sempurna. Padahal... ada kasus-kasus yang kelewat."

Binto kembali buka kode. Benahi validasi tanggal. Tambah pengecekan tahun kabisat. Setelah diuji sendiri — 29 Feb 2024 lolos, 29 Feb 2025 ditolak — dia commit dan push.

"Mbak, udah saya perbaiki."

Mbak Rara test lagi. Semua lolos. Dia pindahin sticky note ke Done.

---

## 4.9 Tombol yang Dipakai

Sore itu, Mas Alin buka GitHub. Merge Pull Request Binto ke main. Beberapa menit kemudian — pipeline CI/CD otomatis berjalan: test, build, deploy. Notifikasi muncul: Success.

"Selesai. Sekarang fitur cetak laporan udah live."

Binto melongo. "Segampang itu, Mas?"

"Segampang itu. Tapi itu karena kita udah siapin pipeline-nya dari dulu. Nanti kamu belajar soal CI/CD."

Pakde Suhar meraih telepon. "Saya kabari Pak Haji dulu. Biar beliau coba sendiri."

Binto menunggu. Jantungnya berdebar. *Gimana kalau ada yang error? Gimana kalau Pak Haji nggak suka?*

Beberapa jam kemudian — matahari hampir tenggelam — telepon berdering. Pakde yang angkat.

"Nggih, Pak Haji... Alhamdulillah, sudah dicoba? Lancar? Syukur... Besok demonya? Siap, InsyaAllah... Nggih, sami-sami."

Pakde menutup telepon dengan senyum lebar. "Pak Haji barusan nyoba sendiri. Katanya PDF-nya muncul. Logo-nya ada. Datanya bener. Besok dia mau demo ke calon investor."

Wawan bersorak. Mbak Rara acungkan jempol.

Binto menghela napas panjang. Entah sejak kapan dia menahan napas.

*Fitur kecil yang aku bikin... udah dipakai orang di Kalimantan.*

*Dan besok... itu akan membantu mereka dapat investor.*

---

## 4.10 Ngopi Sore

Sore itu, Binto dan Mas Alin duduk di teras. Di bawah pohon rambutan. Buahnya mulai banyak yang kuning sekarang.

"Mas... semua alur kerja emang selalu kayak gini?"

Mas Alin nyengir. "Ya enggaklah, Le. Tiap tempat beda."

Dia menatap langit sore. "Di sini kita enak. Ada Wawan yang bantu desain. Mbak Rara yang jadi QA. Kamu dan saya fokus di backend."

"Kalau dulu?"

"Waktu saya pertama kerja... sendirian. Fullstack beneran. Saya yang bikin database. Backend. Frontend. Sampe desain tombolnya. QA-nya? Saya sendiri. Testing sendiri. Kalau ada bug... ya saya yang malu sendiri di depan klien."

Binto membayangkan. Berat.

"Di startup Jakarta... lebih lengkap lagi," Mas Alin melanjutkan. Nada suaranya sedikit berubah. Lebih pelan. "Saya dulu CTO di satu startup fintech di sana. Timnya gede. Ada frontend engineer khusus React. Backend engineer khusus Node. Database engineer. DevOps. Tiap orang cuma megang bagian kecil."

"Enak dong?"

"Enak sih. Tapi kita jadi nggak tahu gambaran besar. Kalau ada masalah... suka lempar-lemparan. 'Ah itu backend-nya yang error.' 'Bukan, itu database-nya lambat.'"

Mas Alin menatap Binto. "Intinya... tim itu dinamis. Nggak ada struktur yang sempurna. Di sini kita kecil. Semua serba fullstack. Kamu belajar dari hulu ke hilir. Itu bagus buat fondasi."

Binto mengangguk. Tapi ada yang mengganjal.

*Orang ini... pernah jadi CTO di startup Jakarta. Tim gede. Gaji pasti besar. Kenapa sekarang ada di Blitar? Di kantor kecil belakang pasar?*

Dia ingin bertanya. Tapi ada sesuatu di nada suara Mas Alin tadi — waktu nyebut startup Jakarta — yang bikin dia urung. Ada yang... nggak enak buat diceritakan.

*Mungkin lain kali*, pikir Binto.

---

## 4.11 Sebuah Tombol

Malam itu, di rumah. Binto duduk di teras. Bapak udah tidur. Rumah sepi.

Dia buka laptop. Buka aplikasi minimarket — masih versi lokal di laptopnya. Dia klik halaman laporan. Pilih tanggal. Klik tombol "Cetak".

Muncul PDF.

Logo minimarket. Tanggal. Data penjualan. Total. Garis-garis rapi.

Tombol kecil. Hitam. Nggak istimewa.

Tapi tombol itu... tombol itu adalah hasil kerjanya. Dan sekarang — sekarang tombol itu sudah ada di server beneran. Tombol itu dipakai orang di Kalimantan. Tombol itu membantu Pak Haji meyakinkan investor.

*Aku yang bikin ini*, pikirnya.

Dan sesuatu yang asing muncul di dadanya. Bukan bangga. Bukan puas. Tapi... hangat.

*Ini beda*, pikirnya. *Ini bukan tugas kuliah.*

Bukan karena dinilai dosen. Bukan karena dapat IPK. Tapi karena sesuatu yang nyata. Yang bisa dipakai. Yang membantu orang di Kalimantan — tempat yang bahkan belum pernah ia kunjungi.

Dia belum berani menyebut dirinya engineer. Terlalu dini. Tapi untuk pertama kalinya... dia merasa mungkin suatu hari nanti... dia bisa.

---

Di luar, pohon rambutan di depan rumahnya — bukan yang di kantor, tapi yang di rumah — juga bergoyang pelan. Buahnya belum ada. Pohonnya masih kecil. Ditanam Bapak dua tahun lalu, tepat di hari kelulusan Binto.

*Kapan ya buahnya?* pikir Binto.

*Mungkin... sama kayak aku.*

*Masih nunggu waktunya.*

---

## 4.12 Fullstack Itu...

Besoknya, Binto masih kepikiran.

Dia teringat obrolan sore kemarin. Tentang fullstack. Tentang hulu ke hilir.

"Mas," katanya pagi itu, sesaat setelah Mas Alin datang. "Fullstack itu maksudnya... harus bisa semuanya?"

Mas Alin nyengir. "Pertanyaan bagus."

Dia duduk. Menyesap kopi.

"Fullstack itu... kamu ngerti cukup untuk bikin fitur dari depan ke belakang. Bukan berarti kamu jago di semua layer. Tapi kamu ngerti... gimana data mengalir dari tombol yang diklik user... sampe ke database... dan balik lagi ke layar."

"Jadi nggak perlu jago semuanya?"

"Nggak perlu. Yang penting kamu ngerti alurnya. Nanti kalau udah senior... kamu bisa milih spesialisasi. Mau fokus di frontend? Backend? Database? DevOps? Itu nanti. Tapi fondasinya... harus fullstack dulu."

Dia menunjuk ke dalam. "Lihat Wawan. Dia jago UI/UX. Tapi dia juga bisa frontend. Bahkan ngerti basic backend. Nggak jago-jago amat. Tapi cukup buat komunikasi sama kita."

"Lihat Mbak Rara. Dia QA. Tapi dia ngerti cara baca kode. Biar bisa nulis test case yang tepat."

"Lihat Andik. Dia infra. Tapi dia juga ngoding. Biar bisa debug kalau server error."

"Di tim kecil kayak kita... nggak ada yang cuma bisa satu hal. Semua harus ngerti gambaran besar."

Binto merenung. Di kampus... dia belajar Java, Python, database, algoritma. Tapi semuanya terpisah-pisah. Nggak pernah disambungin.

*Di sini aku baru belajar... gimana cara nyambungin semuanya.*

---

## 4.13 Aliran Data

Siang itu, Binto melirik ke pojok ruangan. Mas Andik seperti biasa — di depan laptop ThinkPad bekasnya, terminal penuh teks hijau. Nggak bersuara.

Biasanya Binto segan. Tapi hari ini... setelah obrolan soal fullstack, ada yang mengganjal. Dia mengumpulkan keberanian. Berjalan ke sudut itu.

"Mas Andik... maaf ganggu. Saya penasaran."

Mas Andik menoleh. Kacamata tebalnya sedikit turun. Dia nggak jawab. Cuma menunggu.

"Fitur yang saya bikin kemarin... cetak laporan itu. Itu kan sekarang udah live. Tapi... gimana caranya sampai ke Kalimantan? Saya ngoding di laptop itu..." Binto menunjuk mejanya. "...kok bisa dipakai orang di Balikpapan?"

Senyum tipis muncul di sudut bibir Mas Andik. Dia bangkit. "Sini."

Mereka berjalan ke rak server mini di sudut ruangan. Lampu-lampu kecil berkedip. Kabel-kabel rapi — Mas Andik emang paling rapi soal kabel.

"Ini server staging kita," katanya singkat. "Di sini... semua kode yang kita kerjain... dites dulu sebelum naik ke production."

"Production-nya di mana, Mas?"

"Cloud. Server beneran-nya ada di data center. Akses dari mana aja — termasuk dari Kalimantan. Setiap kali user klik tombol di sana... sinyalnya lewat internet... masuk ke cloud. Server proses. Kirim data ke database. Ambil hasilnya. Kirim balik ke browser. Semua dalam hitungan milidetik."

Binto membayangkan perjalanan itu. Tombol kecil di Kalimantan. Server di cloud entah di mana. Data yang bolak-balik dalam hitungan milidetik.

"Jadi... setiap kali aku bikin fitur... itu semua terjadi?"

Mas Andik mengangguk. Senyum tipis. "Itulah kenapa kode harus rapi. Harus aman. Harus efisien. Karena di ujung sana... ada orang beneran yang pakai."

Binto merenung. Selama ini dia ngoding di laptop sendiri. Jalan. Selesai. Aman.

Tapi sekarang... kodenya hidup. Di server beneran. Dipakai orang beneran. Setiap detik.

*Tanggung jawab*, pikirnya. *Ini namanya tanggung jawab.*

---

