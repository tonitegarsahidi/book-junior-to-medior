# Bab 11: Menenangkan Sistem yang Menangis

Dua hari setelah bapaknya jatuh, Binto kembali ke kantor dengan langkah yang lebih pelan dari biasanya.

Bapak sudah jauh membaik. Masih dilarang ke mana-mana, masih harus minum obat teratur, dan masih ngomel kecil tiap kali ibu melarangnya menyentuh sepeda. Tapi setidaknya pagi itu ia sudah bisa duduk di teras sambil menyandarkan punggung ke kursi kayu, memandangi orang lewat seolah tidak pernah bikin satu kampung panik dua hari sebelumnya.

Sebelum berangkat ke kantor, Binto sempat berdiri sebentar di samping pintu, melihat bapaknya menyeruput teh hangat.

"Pak, saya berangkat dulu."

"Iyo. Sing ati-ati." Bapak menoleh sebentar, lalu menambahkan, "Nek ada pusing, istirahat."

Binto hampir tertawa.

Bapak yang baru saja bikin semua orang sibuk kini memberi nasihat seperti tidak terjadi apa-apa.

Tapi justru karena itu, langkah Binto pagi ini terasa lebih ringan.

Tidak sepenuhnya lega.

Masih ada sisa kaget yang belum habis.

Masih ada bayangan bapaknya terbaring lemah di ranjang periksa.

Masih ada satu kalimat Mas Alin yang menempel keras di kepala:

*Kode bisa nunggu.*

Anehnya, kalimat itu ikut mengubah cara Binto melihat hal-hal kecil.

Bahkan saat ia baru masuk kantor dan melihat error message merah di layar HP Mas Andik.

"Mas Binto," kata Andik sambil mengangkat layar ke arahnya. "Ini kenapa ya?"

Di layar smartphone itu tampil pesan error dalam kotak merah:

```text
Error 500: SQLSTATE[42S22]: Column not found: 1054 Unknown column 'stok_minimal' in 'field list'
```

Binto membaca cepat. Lalu mengembuskan napas pendek.

"Waduh. Itu salah saya. Semalam waktu ganti nama kolom dari `stok_minimum` ke `stok_minimal` di kode, saya lupa jalankan migrasi database-nya di server."

Andik menggaruk pelipis. "Aku sih ngerti dikit-dikit, Mas. Tapi kalau sales di lapangan yang lihat beginian, bisa panik duluan."

Kata *panik* itu membuat sesuatu bergerak kecil di kepala Binto.

Dua hari lalu ia melihat sendiri seperti apa rasanya ketika tubuh manusia tiba-tiba oleng, lalu semua orang di sekitarnya sibuk menenangkan keadaan.

Hari ini yang oleng bukan manusia.

Sistem.

Tapi akibatnya sama: orang bisa panik kalau yang mereka lihat hanya kekacauan mentah.

Mbak Rara yang sedang menaruh map di meja depan langsung nimbrung. "Nah. Ini nih yang sering developer lupa. Begitu ada masalah, yang dilempar ke user malah isi dapur. SQLSTATE, line sekian, file ini-itu. Pengguna mau ngapain coba dikasih begituan?"

Binto mengangguk pelan.

Kali ini ia tidak defensif.

Karena untuk pertama kalinya, ia tidak melihat error mentah sebagai sekadar kekeliruan teknis.

Ia melihatnya sebagai kepanikan yang diteruskan mentah-mentah ke orang lain.

Dan ia baru saja belajar, dua hari lalu, bahwa yang paling dibutuhkan saat keadaan goyah bukan selalu jawaban lengkap.

Kadang yang dibutuhkan lebih dulu adalah ketenangan.

---

## 11.1 Kenapa Error Harus Ramah?

Mbak Rara duduk di kursi dekat meja Binto sambil melipat tangan di dada.

"Coba bayangin gini, Mas," katanya. "Kamu lagi buru-buru transfer uang di ATM. Tiba-tiba mesin berhenti, layar blank, terus muncul tulisan panjang bahasa teknis yang kamu gak ngerti. Reaksimu apa?"

"Panik," jawab Binto.

"Nah. Bukan karena kamu bodoh. Tapi karena mesin itu gak bantu kamu paham apa yang sedang terjadi."

Mas Alin yang sejak tadi mendengar dari mejanya ikut mendekat sambil membawa cangkir kopi.

"Rara betul," katanya. "Di dunia software, error itu kadang gak bisa dihindari. Tapi cara kita menyampaikan error ke pengguna, itu pilihan."

Binto menatap lagi pesan merah di layar HP Andik.

`SQLSTATE[42S22]`

Kalau ia yang membaca sebagai developer, pesan itu petunjuk.

Kalau pengguna biasa yang membaca, itu ancaman.

"Jadi... yang salah bukan cuma error-nya muncul?" tanya Binto.

"Bukan cuma itu," jawab Mas Alin. "Yang salah, kamu bikin kepanikan internal sistem ikut bocor ke orang luar. Padahal pengguna gak butuh lihat isi dapur. Mereka cuma butuh tahu: ini gagal, kenapa kira-kira, dan habis ini harus ngapain."

Mbak Rara mengangguk mantap. "Orang panik itu gak selalu butuh penjelasan panjang. Kadang butuh kalimat yang bikin dia merasa situasinya masih terkendali."

Kalimat itu menancap di kepala Binto.

*Situasinya masih terkendali.*

Dua hari lalu ia juga butuh itu.

Dari dokter.

Dari Mas Catur.

Dari Mas Alin.

Bukan kebetulan, pikirnya. Rupanya dunia kerja dan hidup pribadi kadang mengajarkan hal yang sama dengan bahasa berbeda.

---

## 11.2 Exception: Kesalahan yang Bisa Ditebak

Mas Alin meletakkan cangkirnya, lalu menarik kursi ke sebelah Binto.

"Gini, Le. Gak semua error itu sama. Ada yang memang bisa kita duga dari awal. Produk gak ketemu. Input kosong. Stok habis. Itu bukan kiamat. Itu kejadian yang memang harus disiapkan jalurnya."

"Exception," gumam Binto, seperti mengulang istilah yang pernah ia dengar tapi belum benar-benar ia pegang.

"Nah. Exception itu kira-kira begitu. Kondisi menyimpang yang masih bisa kamu antisipasi. Sistemmu harus tetap sopan walau ketemu hal yang tidak ideal."

"Caranya?"

"Try-catch dulu yang paling gampang dipahami." 

Mas Alin memutar laptop Binto sedikit dan mulai mengetik contoh sederhana.

```php
try {
    $produk = Produk::findOrFail($id);
} catch (ModelNotFoundException $e) {
    return response()->json([
        'message' => 'Produk tidak ditemukan'
    ], 404);
}
```

"Kalau produk gak ada, jangan biarkan framework muntah sendiri ke layar user," kata Mas Alin. "Tangkap. Rapikan. Kirim balik pesan yang manusiawi."

Binto membaca contoh itu pelan-pelan.

"Jadi `try` itu blok yang dicoba dulu. Kalau gagal, dilempar ke `catch`?"

"Persis."

Andik mengangguk dari samping. "Dan dari sisi mobile, kalau respons-nya rapi begini, aku juga enak nangani di UI. Gak perlu nebak-nebak ini maksudnya apa."

Binto baru sadar sesuatu.

Selama ini ia terlalu sering menganggap error handling sebagai urusan belakang rumah. Sesuatu yang nanti saja dibersihkan kalau fitur utamanya sudah jadi.

Padahal dari sudut pengguna, justru di situlah sistem menunjukkan wataknya.

Saat semua lancar, semua aplikasi bisa kelihatan pintar.

Yang membedakan adalah: ketika ada yang gagal, siapa yang tetap bisa bersikap waras.

---

## 11.3 Failure: Ketika Bukan Kode yang Rusak

"Tapi ada juga yang beda jenisnya," lanjut Mas Alin. "Kadang bukan input-nya yang salah. Bukan logika cabangnya yang kelewat. Kadang memang server-nya drop. Database-nya mati. Internetnya putus. Itu failure."

"Kalau begitu, kita tetap pakai catch juga?"

"Bisa. Tapi intinya bukan di syntax dulu." Mas Alin bersandar sedikit. "Intinya: jangan bikin pengguna ikut menanggung kepanikan kita."

Mbak Rara tertawa kecil. "Ini kayak kalau orang rumah lagi panik, terus semua orang teriak bareng-bareng. Bukannya selesai, malah tambah kacau."

Binto menoleh padanya.

Mbak Rara mengangkat bahu. "Ya memang begitu, kan? Kalau ada masalah, harus ada yang pertama kali jaga nada suara."

Kata-kata itu membuat kepala Binto seperti menemukan sambungan baru.

Di rumah sakit, dokter tidak bilang, *Wah gawat ini, tensi naik turun, bisa macam-macam!* 

Mas Catur juga tidak datang sambil berteriak-teriak.

Mas Alin tidak menelepon sambil bilang, *Deadline kita hancur!* 

Semua orang yang menenangkan situasi waktu itu melakukan satu hal yang sama:

mereka tidak menambahkan kepanikan baru.

Mungkin itu juga inti error handling.

Bukan menutupi masalah.

Tapi membingkai masalah dengan cara yang masih bisa dihadapi manusia.

---

## 11.4 Graceful Degradation: Tetap Berdiri Walau Goyah

Mas Alin mengambil kertas bekas print-out di meja dan menggambar kotak-kotak kecil.

"Ada konsep lain. Namanya *graceful degradation*."

"Bahasa Indonesianya apa itu, Mas?" tanya Wawan yang baru mendekat sambil membawa kerupuk dari meja tengah.

Mas Alin tersenyum. "Kira-kira: tetap anggun meski lagi pincang."

Wawan langsung nyengir. "Wah, kayak saya kalau gaji belum turun tapi tetap sok tenang."

"Kurang lebih begitu, tapi jangan dibawa ke HR," kata Andik datar.

Satu ruangan tertawa kecil.

Mas Alin melanjutkan, "Misalnya sistemmu punya lima fitur. Kalau satu fitur tambahan gagal, jangan sampai semua ikut mati. Yang utama harus tetap jalan. Ibarat pesawat kehilangan satu mesin—jangan langsung jatuh. Cari cara supaya masih bisa mendarat." 

Binto mengangguk pelan.

Dua hari lalu ia melihat versi manusianya.

Tubuh bapak sempat goyah. Tapi tidak semua runtuh. Warga sekitar bergerak. Mas Catur membantu. Dokter menstabilkan. Ibu menenangkan diri. Tim kantor menahan pekerjaan. Sistem sosial kecil di sekitar bapaknya bekerja seperti penyangga.

Satu titik gagal.

Tapi seluruh dunia tidak ikut roboh.

Mungkin software yang baik juga seharusnya begitu.

"Berarti jangan bikin semua endpoint bergantung ke satu hal kecil tanpa cadangan, ya?" tanya Binto.

Mas Andik mengangguk. "Nah. Kamu mulai nyambung."

---

## 11.5 Logging: Kepanikan untuk Developer, Bukan untuk Pengguna

"Terus kalau pesan ke pengguna dibikin rapi begini," tanya Binto, "kita tahunya dari mana error aslinya apa?"

Mas Alin tersenyum. "Akhirnya nanya yang benar. Dari log."

Ia mengetik contoh lagi di laptop.

```php
catch (Exception $e) {
    Log::error('Gagal memproses pesanan: ' . $e->getMessage(), [
        'user_id' => auth()->id(),
        'data' => $request->all()
    ]);

    return response()->json([
        'message' => 'Terjadi kesalahan. Tim kami sedang menanganinya.'
    ], 500);
}
```

"Lihat bedanya," kata Mas Alin. "Ke user kamu kasih ketenangan. Ke log kamu kasih kejujuran penuh."

Binto membaca ulang pelan.

Ke user: tenang.

Ke dalam: detail.

Itu bagus sekali.

Bukan bohong.

Bukan nutup-nutupi.

Cuma menaruh informasi pada tempat yang tepat.

Mbak Rara mengangguk. "Pengguna nggak perlu ikut baca curhatan sistem. Biar kita saja yang baca buku hariannya nanti."

"Buku harian sistem," gumam Binto.

Andik menoleh. "Nah itu judul bab bagus buat nanti."

Mereka tertawa kecil.

Tapi di kepala Binto, istilah itu langsung menempel.

Log.

Buku harian sistem.

Tempat semua kepanikan internal dicatat rapi supaya pengguna tidak perlu ikut menanggungnya.

---

## 11.6 Praktik: Membungkus Error dengan Elegan

Setelah paham kerangkanya, Binto mulai memperbaiki endpoint satu per satu.

Pertama, ia membungkus pengambilan data produk dengan `try-catch`. Jika produk tidak ditemukan, respons yang keluar harus jelas: 404, produk tidak ditemukan.

Kedua, ia menambahkan validasi stok. Kalau stok tidak cukup, jangan biarkan ujungnya jadi error 500 yang tampak seperti server meledak. Harus ada pesan yang jujur dan tetap menenangkan.

Ketiga, ia menambahkan catch umum untuk hal-hal yang memang tidak terduga. Bukan untuk dipamerkan ke pengguna, tapi untuk dicatat rapi agar nanti bisa dibongkar oleh tim.

Setelah beberapa kali percobaan, mereka menguji skenario yang sebelumnya bermasalah.

Pesan mentah hilang.

Sebagai gantinya, API mengembalikan respons:

```json
{
    "message": "Stok produk tidak mencukupi"
}
```

Status code: 422.

Binto menatap hasilnya beberapa detik.

Sederhana.

Tidak pintar-pintar amat kelihatannya.

Tapi justru itu gunanya.

Karena pengguna tidak butuh melihat betapa ribet isi kepala developer. Pengguna cuma butuh dibimbing lewat masalahnya, bukan dilempar ke tengah belantara istilah teknis.

"Nah, gitu. Lebih manusiawi," kata Mbak Rara.

Wawan yang ikut melongok dari belakang menimpali, "Kalau begini kan sales gak serasa dimaki komputer."

"Komputer juga sebenarnya gak marah," kata Andik. "Cuma developernya kadang belum tahu cara ngomong sopan."

Binto terkekeh.

Dulu komentar seperti itu mungkin akan menusuk egonya.

Hari itu justru terasa pas.

Karena ia tahu, pelajaran ini bukan cuma soal API. Ini soal bagaimana sebuah sistem—dan mungkin juga seorang manusia—belajar untuk tidak memantulkan kepanikannya mentah-mentah ke orang lain.

---

## 11.7 Jaring Penyelamat di Langit Sistem

Mas Alin belum selesai.

"Sekarang, ada satu langkah lagi biar kamu gak nulis pola yang sama terus-menerus," katanya sambil membuka file `app/Exceptions/Handler.php`.

"Global exception handler."

Binto mendekat.

Mas Alin menunjuk struktur fungsi yang mengatur bagaimana exception tertentu diterjemahkan menjadi respons yang sesuai.

"Kalau `ModelNotFoundException`, otomatis jadi 404. Kalau `ValidationException`, jadi 422. Jadi gak semua method harus kamu jaga satu-satu dari nol. Sistemnya kamu ajari supaya punya refleks yang baik."

Kalimat itu membuat Binto diam sebentar.

Sistem diajari punya refleks yang baik.

Bukan sekadar tambal sulam.

Bukan sekadar menunggu setiap masalah muncul lalu dipukul satu-satu.

Tapi menyiapkan fondasi supaya saat hal serupa datang lagi, responsnya sudah lebih dewasa.

Ia teringat bapaknya yang sore kemarin akhirnya mau meletakkan sepeda di teras, dan ibu yang langsung menyembunyikan kuncinya di tempat lain. Reaksi kecil, tapi jelas: rumah mereka juga sedang membangun exception handler versi manusia.

Supaya kejadian yang sama tidak terulang begitu saja.

"Jadi medior itu separuhnya ngoding, separuhnya nyiapin sistem biar gak bikin panik orang?" gumam Binto.

Mas Alin tertawa kecil. "Kalau saya jawab iya penuh, nanti kamu bilang saya kebanyakan filosofi. Tapi kurang lebih begitu."

---

## 11.8 Menenangkan Sistem yang Menangis

Menjelang sore, pekerjaan utama hari itu mulai beres.

Error mentah yang tadi pagi bikin satu meja berkumpul sekarang sudah berubah jadi rangkaian respons yang lebih waras. Tidak sempurna. Belum elegan di semua sisi. Tapi jauh lebih dewasa daripada sebelumnya.

Binto duduk di teras kantor bersama Mbak Rara sambil membawa teh hangat. Angin Blitar lewat pelan di sela-sela daun rambutan kantor yang buahnya makin merah ranum bergelantungan.

"Aku baru ngeh sekarang," kata Binto. "Error handling itu bukan cuma biar developer gampang debugging."

Mbak Rara menatap halaman depan. "Ya jelas. Buat pengguna justru itu yang paling kerasa."

"Iya. Sistem yang baik itu ternyata bukan sistem yang gak pernah salah. Tapi sistem yang tahu cara bersikap waktu salah."

Mbak Rara tersenyum tipis. "Kayak orang tua yang nenangin anak jatuh. Anak nangis karena kaget sama sakitnya. Yang dibutuhkan pertama kali bukan kuliah anatomi. Ya ditenangin dulu. Dibersihin dulu lukanya. Baru dijelasin pelan-pelan."

Binto menoleh padanya.

Analogi itu sederhana.

Tapi pas sekali.

Dua hari lalu ia melihat versi nyatanya di rumah sakit.

Hari ini ia belajar versi teknisnya di kantor.

Ternyata pelajarannya sama:

jangan tambahkan kegaduhan pada sesuatu yang sudah goyah.

"Error handling yang baik itu menenangkan sistem yang menangis," gumam Binto.

"Dan menenangkan pengguna yang kebetulan kena cipratannya," tambah Mbak Rara.

Mereka tertawa pelan.

---

## 11.9 Rambutan yang Disisihkan

Mas Alin keluar dari dalam sambil membawa baskom kecil berisi rambutan.

"Ini sisa panen kemarin. Bu Sari bilang kalau dibiarkan terus nanti keburu kemrungsung semua."

Binto mengambil satu. Kulitnya merah bagus, tapi ketika dibuka, satu sisinya mulai kecokelatan.

"Nah," kata Mas Alin, melihat itu. "Pas sekali."

"Apanya yang pas, Mas?"

Mas Alin menunjuk buah di tangan Binto. "Kalau ada satu rambutan rusak, apa kita buang satu baskom?"

"Ya enggak. Yang jelek disisihkan." 

"Persis. Sistem juga begitu. Ada error, ya tangani titik yang rusak. Jangan sampai satu bagian bermasalah bikin semuanya ikut dibuang. Dan yang penting, jangan kasih rambutan busuk ke tamu."

Wawan yang baru keluar sambil bawa kantong kresek tertawa. "Kalau itu mah bukan error handling, Mas. Itu niat jahat."

Binto ikut tertawa.

Tapi matanya tetap terpaku sebentar pada buah di tangannya.

Dua hari lalu ia belajar ada hal yang tak boleh salah urut.

Hari ini ia belajar ada hal yang tak boleh salah cara menyampaikannya.

Dua-duanya sama-sama tentang tanggung jawab.

Bukan cuma tanggung jawab terhadap pekerjaan.

Tapi tanggung jawab terhadap orang yang menerima dampak dari pekerjaan itu.

Ia menaruh rambutan yang rusak ke pinggir baskom dan mengambil satu lagi yang sehat.

Kali ini daging buahnya bening, manis, dan utuh.

Mas Alin benar.

Tugas engineer bukan cuma membuat sesuatu berjalan.

Tugas engineer juga memastikan, ketika ada yang gagal, dunia di sekitarnya tidak ikut panik tanpa perlu.

Di luar, suara motor lewat satu-dua. Dari meja depan, Bu Sari memanggil semua orang untuk minum teh sebelum pulang. Sore turun pelan di kantor kecil itu.

Dan di kepala Binto, satu pelajaran baru menancap rapi:

kadang yang paling dewasa dari sebuah sistem bukan cara ia bekerja saat semua baik-baik saja,

melainkan cara ia menenangkan keadaan saat sesuatu mulai menangis.