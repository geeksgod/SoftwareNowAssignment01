#adding the user input numbers
sum=0.0
data=input("Enter a number or just enter to quit ")
while data != "":
 number=float(data)
 sum=sum+number
 data=input("enter a number or just enter to quit ")
print("the sum is", sum)

