import requests
from bs4 import BeautifulSoup

def print_table(rows):
    # Hitung lebar setiap kolom
    col_widths = []
    for row in rows:
        for i, cell in enumerate(row):
            cell_width = len(cell)
            if i >= len(col_widths):
                col_widths.append(cell_width)
            elif cell_width > col_widths[i]:
                col_widths[i] = cell_width
    
    # Cetak tabel
    print("\033[94m+" + "-" * (col_widths[0]+2) + \
          "+" + "-" * (col_widths[1]+12) + \
          "+" + "-" * (col_widths[2]+2) + "+\033[0m")
    for row in rows:
        print("\033[94m|\033[0m", end="")
        for i, cell in enumerate(row):
            padding = " " * (col_widths[i] - len(cell))
            if i == 0:
                print(f"\033[1m{cell}\033[0m{padding}\t\033[94m|\033[0m", end="")
            else:
                print(f"\033[91m{cell}\033[0m{padding}\t\033[94m|\033[0m", end="")
        print()
    print("\033[94m+" + "-" * (col_widths[0]+2) + \
          "+" + "-" * (col_widths[1]+12) + \
          "+" + "-" * (col_widths[2]+2) + "+\033[0m")


import pyfiglet
from termcolor import colored

def format_currency(amount, currency):
    if currency == "IDR":
        return colored(f"Rp {amount:,.0f}", "green").replace(".", ",")
    else:
        return colored(f"${amount:,.2f}", "blue")

def calculator(rows):
    print(colored("Pilih jenis konversi:", "yellow"))
    print(colored("1. IDR ke USD", "cyan"))
    print(colored("2. USD ke IDR", "cyan"))
    print(colored("3. Kembali", "cyan"))
    choice = input(colored("Masukkan pilihan Anda: ", "magenta"))
    if choice.isdigit() and 1 <= int(choice) <= 3:
        choice = int(choice)
        if choice == 3:
            return
        else:
            if choice == 1:
                from_currency = "IDR"
                to_currency = "USD"
            else:
                from_currency = "USD"
                to_currency = "IDR"
            print(colored(f"Anda memilih konversi {from_currency} ke {to_currency}", "yellow"))
            print(colored(f"Masukkan jumlah {from_currency}:", "magenta"))
            amount = input(colored(f"{from_currency} ", "blue"))
            if amount.replace(".", "", 1).isdigit():
                amount = float(amount.replace(",", ""))
                if from_currency == "IDR":
                    nilai_jual = float(rows[0][1].replace(",", ""))
                    hasil = amount / (nilai_jual * 1000)
                else:
                    nilai_beli = float(rows[0][2].replace(",", ""))
                    hasil = (amount * nilai_beli) * 1000
                print(colored(f"Jumlah {from_currency} {format_currency(amount, from_currency)} = {to_currency} {format_currency(hasil, to_currency)}", "green" if from_currency == "IDR" else "blue"))
            else:
                print(colored("Mohon masukkan angka yang valid.", "red"))
    else:
        print(colored("Mohon masukkan pilihan yang valid.", "red"))


url = "https://www.klikbca.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

kurs_table = soup.find_all('table', {'width': '139'})[1]
kurs_rows = kurs_table.find_all('tr')

table_rows = []
for row in kurs_rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        mata_uang = cols[0].text.strip()
        nilai_beli = cols[1].text.strip()
        nilai_jual = cols[2].text.strip()
        table_rows.append([mata_uang, nilai_beli, nilai_jual])


# Membuat banner
banner_text = pyfiglet.figlet_format("Kurs BCA ^_^")
colored_banner = colored(banner_text, "green")

print(colored_banner)


while True:
    print(colored("Silakan pilih opsi:", "yellow"))
    print(colored("1. Tampilkan semua kurs", "cyan"))
    print(colored("2. Calculator kurs", "cyan"))
    print(colored("3. Exit", "cyan"))
    choice = input(colored("Masukkan pilihan Anda: ", "magenta"))
    if choice.isdigit() and 1 <= int(choice):
        choice = int(choice)
        
        if choice == 1:
            print_table([["Mata Uang", "Nilai Beli", "Nilai Jual"]] + table_rows)
            
        elif choice == 2:
            calculator(table_rows)
            
        else:
            break
            
    else:
        print(colored("Mohon masukkan pilihan yang valid.", "red"))