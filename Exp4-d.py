# NAME :- TAUSIF KHAN
# ROLL. NO :- 12
# CLASS :- SE COMPS B

x = [int(x)for x in input(" Enter the elements of list ").split()]
y = int(input("Enter any one number "))
flag = 0
for i in x:
	if(i == y):
		flag =1;
if(flag ==1):
	print("Entered number is present in the list ")
else:
	print("Entered number is not present in the list ")

# Output:

# C:\Users\Tausif khan\Desktop\OSTL>python Exp4-d.py
#  Enter the elements of list 45 78 98 34 23
# Enter any one number 45
# Entered number is present in the list

# C:\Users\Tausif khan\Desktop\OSTL>python Exp4-d.py
#  Enter the elements of list 45 78 98 34 23
# Enter any one number 38
# Entered number is not present in the list