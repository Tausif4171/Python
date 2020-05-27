#Name: Tausif Khan
#Rollno: 12
#Branch: SE/COMPS 
#Subject - OSTL 
#Div: B

class employee_sal():
    def __init__(self,basic):
        self.basic=basic
        

    def gross(self):
        gross=self.basic+self.basic*80/100+self.basic*15/100
        return gross
        
    def net(self):    
        net=self.basic+self.basic*80/100+self.basic*15/100-self.basic*10/100-self.basic*15/100
        return net
        
ins=employee_sal(10000)
print('Gross:',ins.gross())
print('Net:',ins.net())
