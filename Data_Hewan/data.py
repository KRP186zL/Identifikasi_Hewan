import random

daftar_pertanyaan= [
    "Apakah dia hidup di lautan ?","Apakah dia hidup di daratan ?","Apakah dia hewan buas ?","Apakah dia hewan nokturnal ?",
    "Apakah dia hewan mamalia ?", "Apakah dia memiliki bulu ?", "Apakah dia memiliki taring ?","Apakah dia hewan amfibi ?",
    "Apakah dia berkaki empat ?","Apakah dia cepat ?", "Apakah dia kecil ?","Apakah dia berbadan besar ?","Apakah dia berkaki dua ?",
    "Apakah dia hidup bersama manusia ?","Apakah dia hewan peliharaan ?", "Apakah dia memiliki belalai ?",
    "Apakah dia suka berada di dinding ?","Apakah dia bertelur ?","Apakah dia melahirkan ?","Apakah dia hewan karnivora ?",
    "Apakah dia hewan omnivora ?","Apakah dia hewan herbivora ?","Apakah dia mudah dilatih ?","Apakah dia hewan predator ?",
    "Apakah dia memiliki leher yang panjang ?","Apakah dia hidup di hutan ?","Apakah dia hidup di savana ?",
    "Apakah dia hewan yang terancam punah ?","Apakah dia memiliki gading ?","Apakah dia memiliki ekor ?",
    "Apakah dia bertubuh panjang ?", "Apakah dia memiliki sisik ?","Apakah dia tidak mempunyai kaki ?",
    "Apakah dia bisa di tunggangi ?","Apakah dia bisa terbang ?","Apakah dia memiliki sayap ?","Apakah dia memiliki kulit yang keras dan bersisik ?",
    "Apakah dia memiliki bulu lebat di sekitar kepala ?","Apakah dia memiliki bisa/racun","Apakah dia memiliki paruh ?",
    "Apakah dia memiliki kantung ?","Apakah dia memiliki delapan kaki ?","Apakah dia memiliki tanduk ?","Apakah dia hidup di perairan dingin ?",
    "Apakah dia hidup berkelompok ?","Apakah dia hidup di dua alam ?","Apakah dia memiliki tangan ?","Apakah dia termasuk primata ?",
    "Apakah dia bisa diminum susunya ?","Apakah dia memiliki enam kaki ?","Apakah dia menyukai bunga ?","Apakah dia memiliki gigi panjang ?",
    "Apakah dia suka wortel ?","Apakah dia suka bambu ?","Apakah dia berasal dari negara china ?","Apakah dia di sekitar matanya berwarna hitam ?",
    "Apakah dia memiliki jaring ?","Apakah dia suka madu ?","Apakah dia memiliki jengger di kepala ?","Apakah dia memiliki tulang tajam di kakinya ?"
]


random.shuffle(daftar_pertanyaan)


daftar_hewan = {
    "Gajah": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","berbadan besar","memiliki belalai","melahirkan","hewan herbivora","mudah dilatih","hidup di hutan",
        "hidup di savana","hewan yang terancam punah","memiliki gading","memiliki ekor","bertubuh panjang","bisa di tunggangi","hidup berkelompok"
    ],

    "Kuda": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","cepat","berbadan besar","hewan peliharaan","melahirkan","hewan herbivora","mudah dilatih",
        "hidup di savana","memiliki ekor","bertubuh panjang","bisa di tunggangi","hidup berkelompok"
    ],
             
    "Kucing": [
        "hidup di daratan","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","kecil","hidup bersama manusia","hewan peliharaan","melahirkan","hewan karnivora",
        "mudah dilatih","hewan predator","hidup di hutan","memiliki ekor"
    ],

    "Kanguru": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berbadan besar","berkaki dua","melahirkan","hewan herbivora","hidup di hutan","hidup di savana","memiliki ekor",
        "memiliki kantung","memiliki tangan"
    ],

    "Sapi": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","berbadan besar","hewan peliharaan","melahirkan","hewan herbivora","memiliki ekor","bisa di tunggangi",
        "memiliki tanduk","hidup berkelompok","bisa diminum susunya"
    ],

    "Penguin":[
        "hidup di daratan","memiliki bulu","kecil","berkaki dua","bertelur","hewan karnivora","hewan predator","memiliki ekor","memiliki sayap","memiliki paruh",
        "hidup di perairan dingin","hidup berkelompok","hidup di dua alam"
    ],

    "Ular":[
        "hidup di daratan","hewan buas","hewan nokturnal","berbadan besar","bertelur","hewan karnivora","hewan predator","hidup di hutan","hidup di savana","memiliki ekor",
        "bertubuh panjang","memiliki sisik","tidak mempunyai kaki","memiliki bisa/racun","hidup di dua alam"
    ],

    "Buaya":[
        "hidup di daratan","hewan buas","memiliki taring","berkaki empat","cepat","berbadan besar","bertelur","hewan karnivora","hewan predator","memiliki ekor",
        "bertubuh panjang","memiliki kulit yang keras dan bersisik","hidup berkelompok","hidup di dua alam"
    ],

    "Monyet":[
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","kecil","hewan peliharaan","melahirkan","mudah dilatih","hidup di hutan","memiliki ekor",
        "hidup berkelompok","memiliki tangan","termasuk primata"
    ],

    "Komodo":[
        "hidup di daratan","hewan buas","memiliki taring","berkaki empat","cepat","berbadan besar","bertelur","hewan karnivora","hewan predator","hidup di hutan",
        "hidup di savana","memiliki ekor","bertubuh panjang","memiliki kulit yang keras dan bersisik","memiliki bisa/racun"
    ],
    "Ikan":[
        "cepat","kecil","berbadan besar","hewan peliharaan","bertelur","hewan karnivora","hewan predator","memiliki ekor","bertubuh panjang","memiliki sisik",
        "tidak mempunyai kaki","hidup berkelompok"
    ],

    "Banteng":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","berkaki empat","cepat","berbadan besar","melahirkan","hewan herbivora","hidup di hutan",
        "hidup di savana","memiliki ekor","bertubuh panjang","memiliki tanduk","hidup berkelompok"
    ],
    "Kelinci":[
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","cepat","kecil","hewan peliharaan","melahirkan","hewan herbivora","hidup di hutan","memiliki ekor",
        "memiliki gigi panjang","suka wortel"
    ],
    "Beruang":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat","berbadan besar","melahirkan","hewan predator",
        "hidup di hutan","memiliki ekor","suka madu"
    ],
    "Anjing":[
        "hidup di daratan","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat","berbadan besar","hidup bersama manusia","hewan peliharaan","melahirkan",
        "mudah dilatih","hewan predator","memiliki ekor"
    ],
    "Katak":[
        "hidup di daratan","hewan amfibi","berkaki empat","cepat","kecil","bertelur","hewan karnivora","hewan predator","memiliki bisa/racun","hidup di dua alam"
    ],
    "Kupu-kupu":[
        "hidup di daratan","kecil","bertelur","hewan herbivora","hidup di hutan","bisa terbang","memiliki sayap","memiliki enam kaki","menyukai bunga"
    ],
    "Laba-laba":[
        "hidup di daratan","memiliki bulu","kecil","suka berada di dinding","bertelur","hewan karnivora","hewan predator","hidup di hutan","hidup di savana","memiliki bisa/racun",
        "memiliki delapan kaki","memiliki jaring"
    ],
    "Babi":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat","berbadan besar","hewan peliharaan","melahirkan",
        "hidup di hutan","hidup di savana","memiliki ekor","memiliki tanduk"
    ],
    "Ayam":[
        "hidup di daratan","memiliki bulu","kecil","berkaki dua","hewan peliharaan","bertelur","hidup di hutan","memiliki ekor","memiliki sayap","memiliki paruh",
        "memiliki jengger di kepala","memiliki tulang tajam  di kakinya"
    ],
    "Panda":[
        "hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","berbadan besar","melahirkan","hewan herbivora","hidup di hutan","memiliki ekor","memiliki tangan",
        "suka bambu","berasal dari negara china","di sekitar matanya berwarna hitam"
    ],
    "Jerapah":[
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","berbadan besar","melahirkan","hewan herbivora","memiliki leher yang panjang","hidup di savana",
        "hewan yang terancam punah","memiliki ekor","memiliki tanduk","hidup berkelompok"
    ],
    "Singa":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat","berbadan besar","melahirkan","hewan karnivora",
        "hewan predator","hidup di savana","memiliki ekor","bertubuh panjang","memiliki bulu lebat di sekitar kepala","hidup berkelompok"
    ],
    "Harimau":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat","berbadan besar","melahirkan","hewan karnivora",
        "hewan predator","hidup di hutan","hewan yang terancam punah","memiliki ekor","bertubuh panjang"
    ],
    "Cicak":[
        "hidup di daratan","hewan amfibi","berkaki empat","kecil","suka berada di dinding","bertelur","hewan predator","memiliki ekor"
    ],
    "Kelelawar":[
        "hidup di daratan","hewan nokturnal","hewan mamalia","memiliki taring","kecil","berkaki dua","melahirkan","hewan predator","hidup di hutan","memiliki ekor","bisa terbang",
        "memiliki sayap","hidup berkelompok"
    ],
    "Burung":[
        "hidup di daratan","memiliki bulu","kecil","berbadan besar","berkaki dua","hewan peliharaan","bertelur","mudah dilatih","hewan predator","hidup di hutan",
        "hidup di savana","memiliki ekor","bisa terbang","memiliki sayap","memiliki paruh","hidup berkelompok"
    ]
}

# Tambah fitur untuk mengajarkan Ai
# contoh: Di main awal bikin menu : Coba Ai, Ajari Ai
# di menu ajari, tambah kan menu : masukkan nama hewan, kemudian masukkan ciri2 hewan 

panjang = len(daftar_hewan.keys())
print(panjang)
