#Buat program python menggunakan kondisi nested If
#Ketentuan : Terdapat input Nilai
#
# Nilai A == >= 80 (A- : 80 - 89, A+ : 90 - 100)
# Nilai B == >= 70 (B- : 70 - 74, B+ : 75 - 79)

#Buat Else jika Kondisi tidak memenuhi

nilai = int(input("Masukkan Nilai anda: "))

if nilai >= 0 and nilai <= 100:
    if nilai >= 80:
        if nilai >= 90:
            print("Nilai anda adalah A+")
        else:
            print("Nilai anda adalah A-")

    elif nilai >= 70:
        if nilai >= 75:
            print("Nilai anda adalah B+")
        else:
            print ("Nilai anda adalah B-")

    else:
        print("Maaf. Nilai anda terlalu rendah untuk memenuhi syarat.")
elif nilai > 100: 
    print("Kok nilaimu tinggi banar???")
else:
    print("Kok nilaimu negatif???")
