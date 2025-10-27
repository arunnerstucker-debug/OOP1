class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
    def add_values_to_customer(self):
        self.cid = input("Input the CID: ")
        self.cname = input("Input the Cname: ")
        self.acc_no = input("Input the account number: ")
        self.phone = input("Input the phone number: ")
        self.emailID = input("Input the emailID: ")
        self.balance = float(input("Input the customer balance as a float: "))
    def debit_from(self, quantity):
        self.balance -= quantity
    def credit_to(self, quantity):
        self.balance += quantity
    def display_cust_info(self):
        print("CID: ", self.cid)
        print("Cname", self.cname)
        print("Account number: ", self.acc_no)
        print("Phone Number: ", self.phone)
        print("email Id: ", self.emailID)
        print("Account Balance: ", self.balance)

#main code
customers = []

customers.append(Customer())
customers[0].add_values_to_customer()


customers.append(Customer())
customers[1].add_values_to_customer()

transfer = int(input("Input the amount of money that you would like to transfer: "))
i = int(input("What is the cid of the customer transferring the money: "))
n = int(input("What is the cid of the customer receiving the money: "))

customers[i-1].debit_from(transfer)
customers[n-1].credit_to(transfer)

customers[0].display_cust_info()
customers[1].display_cust_info()