### Ejercicios

#1. Declare an empty list
emptyList = []*3        #
print(emptyList)

#2. Declare a list with more than 5 items
myList = ["hola",2023,True,["class"],'workspace',29,0]
print(len(myList))
#3. Find the length of your list
#4. Get the first item, the middle item and the last item of the list
sizeList = len(myList)
if(sizeList >= 3) :
    first, second, *rest = myList
    last = myList[len(myList)-1]
    print("First item {}, my second item is {} and my last item is> ".format( first,  second, last))
elif(sizeList == 2):
    print("This list doesn't have more than two element!")
elif(sizeList == 1):
    print("This list doesn't have more than one element!")
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Joel Aparicio", 29, 1.83, "single", "jerez, zacatecas, Mx"]
'''
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.'''
#7. Print the list using _print()_
print(["Hola", "mis amigos", "del curso de python"])
'''
8. Print the number of companies in the list'''

for i in myList:
    print(i)
'''9. Print the first, middle and last company
10. Print the list after modifying one of the companies .
11. Add an IT company to it_companies'''
#12. Insert an IT company in the middle of the companies list
#mid =len(mixed_data_types)/2
#mixed_data_types.append(mid,"Apple")

'''
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list'''
mixed_data_types.clear()
'''
25. Destroy the IT companies list
26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
