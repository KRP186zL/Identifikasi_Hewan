from. import data

jumlah_pertanyaan = 0
nomor = 0
copy_pertanyaan = data.daftar_pertanyaan.copy()
copy_hewan  = data.daftar_hewan.copy()

def pertanyaan_yang_diberikan():
    global jumlah_pertanyaan,nomor
    jumlah_pertanyaan +=1
    if jumlah_pertanyaan <=100: #sebanyak jumlah pertanyaan
        nomor+=1
        return copy_pertanyaan[nomor]  

def identifikasi_hewan(ciri_ciri):
    print(ciri_ciri)
    input()
    for hewan, ciri in copy_hewan.items():
        if all(x in ciri for x in ciri_ciri):
            return f"Hewan yang anda pikirkan adalah {hewan}"
    return "Maaf hewan yang ada dipikiran anda sungguh diluar nalar !\nCoba pikirkan yang benar-benar saja mazsehh"
