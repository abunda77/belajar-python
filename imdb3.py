import requests
import sys
from termcolor import colored

# Ganti YOUR_OMDB_API_KEY dengan API key yang diberikan oleh OMDB API.
url = 'http://www.omdbapi.com/?apikey=57468bce&t={}&y={}&plot={}'


def translate_to_indonesian(text):
    # Menerjemahkan teks dari bahasa Inggris ke Bahasa Indonesia.
    url_translate = "https://api.mymemory.translated.net/get?q={}&langpair=en|id".format(
        text)
    response = requests.get(url_translate)
    result = response.json()["responseData"]["translatedText"]
    return result


def get_imdb_rating():
    if not sys.stdin.isatty():
        judul_film = input()
    else:
        judul_film = input("Masukkan judul film: ")

    # Meminta input tahun rilis dari user (opsional).
    tahun_rilis = input(
        "Masukkan tahun rilis (tekan 'enter' jika tidak tahu): ")
    if not tahun_rilis:
        tahun_rilis = None
    # Menampilkan pilihan tampilan plot (short atau full).
    print("Pilih tampilan plot:")
    print("1. Short")
    print("2. Full")
    pilihan_tampilan = input("Masukkan nomor pilihan Anda: ")

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

    response = requests.get(url_film)
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
            plot_translated_colored = colored(plot_translated, 'blue')
            print("Film '{}' ({}) \nRating IMDb: {} \nDurasi : {} \nAktor/aktris:{}\nPlot (diterjemahkan): {}\nAwards: {}\n".format(
                judul_film_colored, data.get('Year'), imdb_rating_colored, runtime, actors, plot_translated_colored, awards))
        else:
            print("Film '{}' ({}) \nRating IMDb: {} \nDurasi : {} \nAktor/aktris:{}\nPlot: '{}'\nAwards: {}\n".format(
                judul_film_colored, data.get('Year'), imdb_rating_colored, runtime, actors, plot, awards))


get_imdb_rating()
