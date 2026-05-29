import os
import re

# Mendapatkan direktori tempat script dijalankan
dir_path = os.path.dirname(os.path.abspath(__file__))
output_file_name = 'Buku_Junior_to_Medior_Lengkap.md'
output_file_path = os.path.join(dir_path, output_file_name)

# Pola regex untuk mencocokkan bab*.md (case-insensitive)
pattern = re.compile(r'^bab(\d+)\.md$', re.IGNORECASE)

# Mengambil semua file di direktori
files = os.listdir(dir_path)

# Filter dan kumpulkan file bab*.md beserta nomor babnya
bab_files = []
for file in files:
    match = pattern.match(file)
    if match:
        bab_files.append((int(match.group(1)), file))

# Urutkan berdasarkan nomor bab secara numerik (0, 1, 2, ..., 10, 11)
bab_files.sort(key=lambda x: x[0])

if not bab_files:
    print("Tidak ditemukan file bab*.md di direktori ini.")
    exit()

print("Menemukan bab-bab berikut untuk digabungkan:")
for _, file in bab_files:
    print(f" - {file}")

# Gabungkan konten file
combined_content = []
for _, file in bab_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        combined_content.append(f.read())

# Tulis ke file output dengan jeda 3 baris baru antar bab
separator = '\n\n\n'
full_novel = separator.join(combined_content)

try:
    with open(output_file_path, 'w', encoding='utf-8') as out_f:
        out_f.write(full_novel)
    print(f"\nSukses! Semua bab telah digabungkan ke: {output_file_path}")
except Exception as e:
    print(f"Gagal menulis file gabungan: {e}")
