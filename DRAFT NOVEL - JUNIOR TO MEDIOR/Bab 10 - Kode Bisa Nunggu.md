# Bab 10: Kode Bisa Nunggu

Matahari siang itu bersinar terik di atas kota Blitar, memanaskan aspal jalanan hingga membiaskan gelombang udara yang tipis di kejauhan. Di dalam kantor, hawa gerah mulai merayap naik, diredam seadanya oleh desau putaran kipas angin yang berputar tanpa lelah. Aroma kopi tubruk yang mulai dingin bercampur dengan ketegangan yang menggantung pekat di ruang tengah.

Telepon kantor berdering kencang menjelang jam sebelas siang, memecah konsentrasi yang tengah berkumpul di meja-meja kerja.

Binto sedang menatap layar monitor dengan rahang mengeras. Endpoint upload dokumen yang semalam ia rapikan sekarang ngadat lagi. Request masuk, proses jalan sebentar, lalu mati di tengah jalan seperti motor tua kehabisan napas.

*Timeout.*

Lagi.

Ia menekan keningnya sendiri.

Di sebelahnya, Wawan sedang mengutak-atik layout halaman pesanan. Mbak Rara dari meja depan sesekali menoleh sambil membuka daftar test case. Mas Andik berdiri dekat dispenser, memandangi dashboard server dari layar HP. Suasana kantor biasa saja. Tapi di kepala Binto, semuanya terasa sempit.

Deadline tiga hari lagi.

Bug masih banyak.

Dan setiap lima menit sekali, rasanya selalu ada hal baru yang muncul.

"Mas, upload yang kemarin itu sudah aman belum?" tanya Wawan tanpa mengalihkan mata dari monitor.

"Belum. Masih timeout," jawab Binto pendek.

"Yang file besar?"

"Iya. Yang file kecil lolos. Yang agak besar, mati di tengah."

Mbak Rara nimbrung dari kursinya. "Kalau nanti lolos di mesinmu tapi gagal di tempat user, aku catat defect lagi ya, Mas. Biar adil."

Biasanya Binto akan menggerutu balik. Hari itu dia cuma menghela napas.

"Iya, Mbak. Catat saja."

Bu Sari yang baru selesai menaruh gelas kopi di meja Mas Alin melirik ke arah mereka. "Mas Binto ini dari tadi mukanya kayak orang mau ujian negara."

"Lebih parah, Bu," sahut Wawan. "Kalau ujian masih bisa nyontek teman. Kalau server timeout, nyonteknya ke siapa?"

Mas Alin tersenyum kecil dari pojoknya, tapi tidak ikut komentar. Ia hanya menutup buku yang sedari tadi dibaca, lalu memandangi layar Binto sekilas.

"Coba cek ukuran file yang masuk sama setting timeout di upstream-nya," katanya tenang.

"Iya, Mas. Ini lagi tak urut satu-satu."

Binto kembali menunduk. Cursor bergerak. Log dibuka. Config dibandingkan. Ia sedang menahan dirinya sendiri agar tidak panik. Tapi justru karena menahan itu, dadanya terasa makin sesak.

Lalu telepon kantor berbunyi lagi.

Bu Sari yang mengangkat.

"GTN, selamat siang... Iya, Bu Sari sendiri... Oh, Mas Catur? Iya... lho, kenapa?"

Nada suaranya berubah.

Binto belum langsung noleh. Masih menatap layar. Masih mengejar satu baris error yang rasanya tinggal sedikit lagi ketemu ujungnya.

Tapi beberapa detik kemudian kantor mendadak terlalu sunyi.

Ia menoleh.

Bu Sari berdiri di dekat meja tengah. Wajahnya pucat. Gagang telepon masih di tangan.

"Mas Binto..."

Jantung Binto seperti ditarik ke bawah.

"Kenapa, Bu?"

"Ini Mas Catur. Tetanggamu itu lho... yang rumahnya dekat mushola ujung gang. Katanya bapakmu tadi pagi jatuh di jalan pas sepedaan ke desa sebelah."

Binto berdiri terlalu cepat sampai kursinya nyeret lantai.

"Jatuh?"

"Iya. Katanya badan bapak drop di jalan. Gula atau tensinya naik-turun, belum jelas. Sempoyongan terus jatuh. Sekarang sudah dibawa ke RS Bhayangkara."

Dunia seperti mundur dua langkah.

Binto menatap Bu Sari. Lalu telepon. Lalu Bu Sari lagi. Seolah kalau dia mengulang tatapan itu beberapa kali, kabarnya akan berubah.

"Bapak nggak bawa HP?"

"Nggak. Mas Catur bilang nggak bawa. Dompetnya ada. Orang-orang kampung kenal. Mas Catur langsung telepon ke sini karena tahu sampeyan kerja di GTN."

Ada jeda sebentar.

Pendek.

Tapi cukup untuk bikin satu kantor ikut menahan napas.

"Kondisinya gimana sekarang?" suara Binto turun setengah nada.

"Masih diperiksa, Mas. Katanya tadi sempat linglung waktu habis jatuh, terus dibawa warga ke rumah sakit."

Binto meraih HP dari meja, hampir menjatuhkan mouse. Jarinya dingin. Kepalanya panas.

"Saya ke sana sekarang."

Ia sudah mau melangkah keluar ketika pandangannya jatuh ke layar monitor. Log masih terbuka. Terminal masih hidup. Bug masih belum selesai.

Refleksnya, refleks yang sama selama berbulan-bulan, langsung muncul.

*Commit dulu?*

*Kasih catatan ke Wawan?*

*Bilang soal config timeout?*

*Kalau aku pergi sekarang terus upload-nya tetap error gimana?*

"Mas..."

Suara Mas Alin memotong semua itu.

Binto menoleh.

Mas Alin sudah berdiri.

Tidak buru-buru. Tidak panik. Tapi wajahnya serius.

"Berangkat saja."

"Mas, ini upload—"

"Binto."

Nada suaranya tetap tenang. Justru itu yang bikin Binto diam.

"Kode bisa nunggu."

Tiga kata terakhir itu jatuh pelan.

Tapi menghantam keras.

Binto masih berdiri mematung.

Mas Alin melangkah mendekat, menepuk lengan atasnya sekali.

"Mas Catur sudah ngabarin. Bapakmu sekarang yang penting. Yang di sini nanti kami pegang dulu."

Wawan langsung menyahut, kali ini tanpa bercanda. "Mas, jalan aja. File yang kemarin biar aku bantu cek dari sisi frontend."

"Aku tahan test case dulu," kata Mbak Rara. "Kalau ada yang urgent nanti tak catat, nggak tak bombardir sekarang."

Mas Andik mengangkat tangan sedikit dari dekat dispenser. "Config server tak lihat nanti. Kamu nggak usah mikir upstream dulu."

Binto menelan ludah.

Ada sesuatu di dadanya yang retak pelan.

"Saya... izin, Mas."

"Iya," kata Mas Alin. "Berangkat. Kode bisa nunggu. Ayahmu jangan."

Kali ini Binto tidak membantah lagi.

Ia mengambil jaket, HP, dompet, lalu nyaris berlari keluar kantor.

---

## 10.1 Jalan ke Rumah Sakit

Perjalanan dua puluh menit itu terasa seperti ditarik panjang oleh kepala yang kacau.

Beat merahnya melaju di jalan yang sama seperti setiap pagi. Tapi siang ini semuanya seperti ditonton dari layar orang lain. Pedagang buah di pinggir jalan. Anak-anak SD berjalan pulang. Motor-motor selap-selip seperti biasa. Binto melihat semuanya, tapi tidak ada yang benar-benar sampai ke otaknya.

*Bapak jatuh di jalan.*

Bukan di rumah.

Bukan di teras.

Bukan di kamar mandi yang dekat pintu dan mudah ditolong.

Di jalan.

Sendirian.

Naik sepeda.

Mas Catur bilang bapak tadi pagi mau menemui teman lamanya di desa sebelah. Kebiasaan lama yang jarang diceritakan ke siapa-siapa. Kadang kalau badan sedang enak, bapak memang suka sepedaan pelan-pelan. Tidak jauh. Tidak ngebut. Cuma buat ketemu orang, ngopi sebentar, lalu pulang.

Tapi usia enam puluh sekian bukan lagi usia yang bisa ditawar hanya dengan kebiasaan lama.

Binto meremas ujung celananya sendiri.

*Terakhir aku benar-benar ngobrol sama bapak kapan ya?*

Bukan ngobrol sambil lalu.

Bukan jawab seperlunya.

Bukan sambil lihat HP.

Ngobrol betulan.

Ia berusaha mengingat.

Yang muncul justru potongan-potongan kecil.

Bapak nanya, "Kerjamu piye?"

Dia jawab, "Aman, Pak."

Bapak nanya, "Sudah makan?"

Dia jawab, "Sudah."

Selesai.

Sesederhana itu.

Sesedikit itu.

Padahal laki-laki tua itu selalu ada di rumah. Selalu bisa ditemui. Selalu terasa seperti... akan tetap ada besok.

Motor berhenti di depan RS Bhayangkara.

Binto nyaris lupa mematikan mesin sebelum buru-buru turun.

---

## 10.2 Kabar dari Dokter

Mas Catur sudah menunggu di lorong IGD.

Kaosnya basah oleh keringat di punggung. Celana training-nya masih kena debu di bagian lutut. Wajahnya tampak lega begitu melihat Binto datang.

"To. Alhamdulillah, akhirnya nyampe juga."

"Mas Catur... piye?"

Mas Catur menepuk bahunya pelan. "Sudah lebih tenang. Tadi pas jatuh sempat blank sebentar. Untung ada orang warung lihat. Tak bantu angkat sama dua orang lain."

"Jatuhnya parah?"

"Nggak sampai ketabrak apa-apa. Cuma sempoyongan sendiri. Sepedanya nyungsep ke pinggir. Bapakmu kayak orang pusing berat. Keringat dingin. Makanya tadi langsung tak bawa ke sini."

Binto mengangguk, tapi isi kepalanya belum bisa mengejar semua kata-kata itu.

"Ibuk di mana?"

"Masih di dalam sama perawat. Tadi sempat nangis, tapi sekarang sudah agak tenang."

Beberapa menit kemudian dokter keluar dari ruang pemeriksaan sambil membuka map tipis.

"Keluarga Bapak Suwito?"

Binto langsung berdiri. "Saya anaknya, Dok."

Dokter itu masih muda. Matanya lelah, tapi bicaranya rapi.

"Tadi bapak Anda kemungkinan mengalami drop kondisi karena gula darah dan tensi yang tidak stabil. Bukan stroke, bukan perdarahan berat. Setelah jatuh, ada benturan ringan dan badan beliau sempat syok. Makanya kami observasi dulu."

Binto menahan napas.

"Sekarang gimana, Dok?"

"Alhamdulillah membaik. Hasil awalnya cukup tenang. Tidak ada indikasi rawat inap. Sore nanti kalau kondisi tetap stabil, boleh pulang. Tapi beberapa hari ke depan harus benar-benar istirahat. Jangan sepedaan jauh dulu. Makan teratur. Obat jangan telat. Kontrol juga harus lanjut."

Seketika lutut Binto terasa lemas.

Bukan karena kabar buruk.

Justru karena kabar itu cukup baik untuk membuat tubuhnya sadar bahwa ia sedari tadi menahan panik setengah mati.

"Alhamdulillah," katanya lirih.

Dokter mengangguk. "Nanti saya jelaskan lagi ke keluarga ya. Sekarang satu-dua orang saja yang masuk. Bapaknya masih capek."

Mas Catur menepuk punggung Binto. "Masuk sana. Biar saya tunggu luar."

---

## 10.3 Bapak yang Tetap Bapak

Bapak terbaring di ranjang periksa dengan selimut tipis sampai pinggang.

Bukan pemandangan yang dramatis.

Tidak ada alat bunyi panjang. Tidak ada lampu darurat. Tidak ada teriakan.

Justru itu yang membuat adegan itu terasa lebih menusuk.

Laki-laki yang sepanjang hidup Binto selalu tampak lebih dulu bangun, lebih dulu kuat, lebih dulu siap menahan apa pun... sekarang sedang berbaring sambil memejamkan mata, kelelahan seperti anak kecil habis demam.

"Pak..."

Bapak membuka mata pelan.

"Lho," katanya pelan. "Kok kamu ke sini?"

Pertanyaan itu menancap aneh di dada Binto.

Bukan *untung kamu datang*.

Bukan *bapak takut*.

Justru: *kok kamu ke sini?*

Seolah-olah yang sedang merepotkan bukan tubuhnya sendiri, tapi anaknya yang harus meninggalkan kerja.

"Saya dikabari Mas Catur."

"Lho, wong cuma jatuh dikit." Bapak menggeser bahu sedikit. "Nggak usah panik begitu toh."

Binto menatap plester kecil di pelipis bapaknya.

Lalu siku yang lecet.

Lalu tangan yang uratnya makin kelihatan.

Jatuh dikit.

Bapak memang selalu pandai mengecilkan apa yang sebenarnya besar.

"Katanya mau ke desa sebelah, Pak?"

Bapak mengangguk kecil. "Mau nemui Paklik Kasan. Sudah lama nggak ketemu. Wong cuma sepedaan pelan. Lah kok badan malah muter. Kayak orang habis diputer-puter dari dalam."

Ia tertawa tipis, lalu langsung meringis karena masih lelah.

"Dokter bilang gula sama tensi bapak drop, terus naik, terus bikin oleng." 

"Heleh. Dokter itu seneng medeni wong," gumam bapak. Tapi suaranya tidak lagi setegas biasanya.

Binto menarik kursi plastik dan duduk.

Beberapa detik mereka diam.

Diam yang tidak canggung. Tapi juga tidak enteng.

"Kerjamu piye?" tanya bapak.

Itu lagi.

Bukan tanya dirinya sendiri. Bukan tanya tagihan. Bukan tanya sepeda yang mungkin penyok. Yang keluar justru itu.

Kerjamu piye?

"Aman, Pak."

"Jangan bohong. Wajahmu kayak orang belum tidur."

Binto hampir tertawa, tapi suaranya berhenti di tenggorokan.

"Memang lagi banyak, Pak."

"Ya dikerjakan yang bener. Tapi jangan sok kuat terus. Wong badanmu ya badan manusia, bukan mesin pompa air." Bapak memejam lagi, lalu menambahkan pelan, "Bapak aja sok kuat, buktinya ambruk." 

Kali ini Binto benar-benar terkekeh kecil.

Dan justru di situlah rasa sesak itu naik.

Karena bahkan dalam keadaan begini, bapaknya masih sempat menyelipkan canda agar anaknya tidak terlalu takut.

"Pak..."

"Hm?"

"Nanti kalau sudah pulang, sepedanya libur dulu ya."

"Iya. Wong sepeda juga pasti kaget dinaiki orang tua keras kepala begini."

Binto menunduk. Senyumnya ada, tapi matanya panas.

"Matur suwun sudah datang," kata bapak, hampir berbisik.

Kalimat sesederhana itu merobohkan sisa benteng di dada Binto.

Ia mengangguk cepat. Ia takut kalau bicara, suaranya malah akan terserak pecah.

---

## 10.4 Sore yang Turun Pelan

Waktu merangkak lambat, namun perlahan bayang-bayang sore mulai memanjang di lorong rumah sakit. Menjelang ashar, dokter datang lagi dan mengulang penjelasan dengan nada yang jauh lebih ringan.

Kondisi bapak stabil.

Obat jalan disiapkan.

Boleh pulang.

Ibu Binto akhirnya bisa tersenyum lega meski wajahnya masih sembab. Mas Catur ikut membantu urusan administrasi, lalu pamit lebih dulu karena harus kembali ke rumah.

Saat bapak mengganti baju dengan pelan-pelan, Binto berdiri di dekat pintu sambil memandangi notifikasi yang sedari tadi menumpuk di HP.

Dari grup kantor.

Dari Wawan.

Dari Mbak Rara.

Dari Andik.

Dari Mas Alin.

Anehnya, sekarang layar itu tidak terasa seperti sirene perang.

Penting, iya.

Tapi tidak sepenting dua jam lalu.

Tidak sepenting tadi siang ketika ia masih merasa kalau semua bug di monitor harus segera diselamatkan, seolah hidup manusia mau menunggu di pinggir jalan sampai urusan server selesai.

Sekarang urutannya berubah.

Bukan karena kerja jadi tidak penting.

Tapi karena untuk pertama kalinya dalam waktu yang cukup lama, ia dipaksa melihat ukuran dunia dengan benar.

Ada hal yang bisa ditunda.

Ada hal yang tidak.

Dan selama ini ia terlalu sering menyamakan keduanya.

Saat mereka tiba di rumah menjelang magrib, halaman berpaving itu masih hangat oleh sisa matahari. Pohon rambutan kecil di sudut halaman tampak diam saja seperti biasa. Daunnya hijau, batangnya belum besar, dan belum ada tanda-tanda mau berbuah.

Dua tahun lalu, pohon itu ditanam tepat di hari kelulusan Binto.

Waktu itu bapak bilang, "Biar sama-sama tumbuh."

Binto dulu menganggap itu sekadar kalimat orang tua yang suka menempelkan makna ke apa saja.

Sore itu, ia tidak menertawakannya lagi.

---

## 10.5 Orang-Orang GTN Datang

Setelah azan magrib lewat dan bapak sudah minum obat, terdengar suara motor berhenti di depan rumah.

Binto yang sedang menuang air hangat menoleh ke arah pintu.

Dari balik jendela, ia melihat Mas Alin turun lebih dulu. Di belakangnya Pakde Suhar turun pelan sambil membawa kantong plastik besar. Wawan datang paling akhir, menenteng dus kecil yang entah isinya apa.

"Lho..." Binto buru-buru keluar. "Mas? Pakde?"

Pakde Suhar langsung nyengir lebar. "Lho ya masak bosmu iki nggak boleh nengok pegawainya?"

Wawan mengangkat dus di tangannya. "Saya cuma kurir, Mas. Ini Bu Sari nitip bubur sama pisang rebus. Katanya orang habis kaget jangan langsung makan gorengan."

Mas Alin menepuk pundak Binto pelan. "Gimana bapakmu?"

"Alhamdulillah sudah boleh pulang. Cuma harus istirahat total beberapa hari."

"Nah, bagus. Berarti kabar hari ini penutupnya bagus," kata Pakde sambil melongok ke halaman. Pandangannya berhenti ke pohon rambutan kecil di pojok. "Iki sing mbiyen ditandur pas kelulusanmu, ta?"

"Iya, Pakde."

Pakde mendekat dua langkah, mengamati batangnya seperti sedang menilai aset baru. "Masih kecil, tapi sehat. Daunnya apik. Belum waktunya berbuah memang. Wong baru rong taun." 

Bapak yang mendengar suara dari dalam rumah akhirnya muncul di ambang pintu, dibantu ibu. "Lho, Pak Suhar? Repot-repot amat..."

Pakde langsung masuk sambil tertawa. "Repot apanya, Pak? Saya cuma pengin lihat orang yang bikin programmer kami panik setengah mati hari ini."

Bapak ikut tertawa kecil, lalu menoleh ke Binto. "Lha iya?"

Wawan nyelutuk, "Mas Binto tadi mukanya kayak server production mati total, Pak."

"Wawan," tegur Binto pelan, tapi semua orang keburu tertawa.

Suasana yang sejak siang terasa kencang mendadak mengendur.

Mereka duduk seadanya di ruang tamu. Pakde Suhar membuka kantong plastik. Ada jeruk, roti, dan dua bungkus nasi pecel yang dibeli di jalan. Wawan menyerahkan titipan Bu Sari ke ibu Binto. Mas Alin tidak banyak bicara. Ia hanya sesekali menanyakan obat, jadwal kontrol, dan memastikan bapak benar-benar tidak nekat naik sepeda dulu.

"Nek kangen sepedaan, ya jalan kaki di teras dulu saja, Pak," katanya tenang.

"Siap, Mas Alin," jawab bapak dengan gaya seperti anak sekolah ditegur wali kelas.

Di sela obrolan kecil itu, tidak ada yang membahas deadline panjang-panjang.

Tidak ada yang menagih bug.

Tidak ada yang membuat Binto merasa bersalah karena pergi.

Mas Alin hanya bilang singkat, "Yang upload tadi sudah ketemu arahnya. Besok kalau bapak sudah tenang dan kamu juga sudah tidur, baru kita lanjut."

Pakde mengangguk sambil mengupas jeruk. "Kerjaan itu kayak antrean warung. Satu selesai, datang lagi. Tapi orang tua ya cuma satu. Jangan salah urut." 

Biasanya kalimat seperti itu akan terdengar terlalu menggurui di telinga Binto.

Malam itu tidak.

Karena hari itu ia melihat sendiri bagaimana satu kabar bisa membuat semua yang tadi siang terasa mendesak mendadak mengecil ukurannya.

Setelah rombongan GTN pamit, rumah kembali sunyi.

Tapi sunyinya beda.

Bukan sunyi yang kosong.

Lebih seperti sunyi setelah hujan besar lewat.

---

## 10.6 Kode Bisa Nunggu

Malam merayap pelan di rumah Bapak.

Dari kamar depan terdengar suara televisi kecil yang volumenya dikecilkan. Dari dapur ada bunyi sendok beradu gelas. Bapak sudah tertidur lebih cepat dari biasanya. Obat membuat tubuhnya menyerah lebih dulu.

Binto duduk sendirian di teras.

HP-nya ada di tangan.

Layar menyala.

Notifikasi masih banyak.

Tapi kali ini ia tidak buru-buru membuka semuanya.

Di halaman, pohon rambutan kecil itu berdiri diam dalam gelap yang tipis. Belum berbuah. Belum rimbun. Tapi hidup. Tumbuh pelan. Tidak tergesa-gesa. Tidak merasa harus jadi besar besok pagi.

Binto menghembuskan napas panjang.

Lalu untuk pertama kalinya hari itu, ia membiarkan pundaknya benar-benar turun.

Mas Alin benar.

Kode bisa nunggu.

Bug bisa dibetulkan besok.

Config server bisa diulik lagi nanti malam, nanti subuh, atau kapan pun setelah ini.

Tapi siang tadi, kalau ia masih sibuk berdebat dengan layar, ia mungkin akan terlambat sampai di rumah sakit. Mungkin terlambat mendengar bapaknya bercanda tentang sepeda. Mungkin terlambat melihat sendiri bahwa orang yang selama ini selalu ia anggap akan baik-baik saja ternyata juga bisa oleng di jalan desa seperti manusia biasa.

Selama ini ia pikir dewasa berarti selalu sigap pada semua hal.

Ternyata tidak.

Kadang dewasa justru berarti tahu apa yang harus dilepas dulu.

Dari dalam rumah, ibu memanggil pelan, "To... masuk. Anginnya malam dingin."

Binto menoleh ke arah pintu sejenak, lalu untuk terakhir kalinya membiarkan pandangannya menetap pada siluet pohon rambutan di sudut halaman rumahnya.

Masih kecil.

Pasti butuh waktu lama untuk memetik buahnya.

Tapi di bawah siraman embun malam yang bisu, pohon itu tetap hidup. Tetap tumbuh. Dan selayaknya kehidupan, ia tahu persis prioritas utamanya: menguatkan akar sebelum memaksakan buah.

"Iya, Bu. Binto masuk," jawabnya pelan namun tenang.

Ia mematikan layar HP yang masih menyembunyikan tumpukan masalah server, menyurukkannya ke dalam saku, lalu melangkah perlahan kembali ke dalam pelukan hangat rumahnya.