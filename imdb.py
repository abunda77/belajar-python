import requests
import sys

# Ganti YOUR_API_KEY dengan API key yang diberikan oleh omdbapi.
url = 'http://www.omdbapi.com/?apikey=57468bce&t={}&y={}'


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

    # Membuat URL API sesuai input.
    url_film = url.format(judul_film, tahun_rilis)

    response = requests.get(url_film)
    data = response.json()
    if data.get('Response') == 'False':
        print("Judul film tidak ditemukan.")
    else:
        imdb_rating = data.get('imdbRating')
        actors = data.get('Actors')
        plot = data.get('Plot')
        awards = data.get('Awards')
        print("Film '{}' ({}) dengan rating IMDb {} memiliki aktor/aktris:\n{}\nPlot: {}\nAwards: {}\n".format(
            data.get('Title'), data.get('Year'), imdb_rating, actors, plot, awards))


get_imdb_rating()
