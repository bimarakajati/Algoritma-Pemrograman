import Pustaka

def main():
    a=[5,2,10,27,33]
    # p=len(a)
    print('a =', a)
    c=int(input('data yg ingin dicari: '))
    print(c, 'pada a =', Pustaka.SequentialSearch(a,c))
    

if __name__ == '__main__':
    main()