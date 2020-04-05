def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(multiply())

def message(name, msg="Hello"):
    return msg + ' ' + name