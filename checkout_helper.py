import random
import string

def calculateTotal(shoppingCart):
    total = 0.0
    for item in shoppingCart.products:
        total += item.quantity * float(item.product.price[1:])
    return total

def generateConfirmationNumber():
    return "".join(random.choice(string.ascii_uppercase + string.digits) \
        for x in xrange(16))
