#global variables can be accessed in a function
def spam():
    global eggs #you can assigned a global statement to a local variable
    eggs = 'Hello'
    print(eggs) #use the global variable

eggs = 42 #globally defined variable
print(eggs)

spam() #call the function