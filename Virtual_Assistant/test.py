# dictionary yang berisi daftar hewan beserta ciri-cirinya

daftar_hewan = {
    "gajah": ["belalai panjang", "berbulu", "berkaki empat"],
    "kuda": ["berkaki empat", "berbulu", "cepat"],
    "kucing": ["kecil", "berbulu", "pintar"],
    "kanguru": ["memiliki kantong", "berkaki dua", "tinggi"],
    "sapi": ["berkaki empat", "berbulu", "besar"]
}

# fungsi untuk mencocokkan ciri-ciri hewan dengan daftar hewan
def tebak_hewan(ciri_ciri):
    for hewan, ciri in daftar_hewan.items():
        if all(x in ciri for x in ciri_ciri):
            return hewan
    return "tidak ditemukan"

# main program
ciri_ciri = input("Masukkan ciri-ciri hewan (pisahkan dengan koma): ").split(",")
nama_hewan = tebak_hewan(ciri_ciri)

print("Hewan yang cocok dengan ciri-ciri tersebut adalah:", nama_hewan)
