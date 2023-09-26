class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

    def data(self):
        print(f"So name of the vehicle is {self.name_of_vehicle}, max speed of it is {self.max_speed}, average speed of it is {self.average_of_vehicle}")

car = Vehicle("toyota", 100, 25)
car.data()