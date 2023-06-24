import requests
from bs4 import BeautifulSoup

url = "https://www.klikbca.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

tabel_kurs = soup.find_all('table')
usd_beli, usd_jual = None, None
sgd_beli, sgd_jual = None, None
eur_beli, eur_jual = None, None
aud_beli, aud_jual = None, None

for tbl in tabel_kurs:
    if len(tbl.attrs) > 0 and 'width' in tbl.attrs and tbl.attrs['width'] == '139':

        rows = tbl.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]

            if len(cols)>1 and cols[0]=='USD':
                usd_beli = cols[1]
                usd_jual = cols[2]
            elif len(cols)>1 and cols[0]=='SGD':
                sgd_beli = cols[1]
                sgd_jual = cols[2]
            elif len(cols)>1 and cols[0]=='EUR':
              eur_beli = cols[1]
              eur_jual = cols[2]
            elif len(cols)>1 and cols[0]=='AUD':
              aud_beli = cols[1]
              aud_jual = cols[2]

if usd_beli is not None and usd_jual is not None:
    print("Kurs USD/IDR saat ini - Beli:", usd_beli, "Jual:", usd_jual)

if sgd_beli is not None and sgd_jual is not None:
    print("Kurs SGD/IDR saat ini - Beli:", sgd_beli, "Jual:", sgd_jual)

if eur_beli is not None and eur_jual is not None:
    print("Kurs EUR/IDR saat ini - Beli:", eur_beli, "Jual:", eur_jual)

if aud_beli is not None and aud_jual is not None:
    print("Kurs AUD/IDR saat ini - Beli:", aud_beli, "Jual:", aud_jual)

if all(elem is None for elem in [usd_beli, usd_jual, sgd_beli, sgd_jual, eur_beli, eur_jual, aud_beli, aud_jual]):
    print("Tidak bisa menemukan kurs di klikBCA.")

