import sys

count = int(len(sys.argv))
if(count != 3):
    print("Usage: {0} <num1> <num2>".format(sys.argv[0]))
    exit(-1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 <= 0 or num2 <= 0:
    print("Please input positive integers")
    exit(-1)
gcd=min(num1, num2)

while gcd != 0:
    if num1%gcd == 0 and num2%gcd == 0:
        print("GCD of", num1,"and", num2, "is", gcd)
        exit(0)
    gcd = gcd - 1
