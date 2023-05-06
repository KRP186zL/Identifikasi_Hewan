from. import data,probabilitas


chance = probabilitas.prob
programs = True
jumlah_pertanyaan = 0
nomor = -1
copy_pertanyaan = data.daftar_pertanyaan.copy()
copy_hewan  = data.daftar_hewan.copy()


def pertanyaan_yang_diberikan():
    global jumlah_pertanyaan,nomor,programs
    jumlah_pertanyaan +=1
    if jumlah_pertanyaan <=51: #sebanyak jumlah pertanyaan
        nomor+=1
    else:
        programs = False
    return copy_pertanyaan[nomor] 


def menghitung_probabilitas():
    pass


def identifikasi_hewan(ciri_ciri):
    print (ciri_ciri)
    if "hidup di lautan" in ciri_ciri:
        chance["Penguin"]
        chance["Ular"]
        chance["Ikan"]

    if "hidup di daratan" in ciri_ciri:
        chance["Gajah"]
        chance["Kuda"]
        chance["Kucing"]
        chance["Kanguru"]
        chance["Sapi"]
        chance["Penguin"]
        chance["Ular"]
        chance["Buaya"]
        chance["Monyet"]
        chance["Komodo"]
        chance["Banteng"]
        chance["Kelinci"]
        chance["Beruang"]

    if "hewan buas" in ciri_ciri:
        chance["Ular"]
        chance["Buaya"]
        chance["Komodo"]
        chance["Banteng"]
        chance["Beruang"]

    if "hewan nokturnal" in ciri_ciri:
        pass
    if "hewan mamalia" in ciri_ciri:
        pass
    if "memiliki bulu" in ciri_ciri:
        pass
    if "memiliki taring" in ciri_ciri:
        pass
    if "hewan amfibi" in ciri_ciri:
        pass
    if "berkaki empat" in ciri_ciri:
        pass
    if "cepat" in ciri_ciri:
        pass
    if "kecil" in ciri_ciri:
        pass
    if "berbadan besar" in ciri_ciri:
        pass
    if "berkaki dua" in ciri_ciri:
        pass
    if "hidup bersama manusia" in ciri_ciri:
        pass
    if "hewan peliharaan" in ciri_ciri:
        pass
    if "memiliki belalai" in ciri_ciri:
        pass
    if "suka berada di dinding" in ciri_ciri:
        pass
    if "bertelur" in ciri_ciri:
        pass
    if "melahirkan" in ciri_ciri:
        pass
    if "hewan karnivora" in ciri_ciri:
        pass
    if "hewan herbivora" in ciri_ciri:
        pass
    if "hewan omnivora" in ciri_ciri:
        pass
    if "mudah dilatih" in ciri_ciri:
        pass
    if "hewan predator" in ciri_ciri:
        pass
    if "memiliki leher yang panjang" in ciri_ciri:
        pass
    if "hidup di hutan" in ciri_ciri:
        pass
    if "hidup di savana" in ciri_ciri:
        pass
    if "hewan yang terancam punah" in ciri_ciri:
        pass
    if "memiliki gading" in ciri_ciri:
        pass
    if "memiliki ekor" in ciri_ciri:
        pass
    if "bertubuh panjang" in ciri_ciri:
        pass
    if "memiliki sisik" in ciri_ciri:
        pass
    if "tidak mempunyai kaki" in ciri_ciri:
        pass
    if "bisa di tunggangi" in ciri_ciri:
        pass
    if "bisa terbang" in ciri_ciri:
        pass
    if "memiliki sayap" in ciri_ciri:
        pass
    if "memiliki kulit yang keras dan bersisik" in ciri_ciri:
        pass
    if "memiliki bulu lebat di sekitar kepala" in ciri_ciri:
        pass
    if "memiliki bisa/racun" in ciri_ciri:
        pass
    if "memiliki paruh" in ciri_ciri:
        pass
    if "memiliki kantung" in ciri_ciri:
        pass
    if "memiliki delapan kaki" in ciri_ciri:
        pass
    if "memiliki tanduk" in ciri_ciri:
        pass
    if "hidup di perairan dingin" in ciri_ciri:
        pass
    if "hidup berkelompok" in ciri_ciri:
        pass
    if "hidup di dua alam" in ciri_ciri:
        pass
    if "memiliki tangan" in ciri_ciri:
        pass
    if "termasuk primata" in ciri_ciri:
        pass
    if "bisa diminum susunya" in ciri_ciri:
        pass
    if "memiliki enam kaki" in ciri_ciri:
        pass
    if "cantik" in ciri_ciri:
        pass
    if "menyukai bunga" in ciri_ciri:
        pass
    if "memiliki gigi panjang" in ciri_ciri:
        pass
        chance["Gajah"]+=20
        chance["Kuda"]+=10
        chance["Kucing"]+=100
        # return chance
    chance_terbesar = max(chance.values())
    result = [key for key, value in chance.items() if value == chance_terbesar]
    return "".join(result)
    