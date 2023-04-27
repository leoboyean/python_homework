msjStart1 = " Hola que tal vienvenido!"
msjStart2 = " heaqui algunas funciones"
msjError = "Valor inesperado!"

def printer(something = "test to print something"):
    print(something)

def rangoToN(n):
    for i in range(0,n):
        printer(i)

def rangoToSteps(n):
    for i in range(0,n,3):
        printer(i)

def rangeInverse(n):
    for i in reversed(n):
        printer(i)
        
            
def roc(value):
    if type(value) == int:
        if 1:
            rangoToN(10)
        elif 2:
            rangoToSteps(323)
        elif 3:
            rangeInverse(123)
    else:
        printer('the value inserted isn\'t valid')
        
def initializer():
    printer("Hello, welcome to the series program!")
    printer("there are some series that you can check:")
    
#Series collection
def fibonacci(size):
    if (size>=1):
        printer(msjStart1 + str(size) + msjStart2)
        currMemory = 0
        lastElemnt = 1
        for i in range(0, size):
            print("elemento ", currMemory)
            aux  = currMemory + lastElemnt
            lastElemnt = currMemory
            currMemory = aux
    else:
        printer("El elemento {} {}".format(str(size), msjError))        


initializer()
printer()
printer("Hola, como estan?, estamos en el mismo metodo")
rangoToN(23)
rangeInverse("joel")
fibonacci(9)
roc("a")
roc(2)
