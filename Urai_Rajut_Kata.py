##### SOAL 3 - Mengurai dan Merajut Kata
# Buatlah sebuah file python yang berisi 2 buah return function, dengan 1 argumen yang dapat digunakan untuk mengurai & merajut sebuah string

# fungsi urai(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:

# # Function Initialization :
# def urai(...):
#     ......
 
# def rajut(...):
#     ......
    
    
# # Use the function
# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))

# # Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
# Sedangkan fungsi rajut(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. contoh output yang diharapkan adalah sebagai berikut:

# # Use the function
# print(rajut('CCoCodCode'))
# print(rajut('PPyPytPythPythoPython'))
# print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# # Output:
# Code
# Python
# Purwadhika


#############################################
# kata = "kode"

def urai(kata):
    hasil = ''
    a = len(kata)
    for i in range(a):
        for j in range(i+1): #menggunakan looping untuk mengambil index
            print(j)
            hasil += kata[j]  #setelah mengetahui index, dilihat isi data dalam index tersebut dan digabungkan kedalam string
    return hasil

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))


def rajut (kata):
    hasil = []
    panjangkata = len(kata)
    for i in range(50):
        loncat = int(i*(i+1)/2) #mengetahui urutan keberapa dari huruf yang akan diambil
        hasil.append(loncat) #urutan tersebut dimasukkan kedalam list, agar mudah mengetahui urutan index
        # print(hasil)
        if panjangkata in hasil:
            indexloncat = hasil.index(panjangkata) #mengetahui index keberapa hasil panjang kata tersebut
            # print(indexloncat)
            total = panjangkata - indexloncat #mengetahui index keberapa kata yang paling lengkap
            # print(total)
            return kata[(total):]

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))