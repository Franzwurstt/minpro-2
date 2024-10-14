# minpro-2
NAMA= PRAKASA WIRA MUKTI
NIM= 2409116054
![image](https://github.com/user-attachments/assets/65ea1a9a-3944-4eec-8085-f76c0295b5d5)


Penjelasan kodingan:

# 1. login function
   
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

PENJELASAN:
fungsi login digunakan agar pengguna bisa memilih peran(admin atau pelanggan)

kalau '1' dipilih, program akan meminta password,kalo passwordnya benar(admin123), fungsi admin() akan dipanggil

kalau'2' dipilih,function pelanggan() akan dipanggil tapi tidak meminta password

kalau input tidak sesuai, maka akan muncul pesan ("Password salah, coba lagi")

Output:
ketika memilih admin dan password yang dimasukan benar maka akan langsung ditujukan ke menu admin dan ketika memilih pelanggan akan langsung masuk ke opsi pelanggan, tetapi jika input tidak valid maka akan ditampilkan


bukti gambar: Admin
![Screenshot (555)](https://github.com/user-attachments/assets/cb7548b4-9744-45b7-97cd-e992788ba700)

bukti gambar: pelanggan
![Screenshot (561)](https://github.com/user-attachments/assets/12ba8f97-a0fb-4a0f-afe7-5336a367f4ce)

# 2. tabel 

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

penjelasan:
prettytable untuk nampilkan layanan dalam format tabel
function servisan buat nambahkan nomor menu dan harga kedalam tabel

output:
tabel menampilkan informasi menu menu layanan 

contoh gambar:

![Screenshot (559)](https://github.com/user-attachments/assets/41a60e6a-740d-4d5b-ab21-06c01681ef37)

# 3. admin

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

PENJELASAN:
function admin menangani tindakan yang ada untuk pengguna admin
meminta nama admin dan menampilkan menu dengan opsi crud(create,read,update,delete)

output:
menampilkan pesan selamat datang dan ada menu opsinya

contoh gambar:
![Screenshot (555)](https://github.com/user-attachments/assets/2dd99c58-35ea-46b6-9fbf-9f69acec4b87)


# 4. pelanggan

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

PENJELASAN:
function pelanggan membuat pelanggan bisa melihat dan memesan layanan
nampilkan menu dengan opsi untuk melihat dan memesan layanan atau keluar
pilihan yang dibuat akan memanggil function atau keluar dari loop

output:
memperlihatkan opsi layanan yang tersedia untuk pelanggan

contoh gambar:

![Screenshot (561)](https://github.com/user-attachments/assets/54c4eba8-55a9-4f17-a2bc-6f144d75e11c)

# 5. create

def create_servisan():
    no = str(len(table._rows) + 1)
    nama_servisan = input('masukan nama servisan: ')
    harga = input('masukan harga servisan: ')
    servisan (no, nama_servisan, harga)
    print ('layanan berhasil ditambahkan')
    lihat_servisan()

PENJELASAN output 
:menambahkan layanan baru ke tabel lalu memperlihatkan tabel yang sudah diperbarui

contoh gambar:
![Screenshot (556)](https://github.com/user-attachments/assets/04326697-31fc-4be5-802a-2a70866afd55)

# 6. read

def lihat_servisan():
    print(table)

PENJELASAN OUTPUT: 
memperlihatkan tabel

contoh gambar:
![Screenshot (557)](https://github.com/user-attachments/assets/03777715-d258-46a2-b260-4908cc432240)

# 7. update

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

PENJELASAN OUTPUT:
mengubah nama servisan yang ada didalam tabel

contoh gambar:
![Screenshot (558)](https://github.com/user-attachments/assets/8cb46c29-9422-452f-a295-86aad4f6b7ce)

# 8. delete

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

PENJELASAN OUTPUT:
menghapus salah satu daftar servisan

contoh gambar:

![Screenshot (566)](https://github.com/user-attachments/assets/5ace4fbc-15fd-436e-beeb-0d8bafe7b0d2)

# 9. pesan

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

PENJELASAN OUTPUT:
pelanggan bisa memesan layanan, kalau layanan ada maka pesanan dikonfirm, kalau tidak ada maka muncul "layanan tak ditemukan"
import time saya tambahkan agar proses servisan lebih terasa :)

contoh gambar:
![Screenshot (563)](https://github.com/user-attachments/assets/9823c03a-f64a-4a4c-9a66-92b41b0d2dc4)


penjelasan output secara menyeluruh:
saat di run, program dimulai dengan login
peran yang anda pilih memiliki fitur masing masing
admin bisa mengelola layanan 
pelanggan dapat melihat dan memesan layanan




  
