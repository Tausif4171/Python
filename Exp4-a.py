# NAME :- TAUSIF KHAN
# ROLL. NO :- 12
# CLASS :- SE COMPS B

x = int(input("Enter the starting value "))
y = int(input("Enter the ending value "))
for i in range(x,y):
	if(i%3==0 and i%5==0):
		print("Fizz Bizz")
	elif(i%3==0):
		print("Fizz")
	elif(i%5==0):
		print("Bizz")
	else:
		print(i)

#Output:

#C:\Users\Tausif khan\Desktop\OSTL>python Exp4-a.py
# Enter the starting value 1
# Enter the ending value 50
# 1
# 2
# Fizz
# 4
# Bizz
# Fizz
# 7
# 8
# Fizz
# Bizz
# 11
# Fizz
# 13
# 14
# Fizz Bizz
# 16
# 17
# Fizz
# 19
# Bizz
# Fizz
# 22
# 23
# Fizz
# Bizz
# 26
# Fizz
# 28
# 29
# Fizz Bizz
# 31
# 32
# Fizz
# 34
# Bizz
# Fizz
# 37
# 38
# Fizz
# Bizz
# 41
# Fizz
# 43
# 44
# Fizz Bizz
# 46
# 47
# Fizz
# 49