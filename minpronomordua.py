#function buat login
def login():
    while True:
        print("1. Admin")
        print("2. Pelanggan")
        
        pengguna = input("Pilih pengguna: ")
        

        if pengguna == "1":
            password = input("Masukan password: ")
            if password == "admin123":
                
                admin()
        
        elif pengguna == "2":
            pelanggan()
        else:
            print("coba lagi")

# buat bikin prettytable
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["No", "Nama servisan", "Harga servis "]

#membuat list layanan pakai prettytable
def servisan(no, nama_servisan, harga):
    table.add_row([no, nama_servisan, harga])

servisan("1",  "Laptop Pecah", "3000000")
servisan("2",  "Virus Bjorka", "4000000")
servisan("3",  "Pc Makan nasikuning", "5000000")
servisan("4",  "Ram patah", "6000000")
servisan("5",  "UPS Konslet", "7000000")

#function untuk fitur admin
def admin():
    while True:
        nama = input("Masukan Nama Anda: ")
        print(f"Selamat Datang {nama} silahkan pilih pilihan anda")
        while True:
            print("1. tambah servisan")
            print("2. lihat servisan")
            print("3. update servisan")
            print("4. hapus servisan")
            print("5. keluar")
        
            pilihan = input("Masukan pilihan: ")
            if pilihan == "1":
                create_servisan()
            elif pilihan == "2":
                lihat_servisan()
            elif pilihan == "3":
                update_servisan()
            elif pilihan == "4":
                hapus_servisan()
            elif pilihan == "5":
                print("keluar")
                return
            else:
                print("maaf tidak ada pilihan")

#function untuk fitur pelanggan
def pelanggan():
    while True:
        print("1. lihat layanan tersedia")
        print("2. pesan layanan")
        print("3. keluar")
        pilihan = input("Masukan pilihan: ")

        if pilihan == "1":
            lihat_servisan()
        elif pilihan == "2":
            pesan_layanan()
        elif pilihan == "3":
            print("sampai jumpa kembali")
            break
        else:
            print("maaf tidak ada pilihan")

#function create
def create_servisan():
    no = str(len(table._rows) + 1)
    nama_servisan = input('masukan nama servisan: ')
    harga = input('masukan harga servisan: ')
    servisan (no, nama_servisan, harga)
    print ('layanan berhasil ditambahkan')
    lihat_servisan()
    
#function read
def lihat_servisan():
    print(table)

#function update
def update_servisan():
    print(table)
    no = input("Masukkan Nomor Servisan yang ingin diupdate: ")
    for ubah in table._rows:
        if ubah[0] == no:
            
            nama_servisan = input("Masukkan Nama Servisan baru: ")
            harga = input("Masukan Harga Baru: ")
            ubah[1] = nama_servisan
            ubah[2] = harga
            print("Servisan berhasil diupdate!")
            print(table)
            break
    else:
        print("Layanan tidak ditemukan.")

#function delete
def hapus_servisan():
    print(table)
    no = input("Masukkan Nomor Servisan yang ingin dihapus: ")
    for ubah in table._rows:
        if ubah[0] == no:
            table._rows.remove(ubah)
            lihat_servisan()
            print(table)
            break
    else:
        print("Layanan tak ditemukan")

#function untuk pemesanan
import time
def pesan_layanan():
    print(table)
    no = input("Masukkan Nomor Servisan ")
    for pesan in table._rows:
        if pesan [0] == no:
            print(f"Anda telah memesan layanan servis {pesan[1]} dengan harga {pesan[2]}. ")

            
            print("Pesanan dikonfirmasi...")
            time.sleep(2)
            print("Menyiapkan Teknisi...")
            time.sleep(2)
            print("Pesanan diproses...")
            time.sleep(2)
            print("Teknisi: Astagfirullah(dalam proses)... ")
            time.sleep(2)
            print("Selamat masalah anda telah kami selesaikan!")
            
            print("Servisan yang tersedia:")
            
            break
            
    else:
        print('layanan tak ditemukan')

login()

