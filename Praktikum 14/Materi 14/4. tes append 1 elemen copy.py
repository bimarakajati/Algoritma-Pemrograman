from MyList import *

def main():
    objList = SLinkedList() # bikin head
    n1 = Node(20) # node 1, lsg dgn dataval = 20
    objList.headval = n1 # mengarahkan pointer head ke n1
    objList.append('hihi')
    objList.append(True)
    objList.append(5.6)
    objList.listprint()

if __name__ == '__main__':
    main()