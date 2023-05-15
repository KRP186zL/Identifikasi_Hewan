from. import data,probabilitas
import time,os


chance = probabilitas.prob.copy()
programs = True
jumlah_pertanyaan = 0
nomor = -1
copy_pertanyaan = data.daftar_pertanyaan.copy()
copy_hewan  = data.daftar_hewan.copy()


def pertanyaan_yang_diberikan():
    banyak_pertanyaan = len(copy_pertanyaan)
    global jumlah_pertanyaan,nomor,programs
    jumlah_pertanyaan +=1
    if (jumlah_pertanyaan <= banyak_pertanyaan):
        nomor+=1
        if jumlah_pertanyaan == banyak_pertanyaan:
            programs = False
    return copy_pertanyaan[nomor] 


def hasil(final_result:str)->str:
    sistem_operasi = os.name
    match sistem_operasi:
        case"posix":
            os.system("clear")
        case"nt":
            os.system("cls")
    hewan = [x for x in data.daftar_hewan.keys()]
    print(f""" {'='*70}\n|{'menebak hewan yang ada dipikiran pengguna'.upper():^70}|\n|{'='*70}|
| {'|':>70}
| {'Coba pikirkan satu hewan diantara hewan berikut !':<69}{'|'}
| {'|':>70}
| - {hewan[0]:<15}- {hewan[1]:<15}- {hewan[2]}{'|':>28}
| - {hewan[5]:<15}- {hewan[4]:<15}- {hewan[3]}{'|':>27}
| - {hewan[6]:<15}- {hewan[7]:<15}- {hewan[8]}{'|':>28}
| - {hewan[11]:<15}- {hewan[15]:<15}- {hewan[9]}{'|':>28}
| - {hewan[12]:<15}- {hewan[13]:<15}- {hewan[14]}{'|':>28}
| - {hewan[17]:<15}- {hewan[16]:<15}- {hewan[15]}{'|':>29}
| - {hewan[18]:<15}- {hewan[19]:<15}- {hewan[20]}{'|':>29}
| - {hewan[23]:<15}- {hewan[22]:<15}- {hewan[21]}{'|':>27}
| - {hewan[24]:<15}- {hewan[25]:<15}- {hewan[26]}{'|':>28}
| {'|':>70}
| {'|':>70}
| {copy_pertanyaan[-1]:^69}{'|'} 
| {'|':>70}
| {'pertanyaan ke: '.title()}{jumlah_pertanyaan:<40}{'|':>15}
| {'|':>70}
| {'|':>70}
| {'1.Iya':>15}{'2.Tidak':>39}{'|':>16}\n| {'|':>70}\n| {'3.Mungkin':>19}{'4.Tidak Tahu':>40}{'|':>11}
| {'|':>70}
 {'='*70}""")
    print("")
    loading_animation(3)
    return f"Hewan yang anda pikirkan adalah {final_result}"


def loading_animation(duration:int)->str:
    """Untuk membuat Animasi Loading"""
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(4):
            print("Sedang menebak" + "." * i)
            time.sleep(0.5)
            print("\033[F\033[K", end="")  # Menghapus baris sebelumnya
        

        

def identifikasi_hewan(ciri_ciri:list)->str:
    """Mengidentifikasikan Hewan Berdasarkan Nilai 
    terbanyak yang didapatkan dari ciri-ciri"""

    #Nilai di dapatkan dari 100 dibagi banyaknya jumlah hewan yang memiliki ciri tersebut

    if "hidup di lautan" in ciri_ciri:
        chance["Penguin"]+=33
        chance["Ular"]+=33
        chance["Ikan"]+=33

    if "hidup di daratan" in ciri_ciri:
        chance["Gajah"]+=3
        chance["Kuda"]+=3
        chance["Kucing"]+=3
        chance["Kanguru"]+=3
        chance["Sapi"]+=3
        chance["Penguin"]+=3
        chance["Ular"]+=3
        chance["Buaya"]+=3
        chance["Monyet"]+=3
        chance["Komodo"]+=3
        chance["Banteng"]+=3
        chance["Kelinci"]+=3
        chance["Beruang"]+=3
        chance["Anjing"]+=3
        chance["Katak"]+=3
        chance["Kupu-kupu"]+=3
        chance["Laba-laba"]+=3
        chance["Babi"]+=3
        chance["Ayam"]+=3
        chance["Panda"]+=3
        chance["Jerapah"]+=3
        chance["Singa"]+=3
        chance["Harimau"]+=3
        chance["Cicak"]+=3
        chance["Kelelawar"]+=3
        chance["Burung"]+=3

    if "hewan buas" in ciri_ciri:
        chance["Ular"]+=12
        chance["Buaya"]+=12
        chance["Komodo"]+=12
        chance["Banteng"]+=12
        chance["Beruang"]+=12
        chance["Babi"]+=12
        chance["Singa"]+=12
        chance["Harimau"]+=12

    if "hewan nokturnal" in ciri_ciri:
        chance["Ular"]+=50
        chance["Kelelawar"]+=50

    if "hewan mamalia" in ciri_ciri:
        chance["Gajah"]+=6
        chance["Kuda"]+=6
        chance["Kucing"]+=6
        chance["Kanguru"]+=6
        chance["Sapi"]+=6
        chance["Monyet"]+=6
        chance["Banteng"]+=6
        chance["Kelinci"]+=6
        chance["Beruang"]+=6
        chance["Anjing"]+=6
        chance["Babi"]+=6
        chance["Panda"]+=6
        chance["Jerapah"]+=6
        chance["Singa"]+=6
        chance["Harimau"]+=6
        chance["Kelelawar"]+=6

    if "memiliki bulu" in ciri_ciri:
        chance["Gajah"]+=5
        chance["Kuda"]+=5
        chance["Kucing"]+=5
        chance["Kanguru"]+=5
        chance["Sapi"]+=5
        chance["Penguin"]+=5
        chance["Monyet"]+=5
        chance["Banteng"]+=5
        chance["Kelinci"]+=5
        chance["Beruang"]+=5
        chance["Anjing"]+=5
        chance["Laba-laba"]+=5
        chance["Babi"]+=5
        chance["Ayam"]+=5
        chance["Panda"]+=5
        chance["Jerapah"]+=5
        chance["Singa"]+=5
        chance["Harimau"]+=5
        chance["Kelelawar"]+=5
        chance["Burung"]+=5

    if "memiliki taring" in ciri_ciri:
        chance["Kucing"]+=10
        chance["Buaya"]+=10
        chance["Komodo"]+=10
        chance["Beruang"]+=10
        chance["Anjing"]+=10
        chance["Babi"]+=10
        chance["Panda"]+=10
        chance["Singa"]+=10
        chance["Harimau"]+=10
        chance["Kelelawar"]+=10
        
    if "hewan amfibi" in ciri_ciri:
        chance["Katak"]+=50
        chance["Cicak"]+=50

    if "berkaki empat" in ciri_ciri:
        chance["Gajah"]+=5
        chance["Kuda"]+=5
        chance["Kucing"]+=5
        chance["Sapi"]+=5
        chance["Buaya"]+=5
        chance["Monyet"]+=5
        chance["Komodo"]+=5
        chance["Banteng"]+=5
        chance["Kelinci"]+=5
        chance["Beruang"]+=5
        chance["Anjing"]+=5
        chance["Katak"]+=5
        chance["Babi"]+=5
        chance["Panda"]+=5
        chance["Jerapah"]+=5
        chance["Singa"]+=5
        chance["Harimau"]+=5
        chance["Cicak"]+=5
        
    if "cepat" in ciri_ciri:
        chance["Kuda"]+=8
        chance["Buaya"]+=8
        chance["Komodo"]+=8
        chance["Ikan"]+=8
        chance["Banteng"]+=8
        chance["Kelinci"]+=8
        chance["Beruang"]+=8
        chance["Anjing"]+=8
        chance["Babi"]+=8
        chance["Singa"]+=8
        chance["Harimau"]+=8
        chance["Burung"]+=8
        
    if "kecil" in ciri_ciri:
        chance["Kucing"]+=8
        chance["Penguin"]+=8
        chance["Monyet"]+=8
        chance["Ikan"]+=8
        chance["Kelinci"]+=8
        chance["Katak"]+=8
        chance["Kupu-kupu"]+=8
        chance["Laba-laba"]+=8
        chance["Ayam"]+=8
        chance["Cicak"]+=8
        chance["Kelelawar"]+=8
        chance["Burung"]+=8

    if "berbadan besar" in ciri_ciri:
        chance["Gajah"]+=5
        chance["Kuda"]+=5
        chance["Kanguru"]+=5
        chance["Sapi"]+=5
        chance["Ular"]+=5
        chance["Buaya"]+=5
        chance["Komodo"]+=5
        chance["Ikan"]+=5
        chance["Banteng"]+=5
        chance["Beruang"]+=5
        chance["Anjing"]+=5
        chance["Babi"]+=5
        chance["Panda"]+=5
        chance["Jerapah"]+=5
        chance["Singa"]+=5
        chance["Harimau"]+=5
        chance["Burung"]+=5
    
    if "berkaki dua" in ciri_ciri:
        chance["Kanguru"]+=20
        chance["Ayam"]+=20
        chance["Kelelawar"]+=20
        chance["Burung"]+=20
        chance["Penguin"]+=20
        
    if "hidup bersama manusia" in ciri_ciri:
        chance["Kucing"]+=50
        chance["Anjing"]+=50
    
    if "hewan peliharaan" in ciri_ciri:
        chance["Kuda"]+=10
        chance["Kucing"]+=10
        chance["Sapi"]+=10
        chance["Ikan"]+=10
        chance["Kelinci"]+=10
        chance["Monyet"]+=10
        chance["Anjing"]+=10
        chance["Babi"]+=10
        chance["Ayam"]+=10
        chance["Burung"]+=10
    
    if "memiliki belalai" in ciri_ciri:
        chance["Gajah"]+=100
        

    if "suka berada di dinding" in ciri_ciri:
        chance["Laba-laba"]+=50
        chance["Cicak"]+=50

    if "bertelur" in ciri_ciri:
        chance["Penguin"]+=9
        chance["Ular"]+=9
        chance["Buaya"]+=9
        chance["Komodo"]+=9
        chance["Ikan"]+=9
        chance["Katak"]+=9
        chance["Kupu-kupu"]+=9
        chance["Laba-laba"]+=9
        chance["Ayam"]+=9
        chance["Cicak"]+=9
        chance["Burung"]+=9
        
    if "melahirkan" in ciri_ciri:
        chance["Gajah"]+=6
        chance["Kuda"]+=6
        chance["Kucing"]+=6
        chance["Kanguru"]+=6
        chance["Sapi"]+=6
        chance["Monyet"]+=6
        chance["Banteng"]+=6
        chance["Kelinci"]+=6
        chance["Beruang"]+=6
        chance["Anjing"]+=6
        chance["Babi"]+=6
        chance["Panda"]+=6
        chance["Jerapah"]+=6
        chance["Singa"]+=6
        chance["Harimau"]+=6
        chance["Kelelawar"]+=6
        
    if "hewan karnivora" in ciri_ciri:
        chance["Kucing"]+=10
        chance["Penguin"]+=10
        chance["Ular"]+=10
        chance["Buaya"]+=10
        chance["Komodo"]+=10
        chance["Ikan"]+=10
        chance["Laba-laba"]+=10
        chance["Singa"]+=10
        chance["Harimau"]+=10
        chance["Katak"]+=10
    
    if "hewan herbivora" in ciri_ciri:
        chance["Gajah"]+=11
        chance["Kuda"]+=11
        chance["Kanguru"]+=11
        chance["Sapi"]+=11
        chance["Banteng"]+=11
        chance["Kelinci"]+=11
        chance["Kupu-kupu"]+=11
        chance["Panda"]+=11
        chance["Jerapah"]+=11
        
    if "hewan omnivora" in ciri_ciri:
        chance["Monyet"]+=14
        chance["Beruang"]+=14
        chance["Anjing"]+=14
        chance["Ayam"]+=14
        chance["Babi"]+=14
        chance["Kelelawar"]+=14
        chance["Burung"]+=14
    
    if "mudah dilatih" in ciri_ciri:
        chance["Gajah"]+=16
        chance["Kuda"]+=16
        chance["Kucing"]+=16
        chance["Monyet"]+=16
        chance["Anjing"]+=16
        chance["Burung"]+=16
    
    if "hewan predator" in ciri_ciri:
        chance["Kucing"]+=6
        chance["Penguin"]+=6
        chance["Ular"]+=6
        chance["Buaya"]+=6
        chance["Komodo"]+=6
        chance["Ikan"]+=6
        chance["Beruang"]+=6
        chance["Anjing"]+=6
        chance["Katak"]+=6
        chance["Laba-laba"]+=6
        chance["Harimau"]+=6
        chance["Singa"]+=6
        chance["Cicak"]+=6
        chance["Kelelawar"]+=6
        chance["Burung"]+=6
    
    if "memiliki leher yang panjang" in ciri_ciri:
        chance["Jerapah"]+=100
    
    if "hidup di hutan" in ciri_ciri:
        chance["Gajah"]+=6
        chance["Kucing"]+=6
        chance["Kanguru"]+=6
        chance["Ular"]+=6
        chance["Monyet"]+=6
        chance["Komodo"]+=6
        chance["Banteng"]+=6
        chance["Kelinci"]+=6
        chance["Kupu-kupu"]+=6
        chance["Laba-laba"]+=6
        chance["Babi"]+=6
        chance["Ayam"]+=6
        chance["Panda"]+=6
        chance["Burung"]+=6
        chance["Harimau"]+=6
        chance["Kelelawar"]+=6
        chance["Beruang"]+=6


    if "hidup di savana" in ciri_ciri:
        chance["Gajah"]+=9
        chance["Kuda"]+=9
        chance["Kanguru"]+=9
        chance["Ular"]+=9
        chance["Komodo"]+=9
        chance["Banteng"]+=9
        chance["Laba-laba"]+=9
        chance["Babi"]+=9
        chance["Jerapah"]+=9
        chance["Singa"]+=9
        chance["Burung"]+=9


    if "hewan yang terancam punah" in ciri_ciri:
        chance["Gajah"]+=33
        chance["Jerapah"]+=33
        chance["Harimau"]+=33

    if "memiliki gading" in ciri_ciri:
        chance["Gajah"]+=100
        
    if "memiliki ekor" in ciri_ciri:
        chance["Gajah"]+=4
        chance["Kuda"]+=4
        chance["Kucing"]+=4
        chance["Kanguru"]+=4
        chance["Sapi"]+=4
        chance["Penguin"]+=4
        chance["Ular"]+=4
        chance["Buaya"]+=4
        chance["Monyet"]+=4
        chance["Komodo"]+=4
        chance["Ikan"]+=4
        chance["Banteng"]+=4
        chance["Kelinci"]+=4
        chance["Beruang"]+=4
        chance["Anjing"]+=4
        chance["Babi"]+=4
        chance["Ayam"]+=4
        chance["Panda"]+=4
        chance["Jerapah"]+=4
        chance["Singa"]+=4
        chance["Harimau"]+=4
        chance["Cicak"]+=4
        chance["Kelelawar"]+=4
        chance["Burung"]+=4
    
    if "bertubuh panjang" in ciri_ciri:
        chance["Gajah"]+=11
        chance["Kuda"]+=11
        chance["Ular"]+=11
        chance["Buaya"]+=11
        chance["Komodo"]+=11
        chance["Ikan"]+=11
        chance["Banteng"]+=11
        chance["Singa"]+=11
        chance["Harimau"]+=11
    
    if "memiliki sisik" in ciri_ciri:
        chance["Ular"]+=50
        chance["Ikan"]+=50
    
    if "tidak mempunyai kaki" in ciri_ciri:
        chance["Ular"]+=50
        chance["Ikan"]+=50
    
    if "bisa di tunggangi" in ciri_ciri:
        chance["Gajah"]+=33
        chance["Kuda"]+=33
        chance["Sapi"]+=33
    
    if "bisa terbang" in ciri_ciri:
        chance["Kupu-kupu"]+=33
        chance["Kelelawar"]+=33
        chance["Burung"]+=33
        
    if "memiliki sayap" in ciri_ciri:
        chance["Penguin"]+=20
        chance["Kupu-kupu"]+=20
        chance["Ayam"]+=20
        chance["Kelelawar"]+=20
        chance["Burung"]+=20
    
    if "memiliki kulit yang keras dan bersisik" in ciri_ciri:
        chance["Buaya"]+=50
        chance["Komodo"]+=50
    
    if "memiliki bulu lebat di sekitar kepala" in ciri_ciri:
        chance["Singa"]+=100
    
    if "memiliki bisa/racun" in ciri_ciri:
        chance["Ular"]+=25
        chance["Komodo"]+=25
        chance["Katak"]+=25
        chance["Laba-laba"]+=25

    if "memiliki paruh" in ciri_ciri:
        chance["Burung"]+=33
        chance["Ayam"]+=33
        chance["Penguin"]+=33   
    
    if "memiliki kantung" in ciri_ciri:
        chance["Kanguru"]+=100   
    
    if "memiliki delapan kaki" in ciri_ciri:
        chance["Laba-laba"]+=100   
        
    if "memiliki tanduk" in ciri_ciri:
        chance["Sapi"]+=25   
        chance["Banteng"]+=25   
        chance["Babi"]+=25 
        chance["Jerapah"]+=25   
    
    if "hidup di perairan dingin" in ciri_ciri:
        chance["Penguin"]+=100   
    
    if "hidup berkelompok" in ciri_ciri:
        chance["Gajah"]+=8 
        chance["Kuda"]+=8   
        chance["Sapi"]+=8   
        chance["Penguin"]+=8   
        chance["Buaya"]+=8   
        chance["Ikan"]+=8   
        chance["Banteng"]+=8   
        chance["Jerapah"]+=8   
        chance["Singa"]+=8   
        chance["Kelelawar"]+=8   
        chance["Burung"]+=8   
        chance["Monyet"]+=8   
    
    if "hidup di dua alam" in ciri_ciri:
        chance["Penguin"]+=25   
        chance["Ular"]+=25   
        chance["Buaya"]+=25  
        chance["Katak"]+=25   
    
    if "memiliki tangan" in ciri_ciri:
        chance["Kanguru"]+=33   
        chance["Monyet"]+=33   
        chance["Panda"]+=33   
    
    if "termasuk primata" in ciri_ciri:
        chance["Monyet"]+=100   
        
    if "bisa diminum susunya" in ciri_ciri:
        chance["Sapi"]+=100   
        
    if "memiliki enam kaki" in ciri_ciri:
        chance["Kupu-kupu"]+=100   
    
    if "menyukai bunga" in ciri_ciri:
        chance["Kupu-kupu"]+=100   
     
    if "memiliki gigi panjang" in ciri_ciri:
        chance["Kelinci"]+=100

    if "suka wortel" in ciri_ciri:
        chance["Kelinci"]+=100

    if "suka bambu" in ciri_ciri:
        chance["Panda"]+=100

    if "berasal dari negara china" in ciri_ciri:
        chance["Panda"]+=100

    if "di sekitar matanya berwarna hitam" in ciri_ciri:
        chance["Panda"]+=100

    if "memiliki jaring" in ciri_ciri:
        chance["Laba-laba"]+=100

    if "suka madu" in ciri_ciri:
        chance["Beruang"]+=100

    if "memiliki jengger di kepala" in ciri_ciri:
        chance["Ayam"]+=100

    if "memiliki tulang tajam di kakinya" in ciri_ciri:
        chance["Ayam"]+=100

    chance_terbesar = max(chance.values())
    result = [key for key, value in chance.items() if value == chance_terbesar]
    final_result = "".join(result)
    return hasil(final_result)
    
    