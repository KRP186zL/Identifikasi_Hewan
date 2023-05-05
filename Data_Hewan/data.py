import random

daftar_pertanyaan= [
    "Apakah dia hidup di lautan ?","Apakah dia hidup di daratan ?","Apakah dia hewan buas ?","Apakah dia hewan nokturnal ?",
    "Apakah dia hewan mamalia ?", "Apakah dia memiliki bulu ?", "Apakah dia memiliki taring ?","Apakah dia hewan amfibi ?",
    "Apakah dia berkaki empat ?","Apakah dia cepat ?", "Apakah dia kecil ?","Apakah dia berbadan besar ?","Apakah dia berkaki dua ?",
    "Apakah dia hidup bersama manusia ?","Apakah dia hewan peliharaan ?", "Apakah dia memiliki belalai ?",
    "Apakah dia suka berada di dinding ?","Apakah dia bertelur ?","Apakah dia melahirkan ?","Apakah dia hewan karnivora ?",
    "Apakah dia hewan omnivora ?","Apakah dia hewan herbivora ?","Apakah dia mudah dilatih ?","Apakah dia hewan predator ?",
    "Apakah dia memiliki kepala yang panjang ?","Apakah dia hidup di hutan ?","Apakah dia hidup di savana ?",
    "Apakah dia hewan yang terancam punah ?","Apakah dia memiliki gading ?","Apakah dia memiliki ekor ?",
    "Apakah dia bertubuh panjang ?", "Apakah dia memiliki sisik ?","Apakah dia tidak mempunyai kaki ?",
    "Apakah dia bisa di tunggangi ?","Apakah dia bisa terbang ?","Apakah dia memiliki sayap ?","Apakah dia memiliki kulit yang keras",
    "Apakah dia memiliki bulu lebat di sekitar kepala ?","Apakah dia memiliki bisa/racun","Apakah dia memiliki paruh ?",
    "Apakah dia memiliki kantung ?","Apakah dia memiliki delapan kaki ?","Apakah dia memiliki tanduk ?","Apakah dia hidup di perairan dingin ?"
]


random.shuffle(daftar_pertanyaan)


daftar_hewan = {
    "Gajah": [
        "hidup di daratan","mamalia","hewan mamalia","memiliki bulu","berkaki empat","berbadan besar","memiliki belalai",
        "melahirkan","hewan herbivora","mudah di latih","hidup di hutan","hidup di savana","hewan yang terancam punah",
        "memiliki gading","memiliki ekor","bisa ditunggangi"
    ],

    "Kuda": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berkaki empat","cepat","hewan peliharaan","melahirkan","hewan herbivora",
        "hidup di savana","memiliki ekor","bisa di tunggangi","memiliki bulu lebat di kepala"
             
    ],
             
    "Kucing": [
        "hidup di daratan","hewan mamalia","memiliki bulu","memiliki taring","berkaki empat","kecil","hidup bersama manusia",
        "hewan peliharaan","melahirkan","hewan karnivora","mudah di latih","memiliki ekor"
    ],

    "Kanguru": [
        "hidup di daratan","hewan mamalia","memiliki bulu","berbadan besar","berkaki dua","melahirkan","hewan herbivora",
        "hidup di savana","hidup di hutan","memiliki ekor","memiliki kantung"
    ],

    "Sapi": [
        "hidup di daratan","hewan mamalia","berkaki empat","berbadan besar","hewan peliharaan","melahirkan","hewan herbivora",
        "memiliki ekor","memiliki tanduk","memproduksi susu"
    ],

    "Penguin":[
        "hidup di dua "
    ],
    "Ular":["bertubuh panjang", "memiliki sisik", "tidak mempunyai kaki", "hidup di daratan", "hewan karnivora"],
    "Buaya":["memiliki moncong yang panjang", "berbadan panjang dilapisi sisik tanduk", "memiliki empat kaki", "hidup di dua alam", "hewan karnivora"],
    "Monyet":["mempunyai ekor", "hidup dihutan", "memiliki bulu", "memiliki dua kaki dan dua tangan", "hewan omnivora"],
    "Komodo":["mempunyai ekor", "warna kulit kuning kehitaman", "berkaki empat", "memiliki sisik", "hewan karnivora"],
    "Rusa":["ekor pendek", "telinga yang panjang", "mempunyai tanduk", "mempunyai 4 kaki", "hewan herbivora"],
    "Banteng":["mempunyai tanduk panjang melengkung ke atas", "berkaki empat", "memiliki bulu", "besar", "hewan herbivora"],
    "Kelinci":["cara jalan yang unik dengan melompat", "berkaki empat" ,"kecil" ,"memiliki bulu" ,"hewan mamalia"],
    "Beruang":["besar", "mempunyai cakar tajam", "memiliki bulu", "berkaki empat", "hewan karnivora"],
    "Anjing":["memiliki ekor", "kecil", "berkaki empat", "memiliki bulu", "hewan peliharaan", "hewan omnivora","hidup bersama manusia","pintar","hidup di daratan","melahirkan"],
    "Katak":["bertubuh langsing", "tekstur kulit halus, basah dan tipis", "berkaki empat", "hidup di dua alam", "karnivora"],
    "Kupu-kupu":["berkaki enam", "mempunyai sayap dan antena dikepala", "mempunyai belalai seperti sedotan", "hewan herbivora"],
    "Laba-laba":["memiliki empat mata", "berkaki delapan", "tidak bersayap", "berbisa", "hewan karnivora"],
    "Babi":["berkaki empat", "tubuh panjang", "memiliki hidung besar", "mengandung cacing pita", "hewan omnivora"],
    "Ayam":["berkaki dua", "mempunyai dua sayap", "memiliki bulu", "memiliki jengger dikepala", "hewan omnivora"],
    "Orang hutan":["berbadan besar","memiliki bulu","mamalia","hidup di hutan"],
    "Jerapah":["memiliki kepala yang panjang","hidup di savana"],
    "Singa":["hewan buas","memiliki taring","berkaki empat","hidup di savana"],
    "Harimau":["hewan buas","memiliki taring","berkaki empat","hidup di hutan"],
    "Cheetah":[]
}

