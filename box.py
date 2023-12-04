#  from the Debugging section

"""
***************
*             *
*             *
*             *
***************

"""

def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('"symbol" needs to be a string of length 1')
    if  (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2')
    
    print(symbol * width) # top of box

    for i in range(height - 2): # sides of box
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)  # bottom of box

boxPrint('*', 15, 5)  #call the function

boxPrint('O', 5, 16)

boxPrint('*', 1, 1)  # unintended behavior to be detected

boxPrint('**', 15, 5)  # unintended behavior to be detected



