try:
    age = int(input("Enter your age: "))
    if (age < 18):
        raise ValueError
except ValueError:
    print("You are too young")
def OddOrEven ():
    if age%2==0:
        print("Your age number is even")    
    else:
       print("Your age number is odd")    
   