import pickle

class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = []
    def add_values_to_customer(self):
        self.cid = input("Input the CID: ")
        self.cname = input("Input the Cname: ")
        self.acc_no = input("Input the account number: ")
        self.phone = input("Input the phone number: ")
        self.emailID = input("Input the emailID: ")
        self.balance = float(input("Input the customer balance as a float: "))
        self.debit_card = ""
    def add_payment_method(self,type , cardID, balance):
        if type == "credit" or type == "Credit":
            self.credit_card.append(cardID)
            self.balance +=  balance
        elif type == "debit" or type == "Debit":
            self.debit_card.append(cardID)
            self.balance += balance
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

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0.0
    def add_values_to_card(self):
        self.type = input("Input the card type: ")
        self.card_no = input("Input the Card number: ")
        self.cvv = input('Input the cvv: ')
        self.expiry_date = input("Input the expiration date: ")
        self.balance = float(input("Input the card balance: "))
    def spend_money(self, money):
        self.balance -= money
    def receive_money(self, money):
        self.balance += money
    def display_card_info(self):
        print("Type: ", self.type)
        print("Card number", self.card_no)
        print("CVV: ", self.cvv)
        print("Expiration Date: ", self.expiry_date)
        print("Card Balance: ", self.balance)


#main code
customers = []
cards = []

i = 0
n = 0
while 1:
    option = input("choose one of the following:\n"
                   "1. create a customer object:\n"
                   "2. create a card object:\n"
                   "3. Transfer funds between customer objects:\n"
                   "4. Assign card objects to customer objects:\n"
                   "5. Display customer info:\n"
                   "6. Display card info:\n"
                   "7. commit:\n"
                   "8. exit")
    if option == '1':
        customers.append(Customer())
        customers[i].add_values_to_customer()
        i += 1
    elif option == '2':
        cards.append(Card())
        cards[n].add_values_to_card()
        n += 1
    elif option == '3':
        transfer = int(input("Input the amount of money that you would like to transfer: "))
        x4 = int(input("What is the cid of the customer transferring the money: "))
        y4 = int(input("What is the card number that you wish to use: "))
        x5 = int(input("What is the cid of the customer receiving the money: "))
        y5 = int(input("What is the card number you wish to receive the money to? "))

        customers[x4].debit_from(transfer)
        cards[y4].spend_money(transfer)
        customers[x5].credit_to(transfer)
        cards[y5].receive_money(transfer)
    elif option == '4':
        x2 = int(input("Enter the ID of the customer you wish to assign the card object to: "))
        y2 = int(input("Enter the card number you wish to add: "))
        customers[x2].add_payment_method(cards[y2].type, cards[y2].card_no, cards[y2].balance)
    elif option == '5':
        x3 = int(input('Enter the ID of the customer you wish to display: '))
        customers[x3].display_cust_info()
    elif option == '6':
        y3 = int(input('Enter the ID of the card you wish to display: '))
        cards[y3].display_card_info()
    elif option == '7':
        index1 = 0
        index2 = 0
        with open("customers.dat", "ab") as file1:
            for x in customers:
                pickle.dump(customers[index1], file1)
                index1 += 1
            for y in cards:
                pickle.dump(cards[index2], file1)
                index2 += 1
        file1.close()
    elif option == '8':
        break
    else:
        print("Error: Invalid Input. Please try again.")