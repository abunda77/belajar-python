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
          "+" + "-" * (col_widths[1]+2) + \
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
          "+" + "-" * (col_widths[1]+2) + \
          "+" + "-" * (col_widths[2]+2) + "+\033[0m")


    
def format_currency(amount, currency):
    if currency == "IDR":
        return "Rp {:,.0f}".format(amount).replace(".", ",")
    else:
        return "${:,.2f}".format(amount)

def format_currency(amount, currency):
    if currency == "IDR":
        return "Rp {:,.0f}".format(amount).replace(".", ",")
    else:
        return "${:,.2f}".format(amount)

def calculator(rows):
    print("Pilih jenis konversi:")
    print("1. IDR ke USD")
    print("2. USD ke IDR")
    print("3. Kembali")
    choice = input("Masukkan pilihan Anda: ")
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
            print(f"Anda memilih konversi {from_currency} ke {to_currency}")
            print(f"Masukkan jumlah {from_currency}:")
            amount = input(f"{from_currency} ")
            if amount.replace(".", "", 1).isdigit():
                amount = float(amount.replace(",", ""))
                if from_currency == "IDR":
                    nilai_jual = float(rows[0][2].replace(",", ""))
                    hasil = amount / nilai_jual
                else:
                    nilai_beli = float(rows[0][1].replace(",", ""))
                    hasil = amount * nilai_beli
                print(f"Jumlah {from_currency} {format_currency(amount, from_currency)} = {to_currency} {format_currency(hasil, to_currency)}")
            else:
                print("Mohon masukkan angka yang valid.")
    else:
        print("Mohon masukkan pilihan yang valid.")


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

while True:
    print("Silakan pilih opsi:")
    print("1. Tampilkan semua kurs")
    print("2. Calculator kurs")
    print("3. Exit")
    choice = input("Masukkan pilihan Anda: ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        choice = int(choice)
        if choice == 1:
            print_table([["Mata Uang", "Nilai Beli", "Nilai Jual"]] + table_rows)
        elif choice == 2:
            calculator(table_rows)
        else:
            break
    else:
        print("Mohon masukkan pilihan yang valid.")