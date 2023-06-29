import requests
import sys
from termcolor import colored
from tqdm import tqdm
from alive_progress import alive_bar
from time import sleep

# Membaca API keys dari file txt
api_keys = {}

try:
    with open('api_key.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split('=')
                api_keys[key] = value
    print(colored("Berhasil mengakses file API dan membacanya.", 'green'))

    # print("Nilai dalam file api_key.txt:")
    # for key, value in api_keys.items():
    #   print(f"{key}: {value}")
except FileNotFoundError:
    print(colored("File api_key.txt tidak ditemukan.", 'red'))
except IOError:
    print(colored("Terjadi kesalahan saat membaca file api_key.txt.", 'red'))


# Menggunakan API key pertama
api_key_1 = api_keys.get('api_key1')
# print(api_key_1)  # Menampilkan nilai api_key_1 ke layar

if api_key_1:
    # Gunakan API key pertama untuk mengakses API
    url = f"https://www.omdbapi.com/?apikey={api_key_1}&t={{}}&y={{}}&plot={{}}"
    # Ganti YOUR_OMDB_API_KEY dengan API key yang diberikan oleh OMDB API.
    # print(url)  # Menampilkan URL ke layar
# Menggunakan requests.get() untuk mengirim permintaan API
response = requests.get(url.format("Avengers", "2012", "full"))

# Menggunakan API key kedua
api_key_2 = api_keys.get('api_key2')

if api_key_2:
    # Gunakan API key kedua untuk mengakses API
    url2 = f"https://translated-mymemory---translation-memory.p.rapidapi.com/get"

querystring = {
    "langpair": "en|id",
    # "q": "Hello World!",
    "mt": "1",
    "onlyprivate": "0",
    # "de": "a@b.c"
}

headers = {
    "X-RapidAPI-Key": f"{api_key_2}",
    "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
}


def translate_to_indonesian(text):
    querystring["q"] = text
    response = requests.get(url2, headers=headers, params=querystring)
    result = response.json()["responseData"]["translatedText"]
    return result


def get_imdb_rating():
    if not sys.stdin.isatty():
        judul_film = input()
    else:
        judul_film = input(colored("Masukkan judul film: ", 'yellow'))

    # Meminta input tahun rilis dari user (opsional).
    tahun_rilis = input(colored(
        "Masukkan tahun rilis (tekan 'enter' jika tidak tahu): ", 'yellow'))
    if not tahun_rilis:
        tahun_rilis = None

    # Menampilkan pilihan tampilan plot (short atau full).
    print("Pilih tampilan plot:")
    print("1. Short")
    print("2. Full")
    pilihan_tampilan = input(
        colored("Masukkan nomor pilihan Anda: ", "yellow"))

    # Memasukkan opsi plot URL berdasarkan pilihan pengguna.
    if pilihan_tampilan == "1":
        jenis_plot = "short"
    elif pilihan_tampilan == "2":
        jenis_plot = "full"
    else:
        print("Pilihan tidak valid. Menggunakan tampilan plot default (short).")
        jenis_plot = "short"

       # Membuat URL API sesuai input dan pilihan plot.
    url_film = url.format(judul_film, tahun_rilis, jenis_plot)
    # print(url_film)
    # Memulai progress bar dengan spinner ASCII
    with alive_bar(100, title="Searching for movie '{}'".format(judul_film), bar='smooth'), tqdm(total=100, ascii=True) as bar:
        for i in range(100):
            sleep(0.01)
            bar.update(1)

        response = requests.get(url_film)

        if response.status_code != 200:
            print("Permintaan gagal, status code:", response.status_code)
        # return

        data = response.json()

        if data.get('Response') == 'False':
            print("Judul film tidak ditemukan.")
        else:
            imdb_rating = data.get('imdbRating')
            actors = colored(data.get('Actors'), 'yellow', attrs=['bold'])
            plot = colored(data.get('Plot'), 'yellow', attrs=['bold'])
            awards = colored(data.get('Awards'), 'yellow', attrs=['bold'])
            judul_film_colored = colored(
                data.get('Title'), 'yellow', attrs=['bold'])
            imdb_rating_colored = colored(imdb_rating, 'green', attrs=['bold'])
            runtime = colored(data.get('Runtime'), 'yellow', attrs=['bold'])

            # Menerjemahkan isi plot ke Bahasa Indonesia.
            if plot != "N/A":
                plot_translated = translate_to_indonesian(plot)
                plot_translated_colored = colored(plot_translated, 'green')
                print("Film '{}' ({}) \nRating IMDb: {} \nDurasi : {} \nAktor/aktris:{}\nPlot (diterjemahkan): {}\nAwards: {}\n".format(
                    judul_film_colored, data.get('Year'), imdb_rating_colored, runtime, actors, plot_translated_colored, awards))
            else:
                print("Film '{}' ({}) \nRating IMDb: {} \nDurasi : {} \nAktor/aktris:{}\nPlot: '{}'\nAwards: {}\n".format(
                    judul_film_colored, data.get('Year'), imdb_rating_colored, runtime, actors, plot, awards))


get_imdb_rating()
