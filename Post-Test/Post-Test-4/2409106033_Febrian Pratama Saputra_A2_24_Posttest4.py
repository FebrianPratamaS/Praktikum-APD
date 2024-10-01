print("Silahkan login dulu. (Maksimal percobaan 3 kali.)")
percobaan_login = 0
keluar_program = False

while percobaan_login < 3 and not keluar_program:
    nama = str(input("Masukkan Nama anda (huruf kapital diperhatikan!): "))
    nim_password = str(input("Masukkan 3 nomor terakhir NIM anda (Jika diawali 0 tidak usah ditulis): "))

    if nama == "Febrian Pratama Saputra" and nim_password == "33":
        print(f"Selamat datang, {nama}.")
        while not keluar_program:
            banyak_pinjaman = float(input("Masukkan banyak uang yang dipinjam (Masukkan negatif jika ingin keluar): "))
            lama_pinjaman_tahun = float(input("Masukkan lama pinjaman dalam tahun (Masukkan negatif jika ingin keluar): "))

            if banyak_pinjaman < 0 or lama_pinjaman_tahun < 0:
                print("Program akan keluar.")
                keluar_program = True
            else:
                if lama_pinjaman_tahun >= 1 and lama_pinjaman_tahun <= 3:
                    if lama_pinjaman_tahun == 1:
                        bunga_per_bulan = (0.07 / 12) * banyak_pinjaman
                        total_cicilan_bulan = (banyak_pinjaman + bunga_per_bulan) / 12
                        persen_cicilan = 7
                    elif lama_pinjaman_tahun == 2:
                        bunga_per_bulan = (0.13 / 12) * banyak_pinjaman
                        total_cicilan_bulan = (banyak_pinjaman + bunga_per_bulan) / 24
                        persen_cicilan = 13
                    else:
                        bunga_per_bulan = (0.19 / 12) * banyak_pinjaman
                        total_cicilan_bulan = (banyak_pinjaman + bunga_per_bulan) / 36
                        persen_cicilan = 19
                    
                    print(f"Total cicilan per bulan yang dikenakan {nama} dengan cicilan {persen_cicilan}% adalah Rp{total_cicilan_bulan:.0f} per bulan.")
                else:
                    print("Maaf. Mohon masukkan lama pinjaman tahunan diantara 1-3 tahun.")
    else:
        if percobaan_login < 2:
            print("Maaf. Silahkan masukkan username dan password lagi.")
            percobaan_login += 1
        else:
            percobaan_login += 1

if percobaan_login == 3:
    print("Semua percobaan telah habis. Akses ditolak.")