import Pustaka

def main():
    a=[12,15,20,50,100]
    p=len(a)
    print('a =', a)
    c=int(input('data yg ingin dicari: '))
    print(c, 'pada a =', Pustaka.LinearSearchSentinel(c,p,a))    

if __name__ == '__main__':
    main()