import requests
from bs4 import BeautifulSoup
import json

# Masukkan keyword yang ingin dicari
query = input("Masukkan keyword yang ingin dicari: ")

# Set header User-Agent dan API Key Semrush
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.752.1 Safari/537.36 Edg/20.2.9999.0",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
}

semrushApiKey = input("Masukkan API key Semrush Anda: ")
# Kirim permintaan GET ke Google dengan header User-Agent
url = 'https://www.google.com/search?q=' + query
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Periksa apakah objek BeautifulSoup kosong atau tidak
if not soup.body:
    print("Permintaan GET gagal atau objek body kosong.")
    exit()

# Cari semua elemen hasil pencarian
searchResults = soup.find_all('div', class_='g')

num = 1
# Tampung hasil pencarian dalam format tabel berbentuk teks
table = []
table.append(['NO. URUT', 'JUDUL', 'URL', 'VOLUME PER BULAN'])
for result in searchResults[:10]:
    try:
        title = result.find('h3').get_text()
        url = result.find('a')['href']

        # Kirim permintaan API ke Semrush untuk mendapatkan volume per bulan
        semrushUrl = f"https://api.semrush.com/?type=phrase_this&key={semrushApiKey}&phrase={query}&export_columns=Ph,Nq,Cp,Co,Nr,Td&database=us"
        semrushResponse = requests.get(semrushUrl)
        semrushData = json.loads(semrushResponse.text)['data'][0]
        volume = semrushData['Nq']

        table.append([num, '\033[32m{}\033[0m'.format(
            title), '\033[33m{}\033[0m'.format(url), volume])
    except:
        print("Tidak dapat menampilkan hasil pencarian nomor ", num)
    num += 1

# Tentukan lebar tiap kolom dalam tabel
col_width = [max(len(str(item)) for item in col) for col in zip(*table)]

# Cetak tabel dengan border
print('-'*(sum(col_width)+4))
print('|'+'{:<{}}|{:<{}}|{:<{}}|{:<{}}|'.format(
    table[0][0], col_width[0], table[0][1], col_width[1], table[0][2], col_width[2], table[0][3], col_width[3]))
print('='*(sum(col_width)+4))
for row in table[1:]:
    print('|'+'{:<{}}|{:<{}}|{:<{}}|{:<{}}|'.format(row[0], col_width[0], row[1].strip(
    ).replace('\n', ' '), col_width[1], row[2], col_width[2], row[3], col_width[3]))
    print('-'*(sum(col_width)+4))
