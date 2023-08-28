class BankAccount:
    def get(self,cname, balance):
        self.cname=cname
        self.balance = balance
        print("heloo enter your name",self.cname)
        print("account balancde is :",self.balance)
    def credit(self,cno, amount):
        self.cno=cno
        self.amount= amount
        print("card number is ",self.cno,"card balance is ",self.amount)
    def debit(self,cno, amount):
        self.cno=cno
        self.amount=amount
        print("card name ",self.cno,"dabit balance is",self.amount)
    def report_problem(self,tranproblem,accountpb):
        self.tranproblem=tranproblem
        self.accountpb=accountpb
        print("enter your acproblem ",tranproblem,"your accountpb is",accountpb)   
    def call(self,phone_number):
        self.phone_number=phone_number
        print("enter number",phone_number,)
        
b1=BankAccount()
b1.get(" Divya",23000)

while True:
        print("*"*50)
        print("1 to credit")
        print("2 to debit")
        print("3 to report_problem")
        print("4 to call")
        print("5 to exit")
        print("*"*50)
         
        choice =int(input("Enter your choice: "))
        print("*"*50)
        
        if choice==1:
           cno=int(input("Please enter the cno: "))
           amount=int(input(" enter your amount:"))
           b1.credit(cno,amount)
           print("*"*50)

        elif choice==2:
          cno=int(input("enter number :"))
          amount=int(input("enter amunt:"))
          b1.debit(cno,amount)
          print("*"*50)
            
        elif choice==3:
          tranproblem=int(input("enter your problem :"))
          accountpb=int(input("enter your problem :"))
          b1.report_problem(tranproblem,accountpb)
          print("*"*50)
          
        elif choice==4:
           phone_number=int(input("enter your number"))
           b1.call(phone_number)
           print("*"*50)
            
        elif choice ==5:
            print("Thank you ,good  bye!")
            print("*"*50)
            break

        else:
            print("Invalid choice. Please try again.")
            print("*"*50)




