#📌 1. Overview Proyek

- Proyek ini bertujuan melakukan segmentasi pelanggan menggunakan data transaksi e-commerce, sehingga bisnis dapat menentukan strategi pemasaran yang lebih efektif berdasarkan perilaku konsumen.

- Metode utama yang digunakan:

- RFM Analysis (Recency, Frequency, Monetary)

- K-Means Clustering

- Visualisasi interaktif melalui Streamlit

- Insight berbasis negara dan strategi pemasaran berbasis segmen

- Proyek ini dikembangkan sebagai bagian dari tugas akhir Analisis Data / Customer Segmentation.

AC06 - Customer-Segmentation-For-Personalized-Retail-Marketing/
│
├── app.py                     # Dashboard Streamlit
├── caps_pro.ipynb             # Notebook proses analisis & clustering
├── online_retail.csv          # Dataset utama
│
├── rfm_df.csv                 # Output hasil RFM
├── cluster_profile.csv        # Data persona cluster
├── heatmap_data.csv           # Matriks transaksi
├── top10_country.csv          # Revenue per negara
├── revenue_month.csv          # Tren revenue bulanan
│
└── README.md                  # Dokumentasi proyek

#🧠 3. Ringkasan Metodologi
3.1 RFM Analysis

- Menghitung tiga metrik utama customer:
- Recency → kapan terakhir bertransaksi
- Frequency → seberapa sering bertransaksi
- Monetary → total nilai belanja
- Kemudian dilakukan skor & normalisasi data sebelum clustering.

3.2 Clustering (K-Means)

###Notebook caps_pro.ipynb berisi:

- Pembersihan data
- Penghapusan missing value
- Feature engineering (RFM)
- Normalisasi MinMaxScaler
- Penentuan jumlah cluster (Elbow method)

###K-Means

Penamaan segmen dengan mapping:
- Big Spenders
- Loyal Customers
- At Risk Customers
- New Customers

#📊 4. Deskripsi File Utama
1. 📝 caps_pro.ipynb — Proses Analisis & Clustering

Notebook ini mencakup seluruh proses analisis:

- Import dan pembersihan dataset online_retail.csv
- Perhitungan fitur RFM
- Normalisasi data untuk K-Means
- Elbow method untuk menentukan jumlah cluster
- Pembentukan cluster pelanggan

Visualisasi:

- Distribusi RFM
- Scatter Plot Cluster
- Boxplot per fitur cluster
- Penyimpanan output:
- rfm_df.csv
- cluster_profile.csv
- heatmap_data.csv
- top10_country.csv
- revenue_month.csv
- Notebook ini merupakan dasar data yang di-load oleh app.py.

2. 🚀 app.py — Dashboard Streamlit

Dashboard interaktif yang terdiri dari:

#🏠 Overview

- Total pelanggan
- Jumlah cluster
- Rata-rata Monetary
- Distribusi segmen pelanggan

#📊 RFM Analysis

- Heatmap korelasi
- Distribusi Recency, Frequency, Monetary
- Visualisasi sederhana RFM

#🎯 Clustering

- Scatter plot Recency vs Frequency
- Radar chart persona cluster
- Warna segmentasi otomatis

#🌍 Country Insight

- Top 10 negara berdasarkan revenue
- Tren revenue bulanan
- Heatmap transaksi (day vs hour)

#💡 Marketing Strategy

##Rekomendasi strategi otomatis untuk tiap segmen:
- Big Spenders
- Loyal Customers
- At Risk Customers
- New Customers

#📑 5. Dataset
- online_retail.csv
- Dataset transaksi e-commerce internasional yang memuat:
- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

Dataset ini menjadi dasar untuk menghasilkan fitur RFM.

#🛠️ 6. Teknologi yang Digunakan

- Python 3.10+
- Streamlit
- Pandas
- Matplotlib & Seaborn
- Plotly Express
- Scikit-Learn
- Jupyter Notebook

#▶️ 7. Cara Menjalankan Proyek
1. Clone repository
git clone https://github.com/username/AC06-Customer-Segmentation-For-Personalized-Retail-Marketing.git
cd AC06-Customer-Segmentation-For-Personalized-Retail-Marketing

2. Install dependencies
pip install -r requirements.txt

3. Jalankan dashboard
streamlit run app.py


Dashboard akan berjalan di:

http://localhost:8501

#📈 8. Hasil Analisis Utama
##Segmen yang terbentuk:

###Big Spenders
- Pelanggan nilai tinggi, order besar, jarang komplain.

###Loyal Customers
- Sering belanja & stabil.

###New Customers
- Transaksi baru, potensi tinggi.

###At Risk Customers
- Mulai tidak aktif dan berpotensi churn.

Insight Tambahan:
- Negara dengan kontribusi revenue terbesar: United Kingdom
- Pola pembelian tinggi di jam kerja
- Bulan tertentu menunjukkan puncak pembelian (dari revenue_month)
- Dashboard memberi gambaran cepat bagi manajemen untuk mengambil keputusan strategi pemasaran.

#🎯 9. Tujuan Proyek (Untuk Laporan Tugas Akhir)
- Proyek ini dikembangkan untuk:
- Menerapkan konsep segmentasi pelanggan dalam domain retail
- Menunjukkan pemahaman dalam pengolahan data, analisis statistik, dan machine learning
- Menyediakan visualisasi interaktif yang memudahkan interpretasi hasil
- Menghasilkan rekomendasi pemasaran berbasis data
