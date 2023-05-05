import random
daftar_hewan = {
    "Gajah": ["memiliki belalai", "berkaki empat","berbadan besar","hewan mamalia","melahirkan","hewan yang terancam punah","memiliki gading","hewan herbivora","hidup di daratan"],
    "Kuda": ["berkaki empat", "berbulu", "cepat","melahirkan","mamalia",""],
    "Kucing": ["kecil", "berbulu", "pintar","melahirkan","berkaki empat","hewan peliharaan","hewan karnivora","hidup di daratan","hidup bersama manusia","memiliki ekor"],
    "Kanguru": ["memiliki kantong", "berkaki dua", "tinggi"],
    "Sapi": ["berkaki empat", "berbulu", "besar","memiliki ekor"],
    "Penguin":["memiliki tubuh dengan dua warna", "mempunyai dua kaki", "hidup di dua alam", "berbulu", "hewan mamalia"],
    "Ular":["bertubuh panjang", "memiliki sisik", "tidak mempunyai kaki", "hidup di daratan", "hewan karnivora"],
    "Buaya":["memiliki moncong yang panjang", "berbadan panjang dilapisi sisik tanduk", "memiliki empat kaki", "hidup di dua alam", "hewan karnivora"],
    "Monyet":["mempunyai ekor", "hidup dihutan", "berbulu", "memiliki dua kaki dan dua tangan", "hewan omnivora"],
    "Komodo":["mempunyai ekor", "warna kulit kuning kehitaman", "berkaki empat", "memiliki sisik", "hewan karnivora"],
    "Rusa":["ekor pendek", "telinga yang panjang", "mempunyai tanduk", "mempunyai 4 kaki", "hewan herbivora"],
    "Banteng":["mempunyai tanduk panjang melengkung ke atas", "berkaki empat", "berbulu", "besar", "hewan herbivora"],
    "Kelinci":["cara jalan yang unik dengan melompat", "berkaki empat" ,"kecil" ,"berbulu" ,"hewan mamalia"],
    "Beruang":["besar", "mempunyai cakar tajam", "berbulu", "berkaki empat", "hewan karnivora"],
    "Anjing":["memiliki ekor", "kecil", "berkaki empat", "berbulu", "hewan peliharaan", "hewan omnivora","hidup bersama manusia","pintar","hidup di daratan","melahirkan"],
    "Katak":["bertubuh langsing", "tekstur kulit halus, basah dan tipis", "berkaki empat", "hidup di dua alam", "karnivora"],
    "Kupu-kupu":["berkaki enam", "mempunyai sayap dan antena dikepala", "mempunyai belalai seperti sedotan", "hewan herbivora"],
    "Laba-laba":["memiliki empat mata", "berkaki delapan", "tidak bersayap", "berbisa", "hewan karnivora"],
    "Babi":["berkaki empat", "tubuh panjang", "memiliki hidung besar", "mengandung cacing pita", "hewan omnivora"],
    "Ayam":["berkaki dua", "mempunyai dua sayap", "berbulu", "memiliki jengger dikepala", "hewan omnivora"],
    "Orang hutan":["berbadan besar","berbulu","mamalia","hidup dihutan"],
    "Jerapah":["memiliki kepala yang panjang","hidup di savana"],
    "Singa":["hewan buas","memiliki taring","berkaki empat","hidup disavana"]
}


# print(len(daftar_hewan.keys()))

data = [["memiliki belalai","berbulu,","berbadan besar"]]
for hewan,ciri in daftar_hewan.items():
    print(ciri)
        # if i >=2:
        #     print(hewan)

# for i in daftar_hewan.values():
#     print(i)

#buat pertanyaan terpisah antara masing2 hewan supaya lebih akurat dan fleksibel
daftar_pertanyaan= [
    "Apakah dia hidup di lautan ?","Apakah dia hidup di daratan ?","Apakah dia hewan buas ?","Apakah dia aktif dimalam hari ?",
    "Apakah dia hewan mamalia ?", "Apakah dia berbulu ?", "Apakah dia memiliki taring ?","Apakah dia hidup di air dan daratan ?",
    "Apakah dia berkaki empat ?","Apakah dia cepat ?", "Apakah dia kecil ?","Apakah dia berbadan besar ?","Apakah dia berkaki dua ?","Apakah dia hidup bersama manusia ?",
    "Apakah dia hewan peliharaan ?","Apakah dia tinggi ?", "Apakah dia memiliki belalai ?","Apakah dia suka berada di dinding ?","Apakah dia bertelur ?","Apakah dia melahirkan ?",
    "Apakah dia hewan karnivora ?","Apakah dia hewan omnivora ?","Apakah dia hewan herbivora ?","Apakah dia pintar ?","Apakah dia hewan predator ?","Apakah dia memiliki kepala yang panjang ?",
    "Apakah dia hidup di hutan ?","Apakah dia hidup di savana ?","Apakah dia hewan yang terancam punah ?","Apakah dia memiliki gading ?","Apakah dia memiliki ekor ?","Apakah dia bertubuh panjang ?",
    "Apakah dia memiliki sisik ?","Apakah dia tidak mempunyai kaki ?"
]

random.shuffle(daftar_pertanyaan)