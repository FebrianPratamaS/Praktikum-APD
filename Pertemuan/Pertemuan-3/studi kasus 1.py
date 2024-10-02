#Studi Kasus 1
harga = float(input("Masukkan harga barang = "))
jumlah = float(input("Masukkan jumlah barang = " ))
diskon = 0.20
harga_total = harga * jumlah

if harga_total > 100000 and jumlah >= 5:
    diskon_barang = harga_total * diskon
    harga_diskon = harga_total - diskon_barang
    print(f"Harga setelah diskon adalah Rp{harga_diskon:.0f}")

else:
    print("Anda tidak mendapatkan diskon.")