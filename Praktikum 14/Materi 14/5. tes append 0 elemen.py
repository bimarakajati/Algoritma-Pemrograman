from MyList import *

def main():
    objList = SLinkedList() # bikin head
    n1 = Node(20) # node 1, lsg dgn dataval = 20
    objList.append('why')
    objList.append('I')
    objList.append('love')
    objList.append('programming!')
    objList.listprint()

if __name__ == '__main__':
    main()