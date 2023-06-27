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

headers = {
    'Authorization': 'Bearer dk_7dbf26f5757141f6808155c5a5af478a'
}

response = requests.post(url, headers=headers, json=payload)

if response.ok:
    print("Pesan berhasil terkirim!")
else:
    print("Terjadi kesalahan saat mengirimkan pesan:", response.text)
