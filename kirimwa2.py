import requests

url = "http://45.152.84.84:3001/api/v1/messages"

recipient_number = input(
    "Masukkan nomor telepon penerima (dalam format lokal tanpa tanda '+'): ")

if recipient_number.startswith('0'):
    recipient_number = '62' + recipient_number[1:]

message_body = input("Masukkan isi pesan: ")

payload = {
    "recipient_type": "individual",
    "to": recipient_number,
    "type": "text",
    "text": {
        "body": message_body
    }
}

# Membuka file api_key.txt dan membacanya baris per baris
with open('api_key.txt', 'r') as file:
    lines = file.readlines()

# Mencari baris yang mengandung 'api_key3='
target_line = None
for line in lines:
    if 'api_key3=' in line:
        target_line = line
        break

# Jika baris ditemukan, ekstrak nilai api key
if target_line:
    api_key = target_line.split('=')[1].strip()
    # Menggunakan api_key dalam kode Python
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    # Lakukan sesuatu dengan headers di sini
    print("API Key Valid")
else:
    print("Baris dengan api key tidak ditemukan.")


response = requests.post(url, headers=headers, json=payload)

if response.ok:
    print("Pesan berhasil terkirim!")
else:
    print("Terjadi kesalahan saat mengirimkan pesan:", response.text)
