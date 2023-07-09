import requests
import json
from colorama import Fore, Style, init
from tqdm import tqdm
import time

# Inisialisasi modul colorama
init()

# Fungsi untuk mendapatkan data whois domain


def get_whois_data(domain, api_key):
    url = "https://whois40.p.rapidapi.com/whois"
    querystring = {"q": domain}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "whois40.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED}Error: {response.status_code}{Style.RESET_ALL}")
        return None

# Fungsi untuk menampilkan data whois dengan format JSON


def display_whois_data(data):
    json_data = {}
    try:
        json_data = {
            "Domain Name": data['domainName'],
            "Registry Domain ID": data['registryDomainId'],
            "Registrar WHOIS Server": data['registrarWhoisServer'],
            # "Registrar URL": data['registrarUrl'],
            "Updated Date": data['updatedDate'],
            "Creation Date": data['creationDate'],

            # "Registrant Organization": data['registrantOrganization'],
            # "Registrant Street": data['registrantStreet'],
            # "Registrant City": data['registrantCity'],
            # "Registrant State/Province": data['registrantStateProvince'],
            # "Registrant Postal Code": data['registrantPostalCode'],
            # "Registrant Country": data['registrantCountry'],
            # "Registrant Phone": data['registrantPhone'],

            # "Admin Organization": data['adminOrganization'],
            # "Admin Street": data['adminStreet'],
            # "Admin City": data['adminCity'],
            # "Admin State/Province": data['adminStateProvince'],
            # "Admin Postal Code": data['adminPostalCode'],
            # "Admin Country": data['adminCountry'],

            # "Tech Name": data['techName'],
            # "Tech Organization": data['techOrganization'],
            # "Tech Street": data['techStreet'],
            # "Tech City": data['techCity'],
            # "Tech State/Province": data['techStateProvince'],
            # "Tech Postal Code": data['techPostalCode'],
            # "Tech Country": data['techCountry'],
            # "Tech Phone": data['techPhone'],
            # "Tech Email": data['techEmail'],
            # "Name Server": data['nameServer'],
            # "DNSSEC": data['dnssec'],
            # "Registrar Abuse Contact Email": data['registrarAbuseContactEmail'],
            # "Registrar Abuse Contact Phone": data['registrarAbuseContactPhone'],
            # "URL of the ICANN Whois Data Problem Reporting System": data['urlOfTheIcannWhoisDataProblemReportingSystem'],
            "Last Update of WHOIS Database": data['lastUpdateOfWhoisDatabase']
        }
    except KeyError as e:
        print(
            f"{Fore.RED}Error: Data whois tidak valid atau tidak ditemukan.{Style.RESET_ALL}")
    else:
        print(json.dumps([json_data], indent=2))

# Main program


def main():
    # Baca API key dari file api_key.txt
    api_key = ""
    with open("api_key.txt", "r") as f:
        for line in f:
            if line.startswith("api_key6="):
                api_key = line.split("=")[1].strip()
                break
    if not api_key:
        print(f"{Fore.RED}API key tidak ditemukan. Mohon pastikan file api_key.txt berisi API key yang valid.{Style.RESET_ALL}")
        return

    # Meminta pengguna memasukkan nama domain
    domain = input("Masukkan nama domain: ")

    # Mengatur warna untuk progress bar
    bar_format = "{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Style.RESET_ALL)

    # Mengatur jumlah iterasi dan total waktu yang dibutuhkan
    total_iterations = 100
    total_time = 1

    # Menjalankan progress bar
    with tqdm(total=total_iterations, bar_format=bar_format) as pbar:
        for i in range(total_iterations):
            pbar.update(1)
            time.sleep(total_time / total_iterations)

    # Menampilkan pesan selesai
    print(f"{Fore.GREEN}Selesai!{Style.RESET_ALL}")

    # Mendapatkan data whois domain dari API
    whois_data = get_whois_data(domain, api_key)

    # Menampilkan hasil
    if whois_data:
        display_whois_data(whois_data)
    else:
        print(
            f"{Fore.RED}Data whois untuk domain {domain} tidak ditemukan.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
