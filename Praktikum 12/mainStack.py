from Stack import *

def main():
    print("Percobaan stack s1")
    s1 = Stack()
    s1.push(6)
    print(s1)
    s1.pop()
    s1.pop()
    print(s1)
    print("Percobaan stack s2")
    s2 = Stack([1,2,3,4,5])
    s2.push(6)
    print(s2)
    s2.pop()
    s2.pop()
    print(s2)

if __name__ == '__main__':
    main()