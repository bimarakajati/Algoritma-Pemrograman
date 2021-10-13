'''
Bima Rakajati
A11.2020.13088
'''

import random # import random diperlukan untuk membangkitkan nilai acak dari state

# deklarasi variabel global dictGameSaving
global dictGameSaving
# inisialisasi variabel global dictGameSaving sebagai dictionary
dictGameSaving = {}

def saveGame(key,stateValue):
   # merupakan prosedur untuk save game state
   # key adalah kunci bertipe string
   # stateValue adalah vektor atau list dari state
   global dictGameSaving
   if key in dictGameSaving : #jika keynya sama
        h = input("apakah datanya mau ditumpuk (Y/T):")
        if h == "Y" :
            dictGameSaving[key]=stateValue
            lihatGameState()
   else :
      dictGameSaving[key]=stateValue 
      lihatGameState() 
   
def lihatGameState():
   # ambil global variabel
   global dictGameSaving
   # outputkan global variable
   print(dictGameSaving)

def loadGame(key):
   global dictGameSaving
   if key in dictGameSaving:
      return dictGameSaving[key]
   else:
      return 0

def main():
   n = input("apakah mau menyimpan state (Y/T)?")
   while(n != "T"):
      state = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
      k = input("masukkan kunci:")
      saveGame(k,state)
      n = input("apakah mau menyimpan state lagi (Y/T)?")
      if n == "T":
         break
   
if __name__ == "__main__":
   main()
