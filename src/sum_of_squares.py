squares=[]
sum_squares=0

for i in range(1,100):
    squares.append(i**2)
    sum_squares = sum_squares + squares[i-1]

print("Sum of squares : ", sum_squares)
print("List of squares : ", squares)