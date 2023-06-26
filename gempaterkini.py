import requests
from prettytable import PrettyTable
from colorama import init, Fore, Style

init(convert=True)

url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
response = requests.get(url)
data = response.json()

table = PrettyTable()
table.field_names = ["Tanggal", "Jam", "Magnitudo",
                     "Kedalaman (km)", "Lintang", "Bujur", "Wilayah"]

for info in data["Infogempa"]["gempa"]:
    tanggal = info["Tanggal"]
    jam = info["Jam"]
    magnitudo = info["Magnitude"]
    kedalaman = info["Kedalaman"]
    lintang = info["Lintang"]
    bujur = info["Bujur"]
    wilayah = info["Wilayah"]
    table.add_row([tanggal, jam, magnitudo,
                  kedalaman, lintang, bujur, wilayah])

# Menentukan align rata kanan untuk kolom wilayah
table.align['Wilayah'] = 'l'

output_tabel = f"Informasi Gempa Terkini dari BMKG:\n{table}"
print(Fore.GREEN + output_tabel + Style.RESET_ALL)
