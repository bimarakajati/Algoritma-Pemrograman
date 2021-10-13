import pustaka

# entry point dengan prosedur main
def main():
    A=[2,5,10,27,33]
    # p=len(A)
    print('A =',A)
    c=int(input('Data yang ingin dicari : '))
    print(c, 'pada A = ', pustaka.BinarySearch(A,c))

# panggil entry point
if __name__ == '__main__':
    main()