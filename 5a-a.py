#Name: Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Subject - OSTL 
#Div: B

basic=int(input("Enter your basic salary: "))
def hras(basic):
    hra=basic*15/100
    return(hra)
def das(basic):
    da=basic*80/100
    return(da)
def taxs(basic):
    tax=basic*10/100
    return(tax)
def pfs(basic):
    pf=basic*15/100
    return(pf)
def gross(basic):
    gross=basic+das(basic)+hras(basic)
    return gross
def net(basic):    
    net=gross(basic)-taxs(basic)-pfs(basic)
    return net
print('The gross salary:',gross(basic))
print('The net salary:',net(basic))