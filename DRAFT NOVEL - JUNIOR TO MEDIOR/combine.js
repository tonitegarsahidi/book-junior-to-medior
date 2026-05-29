const fs = require('fs');
const path = require('path');

// Menggunakan folder tempat script diletakkan
const dirPath = __dirname;
const outputFileName = 'Buku_Junior_to_Medior_Lengkap.md';
const outputFilePath = path.join(dirPath, outputFileName);

// Membaca semua file di dalam direktori
fs.readdir(dirPath, (err, files) => {
    if (err) {
        console.error('Gagal membaca direktori:', err);
        return;
    }

    // Memfilter file yang namanya berformat bab*.md (misal bab0.md, bab1.md, bab10.md, dll.)
    const babFiles = files.filter(file => {
        const match = file.match(/^bab(\d+)\.md$/i);
        return match !== null;
    });

    // Mengurutkan file secara numerik berdasarkan nomor bab
    babFiles.sort((a, b) => {
        const numA = parseInt(a.match(/^bab(\d+)\.md$/i)[1], 10);
        const numB = parseInt(b.match(/^bab(\d+)\.md$/i)[1], 10);
        return numA - numB;
    });

    if (babFiles.length === 0) {
        console.log('Tidak ditemukan file bab*.md di direktori ini.');
        return;
    }

    console.log('Menemukan bab-bab berikut untuk digabungkan:');
    babFiles.forEach(file => console.log(` - ${file}`));

    // Menggabungkan konten seluruh bab
    let combinedContent = '';
    
    babFiles.forEach((file, index) => {
        const filePath = path.join(dirPath, file);
        const content = fs.readFileSync(filePath, 'utf8');
        
        combinedContent += content;
        
        // Memberikan jeda 3 baris kosong antar bab agar rapi
        if (index < babFiles.length - 1) {
            combinedContent += '\n\n\n'; 
        }
    });

    // Menulis hasil gabungan ke file output
    try {
        fs.writeFileSync(outputFilePath, combinedContent, 'utf8');
        console.log(`\nSukses! Semua bab telah digabungkan ke: ${outputFilePath}`);
    } catch (writeErr) {
        console.error('Gagal menulis file gabungan:', writeErr);
    }
});
