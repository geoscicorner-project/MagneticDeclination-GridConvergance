Magnetic Declination & Grid Convergence (WGS84) — QGIS plugin 1.1.0

TUJUAN
Plugin ini menghitung deklinasi magnetik dan elemen medan geomagnetik dari file koefisien IGRF/WMM (.COF), serta konvergensi grid untuk CRS target. Plugin juga menyediakan ilustrasi arah US (utara sebenarnya), UM (utara magnetik), dan UG (utara grid).

PANDUAN PENGISIAN FIELD
1. Tanggal cetak peta
   Pilih tanggal peta akan diterbitkan/dicetak. Tanggal ini menentukan epoch perhitungan geomagnetik. Tanggal harus berada dalam rentang file model yang dipilih.
2. Lintang
   Isi derajat, menit, detik, lalu pilih N (utara) atau S (selatan). Contoh: 4° 18' 17.40" N.
3. Bujur
   Isi derajat, menit, detik, lalu pilih E (timur) atau W (barat). Contoh: 115° 57' 04.80" E.
4. Elevasi di atas ellipsoid (m)
   Isi tinggi dalam meter terhadap ellipsoid WGS84. Model geomagnetik menggunakan tinggi ellipsoidal, bukan elevasi orthometrik terhadap muka laut. Jika data awal berupa elevasi orthometrik H, konversikan menjadi tinggi ellipsoidal h = H + N menggunakan undulasi geoid yang sesuai. Plugin tidak menerapkan koreksi geoid otomatis.
5. CRS untuk konvergensi grid
   Secara default, plugin memilih UTM otomatis dari lintang dan bujur. Gunakan “Pilih CRS lain…” untuk memilih CRS proyeksi lain. Tombol kemudian dapat digunakan untuk kembali ke UTM otomatis.
6. Model Geomagnetic / File model (.COF)
   File default IGRF14.COF disertakan. “Ganti file…” digunakan untuk memilih file lokal IGRF/WMM. “Cek update” hanya membuka situs resmi NOAA/NCEI dan tidak mengunduh/mengganti file secara otomatis. Pastikan format file valid dan rentang waktunya mencakup tanggal perhitungan.
7. Hitung medan magnet
   Klik tombol ini setelah memeriksa seluruh input. Hasil numerik dan ilustrasi diperbarui.

DATA YANG DIPERLUKAN
- Tanggal perhitungan.
- Lintang dan bujur geodetik WGS84.
- Tinggi ellipsoidal dalam meter.
- File koefisien geomagnetik .COF (misalnya IGRF atau WMM) yang sesuai tanggal.
- CRS target untuk konvergensi grid, atau gunakan UTM otomatis.

METODE PENGHITUNGAN
- Medan geomagnetik: menggunakan koefisien harmonik sferis dari file IGRF/WMM yang dipilih untuk menghitung komponen medan pada tanggal, posisi, dan tinggi masukan. Deklinasi berasal dari hubungan komponen horizontal medan; inklinasi dan intensitas dihitung dari komponen medan terkait.
- Konvergensi grid: dihitung menggunakan fungsi faktor proyeksi QGIS untuk CRS target pada koordinat yang dimasukkan. Konvensi tanda mengikuti hasil fungsi CRS/QGIS; untuk membandingkan dengan perangkat lunak lain, pastikan definisi dan konvensi tanda sama.
- Ilustrasi: US = utara sebenarnya, UM = utara magnetik, UG = utara grid. D adalah sudut US–UM (deklinasi magnetik), sedangkan γ adalah sudut US–UG (konvergensi grid). Sudut pada ilustrasi dapat diskematisasi agar terbaca; nilai numerik adalah acuan.

ARTI HASIL
- D (deklinasi magnetik): sudut antara utara sebenarnya dan utara magnetik, ditampilkan sebagai DMS dan derajat desimal.
- γ (konvergensi grid): sudut antara utara sebenarnya dan utara grid, ditampilkan sebagai DMS dan derajat desimal.
- I (inklinasi magnetik): kemiringan arah medan magnet terhadap bidang horizontal.
- H: intensitas horizontal (nT).
- X: komponen utara (nT).
- Y: komponen timur (nT).
- Z: komponen vertikal ke bawah (nT).
- F: intensitas total (nT).
- dD dan dI: perubahan tahunan sudut (menit busur/tahun); dH, dX, dY, dZ, dan dF: perubahan tahunan intensitas (nT/tahun).

HASIL YANG DIHARAPKAN
Setelah menekan “Hitung medan magnet”, bagian hasil menampilkan informasi lokasi dan model, tiga sudut utama (D, γ, I), komponen H/X/Y/Z/F, serta perubahan tahunan. Ilustrasi memperbarui arah UM dan UG. Nilai yang keluar bergantung pada tanggal, koordinat, elevasi, model .COF, dan CRS. Perbedaan dengan sumber lain dapat terjadi jika salah satu masukan, model, atau konvensi tanda berbeda.

INSTALASI
1. Tutup QGIS.
2. Ekstrak folder `magnetic_declination_grid_convergence` ke folder `python/plugins` pada profil QGIS.
   Contoh Windows: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\magnetic_declination_grid_convergence`
3. Buka QGIS, aktifkan plugin di Plugins > Manage and Install Plugins > Installed.
4. Ikon plugin akan muncul di toolbar QGIS. Jika tidak terlihat, periksa menu View > Toolbars dan pastikan toolbar Plugins aktif; ikon juga tersedia di menu plugin.

VERSI 1.1.0
- Menambahkan tombol Panduan penggunaan di jendela plugin, berisi penjelasan field, data yang diperlukan, metode, dan arti hasil.
- Panduan ringkas dan lengkap ditempatkan pada metadata plugin (deskripsi/About di Plugin Manager); panel General yang menambah ruang di jendela utama dihapus. Tombol Panduan di jendela plugin tetap tersedia.
- Menghubungkan icon.svg ke QAction sehingga ikon muncul pada toolbar dan menu plugin.
- Memperbarui metadata dan dokumentasi.

CATATAN PENGUJIAN
Paket diperiksa untuk struktur arsip dan sintaks Python. Runtime QGIS belum diuji otomatis pada instalasi desktop pengguna.

Version 1.1.1: fixed coordinate-seconds fields to accept pasted decimal values from text editors. Both dot and comma decimal separators are normalized.


Versi 1.1.2: field detik lintang/bujur mempertahankan seluruh angka desimal yang diketik atau ditempel; pemisah desimal titik (.) maupun koma (,) diterima. Koma dinormalisasi menjadi titik saat edit selesai/perhitungan.
