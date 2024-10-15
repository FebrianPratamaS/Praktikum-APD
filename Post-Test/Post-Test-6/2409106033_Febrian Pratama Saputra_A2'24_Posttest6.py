users = {
    "Febrian Pratama Saputra": {"password": "2409106033", "role": "admin"},
    "Tamu": {"password": "123", "role": "user"}
}

obat_obatan = {
    "Paracetamol": {"jenis": "Analgesik", "harga": 5000, "stok": 100},
    "Amoxicillin": {"jenis": "Antibiotik", "harga": 10000, "stok": 50},
    "Ibuprofen": {"jenis": "Anti-inflamasi", "harga": 7500, "stok": 200}
}

sesi_login = False
pengguna_sekarang = ""
fase_login = True

while True:
    while fase_login:
        print("\n=== Sistem Pendataan Obat-Obatan Rumah Sakit ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")

        try:
            pilihan_login = int(input("Pilih opsi menu: "))
        except ValueError:
            print("Input tidak valid. Silahkan coba lagi.")
            pilihan_login = -1

        if pilihan_login == 1:
            print("\n === Silahkan Login (Akun tamu: Username ""'Tamu'"" Password ""'123'"") === ")
            username = input("Masukan username anda: ")
            password = input("Masukkan password anda: ")

            if username in users and users[username]["password"] == password:
                sesi_login = True
                pengguna_sekarang = {"username": username, "role": users[username]["role"]}
                print(f"Login berhasil. Selamat datang {username} sebagai {users[username]['role']}.")
                fase_login = False

            else:
                print("Username atau password salah. Silahkan coba lagi.")

            while sesi_login:
                print("\n=== Menu Obat-Obatan ===")
                print("1. Tambah Data Obat")
                print("2. Liat Data Obat")
                print("3. Ubah Data Obat")
                print("4. Hapus Data Obat")
                print("5. Logout")

                try:
                    pilihan_crud = int(input("Pilih opsi: "))
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka.")
                    pilihan_crud = -1

                if pilihan_crud == 1:
                    if pengguna_sekarang["role"] == "admin":
                        print("\n=== Tambah Data Obat ===")
                        nama_obat = input("Masukkan Nama Obat: ")
                        jenis_obat = input("Masukkan Jenis Obat: ")
                        try:
                            harga_obat = int(input("Masukkan Harga Obat: "))
                            stok_obat = int(input("Masukkan Stok Obat: "))
                            obat_obatan[nama_obat] = {"jenis": jenis_obat, "harga": harga_obat, "stok": stok_obat}
                            print("Data obat berhasil ditambahkan.")
                        except ValueError:
                            print("Input tidak valid. Jumlah dan Harga harus berupa angka. Silahkan coba lagi.")
                    else:
                        print("Hanya admin yang dapat menambah data obat.")

                if pilihan_crud == 2:
                    if len(obat_obatan) == 0:
                        print("Tidak ada data obat.")
                    else:
                        print("\n=== Daftar Obat-Obatan ===")
                        for nama, data in obat_obatan.items():
                            print(f"Nama: {nama}, Jenis: {data['jenis']}, Harga: {data['harga']}, Stok sisa: {data['stok']}")


                if pilihan_crud == 3:
                    if pengguna_sekarang["role"] == "admin":
                        print("\n=== Ubah data obat ===")
                        nama_obat = input("Masukkan nama obat yang ingin diubah: ")
                        if nama_obat in obat_obatan:
                            print(f"Data obat: {obat_obatan[nama_obat]}")
                            nama_obat_baru = input("Masukkan nama obat baru: ")
                            jenis_obat_baru = input("Masukkan jenis obat baru: ")
                            try:
                                harga_obat_baru = int(input("Masukkan harga obat baru: "))
                                stok_obat_baru = int(input("Masukkan stok obat baru: "))
                                obat_obatan[nama_obat_baru] = {"jenis": jenis_obat_baru, "harga": harga_obat_baru, "stok": stok_obat_baru}
                                del obat_obatan[nama_obat]
                                print("Data obat berhasil diubah.")
                            except ValueError:
                                print("Input tidak valid. Jumlah dan Harga harus berupa angka. Silahkan coba lagi.")
                        else:
                            print("Obat dengan nama tersebut tidak ditemukan.")
                    else:
                        print("Hanya admin yang bisa mengubah data obat. Akses ditolak.")
                
                if pilihan_crud == 4:
                    if pengguna_sekarang    ["role"] == "admin":
                        print("\n=== Hapus Data Obat ===")
                        nama_obat = input("Masukkan Nama Obat yang ingin dihapus: ")
                        if nama_obat in obat_obatan:
                            del obat_obatan[nama_obat]
                            print("Data obat berhasil dihapus.")
                        else:
                            print("Obat dengan nama tersebut tidak ditemukan.")
                    else:
                        print("Hanya admin yang dapat menghapus data obat. Akses ditolak")

                if pilihan_crud == 5:
                    sesi_login = False
                    pengguna_sekarang = ""
                    fase_login = True
                    print("Anda telah logout.")

        elif pilihan_login == 2:
            print("\n=== Registrasi akun baru ===")
            username_reg = input("Masukkan username: ")
            password_reg = input("Masukkan password: ")
            role_reg = input("Masukkan role (admin/user): ").lower()

            if username_reg in users:
                print("Username telah terdaftar.")
            else:
                users[username_reg] = {"password": password_reg, "role": role_reg}
                print("Registrasi akun berhasil. Silahkan login.")
    
        elif pilihan_login == 3:
            print("Terima kasih untuk menggunakan program ini.")
            fase_login = False
            exit()
        
        else:
            print("Opsi tidak valid. Silahkan coba lagi.")