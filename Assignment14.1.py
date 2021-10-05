
def gcd(a ,b):

    if b== 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b > a:
    a, b = b, a

gcd_of_num = gcd(a, b)

print("GCD is ", gcd_of_num)
