#Name: Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Subject - OSTL 
#Div: B

def bmi_index(h=6,w=70):
    return w/h**2
## Note - weight in kgs and height in meters
print('BMI Index:',bmi_index(7,68))
print('BMI Index:',bmi_index())
print('BMI Index:',bmi_index(w=70,h=8))