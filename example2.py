def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

# the values Alice and Bob are called arguments
# the variable name is called a parameter

def plusOne (number):
    return number + 1 #return value from the function

newNumber = plusOne(5)
print(newNumber)