
#Name:  Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Div: B
#Course Name: Open Source Technology Lab (OSTL) 

#1.A Python program to create a dictionary from keyboard and display the elements.
x={}
print("Enter how many elements u need in Dictionary: ")
n=int(input()) #n indicates no. of key-value pairs

for i in range(n):
    print('Enter key: ',end='')
    k=input() #key is string
    print('Enter its value: ',end='')
    v=int(input()) #value is integer
    x.update({k:v}) #store the key-value pair in dictionary x
#display the dictionary   
print('Final Dictionary: ',x)

#Output:
    
#Enter how many elements u need in Dictionary: 2
#Enter key: Tausif
#Enter its value: 12
#Enter key: Parth
#Enter its value: 6
#Final Dictionary:  {'Tausif': 12, 'Parth': 6}

#2. A Python program to convert the elements of two lists into key-value pairs of a dictionary.

countries=['India','USA']
cities=['New Delhi','Washigthon']
z=zip(countries,cities)
d=dict(z)
#print(d)
print('{:10s} -- {:10s}'.format('COUNTRY','CAPITAL'))
for k in d:
    print('{:10s} -- {:10s}'.format(k,d[k]))

#Output:

#COUNTRY    -- CAPITAL   
#India      -- New Delhi 
#USA        -- Washigthon

#3. A Python program to convert a string into key-value pairs and store them into a dictionary.
    
#converting string into dictionary
str="Apple=12,Banana=13,Mango=14,Grapes=15"
#break the string at ',' and then at '='
#store the pieces into a list lst
lst=[]
for x in str.split(','):
    y=x.split('=')
    lst.append(y)
#convert the list into dictionary 'd'
#but this 'd' will have both name and Rollno as strings
d=dict(lst)
#print(d)
#create a new dictionary 'd1' with name as string
#and age as integer
d1={}
for k,v in d.items():
    d1[k]=int(v)
#print dictionary
print(d1)

#Output:

#{'Apple': 12, 'Banana': 13, 'Mango': 14, 'Grapes': 15}
    
