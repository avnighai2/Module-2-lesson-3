# Swapping three values
a = int(input("enter the first number"))
b = int(input("enter the third number"))
c = int(input("enter the third number"))

print("Before swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping the values
a, b, c = c, a, b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)