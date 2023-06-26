import requests
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from colorama import init, Fore, Style

init(convert=True)

url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
response = requests.get(url)
data = response.json()

# Membuat Tabel menggunakan prettytable
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
table.align['Wilayah'] = 'r'

# Tampilkan tabel menggunakan prettytable
output_tabel = f"Informasi Gempa Terkini dari BMKG:\n{table}"
print(Fore.GREEN + output_tabel + Style.RESET_ALL)

# Mengumpulkan info Magnitude & Waktu untuk setiap gempa.
list_magnitude = []
list_waktu = []
for info in data["Infogempa"]["gempa"]:
    list_magnitude.append(float(info["Magnitude"]))
    # Memasukkan informasi Tanggal ke dalam list_waktu
    list_waktu.append(info["Tanggal"])

# Membuat plot sederhana
plt.plot(list_waktu, list_magnitude)

# Menambahkan judul dan sumbu pada grafik.
plt.title("Grafik Magnitudo Gempa Bumi Terkini BMKG")
plt.xlabel("Tanggal")  # Mengubah x-label menjadi "Tanggal"
plt.ylabel("Magnitudo")

# Kesampingkan label yang terlalu rapat
fig = plt.gcf()
fig.autofmt_xdate()

# Menampilkan grafik
plt.show()
