#example 1 - find maximum and minimum
first=int(input("enter the first number "))
second=int(input("enter the secomd number "))
if first>second:
 maximum=first
 minimum=second
else:
 maximum=second
 minimum=first
print("maximum",maximum)
print("minimum",minimum)
print("\n")
#example 2 - find maximum and minimum using built-in function
first=int(input("enter the first number "))
second=int(input("enter the secomd number "))
print("maximum",max(first,second))
print("minimum",min(first,second))