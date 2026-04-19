#!/usr/bin/env python3
"""
Script untuk memecah file bookall.md menjadi file terpisah per bab
"""

import re
import os

def split_book_by_chapters(input_file):
    """
    Memecah file markdown menjadi file terpisah per bab
    """
    # Baca file utama
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern untuk mencari judul bab
    chapter_pattern = r'# \*\*Bab (\d+): ([^*]+)\*\*'
    
    # Temukan semua bab
    chapters = list(re.finditer(chapter_pattern, content))
    
    if not chapters:
        print("Tidak menemukan bab dalam file!")
        return
    
    print(f"Menemukan {len(chapters)} bab")
    
    # Buat direktori output jika belum ada
    output_dir = os.path.join(os.path.dirname(input_file), 'bab_terpisah')
    os.makedirs(output_dir, exist_ok=True)
    
    # Proses setiap bab
    for i, match in enumerate(chapters):
        chapter_num = int(match.group(1))
        chapter_title = match.group(2).strip()
        
        # Tentukan posisi awal dan akhir untuk bab ini
        start_pos = match.start()
        
        # Jika ini bukan bab terakhir, ambil sampai awal bab berikutnya
        if i < len(chapters) - 1:
            end_pos = chapters[i + 1].start()
        else:
            # Untuk bab terakhir, ambil sampai akhir file
            end_pos = len(content)
        
        # Ambil konten bab
        chapter_content = content[start_pos:end_pos].strip()
        
        # Buat nama file output
        output_filename = f'bab{chapter_num}.md'
        output_path = os.path.join(output_dir, output_filename)
        
        # Tulis ke file terpisah
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(chapter_content)
        
        print(f"Bab {chapter_num}: {chapter_title} -> {output_filename}")
    
    print(f"\nSelesai! File tersimpan di direktori: {output_dir}")

def main():
    # Path ke file input
    input_file = '/home/ruangrimbun/KERJA/BUKUKU/book-junior-to-medior/dari-kampus-ke-kantor.md/bookall.md'
    
    if not os.path.exists(input_file):
        print(f"File tidak ditemukan: {input_file}")
        return
    
    split_book_by_chapters(input_file)

if __name__ == "__main__":
    main()