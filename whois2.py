import requests
import json
from colorama import Fore, Style, init

# Inisialisasi modul colorama
init()

# Fungsi untuk mendapatkan data whois domain


def get_whois_data(domain, api_key):
    url = f"https://api.apilayer.com/whois/query?domain={domain}"
    headers = {
        "apikey": api_key,
    }
    response = requests.get(url, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED}Error: {status_code}{Style.RESET_ALL}")
        return None

# Fungsi untuk menampilkan data whois dengan format JSON


def display_whois_data(data):
    json_data = {
        "Domain Name": data['domain_name'],
        "registrar": data['registrar'],
        "whois_server": data['whois_server'],
        "referral_url": data['referral_url'],
        "updated_date": data['updated_date'],
        "creation_date": data['creation_date'],
        "expiration_date": data['expiration_date'],
        "name_servers": data['name_servers'],
        "status": data['status'],
        "emails": data['emails'],
        "dnssec": data['dnssec'],
        "name": data['name'],
        "org": data['org'],
        "address": data['address'],
        "city": data['city'],
        "state": data['state'],
        "zipcode": data['zipcode'],
        "country": data['country']
    }
    print(json.dumps([json_data], indent=2))

# Main program


def main():
    # Baca API key dari file api_key.txt
    api_key = ""
    with open("api_key.txt", "r") as f:
        for line in f:
            if line.startswith("api_key5="):
                api_key = line.split("=")[1].strip()
                break
    if not api_key:
        print(f"{Fore.RED}API key tidak ditemukan. Mohon pastikan file api_key.txt berisi API key yang valid.{Style.RESET_ALL}")
        return

    # Meminta pengguna memasukkan nama domain
    domain = input("Masukkan nama domain: ")

    # Mendapatkan data whois domain dari API
    whois_data = get_whois_data(domain, api_key)

    # Menampilkan hasil dengan format yang mudah dibaca
    if whois_data and whois_data.get('result'):
        print(f"\n{Fore.GREEN}Data whois untuk domain '{domain}':{Style.RESET_ALL}")
        display_whois_data(whois_data['result'])
    else:
        print(
            f"\n{Fore.RED}Tidak dapat memperoleh data whois untuk domain '{domain}'{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
