def welcome(name):
    """ Print welcome """
    print(f"Hello {name}, welcome to the program!")
user = input("Please what is your name? ")
welcome(user)


def add(first, second):
    """ about to add two numbers """
    result = first + second
    return result

x = int(input("Enter first number to add: "))
y = int(input("Enter second number to add: "))

total = add(x, y)
print(total)

total = add(y, y)
