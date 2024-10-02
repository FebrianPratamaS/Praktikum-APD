range_maksimal = int(input("Masukkan range maksimal: "))

hitung_prima = 0

for angka in range(1, range_maksimal):
    angka += 1
    apakah_prima = True

    for i in range(2, angka):
        if angka % i == 0:
            apakah_prima = False
            break
    if apakah_prima == True:
        print(f"{angka} prima")
        hitung_prima += 1

print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")
