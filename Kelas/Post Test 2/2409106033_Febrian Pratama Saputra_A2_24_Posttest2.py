print("Masukan Nama Lengkap")
Nama = str(input())
print("Masukan NIM Lengkap")
NIM = str(input())
print("Masukan Harga Beras dalam Rp")
HargaBeras = float(input())

print(f"{Nama} dengan NIM {NIM} ingin membeli beras seharga Rp{HargaBeras}.")
print(f"Jika dia membeli beras Mawar ia harus membayar Rp{HargaBeras - (HargaBeras * 0.11)} setelah mendapatkan diskon 11%.")
print(f"Jika dia membeli beras Sania ia harus membayar Rp{HargaBeras - (HargaBeras * 0.14)} setelah mendapatkan diskon 14%.")
print(f"Jika dia membeli beras Maknyus ia harus membayar Rp{HargaBeras - (HargaBeras * 0.17)} setelah mendapatkan diskon 17%.")