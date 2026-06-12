app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hallabore Project", layout="centered")
st.title("💐 Hallabore Bouquet")
st.write("Selamat datang di katalog resmi Hallabore Bouquet!")

url = "https://docs.google.com/spreadsheets/d/1oKWqQghFwMYztBER22vH3FsGElvT-ZJXX3rJXPw7kqU/export?format=csv"
df = pd.read_csv(url)

search = st.text_input("Cari bouquet...", placeholder="Ketik nama bouquet di sini...")
if search:
    df = df[df['Nama'].str.contains(search, case=False, na=False)]

st.markdown("---")

for idx, row in df.iterrows():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Kita pakai link gambar internet publik dulu biar websitemu LANGSUNG JALAN TANPA EROR!
        if 'Gambar' in df.columns and pd.notna(row['Gambar']) and str(row['Gambar']).startswith('http'):
            st.image(str(row['Gambar']).strip(), use_container_width=True)
        else:
            # Cadangan kalau link gambar di Google Sheets belum beres
            st.warning("Gambar sedang dimuat")
            
    with col2:
        st.subheader(row['Nama'])
        st.write(row['Deskripsi'])
        if 'Harga' in df.columns:
            st.write(f"💰 **Harga:** {row['Harga']}")
        if 'Kategori' in df.columns:
            st.write(f"🏷️ **Kategori:** {row['Kategori']}")
        if 'Stok' in df.columns:
            st.write(f"📦 **Stok:** {row['Stok']}")
        
    st.markdown("---")
