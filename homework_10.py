#34
from random import randint

class Godzila():

    def __init__(self, volume_of_stomach, full_stomach, stomach_limit):
        self.volume_of_stomach = volume_of_stomach
        self.full_stomach = full_stomach
        self.stomach_limit = stomach_limit

    def people_eating(self, food):
        full = 100
        fullness = (self.full_stomach + food) * full / self.volume_of_stomach
        if fullness < self.stomach_limit:
            self.full_stomach += food
            print("I eat :", food, "kg. The stomach is full on :", fullness, "%")
            return False
        else:
            print("Godzilla is full of %d kg and can no longer eat people. The stomach is full on : %d %%" % (self.full_stomach, self.stomach_limit))
            return True

if __name__ == '__main__':
    godzila = Godzila(1000, 0, 90)
    food = 0
    while godzila.people_eating(food) == False:
        food = randint(1, 120)



