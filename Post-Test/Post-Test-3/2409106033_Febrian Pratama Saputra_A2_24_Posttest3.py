nama = str(input("Masukkan Nama anda: "))
nim = str(input("Masukkan NIM anda: "))
banyak_pinjaman = float(input("Masukkan banyak uang yang dipinjam: "))
lama_pinjaman_tahun = float(input("Masukkan lama pinjaman dalam tahun: "))
persen_cicilan = int
bunga_per_bulan = float
total_cicilan_bulan = float


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

    print(f"Total cicilan per bulan yang dikenakan {nama} dengan NIM {nim} dengan cicilan {persen_cicilan}% adalah Rp{total_cicilan_bulan:.0f} per bulan.")
else:
    print("Maaf. Mohon masukkan lama pinjaman tahunan diantara 1-3 tahun.")
    
