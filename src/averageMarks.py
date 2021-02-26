print("Average marks calculator")

phy=int(input("Enter marks for Physics :"))
che=int(input("Enter marks for Chemistry :"))
maths=int(input("Enter marks for Maths :"))

avg = (phy + che + maths)/3

print("Average marks :{}".format(avg)) 
if(avg>=80):
    print("Eligible with distinction!")
elif(avg >= 35):
    print("Eligible")
else:
    print("Not eligible)