import random
print("Welcome to die roller , press enter to begin")
while(True):
    result=random.randint(1, 6)
    print("The die rolled: ", result)
    print("Want to scroll again?(yes/no)")
    n=input()
    if(n.lower()=="no"):
        print("Bye")
        break
