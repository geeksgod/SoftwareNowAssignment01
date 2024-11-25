def print_hollow_triangle(size):
    """This function prints the hollow traingle based on the sie input provided by the user"""
    for i in range(size):
        for j in range(size):
            #Condition to detect the border cordinates of the square
            if(j == 0 or i == size-1 or j == i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
size = int(input("Enter the size of the square: "))
print_hollow_triangle(size=size)