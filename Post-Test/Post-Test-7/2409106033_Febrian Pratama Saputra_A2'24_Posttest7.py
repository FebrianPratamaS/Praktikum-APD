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

def login():
    global sesi_login, pengguna_sekarang, fase_login
    username = input("Masukan username anda: ")
    password = input("Masukkan password anda: ")

    if username in users and users[username]["password"] == password:
        sesi_login = True
        pengguna_sekarang = {"username": username, "role": users[username]["role"]}
        print(f"Login berhasil. Selamat datang {username} sebagai {users[username]['role']}.")
        fase_login = False
    else:
        print("Username atau password salah. Silahkan coba lagi.")

def lihat_obat():
    if len(obat_obatan) == 0:
        print("Tidak ada data obat.")
    else:
        print("\n=== Daftar Obat-Obatan ===")
        for nama, data in obat_obatan.items():
            print(f"Nama: {nama}, Jenis: {data['jenis']}, Harga: {data['harga']}, Stok sisa: {data['stok']}")

def tambah_obat(nama_obat, jenis_obat, harga_obat, stok_obat):
    global obat_obatan
    if pengguna_sekarang["role"] == "admin":
        obat_obatan[nama_obat] = {"jenis": jenis_obat, "harga": harga_obat, "stok": stok_obat}
        print("Data obat berhasil ditambahkan.")
    else:
        print("Hanya admin yang dapat menambah data obat.")

def registrasi():
    global users
    username_reg = input("Masukkan username: ")
    password_reg = input("Masukkan password: ")
    role_reg = input("Masukkan role (admin/user): ").lower()

    if username_reg in users:
        print("Username telah terdaftar.")
    else:
        users[username_reg] = {"password": password_reg, "role": role_reg}
        print("Registrasi akun berhasil. Silahkan login.")

def hapus_obat():
    global obat_obatan
    if pengguna_sekarang["role"] == "admin":
        nama_obat = input("Masukkan Nama Obat yang ingin dihapus: ")
        if nama_obat in obat_obatan:
            del obat_obatan[nama_obat]
            print("Data obat berhasil dihapus.")
        else:
            print("Obat dengan nama tersebut tidak ditemukan.")
    else:
        print("Hanya admin yang dapat menghapus data obat.")

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
            login()

            while sesi_login:
                print("\n=== Menu Obat-Obatan ===")
                print("1. Tambah Data Obat")
                print("2. Liat Data Obat")
                print("3. Hapus Data Obat")
                print("4. Logout")

                try:
                    pilihan_crud = int(input("Pilih opsi: "))
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka.")
                    pilihan_crud = -1

                if pilihan_crud == 1:
                    nama_obat = input("Masukkan Nama Obat: ")
                    jenis_obat = input("Masukkan Jenis Obat: ")
                    try:
                        harga_obat = int(input("Masukkan Harga Obat: "))
                        stok_obat = int(input("Masukkan Stok Obat: "))
                        tambah_obat(nama_obat, jenis_obat, harga_obat, stok_obat)
                    except ValueError:
                        print("Input tidak valid. Jumlah dan Harga harus berupa angka. Silahkan coba lagi.")

                elif pilihan_crud == 2:
                    lihat_obat()

                elif pilihan_crud == 3:
                    hapus_obat()

                elif pilihan_crud == 4:
                    sesi_login = False
                    pengguna_sekarang = ""
                    fase_login = True
                    print("Anda telah logout.")

        elif pilihan_login == 2:
            registrasi()

        elif pilihan_login == 3:
            print("Terima kasih untuk menggunakan program ini.")
            fase_login = False
            exit()

        else:
            print("Opsi tidak valid. Silahkan coba lagi.")