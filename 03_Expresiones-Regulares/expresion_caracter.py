import re

frase= "@tengo 2 hijos que tienn 15 y 11 anios de edad"
email = "joel.ap@hotmai.com.mx"
patron = '[a-z,A-Z,ñ,A-Z,0-9,a-z]+' # esta es una expresion regular
exp_final = re.findall(patron, frase)
print(re.findall(patron, email))
print(exp_final)
