class Cat():
    name = None
    age = None
    color = None

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def Display(self):
        print("***", self.name, "***")
        print("Age : ", self.age)
        print("Color : ", self.color)
        print('''\033[35m 
(\___/)
(=*.*+)
U-----U \033[0m
''')
