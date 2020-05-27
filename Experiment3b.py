#Name:  Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Div: B
#Course Name: Open Source Technology Lab (OSTL) 

#Write a menu driven program to demonstrate use of dictionary in python:
#1. Concatenate an item in the existing dictionary.
#2. Delete item of the existing dictionary.
#3. Retrieve all keys from a dictionary
#4. Retrieve all values from a dictionary
#5. Retrieve all key-value pairs from a dictionary
#6. Find a key and print its value.

dict={'Name':'Tausif','Rollno':12}
def mainMenu():
    selection=int(input("Enter choice"))
    if selection==1:
        concatenate()
    elif selection==2:
        pop()
    elif selection==3:
        keys()
    elif selection==4:
        values()
    elif selection==5:
        items()
    elif selection==6:
        setdefault()
    else:
        print("Enter a valid Selection")
        mainMenu()
def concatenate():
    dict1={"Div":'B'}
    print('Concatenate item to dictionary: ',dict.update(dict1))
    print(dict)
    
def pop():
    print('Delete item from dictionary: ',dict.pop('Name')) 
    print(dict)
    
def keys():
    print('keys in dictionary: ',dict.keys())
    
def values():
    print('Values in dictionary: ',dict.values())
    
def items():
    print('Print dictionary items: ',dict.items())
    
def setdefault():
    x = dict.setdefault("Name", "Mango")
    print('Value returned: ',x)


mainMenu()

#Output-

#Enter choice 1 
#Concatenate item to dictionary: None 
#{'Name': 'Tausif', 'Rollno': 12, 'Div': 'B'}
#Enter choice 2 
#Delete item from dictionary: Tausif 
#{'Rollno': 12}
#Enter choice 3 
#keys in dictionary: dict_keys(['Name', 'Rollno'])
#Enter choice 4 
#Values in dictionary: dict_values(['Tausif', 12])
#Enter choice 5 
#Print dictionary items: dict_items([('Name', 'Tausif'), ('Rollno', 12)]) 
#Enter choice 6 
#Value returned: Tausif

