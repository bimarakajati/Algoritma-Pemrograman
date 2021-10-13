from Koordinat import *
def main():
    titik_c = Koordinat(4,5)
    titik_asal = Koordinat(0,0)
    print("titik c: x=",titik_c.x,"y=",titik_c.y)
    print("titik asal: x=",titik_asal.x,"y=",titik_asal.y)
    titik_c = -titik_c
    print("titik c: x=",titik_c.x,"y=",titik_c.y)
    titik_c.x = 12
    print("titik c: x=",titik_c.x,"y=",titik_c.y)
    print(titik_c)
    print(type(titik_c))
    print(isinstance(titik_c,Koordinat))
    print(titik_c.__dict__)
    print(titik_c.__doc__)
    print(titik_c.__module__)
    print(Koordinat.__name__) 
    print(Koordinat.__base__)
    print(Koordinat.__dict__)
    print(Koordinat.__doc__)
    print(Koordinat.__module__)
    del(titik_c)
    del(titik_asal)
    print(titik_c.__dict__) #error karena titik_c sudah di free memory
       
if __name__ == "__main__": 
    main()