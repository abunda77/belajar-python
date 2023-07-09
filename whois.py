import requests
from colorama import Fore, Style, init
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
        print(f"Error: {status_code}")
        return None

# Fungsi untuk menampilkan data whois


def display_whois_data(data):
    for key, value in data.items():
        print(f"{key}: {value}")

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
        print("API key tidak ditemukan. Mohon pastikan file api_key.txt berisi API key yang valid.")
        return

    # Meminta pengguna memasukkan nama domain
    domain = input("Masukkan nama domain: ")

    # Mendapatkan data whois domain dari API
    whois_data = get_whois_data(domain, api_key)

    # Menampilkan hasil
    if whois_data:
        print(Fore.GREEN +
              f"\nData whois untuk domain '{domain}':\n" + Style.RESET_ALL)
        display_whois_data(whois_data)
    else:
        print(
            Fore.RED + f"\nTidak dapat memperoleh data whois untuk domain '{domain}'" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
