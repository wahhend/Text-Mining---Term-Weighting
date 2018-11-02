# Text-Mining---Term-Weighting

Tugas ini menggunakan library Sastrawi untuk stemming dan xlwt untuk output ke file .xls

Keterangan untuk setiap file:
source.txt: berisi paragraf yang akan diolah.
stopword-list.txt: berisi kata-kata yang termasuk dalam stopword.
Preprocessing.py: berisi fungsi-fungsi untuk melakukan preprocessing.
TermWeighting.py: berisi fungsi-fungsi untuk melakukan term weighting.
Output.py: class yang memiliki fungsi untuk menuliskan array hasil pemrosesan ke dalam file .xls
Main.py: file utama untuk dijalankan. File ini akan menggunakan fungsi-fungsi di file lainnya dan menuliskannya ke dalam file .xls melalui class Output

File Main.py tidak akan mengeluarkan output apapun.
File Main.py akan menghasilkan file result.xls yang berisi semua hasil pemrosesan.
File result.xls berisi 2 sheet.
Sheet Preprocessing berisi hasil pemrosesan dari preprocessing.
Sheet Term Weighting berisi hasil perhitungan TermWeighting.
