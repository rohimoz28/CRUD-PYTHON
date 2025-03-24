# Python Dasar (CRUD) Dengan Command Line

## Rangkuman
Project ini dibuat untuk sarana pembelajaran bahasa pemrograman python. Aplikasi ini adalah CRUD yang sudah terhubung ke database Postgresql menggunakan docker compose. <br>
Untuk menjalankan project ini, penulis berasumsi bahwa docker sudah di install pada sistem operasi kalian.

## Docker Compose
Jalankan docker compose menggunakan perintah `docker compose up -d`.

**NB:** Perhatikan konfigurasi port dan environment variable yang ada di dalam docker-compose.yaml.

## Install Python Dependency
Disini saya menggunakan python virtual environment untuk install python dependency.
- `sudo apt install python3 python3-pip -y`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install psycopg2-binary`

## Jalankan Aplikasi
Jika tidak ada masalah ketika membuat container postgresql dan install python dependency, sekarang mari kita testing aplikasi-nya.

Buka command line/ terminal dan jalankan perintah `python3 main.py`

maka akan muncul tampilan seperti berikut,

![Python CRUD dengan Terminal](/crud-python-terminal.jpg)

Sekian. Terimakasih!