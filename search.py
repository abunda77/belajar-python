from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style

query = input("\n\033[33mMasukkan keyword yang ingin dicari: \033[0m")

# set header User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.752.1 Safari/537.36 Edg/20.2.9999.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
}

# buat session untuk mengirim permintaan GET
with requests.Session() as session:
    session.headers.update(headers)

    # kirim permintaan GET ke Google dengan header User-Agent
    url = 'https://www.google.com/search?q=' + query
    response = session.get(url)

    # periksa kode status HTTP
    if response.status_code == 200:
        soup = BeautifulSoup(
            response.content, 'html.parser', from_encoding='utf-8')

        # pastikan objek BeautifulSoup tidak kosong
        if soup.body:
            # cari elemen hasil pencarian
            resultStats = soup.find(id="result-stats")

            # periksa apakah elemen ditemukan
            if resultStats:
                # ekstrak jumlah total hasil pencarian
                totalResults = resultStats.get_text().split()[1]

                print("\n\033[32mJumlah hasil pencarian untuk '\033[0m" + "\033[33m{}\033[0m".format(
                    query) + "\033[32m' adalah\033[0m" + "\033[33m {}\033[0m".format(totalResults))
            else:
                print("Elemen 'result-stats' tidak ditemukan.")

            # cari semua elemen hasil pencarian
            searchResults = soup.find_all('div', class_='g')

            num = 1
            # simpan hasil pencarian ke dalam list-of-lists
            table_data = [['No. Urut', 'Judul', 'URL']]
            for result in searchResults[:50]:
                try:
                    title = result.find('h3').get_text()
                    url = result.find('a')['href']
                    table_data.append([num, title, url])
                    num += 1
                except Exception as e:
                    print(
                        f"Tidak dapat menampilkan hasil pencarian nomor {num}: {e}")

            # warna tulisan pada tabel
            table_data_colored = [[f"{Fore.YELLOW}{item}{Style.RESET_ALL}" if isinstance(
                item, int) else item for item in row] for row in table_data]

            # cetak tampilan tabel dengan warna dan border
            table = tabulate(table_data_colored, headers='firstrow', showindex=False,
                             tablefmt="plain", colalign=("center", "left", "left"))
            table_with_border = "+----------+------------------------------------------------------------+--------------------------------------------------------------------------------------------+\n" + \
                table + "\n+----------+------------------------------------------------------------+--------------------------------------------------------------------------------------------+"
            print(table_with_border)

            # simpan DataFrame ke dalam file CSV
            df = pd.DataFrame(table_data[1:], columns=table_data[0])
            df.to_csv('hasil_pencarian.csv', index=False)

        else:
            print("Objek body kosong.")
    else:
        print("Permintaan GET gagal dengan kode status HTTP {}".format(
            response.status_code))
