def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read()
            print("Isi dari file", nama_file, ":")
            print(isi)
    except FileNotFoundError:
        print("File not found")

def tulis_file(nama_file, teks):
    with open(nama_file, 'w') as f:
        f.write(teks)
    print("File", nama_file, "telah berhasil ditulis.")

if __name__ == "__main__":
    # Nama file yang akan dibaca dan ditulis
    nama_file = "pesan.txt"

    # Isi teks yang akan ditulis ke dalam file
    isi_teks = """Starts to make its way to me
The playful conversation starts
Counter all your quick remarks
Like passing notes in secrecy
And it was enchanting to meet you
I was enchanted to meet you"""

    # Tulis teks ke dalam file
    tulis_file(nama_file, isi_teks)

    # Baca teks dari file
    baca_file(nama_file)
