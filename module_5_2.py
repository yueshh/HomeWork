class House:
    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        for i in range(new_floor):
            f = i + 1
            if new_floor < self.number_of_floors:
                print(f)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return self.name

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print()
# __str__
print(h1)
print(h2)
print()
# __len__
print(len(h1))
print(len(h2))
