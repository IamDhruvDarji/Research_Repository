RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


class Product():
    product_id: None
    name: None
    price: None
    quantity: None
    status: None

    # constructor
    def __init__(self, product_id, name,  price, quantity, status=True):
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.name = name
        self.__status = status

    def display(self):
        print("********** PRODUCT **********")
        print("ID:", self.product_id)
        print("Name: ", self.name)
        print("price: $", self.price)
        print("quantity: ", self.quantity)
        if self.__status:
            print(GREEN + "ACTIVE" + RESET)
        else:
            print(RED + "ARCHIVE" + RESET)

# cost calculation
    def cost(self):
        return self.price * self.quantity

    # getter
    def get_status(self):
        return self.__status

    # setter
    def set_status(self, new_value):
        self.__status = new_value


# test
p1 = Product(2001, "Peanut cookies", 5.99, 12)
p1.display()
# print(p1.__status)

# test 2
print("cost =", p1.cost())

# test 3
print("is active? ", p1.get_status())

# test 4
p1.set_status(False)
p1.display()
