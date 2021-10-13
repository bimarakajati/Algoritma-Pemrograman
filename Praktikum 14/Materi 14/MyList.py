class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def listprintbyIndex(self, index):
        printval = self.headval
        count = 0
        while printval is not None:
            if index == count:
                print(printval.dataval)
                break
            printval = printval.nextval
            count +=1
        if printval is None:
            printval('Index diluar batas')

    def append(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None: # jika kosong
            self.headval = NewNode
            return # kalau return berhenti
        lastelm = self.headval
        while(lastelm.nextval is not None): # jika isi
            lastelm = lastelm.nextval
        lastelm.nextval = NewNode

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval # merupakan variabel untuk menyimpan data apapun nilainya nanti
        self.nextval = None # merupakan pointer yang akan menunjuk ke node yang lain