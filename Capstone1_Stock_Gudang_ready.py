from prettytable import PrettyTable
barang_warehouse_gudang = PrettyTable() #start di mulai dari pretty table

barang_warehouse_gudang.field_names = ["Code Barang" , "Nama Barang" , "Stock Barang" , "Jenis Barang" ,  "Harga Barang" , "Approval BPOM" , "Expired Date"] #saya gunakan 6 kolom untuk barang

#contoh dictionary barang terdiri dari Skincare, Injectable, dan Machine
list_barang = [
    {
        "code": "SI001",
        "nama": "ISISPHARMA Neotone Gel",
        "stok": 100,
        "jenis": "Skincare",
        "harga": 280000,
        "bpom": "Approve",
        "expired": "10 June 2028"
    },
    {
        "code": "IN001",
        "nama": "Neauvia Hydro Delux",
        "stok": 10,
        "jenis": "Injectable",
        "harga": 1980000,
        "bpom": "Approve",
        "expired": "19 May 2029"
    },
    {
        "code": "SI002",
        "nama": "ISISPHARMA Teen Derm Gel",
        "stok": 78,
        "jenis": "Skincare",
        "harga": 245000,
        "bpom": "Approve",
        "expired": "21 April 2025"
    },
    {
        "code": "IM001",
        "nama": "INMODE Morpheous8",
        "stok": 3,
        "jenis": "Machine",
        "harga": 1009000000,
        "bpom": "Approve",
        "expired": "No Expired"
    }
]

# menaimpilkan isi list barang untuk menjadi tabel melalui system prety table

for barang in list_barang:
    barang_warehouse_gudang.add_row([
        barang["code"],
        barang["nama"],
        barang["stok"],
        barang["jenis"],
        barang["harga"],
        barang["bpom"],
        barang["expired"]
    ])

def read_menu():
    barang_warehouse_gudang.clear_rows()

    #bisa kita tampilkan untuk filter barang
    print("\n=== FILTER TAMPILAN BARANG ===")
    print("1. Semua")
    print("2. Skincare")
    print("3. Injectable")
    print("4. Machine")
    filter_pilihan = input("Pilih filter tampilan (1-4): ")
    
    #pemfilteran barang
    jenis_filter = None
    if filter_pilihan == "2":
        jenis_filter = "Skincare"
    elif filter_pilihan == "3":
        jenis_filter = "Injectable"
    elif filter_pilihan == "4":
        jenis_filter = "Machine"

    #baru menampilkan filter
    for barang in list_barang:
        if jenis_filter and barang["jenis"] != jenis_filter:
            continue  # skip kalau tidak sesuai filter
        barang_warehouse_gudang.add_row([
            barang["code"],
            barang["nama"],
            barang["stok"],
            barang["jenis"],
            barang["harga"],
            barang["bpom"],
            barang["expired"]
        ])

    print(f"\n==== TAMPILKAN BARANG {'SEMUA' if not jenis_filter else jenis_filter.upper()} ====")
    print(barang_warehouse_gudang)

#digunakan untuk menampilkan setiap barang yang sudah di update
def tampilkan_semua_barang():
    barang_warehouse_gudang.clear_rows()
    for barang in list_barang:
        barang_warehouse_gudang.add_row([
            barang["code"],
            barang["nama"],
            barang["stok"],
            barang["jenis"],
            barang["harga"],
            barang["bpom"],
            barang["expired"]
        ])
    print("\n=== SEMUA BARANG DI GUDANG ===")
    print(barang_warehouse_gudang)


def upload_product_sendiri():
    print("\n=== Upload Product Baru ===")
    print(barang_warehouse_gudang)
    
    #Input code terlebih dahulu agar bisa membedakan barang
    while True:
        kode = input("Masukan kode barang (contoh = S003) noted: S untuk Skincare I untuk Injectable M untuk Machine :")

        #checker untuk duplikat apakah code beda atau masih sama
        duplikat = False
        for barang in list_barang:
            if barang["code"] == kode:
                print("Kode telah digunakan silahkan check kembali")
                duplikat = True
                break
    
        if not duplikat:
            break # keluar dari sini jika code sudah menjadi valid

    nama = input("Input nama product: ") #input nama product
    print(f"Nama produk berhasil dicatat: {nama}") #checker untuk nama
    stock_update = int(input("Masukan Stock Barang: ")) #masukan stock barangnya berapa
    print(f"Stock berhasil di masukin : {stock_update} unit") #checker untuk stock
    jenis_barang = input("Masukan jenis barang (Skincare / Injectable / Machine): ") #masukan jenis barangnya
    print(f"Jenis barang diterima : {jenis_barang}") #checker untuk jenis barang
    harga = int(input("Masukan harganya: ")) #masukan harga barangnya
    print(f"Harga barang sudah diterima {harga}")
    bpom = input("Status BPOM (Approved/Waiting/Rejected): ") #masukan status dari BPOM
    print(f"Status BPOM : {bpom} Diterima")
    expired_date = input("Masukan tangga Expired Date barang (DD MM YYYY ex : 18 July 2025 noted: UNTUK MACHINE TIDAK ADA EXPIRED): ") #masukan expired date barangnya
    print(f"Expired : {expired_date} Diterima")

    #Validasi prefix code untuk jenis barang agar kita bisa pisahkan antara skincare,injectable, dan machine
    huruf_pertama = kode[0]
    if jenis_barang == "Skincare" and huruf_pertama != "S":
        print("BARANG TIDAK BISA DI INPUT KARENA KODE BARANG TIDAK DI MULAI DARI S UNTUK SKINCARE")
        return
    elif jenis_barang == "Injectable" and huruf_pertama != "I":
        print("BARANG TIDAK BISA DI INPUT KARENA KODE BARANG TIDAK DI MULAI DARI I UNTUK INJECTABLE")
        return
    elif jenis_barang == "Machine" and huruf_pertama != "M":
        print("BARANG TIDAK BISA DI INPUT KARENA KODE BARANG TIDAK DI MULAI DARI M UNTUK MACHINE")
        return
    
    #update barang nya yang sudah kita input
    barang_baru_update = {
        "code": kode,
        "nama": nama,
        "stok": stock_update,
        "jenis": jenis_barang,
        "harga": harga,
        "bpom" : bpom,
        "expired" : expired_date
    }
    #masukan barang yang sudah kita input ke append dalam list barang
    list_barang.append(barang_baru_update)
    print(f"{nama} TELAH BERHASIL DI UPDATE SILAHKAN DI CHECK KEMBALI!") #lalu kita kasih checker dan bukti bahwa barang sudah di input
    tampilkan_semua_barang() #barang sudah berhasil di update dan check di menu barang

def update_barang():
    tampilkan_semua_barang()
    kode_update = input("Masukan kode barang yang mau di update: ").upper()
    found = False

    for barang in list_barang:
        if barang["code"] == kode_update:
            found = True
            print("Nama barang telah ditemukan!")
            print(f"Nama    : {barang['nama']}")
            print(f"Stock   : {barang['stok']}")
            print(f"Harga   : {barang['harga']}")
            print(f"Expired : {barang['expired']}")
            print(f"BPOM    : {barang['bpom']}")

            konfirmasi = input("Apakah kamu yakin ingin mengubah barang ini? (yes/no): ").lower()
            if konfirmasi != "yes":
                print("Update dibatalkan.")
                return

            if input("Apakah kamu ingin mengubah nama barang? (yes/no): ").lower() == "yes":
                barang["nama"] = input("Masukan nama barang yang baru: ")
                print("Nama berhasil diupdate!")

            if input("Update stok (yes/no): ").lower() == "yes":
                barang["stok"] = int(input("Masukan stok baru: "))
                print("Stok berhasil diupdate!")

            if input("Update harga (yes/no): ").lower() == "yes":
                barang["harga"] = int(input("Masukan harga baru: "))
                print("Harga berhasil diupdate!")

            if input("Update expired date (yes/no): ").lower() == "yes":
                barang["expired"] = input("Masukan expired date baru (DD MM YYYY): ")
                print("Expired date berhasil diupdate!")

            if barang["bpom"].lower() == "approved" and barang["stok"] > 0:
                status_ready = "Barang ini sudah siap digunakan dan terupdate."
            else:
                status_ready = "Barang harus di-hold karena belum siap (cek stok/BPOM)."

            print(f"Update selesai untuk {barang['nama']}")
            print(status_ready)
            tampilkan_semua_barang()
            break

    if not found:
        print(f"Barang dengan kode {kode_update} tidak ditemukan.")


def delete_barang():
    tampilkan_semua_barang()
    kode_delete = input("Masukan kode barang yang mau di hapus: ").upper()
    found = False
    
    for barang in list_barang:
        if barang["code"] == kode_delete:
            found = True
            print(f"Barang berhasil di temukan {barang['nama']}")
            print(f"Stok    : {barang['stok']}")
            print(f"Harga   : {barang['harga']}")
            print(f"Expired : {barang['expired']}")

            if barang['stok'] > 0:
                print(f"Barang masih punya stok sebanyak {barang['stok']} unit.")
                konfirmasi_stok = input('Apakah anda tetap ingin menghapus (y/n): ').lower()
                if konfirmasi_stok == "y":
                    list_barang.remove(barang)
                    print('Barang berhasil dihapus dari gudang')
                    tampilkan_semua_barang()
                else:
                    print('Barang tidak jadi di hapus')
                    tampilkan_semua_barang()
            else:
                konfirmasi = input('apakah kamu yakin ingin menghapus barang ini (y/n): ')
                if konfirmasi == 'y':
                    list_barang.remove(barang)
                    print('Barang berhasil dihapus dari gudang')
                    tampilkan_semua_barang()
                else:
                    print("Barang tidak jadi di hapus")
                    tampilkan_semua_barang()
            break
    
    if not found:
        print(f"Barang dengan kode {kode_delete} tidak ditemukan.")


def menu_utama():
    while True:
        print("\n===== MENU UTAMA GUDANG PRODUK =====") #tampilkan judul
        print("1. Tampilkan Semua Barang") #list barang awal
        print("2. Upload Produk Baru") #upload product baru
        print("3. Update Produk") #update nama/stok/harga/status
        print("4. Hapus Produk") #deleted product
        print("5. Filter Tampilkan Barang") #filter barang
        print("6. Keluar Program") #exit

        pilihan = input("Silakan pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_semua_barang()
        elif pilihan == "2":
            upload_product_sendiri()
        elif pilihan == "3":
            update_barang()
        elif pilihan == "4":
            delete_barang()
        elif pilihan == "5":
            read_menu()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem gudang. Program selesai.")
            print("BYEBYE")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

menu_utama()
    
