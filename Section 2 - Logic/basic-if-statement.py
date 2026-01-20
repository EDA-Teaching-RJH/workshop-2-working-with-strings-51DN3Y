def main():
    age = int(input("Enter Age: ")) 
    category(age)

def category(age):
    if age >= 18:
        print("You are an adult")
    elif age < 18:
        print("You are a child")
    else:
        return

main()