import psycopg2

def get_connection():
    """Membuat koneksi ke database PostgreSQL."""
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="mydb",
        user="odoo",
        password="adminodoodev"
    )

# Fungsi untuk menguji koneksi
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Koneksi ke database berhasil!")
        conn.close()
    except Exception as e:
        print(f"Error koneksi: {e}")