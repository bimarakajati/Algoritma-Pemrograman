import pustaka

# entry point dengan prosedur main
def main():
    A = [10,2,5,33,27]
    # p=len(A)
    print('A =',A)
    c=int(input('Data yang ingin dicari : '))
    print(c, 'pada A = ', pustaka.BinarySearch((pustaka.InsertionSortA(len(A),A)),c))

# panggil entry point
if __name__ == '__main__':
    main()