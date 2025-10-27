import pickle
class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""
    def get_product_details(self):
        self.pid = input("Enter the PID: ")
        self.pname = input("Enter the product name: ")
        self.price = float(input("Enter the price: "))
        self.description = input("Enter a description of the product: ")
    def display_product_info(self):
        print("PID: ", self.pid)
        print("Product name: ", self.pname)
        print("Product Price: $", self.price)
        print("Product Description: ", self.description)


#Main Code
while 1:
    option = input("Choose one of the following:\n"
                   "1. Create a product object\n"
                   "2. get info for the project\n"
                   "3. display the product\n"
                   "4. write the product into a file\n"
                   "5. read from the file and display the product info\n"
                   "6. Exit: ")
    if option == '1':
        product_obj = Product()
    elif option == '2':
        product_obj.get_product_details()
    elif option == '3':
        product_obj.display_product_info()
    elif option == '4':
        f1 = open("product_inventory.dat", "ab")
        pickle.dump(product_obj, f1)
    elif option == '5':
        f2 = open("product_inventory.dat", "rb")
        while 1:
            try:
                recieved_product = pickle.load(f2)
                recieved_product.display_product_info()
                print(recieved_product.pname)
            except EOFError:
                break
    elif option == '6':
        break
    else:
        print("Error: Invalid Input")

