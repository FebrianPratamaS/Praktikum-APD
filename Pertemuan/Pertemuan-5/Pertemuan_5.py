# # nama = ["celio",
# #         "shandy",
# #         "farel",
# #         "ghazali",
# #         "vito",
# #         "yuyun",
# #         "adri",
# #         "rizal",
# #         "afdi",
# #         "ifnu"
# #         ]

# # matkul = ["APD","APL","BASDAT","STRUKDAT", "WEB","JARKOM"]
# # data = nama + matkul

# # print("sebelum: ")
# # print(nama)
# # print("")
# # print("sesudah:")
# # print(data*3)
# # nama.insert(2,"afrizal")
# # print(nama)
# # nama[4]="fufufafa"
# # del nama[2]
# # hapus = nama.pop(2)
# # print(nama)
# # print(hapus)
# # print(nama[1:9:2])

# # data = ["farel","celio",[1,2,["halo",23,2.3,True]]]
# # print(data[2][2][::-1])
# # print(data[::-1])

# # matkul = [[1,2,3],[4,5,6],[7,8,9]]
# # # print(matkul[4][3][1])
# # for i in matkul:
# #     print(i)
# #     # for j in i:
# #         # print(j)

# # nama = ('farrel','vito','shandy','rijal')
# # print(nama[1])

# # mahasiswa = (69,"Informatika","2209106044","Aldy septian")
# # absen, prodi, nim, nama = mahasiswa
# # print(nim)

# print(
#     """
# =========================
# | DATA MAHASISWA A24    |
# =========================
# |    1. TAMBAH DATA     |
# |    2. TAMPILKAN DATA  |
# |    3. UBAH DATA       |
# |    4. HAPUS DATA      |
# |    5. KELUAR          |
# =========================
# """
# )
# data_mahasiswa = []
# while True:
#     pilih = int(input("PILIH : "))
#     if pilih == 1:
#         nama = input("NAMA : ")
#         nim = input("NIM : ")
#         kelas = input("KELAS : ")
#         data_mahasiswa.append([nama,nim,kelas])
#     elif pilih == 2:
#         for i in range(len(data_mahasiswa))
#                 print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
#     elif pilih == 3:
#         nama_lama = input("Nama Baru")
#         for data in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 nama_baru = input ("NAMA : ")
#                 nim_baru = input("NIM : ")
#                 kelas_baru = input("Kelas : ")
#                 data_mahasiswa[i][0] = nama_baru
#                 data_mahasiswa[i][1] = nim_baru
#                 data_mahasiswa[i][2] = kelas_baru
#             else:
#                 print("Data Tidak ditemukan")
#     elif pilih == 4:
#         nama_lama = input("Nama yang ingin dihapus")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
                    
#     elif pilih == 5:
#         break
            
