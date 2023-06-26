import requests
from bs4 import BeautifulSoup

query = input("Masukkan keyword yang ingin dicari: ")

# set header User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.752.1 Safari/537.36 Edg/20.2.9999.0"}

# kirim permintaan GET ke Google dengan header User-Agent
url = 'https://www.google.com/search?q=' + query
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

# pastikan objek BeautifulSoup tidak kosong
if soup.body.contents:

    # cari semua elemen hasil pencarian
    searchResults = soup.find_all('div', class_='g')

    num = 1
    # cetak hasil pencarian dalam format tabel berbentuk tekstual
    table = []
    table.append(['NO. URUT', 'JUDUL', 'URL'])
    for result in searchResults[:10]:
        try:
            title = result.find('h3').get_text()
            url = result.find('a')['href']
            table.append([num, '\033[32m{}\033[0m'.format(
                title), '\033[33m{}\033[0m'.format(url)])
        except:
            print("Tidak dapat menampilkan hasil pencarian nomor ", num)
        num += 1

    # tentukan lebar tiap kolom dalam tabel
    col_width = [max(len(str(item)) for item in col) for col in zip(*table)]

    # cetak tabel dengan border
    print('-'*(sum(col_width)+4))
    print('|'+'{:<{}}|{:<{}}|{:<{}}|'.format(
        table[0][0], col_width[0], table[0][1], col_width[1], table[0][2], col_width[2]))
    print('='*(sum(col_width)+4))
    for row in table[1:]:
        print('|'+'{:<{}}|{:<{}}|{:<{}}|'.format(row[0], col_width[0], row[1].strip(
        ).replace('\n', ' '), col_width[1], row[2], col_width[2]))
        print('-'*(sum(col_width)+4))

else:
    print("Permintaan GET gagal atau objek body kosong.")
