# **Bab 10: Menenangkan Sistem yang Menangis**

## **10.1 Pesan Error Misterius**

Pagi itu, Binto baru saja menyesap teh hangatnya ketika Mas Andik datang dengan wajah bingung. Di tangannya, smartphone menampilkan aplikasi Flutter yang sedang ia kerjakan.

"Mas Binto, ini kenapa ya?" Andik memutar layarnya ke arah Binto.

Di layar, tampak pesan error dalam kotak merah:

text

Error 500: SQLSTATE\[42S22\]: Column not found: 1054 Unknown column 'stok\_minimal' in 'field list'

Binto membaca pesan itu dan langsung tersipu. Itu error dari API-nya sendiri. Tadi malam ia mengubah nama kolom di database dari stok\_minimum menjadi stok\_minimal, tapi lupa menyesuaikan query di kode.

"Waduh, maaf Dik. Itu salah saya. Nanti saya betulin."

Andik menggaruk kepala. "Iya, Mas. Aku sih gak masalah, kan aku ngerti dikit-dikit. Tapi bayangin kalau ini aplikasi sudah dipakai sales di lapangan. Mereka baca SQLSTATE gitu, pasti panik."

Mbak Rara yang sedang mengisi air di dispenser ikut nimbrung. "Nah, ini nih. Salah satu dosa besar developer: nampilin error mentah ke pengguna."

## **10.2 Kenapa Error Harus Ramah?**

Mbak Rara meletakkan gelasnya dan duduk di kursi dekat Binto.

"Coba bayangin, Mas. Kamu lagi buru-buru mau tarik duit di ATM. Masukin kartu, pilih nominal, tiba-tiba mesin cuma bunyi *bip-bip* aneh, kartu ditelan, terus keluar struk kosong. Kamu panik, kan?"

Binto mengangguk. Siapa yang tidak panik?

"Harusnya mesin itu bilang: 'Maaf, transaksi gagal. Silakan coba lagi atau hubungi bank.' Itu baru ramah. Pengguna jadi tenang karena dikasih tahu apa yang terjadi dan apa yang harus dilakukan."

Mas Alin yang sejak tadi diam ikut mendekat. "Rara betul. Di dunia API, kita gak boleh ngasih lihat isi dapur ke pelanggan. Error seperti SQLSTATE itu urusan dapur. Pelanggan cukup tahu 'pesanan gagal, coba lagi'. Detailnya cukup kita yang tahu."

Binto menghela napas. "Iya, Mas. Saya sadar. Tapi gimana caranya biar error-nya gak muncul mentah gitu?"

## **10.3 Exception: Kesalahan yang Bisa Ditebak**

Mas Alin menarik kursi dan duduk di sebelah Binto. "Begini, *Le*. Banyak error sebenarnya bisa kita prediksi sebelumnya. Produk tidak ditemukan? Itu bisa terjadi. Stok habis? Bisa. Pengguna kirim data tidak lengkap? Juga bisa. Error-error seperti ini namanya exception—pengecualian yang bisa kita antisipasi."

"Caranya?"

"Pakai try-catch." Mas Alin membuka laptop Binto dan menunjukkan contoh sederhana.

php

try {

    // Kode yang mungkin error

    $produk \= Produk::findOrFail($id);

} catch (ModelNotFoundException $e) {

    // Kalau error, tangkap di sini

    return response()-\>json(\[

        'message' \=\> 'Produk tidak ditemukan'

    \], 404);

}

"Lihat. Kalau findOrFail tidak menemukan produk, dia akan melempar *exception*. Exception itu kita tangkap pakai catch. Lalu kita kirim respons yang rapi: Produk tidak ditemukan dengan status 404. Pengguna gak lihat error mentah."

Binto mengangguk paham. "Jadi try itu blok yang 'coba dulu', kalau gagal, lempar ke catch?"

"Persis. Dan kita bisa menangkap berbagai jenis exception dengan berbeda-beda."

Binto terdiam sejenak. Ia teringat presentasi tugas akhirnya di kampus. Waktu demo, aplikasinya sempat menampilkan error mentah—*stack trace* panjang di layar proyektor. Dosen penguji hanya geleng-geleng, lalu lanjut ke pertanyaan berikutnya. Tidak ada konsekuensi nyata. Tapi di sini, kata-kata Mas Andik tadi pagi masih terngiang: *"Bayangin kalau ini sudah dipakai sales di lapangan."* Di kampus, error adalah nilai minus. Di dunia nyata, error adalah kepercayaan yang hilang.

## **10.4 Failure: Ketika Sistem Benar-Benar Tumbang**

"Tapi," Mas Alin melanjutkan, "ada error yang di luar kendali kita. Database mati total. Koneksi internet putus. Server kehabisan memori. Itu namanya failure—kegagalan sistem yang tidak bisa kita perbaiki langsung dari kode."

"Terus kita gak bisa apa-apa?"

"Kita tetap bisa kasih respons yang tidak bikin panik. Misalnya: 'Terjadi kesalahan pada server. Tim kami sedang menanganinya.' Itu lebih baik daripada menampilkan *stack trace* panjang yang tidak dimengerti pengguna."

Mbak Rara menimpali. "Intinya, jangan bikin pengguna ikut pusing sama masalah kita. Kasih tahu secukupnya, tapi jangan bohong."

## **10.5 Graceful Degradation: Tetap Anggun Meski Terluka**

Mas Alin menggambar di kertas. "Ada konsep namanya Graceful Degradation. Artinya, sistem boleh gagal di satu bagian, tapi jangan sampai seluruh aplikasi mati."

Ia membuat sketsa pesawat terbang. "Ibarat pesawat kehilangan satu mesin. Pesawat gak langsung jatuh. Masih bisa terbang dengan satu mesin, cari tempat mendarat darurat. Itu *graceful degradation*."

"Di API kita, misalnya fitur rekomendasi produk error karena algoritmanya bermasalah. Tapi pengguna masih bisa lihat daftar produk biasa. Fitur utama tetap jalan. Itu yang kita mau."

## **10.6 Logging: Buku Harian Sistem (Pengantar)**

Binto bertanya lagi. "Tapi Mas, kalau kita kasih pesan 'Terjadi kesalahan' terus, gimana kita tahu sebenarnya error apa?"

Mas Alin tersenyum. "Nah, itu fungsi logging. Setiap kali ada exception yang tidak terduga, kita catat detailnya di file log. Bukan untuk pengguna, tapi untuk kita—developer."

Ia menunjukkan contoh di kode:

php

catch (Exception $e) {

    Log::error('Gagal memproses pesanan: ' . $e-\>getMessage(), \[

        'user\_id' \=\> auth()-\>id(),

        'data' \=\> $request-\>all()

    \]);

    

    return response()-\>json(\[

        'message' \=\> 'Terjadi kesalahan. Tim kami sedang menanganinya.'

    \], 500);

}

"Jadi di catch, selain mengembalikan respons ramah, kita juga mencatat error aslinya ke log. Nanti kita bisa cek log untuk debugging. Ini baru pengantar, ya. Nanti di bab khusus kita bahas lebih dalam soal logging."

Binto mengangguk. "Jadi pengguna tenang, kita tetap bisa investigasi."

## **10.7 Praktik: Membungkus Error dengan Elegan**

Binto kembali ke laptopnya. Ia mulai memperbaiki endpoint pesanan.

Pertama, ia membungkus kode pengambilan produk dengan try-catch. Jika produk tidak ditemukan, ia kembalikan 404 dengan pesan jelas.

Kedua, ia menambahkan validasi stok di dalam try. Jika stok tidak cukup, ia lempar exception khusus (throw new InsufficientStockException()) lalu tangkap di catch yang sesuai, mengembalikan 422.

Ketiga, ia menambahkan catch global di akhir untuk menangkap semua exception lain yang tidak terduga. Di dalamnya, ia catat error ke log menggunakan Log::error(), lalu kembalikan respons 500 dengan pesan generik yang ramah.

Setelah selesai, ia mencoba skenario yang kemarin ditemukan Mbak Rara: pesan produk dengan stok 0\. Alih-alih error 500 mentah, kini API mengembalikan:

json

{

    "message": "Stok produk tidak mencukupi"

}

Status code: 422.

Binto tersenyum. Jauh lebih rapi.

## **10.8 Validasi di Controller dan Exception Handler Global**

Mas Alin melihat hasil kerja Binto dan mengangguk puas. "Bagus. Tapi ada satu trik lagi biar lebih rapi."

"Apa, Mas?"

"Kita bisa bikin global exception handler. Jadi gak perlu try-catch di setiap method."

Mas Alin menunjukkan file app/Exceptions/Handler.php. "Di sini kita bisa atur: kalau ada exception jenis tertentu, ubah jadi respons JSON yang sesuai. Misalnya ModelNotFoundException otomatis jadi 404. ValidationException jadi 422. Kamu gak perlu tulis try-catch berulang-ulang."

Binto mencoba. Ia menambahkan beberapa aturan di handler. Lalu ia menghapus try-catch di beberapa endpoint. Hasilnya, error tetap tertangani dengan rapi.

"Wah, jadi lebih bersih kodenya."

"*Nggih*. Tapi ingat, untuk logika bisnis spesifik—seperti stok habis—kamu tetap perlu tangkap sendiri di kode. Karena itu spesifik ke domain."

## **10.9 Refleksi: Menenangkan Sistem yang Menangis**

Sore hari, Binto dan Mbak Rara duduk di teras. Angin Blitar berembus sejuk.

"Aku dulu pikir error handling itu cuma buat developer. Biar gampang debugging," kata Binto. "Ternyata buat pengguna juga."

Mbak Rara mengangguk. "Iya. Sistem yang baik itu seperti orang tua yang menenangkan anaknya yang jatuh. Anak nangis karena lutut lecet. Orang tua gak ikut panik atau marah-marah. Dia pelan-pelan bilang: 'Sakit ya? Sini diobatin. Nanti juga sembuh.'"

Binto tersenyum mendengar analogi itu.

"Error handling yang baik itu menenangkan. Bukan malah bikin tambah panik dengan kata-kata teknis yang gak dimengerti."

## **10.10 Penutup: Rambutan dan Kesalahan**

Mas Alin keluar membawa baskom kecil berisi rambutan. "Ini, panen sore tadi."

Binto mengambil sebutir. Kulitnya merah sempurna. Tapi begitu dikupas, daging buahnya agak kecokelatan di satu sisi—tanda mulai busuk.

"Nah, lihat," kata Mas Alin. "Rambutan ini kulitnya bagus, tapi dalamnya ada cacat. Apa kita buang semua rambutan di baskom?"

"Ya enggak, Mas. Cuma yang ini aja yang disisihkan."

"Persis. Error handling itu seperti memilih rambutan. Kita identifikasi mana yang busuk, kita sisihkan. Tapi kita gak buang seluruh sistem hanya karena satu error kecil. Dan kita gak sajikan rambutan busuk ke tamu."

Mereka bertiga tertawa. Binto menatap pohon rambutan yang masih sarat buah. Pelajaran hari ini melengkapi fondasinya sebagai *engineer*. API bukan cuma soal data keluar-masuk. Tapi juga tentang bagaimana sistem merespons ketika sesuatu tidak berjalan sempurna.

## **10.11 Nasi Kotak Tasyakuran Wawan**

Keesokan harinya, tepat setelah jam makan siang, suasana kantor mendadak riuh. Sebuah mobil Kijang tua berwarna hijau botol parkir di halaman. Dua orang paruh baya berpakaian rapi—sang bapak mengenakan batik kerah kaku dan peci, sang ibu mengenakan gamis dan jilbab syar'i—keluar sambil menenteng dua tas kresek besar berisi tumpukan nasi kotak.

Wawan yang sedang fokus ngoding UI/UX langsung melompat dari kursinya, wajahnya setengah terkejut setengah malu.

"Lho, Bapak, Ibu? Kok gak bilang-bilang kalau mau ke sini?" 

Sang bapak tersenyum lebar, menyalami Pakde Suhar yang langsung menyambut mereka. "Ngapunten lho, Pak Suhar, ganggu jam kerjanya. Ini ibunya Wawan ngotot minta bawain nasi kotak buat selamatan kecil-kecilan."

"Selamatan apa ini, Pak?" tanya Pakde Suhar antusias.

Sang ibu menyahut bangga. "Wawan kemarin baru lulus sidang skripsi S1-nya, Pak. Alhamdulillah. Kuliah online di UT sambil kerja di sini, akhirnya beres juga."

Semua orang di ruangan langsung menoleh ke Wawan, termasuk Binto. Wawan diam-diam menyembunyikan wajahnya yang memerah. 

"Wah, selamat, Wan!" seru Binto sambil menepuk bahu desainer muda itu. Binto baru ingat, di awal kedatangannya ia memang mendengar Wawan diam-diam kuliah online.

"Iya, Mas. Skripsiku bahas UI/UX aplikasi Pabrik Pakan Ternak Garum yang kemarin kita kerjakan. Aku jadiin bahan studi kasus," bisik Wawan pelan. "Proyek kantor tak kuliahkan, hehe."

Mas Alin tertawa mendengarnya. "Pinter kamu. Sekali merengkuh dayung, dua tiga pulau terlampaui. Itu namanya efisiensi."

Mereka semua berkumpul di meja tengah, membuka nasi kotak yang berisi nasi kuning, ayam goreng bumbu laos, sambal goreng ati, dan telur bumbu bali. Suasananya begitu hangat. Bapak dan ibu Wawan terus-menerus mengucapkan terima kasih kepada Pakde Suhar dan Mas Alin karena sudah membimbing putra mereka sejak masih siswa SMK ingusan hingga kini resmi bergelar sarjana.

"Wawan ini dari dulu kalau belajar komputer sampai lupa waktu, Pakde. Alhamdulillah sekarang ilmunya kepakai buat kerja, malah bisa buat skripsi juga," ujar sang ibu dengan mata berkaca-kaca menatap putra tunggalnya.

Pakde Suhar tersenyum lebar. "Anak jenengan ini aset berharga lho di perusahaan kami, Bu. Desainnya itu dipuji-puji klien dari ujung Jawa sampai Kalimantan."

Wawan hanya bisa menunduk malu, tapi senyum tak bisa lepas dari bibirnya. Binto menatap pemandangan itu dengan rasa hangat yang menjalar di dada. Ia teringat bapaknya sendiri di rumah. Ada kebanggaan yang sama di mata orang tua Wawan, kebanggaan tulus seorang ayah dan ibu yang melihat anaknya berhasil melampaui batasan mereka.

Hari itu, tasyakuran nasi kuning ditutup dengan doa bersama yang dipimpin sang bapak. Sebuah penutup hari yang manis. Dan bagi Binto, pelajaran hari ini—tentang API, tentang *graceful degradation*, dan tentang menghargai pencapaian—adalah langkah solid berikutnya menuju kedewasaan seorang *medior*.

---
## **Ringkasan Materi IT Bab 10**

* **Error Handling (Manajemen Kesalahan)**: Praktik menangkap dan mengelola *error* agar aplikasi tidak mati mendadak (*crash*) atau menampilkan pesan *error* mentah (seperti pesan SQL dari *database*). Menampilkan *error* mentah bukan hanya membuat pengguna panik, tapi juga membuka celah keamanan bagi peretas.
* **Exception vs Failure**:
  * **Exception (Pengecualian)**: *Error* yang bisa diprediksi (misal: stok habis, produk tidak ditemukan). Ditangani menggunakan blok `try-catch` untuk memberikan respons status dan pesan yang ramah pengguna (misal: 422 atau 404).
  * **Failure (Kegagalan Fatal)**: *Error* yang di luar kendali program (misal: *server database* mati, jaringan putus). Ditangani dengan pesan generik yang elegan (misal: "Sedang ada gangguan teknis", status 500) tanpa menunjukkan *stack trace* kode.
* **Graceful Degradation (Degradasi Anggun)**: Filosofi perancangan sistem di mana jika satu komponen non-kritis rusak (misalnya fitur rekomendasi AI *error*), aplikasi secara keseluruhan tetap bisa berfungsi dengan baik untuk fitur utamanya (pengguna tetap bisa mencari barang manual dan bertransaksi).
* **Logging (Pencatatan)**: Menyimpan detail teknis dari setiap *error* (seperti baris kode yang rusak dan parameter yang dikirim) secara rahasia ke dalam berkas log di server. Pengguna mendapat pesan error ramah, sementara *developer* bisa melacak dan memperbaiki masalah aslinya lewat catatan log tersebut.
* **Global Exception Handler**: Pusat penanganan error otomatis di dalam kerangka kerja (*framework* modern seperti Laravel). Fitur ini membantu *developer* membungkus berbagai jenis error sistem menjadi format JSON yang standar secara terpusat, sehingga tidak perlu menulis `try-catch` berulang kali di setiap baris kode.