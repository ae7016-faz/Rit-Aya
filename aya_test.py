#Aya El Fazazi ID: 433000484
"""
This determines the type of triangle it is based of the sides a, b, and c of the triangle.
"""
def Triangle_type_checker(side_a, side_b, side_c):
    #check if all three sides are equal
    if side_a == side_b == side_c:
        print("Equilateral")
    #check if only two sides are equal
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Isosceles")
    #check if all sides are inequeal
    else:
        print("Scalene")

"""
Now the user will input the variables a, b, c which are intigers
"""
def main():
    #get user input
    side_a = int(input("Enter side A of triangle: "))
    side_b = int(input("Enter side B of triangle: "))
    side_c = int(input("Enter side C of triangle: "))
#Call the check function
    triangle_type = Triangle_type_checker(side_a, side_b, side_c)
    print("Your triangle type is: ", triangle_type)
#run the program
main()


