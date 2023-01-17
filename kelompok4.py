from math import floor
import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np  
import datetime
    
st.title('Rekapitulasi Alat dan Bahan Kimia Laboratorium Volumetri👨‍🔬')


with st.sidebar:
    st.sidebar.title("Rekapitulasi Alat dan Bahan Kimia Laboratorium Volumetri👨‍🔬") 
    
    st.sidebar.caption("Aplikasi manajemen persediaan alat dan bahan kimia di laboratorium volumetri.") 
    st.sidebar.markdown("Made by")
    if st.button('[Kelompok 4]'):
        st.write("Fauziah Iriana")
        st.write("Tasya Yasyifa")
        st.write("Mega Maysita")
        st.write("Johathan Sinaga")
        st.write("Fadhil Waviyugo")
    st.sidebar.markdown("---")
    st.sidebar.header("Input Stok")
    add_radio = st.radio(
        "Masukkan stok",
        ("Alat", "Bahan")) 
    st.sidebar.markdown("---")

    
if (add_radio == "Alat"):
    option= tab1, tab2= st.tabs(["Alat Gelas","Alat Non Gelas"])
    with tab1:
            alat = st.text("Pilih Alat Yang Akan Di Input:")
          
            if st.checkbox("Erlenmeyer"):
                option = st.selectbox( 
                    'Ukuran Erlenmeyer',
                    ('100 mL', '250 mL'))
                if (option == '100 mL'):
                    st.image("https://th.bing.com/th/id/OIP.JQiI5TB86A1aZHocOZ6iyAHaKm?pid=ImgDet&rs=1", width=200)
                    Erlen1 = st.number_input('Barang Masuk', 0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirErlen1=Erlen1-harga
                    st.write('Stok Tersedia Sebanyak', akhirErlen1, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [Erlen1],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirErlen1],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                
             
                if (option== '250 mL'):
                    st.image("https://th.bing.com/th/id/OIP.60BhwTi7GCcaTw2ZYB0cpAHaLG?pid=ImgDet&rs=1", width=200)
                    Erlen2 = st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirErlen2=Erlen2-harga
                    st.write('Stok Tersedia Sebanyak', akhirErlen2, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [Erlen2],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirErlen2],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                
            elif st.checkbox("Labu Takar"):
                option = st.selectbox(
                    'Ukuran Labu Takar',
                    ('50 mL', '100 mL', '250 mL'))
                if (option == '50 mL'):
                    st.image("https://s1.bukalapak.com/img/6287227733/s-1000-1000/aHR0cHM6Ly9lY3M3LnRva29wZWRpYS5uZXQvaW1nL3Byb2R1Y3QtMS8yMDE3.jpg", width=200)
                    LT50= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirLT50=LT50-harga
                    st.write('Stok Tersedia Sebanyak', akhirLT50, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [LT50],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirLT50],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                    
                if (option == '100 mL'):
                    st.image("https://cdn.eurekabookhouse.co.id/ebh/product/all/labu100.jpg", width=200)
                    LT100= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirLT100=LT100-harga
                    st.write('Stok Tersedia Sebanyak', akhirLT100, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [LT100],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirLT100],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                if (option == '250 mL'):
                    st.image("https://www.medicalogy.com/images/product/labu-volumetrik-250-ml-duran-2467836.jpg", width=200)
                    LT250= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirLT250=LT1250-harga
                    st.write('Stok Tersedia Sebanyak', akhirLT250, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [LT250],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirLT250],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                    
            elif st.checkbox("Buret"):
                option = st.selectbox(
                    'Jenis Buret',
                    ('Schelbach','Amberglass'))
                if (option == 'Schelbach'):
                    st.image("https://th.bing.com/th/id/OIP.sePcEYHnDcoAwDhKschmuAHaMe?pid=ImgDet&rs=1", width=200)
                    buretSchelbach= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirburetSchelbach=buretSchelbach-harga
                    st.write('Stok Tersedia Sebanyak', akhirburetSchelbach, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [buretSchelbach],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirburetSchelbach],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)

                if (option == 'Amberglass'):
                    st.image("https://cdn.shopify.com/s/files/1/0119/9223/6090/products/Burettes-Amber-Glass-Stopcock-Class-B-Borosilicate-Amber-Glass_1024x1024.png?v=1558074468", width=200)
                    buretAmberglass= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirburetAmberglass=buretAmberglass-harga
                    st.write('Stok Tersedia Sebanyak', akhirburetAmberglass, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [buretAmberglass],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirburetAmberglass],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)

            elif st.checkbox("Pipet Volumetri"):
                option = st.selectbox(
                    'Ukuran Labu Ukur',
                    ('5 mL', '10 mL', '25 mL', '50 mL'))
                if (option == '5 mL'):
                    st.image("https://www.piwine.com/media/Products/ss_size1/VP5.jpg", width=200)
                    P5= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP5=P5-harga
                    st.write('Stok Tersedia Sebanyak', akhirP5, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P5],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP5],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)

                    
                if (option == '10 mL'):
                    st.image("https://5.imimg.com/data5/EJ/WU/FO/SELLER-90855132/pipette-500x500.jpg", width=200)
                    st.image("https://www.piwine.com/media/Products/ss_size1/VP5.jpg", width=200)
                    P10= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP10=P10-harga
                    st.write('Stok Tersedia Sebanyak', akhirP10, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P10],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP10],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                if (option == '25 mL'):
                    st.image("https://images-na.ssl-images-amazon.com/images/I/11vUAKrroML._SX342_QL70_ML2_.jpg", width=200)
                    P25= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP25=P25-harga
                    st.write('Stok Tersedia Sebanyak', akhirP25, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P25],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP25],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                if (option == '50 mL'):
                    st.image("https://www.medicalogy.com/images/product/labu-volumetrik-250-ml-duran-2467836.jpg", width=200)
                    P50= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP50=P50-harga
                    st.write('Stok Tersedia Sebanyak', akhirP50, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P50],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP50],
                            }
                       )
                    df = load_data()
                    st.dataframe(df)

            elif st.checkbox("Pipet Serologi"):
                option = st.selectbox(
                    'Ukuran Pipet Serologi',
                    ('1 mL', '2 mL', '10 mL', '25 mL'))
                if (option == '1 mL'):
                    st.image("https://images-na.ssl-images-amazon.com/images/I/31pGCH+qQ0L._SX342_.jpg", width=200)
                    P1= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP1=P1-harga
                    st.write('Stok Tersedia Sebanyak', akhirP1, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P1],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP1],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                if (option == '2 mL'):
                    st.image("https://cdn.shopify.com/s/files/1/1007/2144/products/Pipette-Serological-Glass-2mlx0.2ml_1024x1024.jpg?v=1519655337", width=200)
                    P2= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP2=P2-harga
                    st.write('Stok Tersedia Sebanyak', akhirP2, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P2],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP2],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)

                if (option == '10 mL'):
                    st.image("https://th.bing.com/th/id/OIP.ixr2VZZONbd4jrqLV-NBBwHaHa?pid=ImgDet&rs=1", width=200)
                    P10= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP10=P10-harga
                    st.write('Stok Tersedia Sebanyak', akhirP10, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P10],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP10],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)
                if (option == '25 mL'):
                    st.image("https://diagnocine.com/Content/Upload/Product/328001_1200.png", width=200)
                    P25= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP25=P25-harga
                    st.write('Stok Tersedia Sebanyak', akhirP25, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P25],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP25],
                            }

                        )
                    df = load_data()
                    st.dataframe(df)
            elif st.checkbox("Corong"):
                    st.image("https://5.imimg.com/data5/YS/DR/SN/SELLER-102650417/borosil-funnels-plain-long-stem-100-mm-6140077--500x500.jpg", width=200)
                    C= st.number_input('Barang Masuk',0,1000,100)
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirC=C-harga
                    st.write('Stok Tersedia Sebanyak', akhirC, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [C],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirC],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)


            elif st.checkbox("Batang Pengaduk"):      
                    st.image("https://cdn.eurekabookhouse.co.id/ebh/product/all/pengaduk_kaca.jpg", width=200)
                    P= st.number_input('Barang Masuk',0,1000,100) 
                    harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                    akhirP=P-harga
                    st.write('Stok Tersedia Sebanyak', akhirP, 'Pcs')
                    def load_data():
                        return pd.DataFrame(
                            {
                                "Barang Masuk": [P],
                                "Barang Pecah/Rusak": [harga],
                                "Jumlah Barang": [akhirP],
                            }
                        )
                    df = load_data()
                    st.dataframe(df)


   
              
    with tab2:
        alat = st.text("Pilih Alat Yang Akan Di Input:")
        if st.checkbox("Bulb"):
                st.image("https://th.bing.com/th/id/OIP.wv0JtwJ2tiTn0AtFFhrCbAHaGZ?pid=ImgDet&rs=1", width=200)
                Bulb = st.number_input('Barang Masuk',0,1000,100) 
                harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                akhirBulb=Bulb-harga
                st.write('Stok Tersedia Sebanyak', akhirBulb, 'Pcs')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [Bulb],
                            "Barang Pecah/Rusak": [harga],
                            "Jumlah Barang": [akhirBulb],
                        }
                    )
                df = load_data()
                st.dataframe(df)
           
        elif st.checkbox("Statif"):
                st.image("https://www.vilitek.com/upload/medialibrary/4f4/4f44cbc026de8a4642a5b6bda80f3bce.jpg", width=200)
                Statif = st.number_input('Barang Masuk',0,1000,100) 
                harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                akhirStatif=Statif-harga
                st.write('Stok Tersedia Sebanyak', akhirStatif, 'Pcs')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [Statif],
                            "Barang Pecah/Rusak": [harga],
                            "Jumlah Barang": [akhirStatif],
                        }
                    )
                df = load_data()
                st.dataframe(df)
                   
        elif st.checkbox("Bunsen"):
                st.image("https://assets.fishersci.com/TFS-Assets/CCG/product-images/F56236~p.eps-650.jpg", width=200)
                Bunsen = st.number_input('Barang Masuk',0,1000,100) 
                harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                akhirBunsen=Statif-harga
                st.write('Stok Tersedia Sebanyak', akhirBunsen, 'Pcs')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [Bunsen],
                            "Barang Pecah/Rusak": [harga],
                            "Jumlah Barang": [akhirBunsen],
                        }
                    )
                df = load_data()
                st.dataframe(df)
                
        elif st.checkbox("Kaki Tiga"):
                st.image("https://www.bing.com/th?id=OIP.9_ILOQnIFrQZAMlyDf4jtQHaHa&w=150&h=150&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2", width=200)
                KT = st.number_input('Barang Masuk',0,1000,100) 
                harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                akhirKT=KT-harga
                st.write('Stok Tersedia Sebanyak', akhirKT, 'Pcs')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [KT],
                            "Barang Pecah/Rusak": [harga],
                            "Jumlah Barang": [akhirKT],
                        }
                    )
                df = load_data()
                st.dataframe(df)
                
                   
        elif st.checkbox("Kasa Asbes"):
                st.image("https://www.bing.com/th?id=OIP.cFRNXjIGUZ4Gt0BPozd3YgHaFj&w=150&h=112&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2", width=200)
                KA = st.number_input('Barang Masuk',0,1000,100) 
                harga = st.number_input('Barang Pecah/Rusak',0,1000) 
                akhirKA=KA-harga
                st.write('Stok Tersedia Sebanyak', akhirKA, 'Pcs')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Barang Masuk": [KA],
                            "Barang Pecah/Rusak": [harga],
                            "Jumlah Barang": [akhirKA],
                        }
                    )
                df = load_data()
                st.dataframe(df)
        
        
if (add_radio == "Bahan"):
    alat = st.text("Pilih Bahan Yang Akan Di Input:")
    option= tab1, tab2= st.tabs(["Padat","Cair"])
    with tab1:
        if st.checkbox("NaOH"):
                NaOH= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirNaOH=NaOH-harga
                st.write('Stok Tersedia Sebanyak', akhirNaOH, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [NaOH],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhiRNaOH],
                        }
                    )
                df = load_data()
                st.dataframe(df)
        
            
        if st.checkbox("K2Cr2O7"):
                K2Cr2O7= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirK2Cr2O7=K2Cr2O7-harga
                st.write('Stok Tersedia Sebanyak', akhirK2Cr2O7, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [K2Cr2O7],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirK2Cr2O7],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
        if st.checkbox("Na2B4O7"):
                Na2B4O7= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirNa2B4O7=Na2B4O7-harga
                st.write('Stok Tersedia Sebanyak', akhirNa2B4O7, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [Na2B4O7],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhiNa2B4O7],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
            
        if st.checkbox("KMnO4"):
                KMnO4= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirKMnO4=KMnO4-harga
                st.write('Stok Tersedia Sebanyak', akhirKMnO4, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [KMnO4],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirKMnO4],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
        if st.checkbox("AgNO3"):
                AgNO3= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirAgNO3=AgNO3-harga
                st.write('Stok Tersedia Sebanyak', akhirAgNO3, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [AgNO3],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirAgNO3],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
        if st.checkbox("CaCO3"):
                CaCO3= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirCaCO3=CaCO3-harga
                st.write('Stok Tersedia Sebanyak', akhirCaCO3, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [CaCO3],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirCaCO3],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
            
        if st.checkbox("Na2CO3"):
                Na2CO3= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirNa2CO3=Na2CO3-harga
                st.write('Stok Tersedia Sebanyak', akhirNa2CO3, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [Na2CO3],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirNa2CO3],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
        if st.checkbox("NaCl"):
                NaCl= st.number_input('Bahan Masuk',0,1000,100) 
                harga = st.number_input('Bahan Terpakai',0,1000) 
                akhirNaCl=NaCl-harga
                st.write('Stok Tersedia Sebanyak', akhirNaCl, 'gram')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [NaCl],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirNaCl],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)
    with tab2:
        Bahan = st.text("Pilih Bahan Yang Akan Di Input:")
        if st.checkbox("HCl"):
                HCl= st.number_input('Bahan Masuk',0,10,4) 
                harga = st.number_input('Bahan Terpakai',0,10) 
                akhirHCl=HCl-harga
                st.write('Stok Tersedia Sebanyak', akhirHCl, 'liter')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [HCl],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirHCl],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)  
            
        if st.checkbox("CH3COOH"):
                CH3COOH= st.number_input('Bahan Masuk',0,10,4) 
                harga = st.number_input('Bahan Terpakai',0,10) 
                akhirCH3COOH=CH3COOH-harga
                st.write('Stok Tersedia Sebanyak', akhirCH3COOH, 'liter')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [CH3COOH],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirCH3COOH],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)  
            
        if st.checkbox("H2C2O4"):
                H2C2O4= st.number_input('Bahan Masuk',0,10,4) 
                harga = st.number_input('Bahan Terpakai',0,10) 
                akhirH2C2O4=H2C2O4-harga
                st.write('Stok Tersedia Sebanyak', akhirH2C2O4, 'liter')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [H2C2O4],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirH2C2O4],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)    
            
        if st.checkbox("AgOH"):
                AgOH= st.number_input('Bahan Masuk',0,10,4) 
                harga = st.number_input('Bahan Terpakai',0,10) 
                akhirAgOH=AgOH-harga
                st.write('Stok Tersedia Sebanyak', akhirAgOH, 'liter')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [AgOH],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirAgOH],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)    
            
        if st.checkbox("H2SO4"):
                H2SO4= st.number_input('Bahan Masuk',0,10,4) 
                harga = st.number_input('Bahan Terpakai',0,10) 
                akhirH2SO4=H2SO4-harga
                st.write('Stok Tersedia Sebanyak', akhirH2SO4, 'liter')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [H2SO4],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirH2SO4],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)    
            
        if st.checkbox("Aquadest"):
                Aquadest= st.number_input('Bahan Masuk',0,10,4) 
                harga = st.number_input('Bahan Terpakai',0,10) 
                akhirAquadest=Aquadest-harga
                st.write('Stok Tersedia Sebanyak', akhirAquadest, 'liter')
                def load_data():
                    return pd.DataFrame(
                        {
                            "Bahan Masuk": [Aquadest],
                            "Bahan Terpakai": [harga],
                            "Jumlah Barang": [akhirAquadest],
                        }
                    )
                df = load_data()
                st.dataframe
                st.dataframe(df)  
   
            


