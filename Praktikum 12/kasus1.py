# Bima Rakajati
# A11.2020.13088

def main():
 stack = [1,2,3,4,5]
 stack.append(6) # Bawah -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (Atas)
 print(stack)
 stack.pop() # Bawah -> 1 -> 2 -> 3 -> 4 -> 5 (Atas)
 stack.pop() # Bawah -> 1 -> 2 -> 3 -> 4 (Atas)
 print(stack)

if __name__ == '__main__':
 main()