import requests
from bs4 import BeautifulSoup
from datetime import date
import csv
import re

# Get the date in "ddmmyyyy" format
today = date.today().strftime("%d%m%Y")

print("Pilihan menu:")
print("1. Most Popular by Date")
print("2. Most Popular by Rating")
print("3. IMDB Top 250 By Date")

# Ambil input pilihan user
pilihan = int(input("Masukkan pilihan Anda (1/2/3) : "))

if pilihan == 1:
    url = 'https://www.imdb.com/chart/moviemeter/?sort=us,desc&mode=simple&page=1'
    filename = f'imdb-popular-by-date-{today}.csv'
elif pilihan == 2:
    url = 'https://www.imdb.com/chart/moviemeter/?sort=rk,asc&mode=simple&page=1'
    filename = f'imdb-popular-by-rating-{today}.csv'
elif pilihan == 3:
    url = 'https://www.imdb.com/chart/top/?sort=us,desc&mode=simple&page=1'
    filename = f'imdb-top-250-{today}.csv'
else:
    print("Input yang anda masukkan salah!")
    exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.752.1 Safari/537.36 Edg/20.2.9999.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

movies = []
for tr in soup.find_all('tr'):
    row = {}
    title_col = tr.find(class_='titleColumn')

    try:
        title = f"{title_col.a.text.strip()} ({title_col.span.text.strip('()')})"
    except AttributeError:
        title = ''

    try:
        rating = tr.find(class_='imdbRating').strong.text
    except AttributeError:
        rating = ''

    row['No.'] = str(len(movies) + 1)
    row['Title'] = str(title)
    row['IMDb Rating'] = str(rating)
    movies.append(row)

# Simpan data ke dalam file CSV
with open(filename, mode='w', newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=movies[0].keys())
    writer.writeheader()
    for movie in movies:
        # Ganti karakter khusus dengan spasi kosong
        sanitized_value = {k: re.sub(r'[^\x00-\x7F]+', ' ', v)
                           for k, v in movie.items()}
        writer.writerow(sanitized_value)

print(f"Data telah berhasil diekspor ke file {filename}!")
