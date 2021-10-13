'''
Bima Rakajati
A11.2020.13088
'''

def pasanganNimNama(nim,nama):
   return nim,nama

def tukarNamaNim(tNimNama):
   nim = tNimNama[0]
   nama = tNimNama[1]
   (nim,nama) = (nama,nim)
   return (nim,nama)

def main():
   (nm,nam) = pasanganNimNama("A11.2020.13088","Bima Rakajati")
   print(nm," ",nam)
   (nm,nam) = tukarNamaNim((nm,nam))
   print(nm," ",nam)

if __name__ == "__main__":
   main()