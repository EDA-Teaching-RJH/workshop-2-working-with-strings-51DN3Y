import math  

def main():
    A = float(input("Enter value A: "))  
    B = float(input("Enter value B: "))
    pythag(A,B)

def pythag(A,B):
    C = float(math.sqrt(A**2 + B**2))
    print(C)

main()
