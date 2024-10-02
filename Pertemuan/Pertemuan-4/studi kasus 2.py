total = 0
while True:
    angka = int (input("Masukkan angka positif (input negatif jika berhenti): "))
    if angka < 0:
        break
    total += angka
    print(f"jumlah total adalah {total}.")