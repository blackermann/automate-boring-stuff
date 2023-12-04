# logging example
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  #disable the logging

logging.debug('start of program')
# buggy factorial program
def factorial(n):
    logging.debug('start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n+1):  #range begins at 0 if just given one argument
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('end of program')