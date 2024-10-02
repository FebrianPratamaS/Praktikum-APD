
print("""
    ========================
    Kalkulator Sederhana
    1. +
    2. -
    3. *
    4. /  
    =======================""")
fitur = int(input("Pilih Fitur : "))

match fitur:
    case 1:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a + b
        print(f"Hasil Pertambahan Angka 1 dan Angka 2 adalah {c}")
    case 2:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a - b
        print(f"Hasil Pengurangan Angka 1 dan Angka 2 adalah {c}")
    case 3:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a * b
        print(f"Hasil Perkalian Angka 1 dan Angka 2 adalah {c}")
    case 4:
        a = int(input("Masukkan Angka 1 : "))
        b = int(input("Masukkan Angka 2 : "))
        c = a / b
        print(f"Hasil Pembagian Angka 1 dan Angka 2 adalah {c}")
    case _:
        print("Invalid Input!")

