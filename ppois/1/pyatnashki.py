import random


# Пятнашки

class Fives:
    def __init__(self):
        self.correct_matrix = [x for x in range(1,10)]
        self.current_matrix = [x for x in range(1,10)]
        random.shuffle(self.current_matrix)

    def __str__(self):
        return f"{self.current_matrix[0:3]} \n{self.current_matrix[3:6]} \n{self.current_matrix[6:9]}"

    def __bool__(self):
        return True if self.current_matrix == self.correct_matrix else False

if __name__ == "__main__":
    game = Fives()
    print(game)
