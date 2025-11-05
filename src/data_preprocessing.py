import pandas as pd
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # menghapus missing value
    df.dropna(inplace=True)

    # menghapus duplikat
    df.drop_duplicates(inplace=True)

    # ubah tipe data object ke datetime
    kolom_datetime = ['Tanggal', 'Waktu_Keberangkatan', 'Waktu_Kedatangan']
    for kol in kolom_datetime:
        df[kol] = pd.to_datetime(df[kol])
    
    # outlier 
    #1 hari = 1440 menit, hapus nilai yang lebih dari 1 hari
    df = df[df['Durasi_Pengiriman_Menit'] < 1440]
    return df
