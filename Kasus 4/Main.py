from Mylib import * 

n = int(input('Masukkan Kapasitas Barang: ')) 
arr_ID = [int]*n 
arr_Barang = [str]*n 
arr_Harga = [int]*n 

menu = '1' 

while menu != '0': 
    print('''Kapasitas Barang: 
    Pilih Menu (Ketik 1/2/3 dan 0 untuk keluar)
    1. Input Data
    2. Lihat Data
    3. Lihat Data Terurut''')

    menu = input('Pilih opsi yang diinginkan: ') 
    if menu == '1': 
        for i in range(n): 
            print('Data ke-',i+1) 
            arr_ID[i] = int(input('Masukkan Id barang: ')) 
            arr_Barang[i] = input('Nama Barang: ') 
            arr_Harga[i] = int(input('Harga Barang: ')) 
        InputData(arr_ID, arr_Barang, arr_Harga, n) 
    elif menu == '2': 
        LihatData(arr_ID, arr_Barang, arr_Harga, n) 
    elif menu == '3':
        LihatDataSort(arr_ID, arr_Barang, arr_Harga, n) 
    elif menu == '0': 
        break