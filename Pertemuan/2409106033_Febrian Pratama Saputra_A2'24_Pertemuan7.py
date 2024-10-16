# def menu():
#     print("Menu Pilihan")
#     print("1. Tambah")
#     print("2. Kurang")
#     print("3. Kali")
#     print("4. Bagi")

# menu()

# def salam():
#     print ("Selamat Pagi, FT Muda")
# def kali():
#     x = 6*4
#     print(x)

# salam()
# kali()

# dengan parameter
# def salam(nama):
#     print("Selamat Pagi", nama)

# salam("ridho")

# a = int(input("Masukkan angka pertama: "))
# b = int(input("Masukkan angka kedua: "))
# def tambah(a,b):
#     hasil = a + b
#     print(hasil)

# tambah(a,b)

# tanpa parameter
# def penjumlahan():

#     a = int(input("Masukkan angka pertama: "))
#     b = int(input("Masukkan angka kedua: "))
#     hasil = a + b
#     print(hasil)

# penjumlahan()

# Fungsi
# a = int(input("Masukkan angka pertama: "))
# b = int(input("Masukkan angka kedua: "))
# print(a)
# print(b)

# def tambah(a,b):
#     hasil = a + b
#     return hasil

# print(hasil)

# nama = "shandy"

# def salam():
#     nama = "ibnu"
#     print(nama)

# salam()

# rumus: sisi x sisi
# rumus: sisi x sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
# # pemanggilan Fungsi
# volume_persegi(6)

# Variabel global untuk menyimpan data Buku
buku = []

# fungsi untuk menampilkan semua data
buku =[]
def show_data():
    if len(buku) <= 0:
        print ("Belum Ada data")
    else:
        print("ID", "Nama Buku")
    for indeks in range(len(buku)):
        print (indeks, buku[indeks])

# fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks >= len(buku) or indeks < 0):
        print ("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks >= len(buku) or indeks < 0):
        print ("ID salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU---------- ")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    menu = input("PILIH MENU> ")
    print ("\n")
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
     edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print ("Salah pilih!")
while (True):
    show_menu()



# ============ *Selamat Anda Telah Selesai menjadi programmer Python Pemula.* ============                            