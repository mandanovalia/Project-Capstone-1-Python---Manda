print("Selamat Datang di Rental Mobil ABC")

semuaMobil = {
    'dictMobil1' : {
        'kode' : 'H1',
        'brand' : 'Honda',
        'tipe' : 'Brio',
        'tahun' : '2015',
        'status' : 'tersewa'
    },
    'dictMobil2' : {
        'kode' : 'M1',
        'brand' : 'Mitsubishi',
        'tipe' : 'Xpander',
        'tahun' : '2021',
        'status' : 'tersedia'
    },
    'dictMobil3' : {
        'kode' : 'T1',
        'brand' : 'Toyota',
        'tipe' : 'Avanza',
        'tahun' : '2019',
        'status' : 'tersedia'
    },
    'dictMobil4' : {
        'kode' : 'T2',
        'brand' : 'Toyota',
        'tipe' : 'Rush',
        'tahun' : '2021',
        'status' : 'tersewa'
    },
    'dictMobil5' : {
        'kode' : 'H2',
        'brand' : 'Honda',
        'tipe' : 'Civic',
        'tahun' : '2017',
        'status' : 'teredia'
    }
}

#LIST MOBIL
def rincian():
    print(semuaMobil['dictMobil1']),
    print(semuaMobil['dictMobil2']),
    print(semuaMobil['dictMobil3']),
    print(semuaMobil['dictMobil4']),
    print(semuaMobil['dictMobil5'])

#LIST DATA TERTENTU
def info():
    print('List kode kendaraan : H1, H2, T1, T2, M1')
    while(True):
        inputKode = input('Masukkan kode kendaraan : ')
        if inputKode.upper() == 'H1':
            print('data tersedia')
            print(semuaMobil['dictMobil1'])
            break
        elif inputKode.upper() == 'H2':
            print('data tersedia')
            print(semuaMobil['dictMobil5'])
            break
        elif inputKode.upper() == 'T1':
            print('data tersedia')
            print(semuaMobil['dictMobil3'])
            break
        elif inputKode.upper() == 'T2':
            print('data tersedia')
            print(semuaMobil['dictMobil4'])
            break
        elif inputKode.upper() == 'M1':
            print('data tersedia')
            print(semuaMobil['dictMobil2'])
        else :
            print('Data tidak tersedia. Silakan ulangi')

            
#SUBLIST DARI MENU READ DATA
def sublist():
    while(True):
        print('----------Sub Menu Read Data----------'),
        print('1. Semua Data Mobil'),
        print('2. Data Mobil Tertentu'),
        print('3. Kembali Ke Menu Utama')
        subMenu = input('Masukkan submenu: ')
        if subMenu == '1':
            rincian()
        elif subMenu == '2':
            info()
        elif subMenu == '3' :
            menu()
        else :
            print('Data salah. masukkan yang lain')

#MENAMBAH DATA
def addData():
    isExistKode=False
    while(True):
        if isExistKode!=True:
            kodeBaru = input('Masukkan Kode Kendaraan = ')
            for key, val in semuaMobil.items():
                if kodeBaru.upper() in val.values():
                    print("Data sudah ada")
                    isExistKode=False 
                    break #karena data udah ketemu. jd gak perlu loop semua data lain. langsung ke while loop lg.
                else:
                    isExistKode=True

        else:
            break
    brandBaru = input('Masukkan brand : ')
    tipeBaru = input('Masukkan tipe : ')
    tahunBaru = input('Masukkan tahun baru : ')
    statusBaru = input('Masukkan status baru : ')

    askSave = input('Apakah anda akan menyimpan data (Y/N) : ')
    if askSave.upper() == 'Y':
        print('Data sudah tersimpan')
    else :
        print('Data tidak disimpan. Kembali ke menu utama')
        menu()

    index=len(semuaMobil);
    print(str(index+1))
    indexDict=str(index+1)
    semuaMobil['dictMobil'+indexDict] = {} 

    semuaMobil['dictMobil'+indexDict]['kode'] = kodeBaru
    semuaMobil['dictMobil'+indexDict]['brand'] = brandBaru
    semuaMobil['dictMobil'+indexDict]['tipe'] = tipeBaru
    semuaMobil['dictMobil'+indexDict]['tahun'] = tahunBaru
    semuaMobil['dictMobil'+indexDict]['status'] = statusBaru
    print("\nAfter adding dictionary Dict1")
    print(semuaMobil)
    menu()


#MENAMBAH DATA
def tambah():
    while(True):
        print('----------Sub Menu Tambah Data----------'),
        print('1. Tambah Data Mobil'),
        print('2. Kembali Ke Menu Utama')
        tambahData = input('Masukkan submenu tambah data : ')
        if tambahData == '1':
            addData()
            break
        elif tambahData == '2':
            menu()
            break
        else:
            print('Menu tidak ada. Silakan pilih yang lain')
            
#UPDATE DATA
def updateData():
    isExistKode=False
    while(True):
        if isExistKode!=True:
            kodeBaru = input('Masukkan Kode Kendaraan  yang ingin anda Update= ')
            for key, val in semuaMobil.items():
                if kodeBaru.upper() in val.values():
                     kodeBaru = input('Masukkan kode : ')
                     brandBaru = input('Masukkan brand : ')
                     tipeBaru = input('Masukkan tipe : ')
                     tahunBaru = input('Masukkan tahun : ')
                     statusBaru = input('Masukkan status : ')
                     print('Data terupdate')
                     semuaMobil[key] = {'kode': kodeBaru, 'brand': brandBaru, 'tipe':tipeBaru, 'tahun':tahunBaru, 'status':statusBaru}
                     isExistKode=True
                     break
                else:
                    print("Data tidak ada")
                    isExistKode=False

        else:
            break

    menu()

def hapusData():
    isExistKode=False
    while(True):
        if isExistKode!=True:
            kodeBaru = input('Masukkan Kode Kendaraan  yang ingin anda hapus= ')
            for key, val in semuaMobil.items():
                if kodeBaru.upper() in val.values():
                    del semuaMobil[key]
                    print('Data {} sudah terhapus'.format(kodeBaru))
                    isExistKode=True
                    break
                else:
                    print("Data tidak ada")
                    isExistKode=False

        else:
            break

    menu()

       
#FUNGSI MENU UTAMA 
def menu():
    while(True):
        print('--------------Menu Utama-----------------')
        print('1. List Semua Mobil'),
        print('2. Menambahkan Data Mobil'),
        print('3. Mengubah Data Mobil'),
        print('4. Menghapus Data Mobil'),
        print('5. Keluar')
        menuUtama = input("Silakan pilih menu berikut [1-5] : ")
        if menuUtama == '1':
            sublist()
            break
        elif menuUtama == '2':
            tambah()
            break
        elif menuUtama == '3':
            updateData()
            break
        elif menuUtama == '4':
            hapusData()
            break
        elif menuUtama == '5':
            print('Sampai Jumpa Lagi')
            break
        else :
            print('Menu yang anda masukkan salah. Masukkan lagi')
       

menu()

