#input validation
#without the try block the program crashes with a ValueError error
#when you put a string in
print('howmany cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print('That is not that many cats.')
except ValueError: #catches the ValueError
    print('you did not enter a number')
    