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
    "Apakah dia memiliki jaring ?","Apakah dia suka madu ?","Apakah dia memiliki jengger di kepala ?","Apakah dia memiliki tulang tajam  di kakinya ?"
]


random.shuffle(daftar_pertanyaan)


daftar_hewan = {
    "Gajah": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat",
    ],

    "Kuda": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","cepat",
             
    ],
             
    "Kucing": [
        "hidup di daratan","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","kecil",
    ],

    "Kanguru": [
        "hidup di daratan","hewan mamalia","memiliki bulu",
    ],

    "Sapi": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat",
    ],

    "Penguin":[
        "hidup di daratan","memiliki bulu","kecil",
    ],

    "Ular":[
        "hidup di daratan","hewan buas","hewan nokturnal",
    ],

    "Buaya":[
        "hidup di daratan","hewan buas","memiliki taring","berkaki empat","cepat",
    ],

    "Monyet":[
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","kecil",
    ],

    "Komodo":[
        "hidup di daratan","hewan buas","memiliki taring","berkaki empat","cepat",
    ],
    "Ikan":[
        "cepat","kecil",
    ],

    "Banteng":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","berkaki empat","cepat",
    ],
    "Kelinci":[
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","cepat","kecil",
    ],
    "Beruang":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat",
    ],
    "Anjing":[
        "hidup di daratan","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat",
    ],
    "Katak":[
        "hidup di daratan","hewan amfibi","berkaki empat","cepat","kecil",
    ],
    "Kupu-kupu":[
        "hidup di daratan","kecil",
    ],
    "Laba-laba":[
        "hidup di daratan","memiliki bulu","kecil",
    ],
    "Babi":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat",
    ],
    "Ayam":[
        "hidup di daratan","memiliki bulu","kecil",
    ],
    "Panda":[
        "hewan mamalia","memiliki bulu","memiliki taring","berkaki empat",
    ],
    "Jerapah":[
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat",
    ],
    "Singa":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat",
    ],
    "Harimau":[
        "hidup di daratan","hewan buas","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","cepat",
    ],
    "Cicak":[
        "hidup di daratan","hewan amfibi","berkaki empat","kecil",
    ],
    "Kelelawar":[
        "hidup di daratan","hewan nokturnal","hewan mamalia","memiliki taring","kecil",
    ],
    "Burung":[
        "hidup di daratan","memiliki bulu","kecil",
    ]
}

# Tambah fitur untuk mengajarkan Ai
# contoh: Di main awal bikin menu : Coba Ai, Ajari Ai
# di menu ajari, tambah kan menu : masukkan nama hewan, kemudian masukkan ciri2 hewan 

panjang = len(daftar_hewan.keys())
print(panjang)
