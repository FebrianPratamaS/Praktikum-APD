bmr = float
level_aktivitas = float
kebutuhan_kalori = float

try:

    print("""Pilih jenis kelamin:
        1. Pria
        2. Wanita""")

    input_jenis_kelamin = int(input("Masukkan jenis kelamin anda (taruh nomornya): "))

    if input_jenis_kelamin == 1 or input_jenis_kelamin == 2:
        while True:
            print("""Pilih level aktivitas harian
            1. Aktivitas Minimal (jarang bergerak)
            2. Aktivitas Sedang (olahraga 1-3 kali seminggu)
            3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)""")
            input_level_aktivitas = int(input("Masukkan level aktivitas anda: "))
            if input_level_aktivitas == 1:
                level_aktivitas = 1.25
                break
            elif input_level_aktivitas == 2:
                level_aktivitas = 1.36
                break
            elif input_jenis_kelamin == 3:
                level_aktivitas = 1.72
                break
            else:
                print("Mohon masukkan level aktivitas anda dengan benar.")

        berat_badan = float(input("Masukkan berat badan anda dalam gram: ")) * 0.001
        tinggi_badan = float(input("Masukkan tinggi badan anda dalam kilometer: ")) * 100000
        umur = float(input("Masukkan umur anda: "))

        if input_jenis_kelamin == 1:
            bmr = (10 * berat_badan) + (6.25 * tinggi_badan) - (5 * umur) + 5
        else:
            bmr = (10 * berat_badan) + (6.25 * tinggi_badan) - (5 * umur) - 161
        
        kebutuhan_kalori = bmr * level_aktivitas
        print(f"Kebutuhan kalori anda per hari adalah {kebutuhan_kalori} cal.")
    else:
        print("Maaf. Mohon pilih jenis kelamin anda dengan benar.")

except ValueError:
    print("INPUT SEMUANYA BILANGAN WOY!!!")