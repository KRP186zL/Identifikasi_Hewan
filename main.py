import Data_Hewan as dh


validasi = []
if __name__ == "__main__":
    while dh.operasi.programs == True:
        import os
        sistem_operasi = os.name
        match sistem_operasi:
            case"posix":
                os.system("clear")
            case"nt":
                os.system("cls")
        pertanyaan = dh.operasi.pertanyaan_yang_diberikan()
        hewan = [x for x in dh.data.daftar_hewan.keys()]
        print(f""" {'='*70}\n|{'menebak hewan yang ada dipikiran pengguna'.upper():^70}|\n|{'='*70}|
| {'|':>70}
| {'Coba pikirkan satu hewan diantara hewan berikut !':<69}{'|'}
| {'|':>70}
| - {hewan[0]:<15}- {hewan[1]:<15}- {hewan[2]}{'|':>28}
| - {hewan[5]:<15}- {hewan[4]:<15}- {hewan[3]}{'|':>27}
| - {hewan[6]:<15}- {hewan[7]:<15}- {hewan[8]}{'|':>28}
| - {hewan[11]:<15}- {hewan[15]:<15}- {hewan[9]}{'|':>28}
| - {hewan[12]:<15}- {hewan[13]:<15}- {hewan[14]}{'|':>29}
| - {hewan[17]:<15}- {hewan[16]:<15}- {hewan[15]}{'|':>25}
| - {hewan[18]:<15}- {hewan[19]:<15}- {hewan[20]}{'|':>27}
| - {hewan[23]:<15}- {hewan[22]:<15}- {hewan[21]}{'|':>29}
| - {hewan[24]:<15}- {hewan[25]:<15}- {hewan[26]}{'|':>28}
| - {hewan[27]:<15}- {hewan[27]:<15}- {hewan[27]}{'|':>25}
| {'|':>70}
| {'|':>70}
| {pertanyaan:^69}{'|'} 
| {'|':>70}
| {'pertanyaan ke: '.title()}{dh.operasi.jumlah_pertanyaan:<40}{'|':>15}
| {'|':>70}
| {'|':>70}
| {'1.Iya':>15}{'2.Tidak':>39}{'|':>16}\n| {'|':>70}\n| {'3.Mungkin':>19}{'4.Tidak Tahu':>40}{'|':>11}
| {'|':>70}
 {'='*70}""")

        pilih = input("\nPilih[1/2/3/4]: ")
        match pilih:
            case"1":
                ganti = pertanyaan.replace(" ?","")
                validasi.append(ganti[11:])
        # if len(validasi) == 47: #ganti jika 7 data yang ada didalam validasi cocok dengan data hewan yang anda, kemduian tampilkan hewan nya
        #     break

        
hasil = dh.operasi.identifikasi_hewan(validasi)
print(hasil)


