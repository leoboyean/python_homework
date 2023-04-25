# Operador - SUMA
print()
print()
print('****---Operador suma  + --------******** ')

a = 10 + 3
print(a,type(a))    # 13 <class 'int'>
a = 5.5 + 5
b = 3j
c = a + b
print(a, type(a))   #  10.5 <class 'float'>
print(c, type(c))   #  (10.5+3j) <class 'complex'>
print(5+3)          #  8

print('-----------------------------------------------------------------------------------------------')

### Operador - RESTA

print('****---Operador RESTA  "-" --------******** ')

a = 12 - 2.5
print(a,type(a) )           # 9.5 <class 'float'>
a = 5.323           
b = 3.23J
c = a - b
print(c,type(c))            # (5.323-3.23j) <class 'complex'>
print(5-6, type(5-6))       # -1 <class 'int'>

print('-----------------------------------------------------------------------------------------------')

### Operador MULTIPLICACION*.

print('****---Operador MULTIPLICACION  "*" --------******** ')


a = 7 * 4
print(a)        #28
a = 8.5
b = 3
c = a * b
print(c)        #25.5
print(8*7)      #56


print('-----------------------------------------------------------------------------------------------')

### Operador DIVISION/.

print('****---Operador DIVISION  "/" --------******** ')


a = 6 / 2
print(a)
a = 5
b = 3
c = a / b
print(c)
print(10/3)

print('-----------------------------------------------------------------------------------------------')


### Operador MODULO%.

print('****---Operador MODULO  "%" --------******** ')



a = 8 % 4
print(a)
a = 9
b = 2
c = a % b
print(c)
print(6%3)

print('-----------------------------------------------------------------------------------------------')

print('****---Operador POTENCIA  "**" --------******** ')

### Operador **.


a = 3 ** 3
print(a)
a = 2
b = 4
c = a ** b
print(c)
print(4**3)

print('-----------------------------------------------------------------------------------------------')

###  ********   Expresiones relacionales  *******


### Operador <.

print('****---Operador MENOR QUE  "<" --------******** ')

a = 3 < 3
print(a)
a = 2
b = 4
c = a < b
print(c)
print(4<3)

print('-----------------------------------------------------------------------------------------------')


### Operador >.

print('****---Operador MAYOR QUE  ">" --------******** ')

a = 4 > 2
print(a)
a = 5
b = 7
c = a > b
print(c)
print(9>2)

print('-----------------------------------------------------------------------------------------------')


### Operador ==.
print('****---Operador "IGUAL A  "==" --------******** ')

a = 5 == 5
print(a)
a = 6
b = 9
c = a == b
print(c)
print(6==2)

print('-----------------------------------------------------------------------------------------------')


### Operador   !=.

print('****---Operador " DIFERENTE QUE "!=" --------******** ')


a = 4 != 2
print(a)
a = 5
b = 3
c = a != b
print(c)
print(8!=8)

print('-----------------------------------------------------------------------------------------------')


### Operador <=.

print('****---Operador "MENOR O IGUAL QUE "<=" --------******** ')



a = 5 <= 3
print(a)
x = 7
y = 5
z = x <= y
print(z)
print(9<=4)

print('-----------------------------------------------------------------------------------------------')

### Operador >=.

print('****------Operador "MAYOR O IGUAL QUE ">=" --------******** ')


a = 2 >= 8
print(a)
a = 3
b = 4
c = a >= b
print(c)
print(7>=3)

print('-----------------------------------------------------------------------------------------------')


## Expresiones lógicas.


### Operador and.

print('****-------Operador "AND" --------******** ')


print(4-1==3 and 5>6)
print(6+7 > 11 and 3==3)

print('-----------------------------------------------------------------------------------------------')


### Operador or.

print('****-------Operador "OR" --------******** ')



print(4-1==3 or 5>6)
print(6+7 > 11 or 3==3)

print('-----------------------------------------------------------------------------------------------')

### Operador not.



print('****-------Operador "NOT" --------******** ')


print(not 5.5>6)
print(not 5>4)

print('-----------------------------------------------------------------------------------------------')

## Expresiones de carácter

import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(patron, frase)