import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# ========== LOAD DATA ==========
rfm_df = pd.read_csv("rfm_df.csv")
revenue_month = pd.read_csv("revenue_month.csv")
heatmap_data = pd.read_csv("heatmap_data.csv", index_col=0)
top_country = pd.read_csv("top10_country.csv")
cluster_profile = pd.read_csv("cluster_profile.csv")

# ========== SIDEBAR ==========
st.sidebar.image("https://images.icon-icons.com/574/PNG/512/Shopping_cart_icon-icons.com_54796.png", width=80)
st.sidebar.title("🔍 Navigation")

menu = st.sidebar.radio(
    "Pilih Halaman:",
    ["🏠 Overview", "📊 RFM Analysis", "🎯 Clustering", "🌍 Country Insight", "💡 Marketing Strategy"]
)

st.sidebar.markdown("---")

# ========== OVERVIEW ==========
if menu == "🏠 Overview":
    st.title("🛍️ Customer Segmentation Dashboard")
    st.write("Analisis perilaku pelanggan menggunakan RFM dan K-Means clustering.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", len(rfm_df))
    col2.metric("Clusters Formed", rfm_df['Cluster'].nunique())
    col3.metric("Avg Monetary 💰", f"${rfm_df['Monetary'].mean():.2f}")

    try:
        st.subheader("📌 Distribusi Customer per Segmen")
        count_seg = rfm_df['Cluster_Name'].value_counts().reset_index()
        count_seg.columns = ['Cluster_Name', 'CustomerCount']
        
        fig = px.bar(
            count_seg,
            x='Cluster_Name', y='CustomerCount',
            title="Jumlah Customer per Segment",
            color='Cluster_Name', text_auto=True
        )
        fig.update_layout(
            xaxis_title="Segment",
            yaxis_title="Jumlah Customer",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error pada grafik segmen: {e}")


    fig.update_layout(
    xaxis_title="Segment",
    yaxis_title="Jumlah Customer",
    showlegend=False
)



# ========== RFM ANALYSIS ==========
elif menu == "📊 RFM Analysis":
    st.title("📊 RFM Feature Analysis")

    # Heatmap Korelasi
    st.subheader("🔥 Korelasi antar fitur RFM")
    fig = px.imshow(
        rfm_df[['Recency','Frequency','Monetary']].corr(),
        text_auto=True, color_continuous_scale="viridis"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Distribusi RFM dalam Tabs
    st.subheader("📈 Distribusi RFM")
    tab1, tab2, tab3 = st.tabs(["Recency", "Frequency", "Monetary"])
    with tab1:
        st.bar_chart(rfm_df['Recency'])
    with tab2:
        st.bar_chart(rfm_df['Frequency'])
    with tab3:
        st.bar_chart(rfm_df['Monetary'])

# ========== CLUSTERING ==========
elif menu == "🎯 Clustering":
    st.title("🎯 Customer Segmentation Result")

    # Scatter Plot
    st.subheader("Cluster Visualization")
    fig = px.scatter(
        rfm_df, x='Recency', y='Frequency',
        color='Cluster_Name', size='Monetary',
        hover_data=['CustomerID'],
        title="Recency vs Frequency by Segment"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Radar Chart Plotly Version (lebih modern)
    st.subheader("🛡 Cluster Persona Radar Chart")
    from math import pi
    import plotly.graph_objects as go

    categories = ['Recency','Frequency','Monetary']
    fig_radar = go.Figure()

    for _, row in cluster_profile.iterrows():
        fig_radar.add_trace(go.Scatterpolar(
            r=row[categories],
            theta=categories,
            fill='toself',
            name=row['Cluster_Name']
        ))

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=True
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# ========== COUNTRY ANALYSIS ==========
elif menu == "🌍 Country Insight":
    st.title("🌍 Country Purchase Insights")

    st.subheader("Top 10 Countries by Revenue")
    fig = px.bar(
        top_country, x='Country', y='TotalPrice',
        title="Revenue Contribution by Country",
        color='Country'
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Revenue Trend per Month")
    fig = px.line(
        revenue_month, x='InvoiceMonth', y='TotalPrice',
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Heatmap of Transactions (Day vs Hour)")
    fig = px.imshow(heatmap_data,
                    color_continuous_scale="inferno",
                    aspect="auto")
    st.plotly_chart(fig, use_container_width=True)

# ========== STRATEGY ==========
elif menu == "💡 Marketing Strategy":
    st.title("💡 Marketing Strategy Recommendation")

    for seg in rfm_df['Cluster_Name'].unique():
        st.markdown(f"## 🎯 {seg}")

        if seg == "Big Spenders":
            st.success("""
💎 **Strategi untuk Big Spenders**
Pelanggan bernilai tinggi yang sering belanja dan berkontribusi besar pada revenue.

**Fokus Utama:**
- Menjaga eksklusivitas dan kepuasan maksimal

**Strategi:**
- Program **VIP Membership** dengan akses produk premium lebih awal
- **Personalized recommendation** berbasis histori pembelian
- **Private support** & layanan konsultatif
- Undangan event terbatas dan hadiah eksklusif
- Program **tier-based reward** agar makin sering belanja
""")

        elif seg == "Loyal Customers":
            st.info("""
🤝 **Strategi untuk Loyal Customers**
Mereka rutin berbelanja dan memiliki loyalitas tinggi.

**Fokus Utama:**
- Memperkuat hubungan jangka panjang

**Strategi:**
- **Loyalty reward** berupa poin yang bisa ditukar
- Program **referral** untuk mengajak teman
- **Gamifikasi** (badge, level, streak)
- Newsletter mingguan berisi tips & promo khusus
- Penawaran **bundling** lebih hemat untuk repeat purchase
""")

        elif seg == "At Risk Customers":
            st.warning("""
⛔ **Strategi untuk At Risk Customers**
Pelanggan yang sebelumnya aktif tetapi mulai jarang berbelanja.

**Fokus Utama:**
- Win-back & re-engagement untuk mencegah churn

**Strategi:**
- **Win-back campaign**: voucher comeback & promo spesial
- Email reminder: notifikasi barang yang pernah diminati
- Penawaran **free shipping** periode terbatas
- Survei kepuasan untuk mengetahui penyebab menurun
- Retargeting ads ke histori produk yang sering dilihat
""")

        elif seg == "New Customers":
            st.info("""
✨ **Strategi untuk New Customers**
Pelanggan baru yang masih eksplorasi produk.

**Fokus Utama:**
- Mendorong pembelian kedua & membangun kepercayaan

**Strategi:**
- **Welcome discount** untuk transaksi berikutnya
- Onboarding edukatif: cara memilih produk & rekomendasi awal
- **Social proof**: highlight review dan testimoni
- Penawaran “**Buy 2 Get Discount**” untuk coba lebih banyak produk
- Reminder follow-up setelah pembelian pertama
""")

    st.markdown("<br>📌 Strategi dibuat berdasarkan karakteristik segmen hasil analisis RFM & Clustering.", unsafe_allow_html=True)
