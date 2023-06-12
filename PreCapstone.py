import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout='wide')

st.markdown('<h1 style="font-family: Arial, sans-serif; font-size: 36px; color: #FF9900; text-align: center;">Kriminalitas Indonesia Dashboard</h1>', unsafe_allow_html=True)

import streamlit as st

data_1 = pd.read_csv(r'kriminal_2021.csv')
data_2 = pd.read_csv(r'kriminal_2020.csv')
data_3 = pd.read_csv(r'kriminal_2019.csv')

# Menu Sidebar
st.sidebar.title('Menu')
menu_options = ['Summary', 'Tahun : 2019', 'Tahun : 2020', 'Tahun : 2021']
selected_menu = st.sidebar.radio('', menu_options) 

# Konten berdasarkan pilihan menu
if selected_menu == 'Summary':
    st.markdown('<p style="font-family: \'Bebas Neue\', sans-serif; font-size: 24px; border: 1px solid #000; background-color: #fff; color: #000; padding: 10px; display: inline; border-radius: 20px;">Pengertian Kriminalitas</p></p></p>', unsafe_allow_html=True)

    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Kriminalitas merujuk pada perilaku yang melanggar hukum atau tindakan yang dianggap ilegal dalam suatu masyarakat atau negara. Ini mencakup berbagai jenis kejahatan seperti pembunuhan, pencurian, pemerkosaan, penipuan, perampokan, narkotika, dan banyak lagi. Kriminalitas dapat melibatkan tindakan fisik, seperti kekerasan atau merampok, atau tindakan non-fisik, seperti penipuan melalui internet atau pemalsuan dokumen. Berikut merupakan rangkuman sederhana tentang data kriminalitas berdasarkan Badan Pusat Statistik dalam kurun waktu 2017-2021. </p>', unsafe_allow_html=True)

    line_plot, Description = st.columns(2)
    with line_plot :
        data_5 = pd.read_csv(r'jumlah_kriminalitas.csv')
        # Menghitung total kriminalitas per tahun
        total_kriminal_2017 = data_5['kriminal_2017'].sum()
        total_kriminal_2018 = data_5['kriminal_2018'].sum()
        total_kriminal_2019 = data_5['kriminal_2019'].sum()
        total_kriminal_2020 = data_5['kriminal_2020'].sum()
        total_kriminal_2021 = data_5['kriminal_2021'].sum()

        df_line = pd.DataFrame({
        'Tahun': ['2017', '2018', '2019', '2020', '2021'],
        'Total_Kriminalitas': [total_kriminal_2017, total_kriminal_2018, total_kriminal_2019, total_kriminal_2020, total_kriminal_2021]
        })

        # Membuat Point chart dengan Altair
        line_chart = alt.Chart(df_line).mark_circle(color='Orange', size=100).encode(
        x=alt.X('Tahun:O', title='Tahun'),
        y=alt.Y('Total_Kriminalitas:Q', title='Total Kriminalitas'),
        tooltip=['Tahun:O', 'Total_Kriminalitas:Q']
        ).properties(
        title='Total Kriminalitas per Tahun',
        width=400,
        height=400
        ).configure_title(
        fontSize=18,
        font='Helvetica',
        color='#0099FF'
        )
        st.altair_chart(line_chart, use_container_width=False)
    with Description : 
        
        st.write('<p><p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify; color: #0099FF;"> Kriminalitas  sering  kali  terjadi  di  Indonesia,  bahkan hingga saat ini berita yang disampaikan baik dari media cetak maupun elektronik selalu berkaitan dengan kejahatan kriminalitas. Berdasarkan grafik kriminalitas dari tahun 2017 hingga 2021, terlihat tren menarik bahwa tingkat kejahatan secara konsisten mengalami penurunan seiring berjalannya waktu. </p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family: \'Bebas Neue\', sans-serif; font-size: 24px; border: 1px solid #000; background-color: #fff; color: #000; padding: 10px; display: inline; border-radius: 20px;">Penyelesaian Kriminalitas</p></p></p>', unsafe_allow_html=True)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Penyelesaian kriminalitas merupakan suatu upaya yang melibatkan berbagai faktor dan strategi yang bertujuan untuk mengurangi atau mengatasi tingkat kejahatan dalam suatu masyarakat. Hal ini dapat dilakukan melalui langkah-langkah seperti penegakan hukum yang efektif, pencegahan kejahatan, rehabilitasi narapidana, serta pemenuhan kebutuhan sosial dan ekonomi masyarakat yang rentan terhadap kriminalitas.</p>', unsafe_allow_html=True)


    data_4 = pd.read_csv(r'persent_selesai perprov.csv')
    st.markdown('<h1 style="font-size: 18px; font-family: Helvetica, sans-serif; color: lightyellow;">Persentase Kasus Selesai</h1>', unsafe_allow_html=True)
    st.dataframe(data_4.style.set_properties(**{'background-color': 'lightyellow', 'color': 'black'}))
    
    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Dari tabel persentase kasus selesai. diperoleh kesimpulan bahwa, penyelesaian kasus kriminalitas terlihat beragam dan tidak semua laporan terjadinya tindak kriminal dapat di selesaikan dengan baik. masih banyak di beberapa daerah provinsi bahkan kurang dari 50% laporan tindak pidana diselesaikan. akan tetapi banyak juga di beberapa daerah yang dapat menyeselesaikan lebih dari 50%. Selanjutnya bisa dilihat tren dari beberapa provinsi terkait penyelesain kriminalitas.</p>', unsafe_allow_html=True)
    # Membuat data frame dalam format long
    df_long = data_4.melt(id_vars='polda', var_name='Tahun', value_name='Persentase')

    # Membuat trend line chart dengan Altair
    trend_chart = alt.Chart(df_long).mark_line().encode(
    x=alt.X('Tahun:O', title='Tahun'),
    y=alt.Y('Persentase:Q', title='Persentase Kasus Selesai'),
    color=alt.Color('polda:N', title='Polda')
    ).properties(
    title='Trend Kasus Selesai per Tahun',
    width=400,
    height=1000
    )
    # Menampilkan chart menggunakan Streamlit
    st.altair_chart(trend_chart, use_container_width=True)
  
    # Membaca data dari file CSV
    data_6 = pd.read_csv(r"Kasus selesai 5 teratas.csv")
    data_7 = pd.read_csv(r"Kasus selesai 5 terbawah.csv")

    # Mengatur layout dengan Streamlit
    st.columns(2)
    col1, col2 = st.columns(2)

    # Menampilkan tabel pertama di sebelah kiri
    with col1:
        st.markdown('Kasus Selesai 5 teratas')
        st.dataframe(data_6.style.set_properties(**{'background-color': 'lightyellow', 'color': 'black'}))

    # Menampilkan tabel kedua di sebelah kanan
    with col2:
        st.markdown('Kasus Selesai 5 terbawah')
        st.dataframe(data_7.style.set_properties(**{'background-color': 'lightyellow', 'color': 'black'}))
    
    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Tabel diatas merupakan rata-rata per 5 tahun terkait angka Penyelesaian Kriminalitas. Diperoleh bahwa Provinsi Jawa Tengah merupakan yang tertinggi berhasil dengan angka mencapai 93.8% selesai menangani laporan per 5 tahun dimulai dari 2017-2021.</p>', unsafe_allow_html=True)

    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Sementara untuk penanganan kasus yang cukup lambat per 5 tahun ada di Provinsi Papua Barat yang berkisar 10.11%. </p></p></p>', unsafe_allow_html=True)

    st.markdown('<p style="font-family: \'Bebas Neue\', sans-serif; font-size: 24px; border: 1px solid #000; background-color: #fff; color: #000; padding: 10px; display: inline; border-radius: 20px;">Tipe Kasus Kriminalitas</p></p></p>', unsafe_allow_html=True)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Di Indonesia, jenis-jenis kriminalitas yang umum meliputi pencurian, pemerkosaan, peredaran narkotika, korupsi, kekerasan dalam rumah tangga, terorisme, penculikan, perdagangan manusia, kekerasan jalanan dan lain-lain. Tindakan-tindakan ini melanggar hukum dan dapat dikenai sanksi pidana. Penanggulangan kriminalitas menjadi fokus penting pemerintah dalam rangka menjaga keamanan dan perlindungan masyarakat. Dibawah ini merupakan grafik gambaran jenis jenis kasus dan jumlah kasus yang terjadi di indonesia per tahun nya.</p>', unsafe_allow_html=True)
    
    # Membaca data dari file CSV
    data_8 = pd.read_csv("Tipe_Kejahatann.csv")

    # Mengubah format data menjadi long format
    data_long = data_8.melt(id_vars=['Tipe Kasus'], var_name='Tahun', value_name='Jumlah')

    # Membuat histogram dengan Altair
    histogram = alt.Chart(data_long).mark_bar().encode(
    x=alt.X ('Tahun:N', title='Tahun'),
    y=alt.Y ('Jumlah:Q', stack=None, title='Jumlah Kasus'),
    color=alt.Color('Tipe Kasus:N', legend=alt.Legend(title='Tipe Kasus')),
    column=alt.Column('Tipe Kasus:N', header=alt.Header(title='Tipe Kasus'))
    ).properties(
    title='Tipe Kasus per tahun',
    width=45,
    height=300
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=18,
    font='Helvetica',
    color='purple'
    ).configure_legend(
    labelFontSize=12,
    titleFontSize=14
    )

    # Menampilkan histogram
    st.altair_chart(histogram, use_container_width=False)
    
    data_9 = pd.read_csv("TipeTotalKasus.csv")
    bar_plot = alt.Chart(data_9).mark_bar().encode(
    x=alt.X('Tipe Kasus:N', title='Tipe Kasus', axis=alt.Axis(labelFontSize=12, titleFontSize=14)),
    y=alt.Y('Total Kasus:Q', title='Total Kasus'),
    color=alt.Color('Tipe Kasus:N', legend=alt.Legend(title='Tipe Kasus', labelFontSize=12, titleFontSize=14))
    ).properties(
    title='Total Kasus per Tipe Kasus',
    width=600,
    height=400
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=18,
    font='Helvetica',
    color='purple'
    ).configure_legend(
    labelFontSize=12,
    titleFontSize=14
    )
    st.altair_chart(bar_plot, use_container_width=False)
    st.write('<p style="font-family: Times New Roman, serif; font-size: 16px; text-align: justify;">Terlihat bahwa kasus yang paling sering terjadi dalam kurun waktu 5 tahun, dari 2017 sampai 2021. yang paling menonjol di urutan pertama terbanyak adalah kasus narkoba dan psikotropika. Dan yang paling sedikit diantara beberapa jenis kasus adalah pencurian dengan senjata api. Hal ini cukup logis, karena di Indonesia senjata api di kalangan umum bukanlah hal yang legal. Tetapi menariknya selalu saja masih ada jenis kasus ini setiap tahunnya dalam periode 2017-2021. </p>', unsafe_allow_html=True)

    
    
elif selected_menu == 'Tahun : 2019':
    st.header('Tahun : 2019')
    mx_crime_2, mx_rate_2 = st.columns(2)

    with mx_crime_2:
        jlh_kasus1 = data_3['Jumlah_Kriminalitas'].sum()
        jlh_kasus_formatted = '{:,.0f}'.format(jlh_kasus1)  # Format dengan pemisah ribuan
        diff_pct = (247.218 - 239.481) / 247.218 * 100
        diff_pct_formatted = '{:.2f}'.format(diff_pct)
        st.metric('Jumlah Kasus', jlh_kasus_formatted)

    with mx_rate_2:
        st.metric('Tingkat Risiko Kejahatan', f"{103}/100,000 Penduduk")
    
    # Mengurutkan dataframe berdasarkan Jumlah_Kriminalitas dari tertinggi ke terendah
    data_3_sorted = data_3.sort_values(by='Jumlah_Kriminalitas', ascending=False)

    # Membuat bar plot dengan Altair (Jumlah Kriminalitas)
    chart5 = alt.Chart(data_3_sorted).mark_bar(color='purple').encode(
    x=alt.X('Polda:N', title='POLDA', sort='-y'),
    y=alt.Y('Jumlah_Kriminalitas:Q', title='Jumlah Kriminalitas'),
    tooltip=['Polda:N', 'Jumlah_Kriminalitas:Q']
    ).properties(
    title='Jumlah Kriminalitas Berdasarkan POLDA (Kepolisian Daerah)'
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=16,
    color='purple',
    font='Verdana'
    )

    # Membuat bar plot dengan Altair (Tingkat Risiko Kejahatan)
    chart6 = alt.Chart(data_3_sorted).mark_bar(color='green').encode(
    x=alt.X('Polda:N', title='POLDA', sort='-y'),
    y=alt.Y('Risiko_Kejahatan:Q', title='Tingkat Risiko Kejahatan'),
    tooltip=['Polda:N', 'Risiko_Kejahatan:Q']
    ).properties( title='Tingkat Risiko Kejahatan Berdasarkan Laporan POLDA (Kepolisian Daerah)'
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=16,
    color='green',
    font='Verdana'
    )

    # Menampilkan bar plot
    st.altair_chart(chart5, use_container_width=True)
    st.altair_chart(chart6, use_container_width=True)
    

elif selected_menu == 'Tahun : 2020':
    st.header('Tahun : 2020')
    mx_crime_1, mx_rate_1 = st.columns(2)

    with mx_crime_1:
        jlh_kasus2 = data_2['Jumlah_Kriminalitas'].sum()
        jlh_kasus_formatted = '{:,.0f}'.format(jlh_kasus2)  # Format dengan pemisah ribuan
        diff_pct = (269324 - jlh_kasus2) / jlh_kasus2 * 100
        diff_pct_formatted = '{:.2f}'.format(diff_pct)
        st.metric('Jumlah Kasus', jlh_kasus_formatted, f'-{diff_pct_formatted}%')

    with mx_rate_1:
        st.metric('Tingkat Risiko Kejahatan', f"{94}/100,000 Penduduk", delta= '-9')
    
    # Mengurutkan dataframe berdasarkan Jumlah_Kriminalitas dari tertinggi ke terendah
    data_2_sorted = data_2.sort_values(by='Jumlah_Kriminalitas', ascending=False)

    # Membuat bar plot dengan Altair (Jumlah Kriminalitas)
    chart3 = alt.Chart(data_2_sorted).mark_bar(color='purple').encode(
    x=alt.X('Polda:N', title='POLDA', sort='-y'),
    y=alt.Y('Jumlah_Kriminalitas:Q', title='Jumlah Kriminalitas'),
    tooltip=['Polda:N', 'Jumlah_Kriminalitas:Q']
    ).properties(
    title='Jumlah Kriminalitas Berdasarkan POLDA (Kepolisian Daerah)'
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=16,
    color='purple',
    font='Verdana'
    )

    # Membuat bar plot dengan Altair (Tingkat Risiko Kejahatan)
    chart4 = alt.Chart(data_2_sorted).mark_bar(color='green').encode(
    x=alt.X('Polda:N', title='POLDA', sort='-y'),
    y=alt.Y('Risiko_Kejahatan:Q', title='Tingkat Risiko Kejahatan'),
    tooltip=['Polda:N', 'Risiko_Kejahatan:Q']
    ).properties( title='Tingkat Risiko Kejahatan Berdasarkan Laporan POLDA (Kepolisian Daerah)'
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=16,
    color='green',
    font='Verdana'
    )

    # Menampilkan bar plot
    st.altair_chart(chart3, use_container_width=True)
    st.altair_chart(chart4, use_container_width=True)

elif selected_menu == 'Tahun : 2021':
    st.header('Tahun : 2021')
    mx_crime, mx_rate = st.columns(2)

    with mx_crime:
        jlh_kasus3 = data_1['Jumlah_Kriminalitas'].sum()
        jlh_kasus_formatted = '{:,.0f}'.format(jlh_kasus3)  # Format dengan pemisah ribuan
        diff_pct = (247.218 - 239.481) / 247.218 * 100
        diff_pct_formatted = '{:.2f}'.format(diff_pct)
        st.metric('Jumlah Kasus', jlh_kasus_formatted, f'-{diff_pct_formatted}%')

    with mx_rate:
        penduduk_2021 = 266090000
        rate_risk = int(data_1['Jumlah_Kriminalitas'].sum() / penduduk_2021 * 100000)
        rate_risk_formatted = '{:,.0f}'.format(rate_risk).replace(',', '.')  # Format dengan pemisah ribuan
        st.metric('Tingkat Risiko Kejahatan', f"{rate_risk_formatted}/100.000 Penduduk", delta='-4')
    
    # Mengurutkan dataframe berdasarkan Jumlah_Kriminalitas dari tertinggi ke terendah
    data_1_sorted = data_1.sort_values(by='Jumlah_Kriminalitas', ascending=False)

    # Membuat bar plot dengan Altair (Jumlah Kriminalitas)
    chart1 = alt.Chart(data_1_sorted).mark_bar(color='purple').encode(
    x=alt.X('Polda:N', title='POLDA', sort='-y'),
    y=alt.Y('Jumlah_Kriminalitas:Q', title='Jumlah Kriminalitas'),
    tooltip=['Polda:N', 'Jumlah_Kriminalitas:Q']
    ).properties(
    title='Jumlah Kriminalitas Berdasarkan POLDA (Kepolisian Daerah)'
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=16,
    color='purple',
    font='Verdana'
    )

    # Membuat bar plot dengan Altair (Tingkat Risiko Kejahatan)
    chart2 = alt.Chart(data_1_sorted).mark_bar(color='green').encode(
    x=alt.X('Polda:N', title='POLDA', sort='-y'),
    y=alt.Y('Risiko_Kejahatan:Q', title='Tingkat Risiko Kejahatan'),
    tooltip=['Polda:N', 'Risiko_Kejahatan:Q']
    ).properties( title='Tingkat Risiko Kejahatan Berdasarkan Laporan POLDA (Kepolisian Daerah)'
    ).configure_axis(
    labelFontSize=12,
    titleFontSize=14
    ).configure_title(
    fontSize=16,
    color='green',
    font='Verdana'
    )

    # Menampilkan bar plot
    st.altair_chart(chart1, use_container_width=True)
    st.altair_chart(chart2, use_container_width=True)








