def print_hollow_square(size):
    """This function prints the hollow square based on the input size provided by the user"""
    for i in range(size):
        for j in range(size):
            #Condition to detect the border cordinates of the square
            if(i == 0 or i == size-1 or j == 0 or j == size-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()





size = int(input("Enter the size of the square(press 0 to exit): "))
while(size != 0):
    print_hollow_square(size=size)
    size = int(input("\nEnter the size of the square(press 0 to exit): "))

