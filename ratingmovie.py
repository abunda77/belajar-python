import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from termcolor import colored

print("Pilihan menu:")
print("1. Most Popular by Date")
print("2. Most Popular by Rating")
print("3. IMDB Top 250 By Date")

# Ambil input pilihan user
pilihan = int(input("Masukkan pilihan Anda (1/2/3) : "))

if pilihan == 1:
    url = 'https://www.imdb.com/chart/moviemeter/?sort=us,desc&mode=simple&page=1'
elif pilihan == 2:
    url = 'https://www.imdb.com/chart/moviemeter/?sort=rk,asc&mode=simple&page=1'
elif pilihan == 3:
    url = 'https://www.imdb.com/chart/top/?sort=us,desc&mode=simple&page=1'
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

    # Menambahkan try-except statement
    try:
        title = colored(title_col.a.text.strip(), 'yellow')
    except AttributeError:
        title = 'N/A'

    try:
        year = title_col.span.text.strip('()')
    except AttributeError:
        year = 'N/A'

    try:
        rating = tr.find(class_='imdbRating').strong.text
    except AttributeError:
        rating = 'N/A'

    row['No.'] = len(movies) + 1
    row['Title'] = title
    row['Year'] = year
    row['IMDb Rating'] = rating
    movies.append(row)

# Menampilkan data dalam bentuk tabel
table = tabulate(movies, headers='keys', showindex=False, tablefmt='pretty')

# Tampilkan tabel
print(table)
