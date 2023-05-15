import numpy as np, pandas as pd
from tabulate import tabulate

diseases = [["P01","Kanker Ovarium"],
           ["P02","Kista Denoma Ovarii Serosum"],
           ["P03","Kista Denoma Ovarii Musinosum"],
           ["P04","Kista Dermoid"],
           ["P05","Kista Endometriosis"],
           ["P06","PCOS (Polycystic Ovary Syndrome)"],
           ["P07","Ooforitis (Peradangan pada indung telur)"],
           ["P08","Menopause"]]

symptoms = {
    "G001":"Perut terasa kembung",
    "G002":"Merasa cepat kenyang",
    "G003":"Mual-mual",
    "G004":"Nyeri perut bagian bawah",
    "G005":"Mengalami kostipasi (Sembelit)",
    "G006":"Adanya pembengkakan pada perut",
    "G007":"Mengalami penurunan berat badan",
    "G008":"Sering buang air kecil",
    "G009":"Sakit punggung bagian bawah",
    "G0010":"Vagina terasa sakit saat berhubungan seks",
    "G0011":"Mengalami hormon androgen yang meningkat (Tumbuhnya rambut yang lebat di wajah, dagu, bawah hidung)",
    "G0012":"Mengalami perubahan siklus menstruasi",
    "G0013":"Haid tidak normal dan dalam jumlah banyak",
    "G0014":"Warna kulit menjadi gelap",
    "G0015":"Mengalami panas dingin",
    "G0016":"Keputihan yang disertai dengan bau busuk",
    "G0017":"Mengalami kerontokan rambut",
    "G0018":"Kulit menjadi kering",
    "G0019":"Berat badan bertambah",
    "G0020":"Suasana hati berubah-ubah atau moody",
    "G0021":"Vagina menjadi kering",
    "G0022":"Penurunan Libido (gairah seksual)",
    "G0023":"Berkeringat di malam hari",
    "G0024":"Adanya timbul benjolan pada perut",
    "G0025":"Nyeri saat menstruasi",
    "G0026":"Tidak sanggup mencerna",
    "G0027":"Menstruasi yang datang terlambat",
    "G0028":"Nyeri perut secara tiba-tiba",
    "G0029":"Tubuh terasa lemas",
    "G0030":"Sering muntah-muntah",
    "G0031":"Gangguan buang air besar atau kecil, adanya darah pada urine",
    "G0032":"Sulit punya anak dalam kurun waktu 1 tahun",
    "G0033":"Jerawat pada wajah, dada dan punggung atas",
    "G0034":"Tonjolan daging bersifat jinak di ketiak atau leher",
    "G0035":"Merasa tidak tenang",
    "G0036":"Sulit tidur"
    }
            
patient_symp = []
            
#menu 1
def show_symtoms():
    data = [x for x in symptoms.items()]
    dataframe = pd.DataFrame(data)
    diseases_table = tabulate(dataframe, headers =["Kode Gejala","Nama Gejala"],
                             tablefmt = "fancy_grid",numalign="left")
    print(diseases_table)
    main()
            
#menu 2 
def add_symptoms():
        for i in range (len(symptoms.keys())):
            symptomp = input("Masukkan kode gejala yang anda alami: ")
            if symptomp in symptoms.keys():
                patient_symp.append(symptomp)
                choice = input("Apakah ada gejala lain ? [Y/N]: ").lower()
                if choice == "n":
                    break
            else:
                print("Kode gejala yang anda masukkan tidak ada, mohon masukkan dengan benar (cek menu 1) !")
        main()
                
#menu 3
def show_pt_sysmptomps():
    patient_symp_copy = patient_symp.copy()
    if not patient_symp:
        print("Silahkan masukkan gejala terlebih dahulu !")
        main()
    else:
        patient_symp_copy.sort()
        gejala_yang_dialami= list(filter(lambda item: item[0] in patient_symp, symptoms.items()))
        dataframes = pd.DataFrame(gejala_yang_dialami)
        diseases_table = tabulate(dataframes,headers=["Kode Gejala","Nama Gejala"],
                                 tablefmt="fancy_grid",numalign="left")
        print(diseases_table)
    choice = input("Adakah gejala lain yang belum anda sebutkan ? [Y/N]: ").lower()
    if choice == "y":
        add_symptoms()
    else:
        main()
           
#menu 4
def diagnose(sy):
    if not sy:
        print("Silahkan masukkan gejala terlebih dahulu !")
        main()
    else:
        if len(sy) <=3:
            print("Penyakit yang anda alami tidak diketahui, mungkin gejala yang di masukkan tidak lengkap. Mohon di ulangi lagi!")
            main()
        elif sy [0] == "G001" and sy[1] == "G002" and sy[2] == "G003" and sy[3] == "G004" and sy[4] == "G005" and sy[5] == "G006" and sy[6] == "G007" and sy[7] == "G008":
            return diseases[0][1]
        elif sy[0] == "G001" and sy [1] == "G004" and sy[2] == "G0012" and sy[3] == "G0024":
            return diseases[1][1]
        elif sy[0] == "G007" and sy [1] == "G0025" and sy[2] == "G0026" and sy[3] == "G0027":
            return diseases[2][1]
        elif sy[0] == "G009" and sy [1] == "G0028" and sy[2] == "G0029" and sy[3] == "G0030":
            return diseases[3][1]
        elif sy[0] == "G004" and sy [1] == "G009" and sy[2] == "G0010" and sy[3] == "G0013" and sy[4] == "G0025" and sy[5] == "G0031" and sy[6] == "G0032":
            return diseases[4][1]
        elif sy[0] == "G0011" and sy [1] == "G0012" and sy[2] == "G0014" and sy[3] == "G0017" and sy[4] == "G0019" and sy[5] == "G0033" and sy[6] == "G0034":
            return diseases[5][1]
        elif sy[0] == "G003" and sy [1] == "G004" and sy[2] == "G008" and sy[3] == "G009" and sy[4] == "G0010" and sy[5] == "G0012" and sy[6] == "G0013" and sy[7] == "G0015" and sy[8] == "G0016":
            return diseases[6][1]
        elif sy[0] == "G0018" and sy [1] == "G0020" and sy[2] == "G0021" and sy[3] == "G0022" and sy[4] == "G0023" and sy[5] == "G0035" and sy[6] == "G0036":
            return diseases[7][1]
        else:
            print("Penyakit yang anda alami tidak diketahui, mungkin gejala yang di masukkan tidak lengkap. Mohon di ulangi lagi!")
            patient_symp.clear()
            main()

def main():
    print(f"""\n{'-'*30}
Silahkan pilih menu di bawah: 
1. Tampilkan Daftar Gejala
2. Masukkan Gejala
3. Tampilkan Gejala
4. Tampilkan Diagnosa
5. Keluar""")
    try:
        choice = int(input("Masukkan pilihan: "))
        print("-"*20)
        if choice == 1:
            show_symtoms()
        elif choice == 2:
            add_symptoms()
        elif choice == 3:
            show_pt_sysmptomps()
        elif choice == 4:
            diseases = diagnose(patient_symp)
            hasil_diagnose = "".join(diseases)
            print(f"Anda mengalami gejala penyakit: {hasil_diagnose}")
            exit()
        elif choice == 5:
            exit()
        print("-"*30)
    except ValueError:
        print("Tidak boleh menggunakan angka!")
        main()
    
main()
    