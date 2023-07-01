import subprocess


# Menjalankan perintah shell untuk menjalankan skrip PHP dari file
command = ['php', 'phpinfo.php']
result = subprocess.run(command, capture_output=True)

# Menghapus file sementara
subprocess.run(['rm', 'phpinfo.php'])

# Mengambil output dari hasil eksekusi skrip PHP
output = result.stdout.decode('utf-8')

# Menampilkan output
print(output)
