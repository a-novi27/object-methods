class House:

    def __init__(self):
        self.number = 10

house = House

house.numberOfFloors = 10

while house.numberOfFloors > 10:
    house.numberOfFloors *= 1

print('Текущий этаж равен ', house.numberOfFloors)









