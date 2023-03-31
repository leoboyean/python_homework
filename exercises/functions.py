msjError = " es un número inválido para la serie!"
msjStart1 = "Los "
msjStart2 = " elementos de la serie de Fibonacci son:"

def fibonacci(size):
    if (size>=1):
        message(msjStart1 + str(size) + msjStart2)
        currMemory = 0
        lastElemnt = 1
        for i in range(0, size):
            print("elemento ", currMemory)
            aux  = currMemory + lastElemnt
            lastElemnt = currMemory
            currMemory = aux
    else:
        message("El elemento "+str(size) + msjError)


def message(msg):
    if msg!="" :
        print(msg)        




fibonacci(-9)

