import requests
from bs4 import BeautifulSoup

url = "https://www.klikbca.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

currency_table = soup.find('table', class_='tbl_currn')

if currency_table is not None:
    print(currency_table.prettify())
else:
    print("Tidak bisa menemukan tabel kurs.")

