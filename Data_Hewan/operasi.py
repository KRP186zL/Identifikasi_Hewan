from. import data,probabilitas

chance = probabilitas.prob
programs = True
jumlah_pertanyaan = 0
nomor = 0
copy_pertanyaan = data.daftar_pertanyaan.copy()
copy_hewan  = data.daftar_hewan.copy()

def pertanyaan_yang_diberikan():
    global jumlah_pertanyaan,nomor,programs
    jumlah_pertanyaan +=1
    if jumlah_pertanyaan <=48: #sebanyak jumlah pertanyaan
        nomor+=1
    else:
        programs = False
    return copy_pertanyaan[nomor] 
        

def identifikasi_hewan(ciri_ciri):
    print (ciri_ciri)
    if "hidup di daratan" and "hewan mamalia" and "berkaki empat" in ciri_ciri:
        chance["Gajah"]+=20
        chance["Kuda"]+=10
        chance["Kucing"]+=100
        # return chance
    chance_terbesar = max(chance.values())
    result = [key for key, value in chance.items() if value == chance_terbesar]
    return result
    input()

    # print(ciri_ciri)
    # input()
    # for hewan, ciri in copy_hewan.items():
    #     if all(x in ciri for x in ciri_ciri):
    #         return f"Hewan yang anda pikirkan adalah {hewan}"
    # return "Maaf hewan yang ada dipikiran anda sungguh diluar nalar !\nCoba pikirkan yang benar-benar saja mazsehh"
