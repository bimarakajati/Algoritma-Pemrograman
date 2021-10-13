# Bima Rakajati
# A11.2020.13088
# 4214
# Kasus 3 - Meneruskan fungsi sebagai argument untuk fungsi yang lain

def kapital(text):
    return text.upper()

def kecil(text):
    return text.lower()

def greet(func, text):
    # menyimpan fungsi di dalam variabel
    greeting = func(text)
    print(greeting)

def main():
    teks = input() # string
    greet(kapital, teks)
    greet(kecil, teks)

if __name__ == '__main__':
    main()