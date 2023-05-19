#example of a mutable list getting modified by a function

#function that appends Hello to a list
def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3] #list
eggs(spam)  #pass the list into eggs function
print(spam)  #spam will show as changed

#references!