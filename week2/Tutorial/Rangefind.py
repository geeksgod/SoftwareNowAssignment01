#while Loop and break statement
while True:
 number=int(input("Enter a number or just enter to quit: "))
 if number >=0 and number <=100:
    break
 else:
    print("not in range")
print(number)
