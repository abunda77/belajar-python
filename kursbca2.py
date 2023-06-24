import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(convert=True)

url = "https://www.klikbca.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

tabel_kurs = soup.find_all('table')
mata_uang = {'USD': None, 'SGD': None, 'EUR': None, 'AUD': None}

for tbl in tabel_kurs:
    if len(tbl.attrs) > 0 and 'width' in tbl.attrs and tbl.attrs['width'] == '139':

        rows = tbl.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]

            for key in mata_uang.keys():
                if len(cols)>1 and cols[0]==key:
                    mata_uang[key] = (cols[1], cols[2])

print(Fore.YELLOW + "Pilih mata uang (USD/SGD/EUR/AUD): " + Style.RESET_ALL)
pilihan = input().upper()

if pilihan in mata_uang.keys():
    if mata_uang[pilihan][0] is not None and mata_uang[pilihan][1] is not None:
        print(Fore.GREEN + f"Kurs {pilihan}/IDR saat ini - Beli: {mata_uang[pilihan][0]} Jual: {mata_uang[pilihan][1]}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Tidak dapat menemukan kurs untuk mata uang {pilihan}" + Style.RESET_ALL)
else:
    print(Fore.RED + "Maaf, mata uang yang Anda pilih tidak valid." + Style.RESET_ALL)

