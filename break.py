import logging

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.debug("program start.")

#logging.disable(logging.DEBUG)

for n in range(2, 10):
    for x in range(2, n):
        #x in range(2, 2) = None.
        logging.debug("x = {},n = {}" .format(x,n))
        if n % x == 0:
            logging.debug("n = {}, x = {}" .format(n, x))
            print(n, "equals", x, n//x)
            break
    else:
         print(n, "is prime number.")