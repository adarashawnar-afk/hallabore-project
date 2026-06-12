import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Hallabore Project", layout="centered")
st.title("💐 Hallabore Bouquet")
st.write("Selamat datang di katalog resmi Hallabore Bouquet!")

url = "https://docs.google.com/spreadsheets/d/1oKWqQghFwMYztBER22vH3FsGElvT-ZJXX3rJXPw7kqU/export?format=csv"
df = pd.read_csv(url)

search = st.text_input("Cari bouquet...", placeholder="Ketik nama bouquet di sini...")
if search:
    df = df[df['Nama'].str.contains(search, case=False, na=False)]

st.markdown("---")

# Foto lokal yang sudah tersimpan di laptopmu
foto_lokal = {
    "LilyHallabore": "lily.jpg",
    "TulippiesHallabore": "tulip.jpg",
    "MixesHallabore": "mix.jpg"
}

for idx, row in df.iterrows():
    col1, col2 = st.columns([1, 2])
    nama_bunga = row['Nama'].strip()
    
    with col1:
        if nama_bunga in foto_lokal and os.path.exists(foto_lokal[nama_bunga]):
            st.image(foto_lokal[nama_bunga], use_container_width=True)
        else:
            st.warning("Gambar tidak tersedia")
            
    with col2:
        st.subheader(row['Nama'])
        st.write(row['Deskripsi'])
        
        # Menampilkan Harga
        if 'Harga' in df.columns:
            st.write(f"💰 **Harga:** {row['Harga']}")
            
        # Menampilkan Kategori
        if 'Kategori' in df.columns:
            st.write(f"🏷️ **Kategori:** {row['Kategori']}")
            
        # Menampilkan Stok
        if 'Stok' in df.columns:
            st.write(f"📦 **Stok:** {row['Stok']}")
        
    st.markdown("---")
