import Data_Hewan as dh
program = True
validasi = []
if __name__ == "__main__":
    while program:
        pertanyaan = dh.operasi.pertanyaan_yang_diberikan()
        import os
        sistem_operasi = os.name
        match sistem_operasi:
            case"posix":
                os.system("clear")
            case"nt":
                os.system("cls")
        print(f""" {'='*50}\n|{'menebak hewan yang ada dipikiran pengguna'.upper():^50}|\n|{'='*50}|
| {'Coba pikirkan satu hewan !':^49}{'|'}
| {'|':>50}
| {'pertanyaan ke: '.title()}{dh.operasi.jumlah_pertanyaan:<20}{'|':>15}
| {'|':>50}
| {'|':>50}
| {pertanyaan:45}{'|':>5} 
| {'|':>50}
| {'1.Iya':<15}2.Tidak{'|':>28}\n| {'|':>50}\n| {'3.Mungkin':<15}4.Tidak Tahu{'|':>23}
| {'|':>50}
 {'='*50}""")

        pilih = input("\nPilih[1/2/3/4]: ")
        match pilih:
            case"1":
                ganti = pertanyaan.replace(" ?","")
                validasi.append(ganti[11:])
        if len(validasi) == 7: #ganti jika 7 data yang ada didalam validasi cocok dengan data hewan yang anda, kemduian tampilkan hewan nya
            break

        
hasil = dh.operasi.identifikasi_hewan(validasi)
print(hasil)


