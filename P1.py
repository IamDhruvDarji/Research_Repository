class Book:
    quantity = None
    price = None
    publication_name = None

    def __init__(self, quantity, price, publication_name):
        self.quantity = quantity
        self.price = price
        self.publication_name = publication_name

    def displayData(self):
        print("*** BOOK ***")
        print("The quantity is : ", self.quantity)
        print("The price is : ", self.price)
        print("Publication name is : ", self.publication_name)


# B1 = Book()
# B1.displayData()
B2 = Book(1, 100.00, "John")
B2.displayData()
