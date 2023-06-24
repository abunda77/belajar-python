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

menu_pilihan = f"Silakan pilih mata uang, cukup ketik angka:\n1. USD\n2. EUR\n3. SGD\n4. AUD\n5. Exit\n"
print(Fore.YELLOW + menu_pilihan + Style.RESET_ALL)

while True:
    pilihan = input()

    if pilihan == '5':
        print(Fore.YELLOW + "Terima kasih telah menggunakan program ini." + Style.RESET_ALL)
        break

    if pilihan in ['1', '2', '3', '4']:
        key = list(mata_uang.keys())[int(pilihan)-1]
        if mata_uang[key] is not None:
            beli, jual = mata_uang[key]
            hasil_output = f"|| Kurs {key}/IDR saat ini - Beli: {beli} || Jual: {jual} ||"
            divider = "-"*len(hasil_output)
            print(Fore.GREEN + f"\n{divider}\n{hasil_output}\n{divider}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Tidak dapat menemukan kurs untuk mata uang {key}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Maaf, pilihan mata uang Anda tidak valid. Silakan coba lagi." + Style.RESET_ALL)
    print(Fore.YELLOW + menu_pilihan + Style.RESET_ALL)
