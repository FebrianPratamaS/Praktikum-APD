users = [["Febrian Pratama Saputra", "2409106033", "admin"],
         ["Tamu", "123", "user"]]

obat_obatan = [["Paracetamol", "Analgesik", 5000, 100],
               ["Amoxicillin", "Antibiotik", 10000, 50],
               ["Ibuprofen", "Anti-inflamasi", 7500, 200]]

login_session = False
current_user = ""
login_phase = True

while True:
    while login_phase:
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

            akun_ketemu = False
            for user in users:
                if user[0] == username and user[1] == password:
                    login_session = True
                    current_user = user
                    akun_ketemu = True
                    print(f"Login berhasil. Selamat datang {username} sebagai {user[2]}.")
                    login_phase = False

            if not akun_ketemu:
                print("Username atau password salah. Silahkan coba lagi.")

            while login_session:
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
                    if current_user[2] == "admin":
                        print("\n=== Tambah Data Obat ===")
                        try:
                            nama_obat = input("Masukkan Nama Obat: ")
                            jenis_obat = input("Masukkan Jenis Obat: ")
                            harga_obat = int(input("Masukkan Harga Obat: "))
                            stok_obat = int(input("Masukkan Stok Obat: "))
                            obat_obatan.append([nama_obat, jenis_obat, harga_obat, stok_obat])
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
                        for obat in obat_obatan:
                            print(f"Nama: {obat[0]}, Jenis: {obat[1]}, Harga: {obat[2]}, Stok sisa: {obat[3]}")

                if pilihan_crud == 3:
                    if current_user[2] == "admin":
                        print("\n=== Ubah data obat ===")
                        nama_obat = input("Masukkan nama obat yang ingin diubah: ")
                        obat_ketemu = False
                        for obat in obat_obatan:
                            if obat[0] == nama_obat:
                                obat_ketemu = True
                                print(f"Data obat: {obat}")
                                nama_obat_baru = input("Masukkan nama obat baru: ")
                                jenis_obat_baru = input("Masukkan jenis obat baru: ")
                                try:
                                    harga_obat_baru = int(input("Masukkan harga obat baru: "))
                                    stok_obat_baru = int(input("Masukkan stok obat baru: "))
                                    obat[0] = nama_obat_baru
                                    obat[1] = jenis_obat_baru
                                    obat[2] = harga_obat_baru
                                    obat[3] = stok_obat_baru
                                    print("Data obat berhasil diubah.")
                                except ValueError:
                                    print("Input tidak valid. Jumlah dan Harga harus berupa angka. Silahkan coba lagi.")
                                break
                        if not obat_ketemu:
                            print("Obat dengan nama tersebut tidak ditemukan.")
                    else:
                        print("Hanya admin yang bisa mengubah data obat. Akses ditolak.")

                
                if pilihan_crud == 4:
                    if current_user[2] == "admin":
                        print("\n=== Hapus Data Obat ===")
                        nama_obat = input("Masukkan Nama Obat yang ingin dihapus: ")
                        obat_ketemu = False
                        for obat in obat_obatan:
                            if obat[0] == nama_obat:
                                obat_obatan.remove(obat)
                                obat_ketemu = True
                                print("Data obat berhasil dihapus.")
                                break
                        if not obat_ketemu:
                            print("Obat dengan nama tersebut tidak ditemukan.")
                    else:
                        print("Hanya admin yang dapat menghapus data obat. Akses ditolak")

                if pilihan_crud == 5:
                    login_session = False
                    current_user = ""
                    login_phase = True
                    print("Anda telah logout.")

        elif pilihan_login == 2:
            print("\n=== Registrasi akun baru ===")
            username_reg = input("Masukkan username: ")
            password_reg = input("Masukkan password: ")
            role_reg = input("Masukkan role (admin/user): ").lower()

            if role_reg not in ["admin", "user"]:
                print("Role tidak valid. Harus admin atau user. Silahkan coba lagi.")
                continue
            else:
                akun_ketemu = False
                for user in users:
                    if user [0] == username_reg:
                        akun_ketemu = True
                        print("Username telah terdaftar.")
                        break
            
            if not akun_ketemu:
                users.append([username_reg, password_reg, role_reg])
                print("Regitrasi akun berhasil. Silahkan login.")
    
        elif pilihan_login == 3:
            print("Terima kasih untuk menggunakan program ini.")
            login_phase = False
            exit()
        
        else:
            print("Opsi tidak valid. Silahkan coba lagi.")