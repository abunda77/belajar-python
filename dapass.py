import requests
from tabulate import tabulate
from colorama import Fore, Style

def load_api_key():
    try:
        with open('apikey.txt', 'r') as file:
            api_key = file.read().strip().split('=')[1]
        return api_key
    except Exception:
        return None

def save_api_key(api_key):
    try:
        with open('apikey.txt', 'w') as file:
            file.write(f'api_key={api_key}\n')
        print('Kunci API berhasil disimpan dalam file api_key.txt.')
    except Exception as e:
        print(f'Gagal menyimpan kunci API: {str(e)}')

def get_domain_metrics(domain, api_key):
    base_url = 'https://domain-da-pa-check.p.rapidapi.com/'

    headers = {
        "X-RapidAPI-Key": api_key,
	    "X-RapidAPI-Host": "domain-da-pa-check.p.rapidapi.com"
    }

    params = {
        'target': domain,
        'cols': '103079215140',
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        result = data['result']
        body = data['body']
        
        if result == 'success':
            target = body['target']
            da_score = body['da_score']
            pa_score = body['pa_score']
            spam_score = body['spam_score']
            total_backlinks = body['total_backlinks']
            
            table_data = [[Fore.GREEN + target, da_score, pa_score, spam_score, total_backlinks]]
            table_header = [Fore.GREEN + "Target", Fore.YELLOW + "DA", Fore.YELLOW + "PA", Fore.YELLOW + "SS", Fore.YELLOW + "Backlink"]
            table = tabulate(table_data, headers=table_header, tablefmt="fancy_grid")
            print(Style.RESET_ALL + table)
        else:
            print('Gagal memperoleh data metrik.')
    else:
        print(f'Gagal memperoleh data metrik. Status Code: {response.status_code}')


def menu():
    api_key = load_api_key()
    while True:
        print('\n===== Aplikasi Cek SEO =====')
        print('1. Simpan/Ganti API Key')
        print('2. Cek Domain Metrics')
        print('3. Exit')

        choice = input('Pilihan Anda: ')

        if choice == '1':
            api_key = input('Masukkan API Key Anda: ')
            save_api_key(api_key)
        elif choice == '2':
            if api_key is None:
                print('Silakan simpan API Key terlebih dahulu.')
            else:
                domain = input('Masukkan Domain yang ingin Anda cek: ')
                get_domain_metrics(domain, api_key)
        elif choice == '3':
            print('Terima kasih telah menggunakan aplikasi ini.')
            break
        else:
            print('Pilihan tidak valid. Silakan pilih 1, 2, atau 3.')

# Menjalankan aplikasi
menu()
