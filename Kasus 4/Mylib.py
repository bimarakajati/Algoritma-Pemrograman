ar_ID = [] 
ar_Barang = [] 
ar_Harga = [] 

def InputData(arr_id, arr_items, arr_price, n): 
    for i in range(n):
        ar_ID.append(arr_id[i]) 
        ar_Barang.append(arr_items[i]) 
        ar_Harga.append(arr_price[i]) 
        
def LihatData(arr_id, arr_items, arr_price, n): 
    print('Id | Barang | Harga ') 
    for i in range(n): 
        print(ar_ID[i], '|', ar_Barang[i], '|', ar_Harga[i]) 
        
def LihatDataSort(arr_id, arr_items, arr_price, n): 
    # Ascending 
    temp_id = 0 
    temp_items = '' 
    temp_price = 0 
    for i in range(1, n): 
        temp_id = ar_ID[i] 
        temp_items = ar_Barang[i] 
        temp_price = ar_Harga[i] 
        j = i - 1 
        while j >= 0 and temp_id < ar_ID[j]: 
            ar_ID[j + 1] = ar_ID[j] 
            ar_Barang[j + 1] = ar_Barang[j] 
            ar_Harga[j + 1] = ar_Harga[j] 
            j = j - 1 
        ar_ID[j + 1] = temp_id 
        ar_Barang[j + 1] = temp_items 
        ar_Harga[j + 1] = temp_price 
    print('Id | Barang | Harga ') 
    for i in range(n): 
        print(ar_ID[i], '|', ar_Barang[i], '|', ar_Harga[i])