import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = 'Logistics',
    page_icon = '🚚',
    layout = 'wide'
)

st.title('Logistics Delivery Time & Delay Prediction')

df = pd.read_csv('../data/data_sudah_bersih.csv')
jumlah_kurir = df['ID_Kurir'].nunique()
jumlah_paket = df['Jumlah_Paket'].sum()
rata_waktu_pengiriman = df['Durasi_Pengiriman_Menit'].mean()
presentase_sukses = (df['Status_Keterlambatan'].value_counts()[0]/len(df['Status_Keterlambatan']))*100

with st.container(horizontal=True, gap='medium'):
    cols = st.columns(2, gap='medium')

    with cols[0]:
        st.metric(
            '👷Active Couriers',
            jumlah_kurir,
            width='content'
        )
    with cols[1]:
        st.metric(
            '📦Total Shipments',
            jumlah_paket,
            width='content'
        )
    cols = st.columns(2, gap='medium')

    with cols[0]:
        st.metric(
            '⏱️Average Delivery Time',
            f'{rata_waktu_pengiriman:0.1f} menit',
            width='content'
        )
    with cols[1]:
        st.metric(
            '✅Non-Delay Rate',
            f'{presentase_sukses:0.1f}%',
            width='content'
        )
    
        
