
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