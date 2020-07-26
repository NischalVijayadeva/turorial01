class Car:
    def __init__(self,model, year, price,color):
        self.model = model
        self.year = year
        self.price = price
        self.color = color

    def start(self):
        self.ignision = "ON"
        print("{} Car started!! \n".format(self.model))

    def move(self, direction):
        self.direction = direction
        print("{} Car moving in the direction of  {} ".format(self.model,direction))
    
    def stop(self):
        self.ignision = "Off"
        print("{} Car Stopped!!".format(self.model))


