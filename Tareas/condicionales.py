
name = "Joel"
age = 29
address = "Jerez"

resume = "New person in python course, his name is: "

if (age >= 18 & age <=30):
    if (name != ""):
        resume += name
        if address != "":
            resume += "and your address is:"
            resume += address
        else:
            print("your address is missing!")
    else:
        print("Add a name")

print(resume)

def subjects_results(subject, value):
    if (value >= 0 & value <= 10):
        if (value <= 6):
            print("Sorry, you don't approve the {} subject".format(subject))
        elif(value >=6):
            print("Congratulations, you approve the {} subject".format(subject))
    else:
        print("Your qualification have an error")

subjects_results("Math",3)
subjects_results("English",7)
subjects_results("History",8)

def passTotheClub(age):
    if (age >= 18):
        print("Congratulations, Come in to our club")
    elif(age <18):
        print("Sorry you can't come in, you're so young!")

passTotheClub(13)
passTotheClub(23)
passTotheClub(28)

def got_to_travel(amount):
    if(amount > 34 and amount < 55):
        print("you can use our tour #C")
    elif(amount > 56 and amount < 75):
        print("you can use our tour #B")
    elif(amount > 76 and amount < 100):
        print("you can use our tour #A")
    else:
        print("sorry you cannot coiver any tour")

got_to_travel(23)
got_to_travel(39)
got_to_travel(62)
got_to_travel(88)

def multiplos(numero):
    if numero % 2 == 0 and numero % 4 != 0:
        print(f"{numero} es múltiplo de dos")
    elif numero % 2 == 0:
        print(f"{numero} es múltiplo de cuatro y de dos")
    else:
        print(f"{numero} no es múltiplo de dos")

multiplos(2)
multiplos(23)
multiplos(7)
multiplos(9)
multiplos(16)

