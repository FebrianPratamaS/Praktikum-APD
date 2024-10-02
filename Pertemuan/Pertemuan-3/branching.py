Umur = int(input("Masukkan umur Anda : "))
if Umur > 0:
    if Umur <= 10:
        print("Umur Anda termasuk kategori anak-anak")
    elif Umur <= 18:
        print("Umur Anda termasuk kategori remaja")
    elif Umur <=35:
        print("Umur Anda termasuk kategori dewasa")
    elif Umur <=65:
        print("Umur Anda termasuk kategori paruh baya")
    else:
        print("Umur Anda termasuk kategori Tua")
else:
    print("Umur harus bilangan positif")