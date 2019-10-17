import sys

def fibanocci (num):
    if num <= 1:
        return num
    else:
        return (fibanocci(num-1) + fibanocci(num-2))

count = int(len(sys.argv))
if(count != 2):
    print("Usage: {0} <num>".format(sys.argv[0]))
    exit(-1)

num = int(sys.argv[1])

if num < 1:
    print("Input a number greater than or equal to 1")

for i in range(0, num):
    print(fibanocci(i))
