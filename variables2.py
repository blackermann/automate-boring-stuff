#example of using the same names for variables in different functions
def spam():
    eggs = 99
    bacon() #calls the bacon() function
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
