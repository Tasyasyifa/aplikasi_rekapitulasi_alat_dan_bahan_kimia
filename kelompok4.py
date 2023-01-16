from math import floor
import pandas as pd
import streamlit as st
import numpy as np


st.title('Rekapitulasi Alat dan Bahan Kimia Laboratorium Volumetri')


with st.sidebar:
    add_radio = st.radio(
        "Rekapitulasi",
        ("Alat", "Bahan"))
    
if (add_radio == "Alat"):
    option= tab1, tab2= st.tabs(["Alat Gelas","Alat Non Gelas"])
    with tab1:
        if st.checkbox("erlenmeyer"):
            option = st.selectbox(
                'Ukuran Erlenmeyer',
                ('100 mL', '250 mL'))
            if (option == '100 mL'):
                st.image("https://th.bing.com/th/id/OIP.JQiI5TB86A1aZHocOZ6iyAHaKm?pid=ImgDet&rs=1", width=200)
                erlenmeyer = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', erlenmeyer)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirerlenmeyer100 = erlenmeyer-harga
                st.write("STOK TERSEDIA SEBANYAK", akhirerlenmeyer100," Buah")
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [erlenmeyer],
                            "Barang Pecah": [harga],
                            "Total Barang": [akhirerlenmeyer100],
                        }
                    )
                df = load_data()
                st.dataframe(df)
                
                
            if (option== '250 mL'):
                st.image("https://th.bing.com/th/id/OIP.60BhwTi7GCcaTw2ZYB0cpAHaLG?pid=ImgDet&rs=1", width=200)
                erlenmeyer = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', erlenmeyer)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirerlenmeyer250 = erlenmeyer-harga
                st.write('stok tersedia', akhirerlenmeyer250)
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [erlenmeyer],
                            "Barang Pecah": [harga],
                            "Total Barang": [akhirerlenmeyer250],
                        }
                    )
                df = load_data()
                st.dataframe(df)

        
        elif st.checkbox("labu takar"):
            option = st.selectbox(
                'Ukuran Labu Ukur',
                ('50 mL', '100 mL', '250 mL'))
            if (option == '50 mL'):
                st.image("https://s1.bukalapak.com/img/6287227733/s-1000 1000/aHR0cHM6Ly9lY3M3LnRva29wZWRpYS5uZXQvaW1nL3Byb2R1Y3QtMS8yMDE3.jpg", width=200)
                labu50 = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', labu50)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirlabu50=labu50-harga
                st.write('stok tersedia',akhirlabu50)
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [erlenmeyer],
                            "Barang Pecah": [harga],
                            "Total Barang": [akhirlabu50],
                        }
                    )
                df = load_data()
                st.dataframe(df)
                
            if (option == '100 mL'):
                st.image("https://cdn.eurekabookhouse.co.id/ebh/product/all/labu100.jpg", width=200)
                labu100 = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirlabu100=labu100-harga
                st.write('stok tersedia', akhirlabu100)
            if (option == '250 mL'):
                st.image("https://www.medicalogy.com/images/product/labu-volumetrik-250-ml-duran-2467836.jpg", width=200)
                labu250 = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirlabu250=labu250-harga
                st.write('stok tersedia', akhirlabu250)

        elif st.checkbox("Buret"):
            option = st.selectbox(
                'Ukuran Labu Ukur',
                ('Schelbach','Amberglass'))
            if (option == 'Schelbach'):
                st.image("https://www.piwine.com/media/Products/ss_size1/VP5.jpg", width=200)
                buretSchelbach = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirburetSchelbach=buretSchelbach-harga
                st.write('stok tersedia', akhirburetSchelbach)
            if (option == 'Amberglass'):
                st.image("https://5.imimg.com/data5/EJ/WU/FO/SELLER-90855132/pipette-500x500.jpg", width=200)
                buretAmberglass = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                akhirburetAmberglass=buretAmberglass-harga
                st.write('stok tersedia',  akhirburetAmberglass)
           
        elif st.checkbox("Pipet Volumetri"):
            option = st.selectbox(
                'Ukuran Labu Ukur',
                ('5 mL', '10 mL', '25 mL', '50 mL'))
            if (option == '5 mL'):
                st.image("https://www.piwine.com/media/Products/ss_size1/VP5.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
            if (option == '10 mL'):
                st.image("https://5.imimg.com/data5/EJ/WU/FO/SELLER-90855132/pipette-500x500.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
            if (option == '25 mL'):
                st.image("https://images-na.ssl-images-amazon.com/images/I/11vUAKrroML._SX342_QL70_ML2_.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
            if (option == '50 mL'):
                st.image("https://www.medicalogy.com/images/product/labu-volumetrik-250-ml-duran-2467836.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)

        elif st.checkbox("Pipet Serologi"):
            option = st.selectbox(
                'Ukuran Pipet Serologi',
                ('1 mL', '2 mL', '10 mL', '25 mL'))
            if (option == '1 mL'):
                st.image("https://images-na.ssl-images-amazon.com/images/I/31pGCH+qQ0L._SX342_.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
            if (option == '2 mL'):
                st.image("https://cdn.shopify.com/s/files/1/1007/2144/products/Pipette-Serological-Glass-2mlx0.2ml_1024x1024.jpg?v=1519655337", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
            if (option == '10 mL'):
                st.image("https://th.bing.com/th/id/OIP.ixr2VZZONbd4jrqLV-NBBwHaHa?pid=ImgDet&rs=1", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
            if (option == '25 mL'):
                st.image("https://diagnocine.com/Content/Upload/Product/328001_1200.png", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)


        elif st.checkbox("corong"):
                st.image("https://5.imimg.com/data5/YS/DR/SN/SELLER-102650417/borosil-funnels-plain-long-stem-100-mm-6140077--500x500.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
                
        elif st.checkbox("Batang Pengaduk"):
                st.image("https://5.imimg.com/data5/YS/DR/SN/SELLER-102650417/borosil-funnels-plain-long-stem-100-mm-6140077--500x500.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)

              
    with tab2:
        if st.checkbox("Bulb"):
                st.image("https://th.bing.com/th/id/OIP.wv0JtwJ2tiTn0AtFFhrCbAHaGZ?pid=ImgDet&rs=1", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
           
        elif st.checkbox("Statif"):
                st.image("https://www.vilitek.com/upload/medialibrary/4f4/4f44cbc026de8a4642a5b6bda80f3bce.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
                   
        elif st.checkbox("Bunsen"):
                st.image("https://assets.fishersci.com/TFS-Assets/CCG/product-images/F56236~p.eps-650.jpg", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
                   
        elif st.checkbox("Kaki Tiga"):
                st.image("https://www.bing.com/th?id=OIP.9_ILOQnIFrQZAMlyDf4jtQHaHa&w=150&h=150&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
                   
        elif st.checkbox("Kasa Asbes"):
                st.image("https://www.bing.com/th?id=OIP.cFRNXjIGUZ4Gt0BPozd3YgHaFj&w=150&h=112&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2", width=200)
                number = st.number_input('Jumlah Pemasukan') 
                st.write('Barang Masuk', number)
                harga = st.number_input('Jumlah Pengeluaran') 
                st.write('Jumlah Pengeluaran', harga)
                st.write('stok tersedia', number-harga)
        
        
else:
    option= tab1, tab2= st.tabs(["Padat","Cair"])
    with tab1:
        if st.checkbox("NaOH"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("K2Cr2O7"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)      

        if st.checkbox("Na2B4O7"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)   
            
        if st.checkbox("KMnO4"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("AgNO3"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("CaCO3"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("Na2CO3"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
          
        if st.checkbox("NaCl"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            

    with tab2:
        if st.checkbox("HCl"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("CH3COOH"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)      

        if st.checkbox("H2C2O4"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)   
            
        if st.checkbox("AgOH"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("H2SO4"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga)  
            
        if st.checkbox("Aquadest"):
            number = st.number_input('Jumlah Pemasukan') 
            st.write('Barang Masuk', number)
            harga = st.number_input('Jumlah Pengeluaran') 
            st.write('Jumlah Pengeluaran', harga)
            st.write('stok tersedia', number-harga) 
            
   
            


