# 1. minta input dari pengguna 
# kita gunakan try-except untuk menangani jika pengguna memasukkan selain angka 
try:
    angka_input = int(input("masukkan sebuah bilangan (maks 7 digital): "))
     # 2. proses perhitungan nilai tempat
     # asumsi berdasarkan contoh, kita batasi hingga 9999
    if 0 <= angka_input <= 9999999:
        # ambil nilai untuk jutaan
        jutaan = angka_input // 1000000
        # hitung sisa setelah diambil jutaan
        sisa_jutaan = angka_input % 1000000

        # ambil nilai untuk ratusan ribu
        ratusan_ribuan = sisa_jutaan // 100000
        # hitung sisa setelah diambil ratus_ribuan
        sisa_ratusan_ribuan = sisa_jutaan % 100000

        # ambil nilai untuk puluhan ribuan
        puluhan_ribuan = sisa_ratusan_ribuan // 10000
        # hitung sisa setelah diambil puluhan ribuan 
        sisa_puluhan_ribuan = sisa_ratusan_ribuan % 10000


     # ambil nilai ribuan 
        ribuan = sisa_puluhan_ribuan // 1000
     # hitung sisa setelah diambil ribuannya
        sisa_ribuan = sisa_puluhan_ribuan % 1000
    
     # ambil nilai ratusan dari sisa_ribuan
        ratusan = sisa_ribuan // 100
     # hitung  sisa setelah diambil ratusannya
        sisa_ratusan = sisa_ribuan % 100

     # ambil nilai puluhan dari sisa_ratusan
        puluhan = sisa_ratusan // 10
     # sisa trakhir adalah satuan 
        satuan = sisa_ratusan % 10
     # 3. tampilkan hasil sesuai format
        print(f"\nAnda memasukkan bilangan {angka_input} dimana:")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratusan_ribuan} merupakan ratusan ribuan")
        print(f"{puluhan_ribuan} merupakan puluhan ribuan")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")
        
    else:
        print("harap masukkan bilangan antara 0 dan 9999.")

except ValueError:
    print("input tidak valid! harap memasukkan angka saja.")


       
