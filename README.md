Data Identifikasi & Waktu ---> Kolom-kolom ini menetapkan identitas unik setiap pengiriman dan kapan peristiwa kunci terjadi.
ID_Pengiriman : dentifier unik untuk setiap entri pengiriman. Relevansi: Digunakan untuk melacak data per individu dan untuk menggabungkannya dengan data eksternal lainnya (jika ada).
Waktu_Keberangkatan : Waktu dan tanggal kurir memulai pengiriman. Relevansi: Ini adalah fitur kunci untuk mengekstrak variabel temporal (Jam, Hari dalam Minggu) yang memengaruhi durasi pengiriman. (Ingat, kolom ini sengaja dibuat kotor dengan berbagai format).
Waktu_Kedatangan : Waktu dan tanggal kurir tiba di tujuan. Relevansi: Digunakan (bersama Waktu_Keberangkatan) untuk menghitung durasi aktual.


Data Spasial & Rute ---> Kolom-kolom ini mendefinisikan geometri rute pengiriman.
Lat_Jemput : Garis Lintang (Latitude) lokasi penjemputan.
Lon_Jemput : Garis Bujur (Longitude) lokasi penjemputan.
Lat_Tujuan : Garis Lintang (Latitude) lokasi tujuan.
Lon_Tujuan : Garis Bujur (Longitude) lokasi tujuan.
Jarak_KM_Terukur : Jarak tempuh aktual yang diukur atau disimulasikan di lapangan (mengikuti jalan, bukan garis lurus). Relevansi: Jarak riil adalah prediktor utama durasi. Mengubah kolom kotor ini menjadi numerik adalah tugas cleaning Anda.


Data Operasional ---> Kolom-kolom ini memberikan detail tentang sumber daya (kurir dan kendaraan) yang digunakan.
ID_Kurir : Identifier unik kurir yang bertugas. Relevansi: Dapat digunakan untuk menganalisis kinerja kurir individu (jika ada kurir yang secara konsisten lambat atau cepat).
Tipe_Kendaraan : Jenis kendaraan yang digunakan (Motor, Mobil Van, Truk Kecil). Relevansi: Berpengaruh signifikan pada kecepatan, kemampuan melewati lalu lintas (Motor vs Truk), dan batasan rute.
Pengalaman_Kurir : Tingkat pengalaman kurir (Rendah, Menengah, Tinggi). Relevansi: Ekspektasinya, kurir berpengalaman akan lebih efisien dalam memilih rute dan mengatasi masalah.
Jumlah_Paket : Jumlah paket yang dibawa kurir untuk pengiriman ini. Relevansi: Kapasitas dan kepadatan pengiriman dapat memengaruhi kecepatan total.


Data Eksternal (Konteks)---> Kolom-kolom ini menjelaskan kondisi lingkungan yang tidak dikontrol perusahaan.
Kondisi_Cuaca : Kondisi cuaca saat pengiriman (Cerah, Hujan Ringan, Badai). Relevansi: Faktor eksternal yang secara langsung memengaruhi kecepatan dan keselamatan.
Kondisi_Lalu_Lintas : Kondisi kepadatan lalu lintas di rute tersebut (Ringan, Sedang, Padat). Relevansi: Salah satu prediktor keterlambatan terkuat, terutama di wilayah perkotaan.
Tipe_Area_Tujuan : Jenis area di lokasi tujuan (Perumahan, Bisnis, Industri). Relevansi: Memengaruhi kemudahan parkir, waktu bongkar muat, dan pola lalu lintas.


Variabel Target & Metrik ---> Kolom-kolom ini adalah target yang ingin Anda prediksi dan metrik yang ada untuk membandingkan.
Durasi_Pengiriman_Menit : Variabel Target Regresi. Waktu total pengiriman dari keberangkatan hingga kedatangan (dalam menit). Relevansi: Memprediksi nilai ini menghasilkan ETA yang akurat. (Kolom ini memiliki nilai NaN yang harus Anda tangani).
ETA_Awal_Menit : Perkiraan Waktu Kedatangan (Estimated Time of Arrival) awal dari sistem logistik (dalam menit). Relevansi: Digunakan untuk menghitung selisih dan status keterlambatan.
Status_Keterlambatan : Variabel Target Klasifikasi. Status apakah pengiriman dianggap terlambat (1) atau tepat waktu (0). (Didefinisikan jika Durasi > ETA Awal + 30 menit). Relevansi: Memprediksi status ini membantu manajemen mengidentifikasi risiko pengiriman secara proaktif.




BISNIS PROBLEM
Dalam proyek analisis logistik ini, masalah bisnis utama yang ingin dipecahkan dapat dikategorikan menjadi tiga area utama: Prediksi (Predictive), Preskriptif (Prescriptive), dan Evaluatif (Evaluative).

Tujuan besarnya adalah meningkatkan efisiensi operasional, mengurangi biaya keterlambatan, dan meningkatkan kepuasan pelanggan melalui ETA yang lebih akurat.

1. Masalah Prediksi: Mengatasi Ketidakpastian Waktu Tiba (ETA)
Masalah paling mendasar dalam logistik last-mile adalah ketidakpastian waktu tiba. Sistem ETA lama seringkali tidak akurat karena hanya mengandalkan faktor dasar (seperti jarak).

Masalah Utama: Keterlambatan Pengiriman
Pertanyaan Bisnis: Bisakah kita secara akurat memprediksi kapan pengiriman akan tiba dan, yang lebih penting, apakah pengiriman tersebut berisiko terlambat sebelum hal itu terjadi?

Tujuan Model:

Model Klasifikasi (Risiko): Memprediksi variabel target Status_Keterlambatan (0 atau 1) dengan akurasi tinggi. Ini memungkinkan intervensi proaktif (misalnya, memberi tahu pelanggan atau mengirim kurir cadangan).

Model Regresi (Durasi): Memprediksi variabel target Durasi_Pengiriman_Menit yang jauh lebih akurat daripada sistem ETA lama (ETA_Awal_Menit).

2. Masalah Preskriptif: Mengoptimalkan Operasi dan Sumber Daya
Setelah mengetahui risiko dan durasi yang akurat, perusahaan ingin mengubah alokasi sumber daya dan rute mereka.

Masalah Utama: Efisiensi Rute dan Biaya Operasional
Pertanyaan Bisnis: Bagaimana kita bisa merancang rute harian yang lebih logis untuk kurir, dan faktor apa yang harus kita minimalkan untuk mengurangi durasi pengiriman?

Tujuan Analisis:

Optimasi Rute (Clustering): Menggunakan koordinat tujuan untuk mengelompokkan pengiriman ke dalam rute yang lebih efisien secara geografis (misalnya, menggunakan algoritma K-Means), meminimalkan waktu tempuh dan biaya bahan bakar.

Identifikasi Faktor Dominan: Menentukan feature importance (misalnya, Rasio_Efisiensi_Rute, Jam Sibuk) untuk mengetahui faktor mana yang paling harus dihindari oleh kurir untuk memastikan ketepatan waktu.

3. Masalah Evaluatif: Memahami Pendorong Kinerja
Masalah evaluatif bertujuan untuk mengubah temuan data menjadi wawasan yang dapat ditindaklanjuti untuk kebijakan perusahaan.

Masalah Utama: Kualitas Data dan Pengambilan Keputusan Strategis
Pertanyaan Bisnis: Apa dampak nyata dari faktor eksternal (cuaca, lalu lintas) dan faktor internal (pengalaman kurir, tipe kendaraan) terhadap kinerja pengiriman?

Tujuan Wawasan:

Menetapkan Baseline: Mengukur seberapa buruk kinerja ETA_Awal_Menit (sistem lama) dibandingkan dengan kinerja model Machine Learning baru Anda, membuktikan nilai dari proyek ini.

Strategi Kontinjensi: Memberikan bukti data kepada manajemen bahwa kondisi tertentu (misalnya, Kondisi_Cuaca_Badai dikombinasikan dengan Kondisi_Lalu_Lintas_Padat) harus memicu kenaikan harga layanan atau penggunaan kendaraan yang berbeda, sehingga mengurangi risiko operasional.

Secara ringkas, proyek ini bertujuan untuk bertransisi dari reaktif (menanggapi keluhan keterlambatan) menjadi proaktif (memprediksi dan mencegah keterlambatan) melalui penggunaan data dan Machine Learning.