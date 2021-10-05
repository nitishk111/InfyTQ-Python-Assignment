class Employee:
    def __init__(self,name,amm):
        self.Ename=name
        self.Bill_amm=amm
    def purchase(self):
        self.bill=Bill_amm-(Bill_amm*5/100)
    def pay_bill(self):
        #print(self.name+' pays bill amount of Rs. '+str(bill)
        pass



c1=Employee('Nitish',7835)
c1.purchase()
