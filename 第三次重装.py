class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f%"


Bed = HouseItem("席梦思", 4)
print(Bed)
