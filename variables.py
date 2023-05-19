#example of local variable behavior in global scope
spam():
    eggs = 99 #local value to the spam() function

spam()
print(eggs) #this will error because the eggs variable is destroyed after the 
                #spam() function is run
