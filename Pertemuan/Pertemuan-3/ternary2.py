# Pak Kades sedang mendata penduduknya berdasarkan jenis kelamin, buatlah program
# sederhana untuk menentukan jenis kelamin seseorang dengan menggunakan ternary
# operator.

nama = input("Masukkan nama: ")
kelamin = input("Masukkan jenis kelamin (L untuk Laki-laki, P untuk Perempuan): ")
jenis_kelamin = "Laki-laki" if kelamin == "L" else "Perempuan" if kelamin == "P" else "Tidak diketahui"
print(f"{nama} adalah {jenis_kelamin}.")