from MyList import *

def main():
    objList = SLinkedList() # bikin head
    n1 = Node(20) # node 1, lsg dgn dataval = 20
    objList.headval = n1 # mengarahkan pointer head ke n1
    n2 = Node(10) # bikin n2, lsg dgn dataval = 10
    n3 = Node() # bikin n3, dataval masih None, akan diisi
    n3.dataval = 100 # ngisi node n3
    n4 = Node(5) # bikin node n4, isinya 5
    # pastikan sebelum meng-assign nextval,
    # node objeknya dibuat terlebih dahulu
    n1.nextval = n2
    n2.nextval = n3
    n3.nextval = n4
    
    objList.listprint()
    print()
    objList.listprintbyIndex(1)
    objList.listprintbyIndex(2)
    objList.listprintbyIndex(3)

if __name__ == '__main__':
    main()