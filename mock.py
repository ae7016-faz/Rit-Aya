def check_even_odd(a):
    if a % 2 == 0:
        print("Even")  
    else:
        print("Odd") 


def check_pos_neg(b):
    if b > 0:
        print("Positive") 
    else:
        print("Negative")

def square(c):
    total=0
    total = c ** 2
    print(total)

def cube(d):
    total1=0
    total1 = d ** 3
    print(total1)



def main():
    number = int(input("Enter a number: "))
    check_even_odd(number)
    check_pos_neg(number)
    square(number)
    cube(number)
    
main()