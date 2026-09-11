from random import shuffle


# Пятнашки

class Fives:
    def __init__(self):
        self.correct_matrix = [x for x in range(9)]
        self.current_matrix = [x for x in range(9)]
        self.ready_to_move = []
        shuffle(self.current_matrix)

    def __str__(self):
        return f"{self.current_matrix[0:3]} \n{self.current_matrix[3:6]} \n{self.current_matrix[6:9]}"

    def __bool__(self):
        return True if self.current_matrix == self.correct_matrix else False

    def _move(self):
        index = self.current_matrix.index(0)
        line = 1 if index < 3 else 2 if index < 6 else 3

        self.ready_to_move.extend([self.current_matrix[index - 3], self.current_matrix[index + 3]] if line == 2 else
                                  [self.current_matrix[index + 3]] if line == 1 else
                                  [self.current_matrix[index - 3]])

        self.ready_to_move.extend([self.current_matrix[index - 1]] if (index + 1) % 3 == 0 else
                                  [self.current_matrix[index - 1], self.current_matrix[index + 1]] if (
                                                                                                                  index + 2) % 3 == 0 else
                                  [self.current_matrix[index + 1]])

    def _choose(self):
        print(self)
        data = int(input("Number to switch: "))
        self._move()
        if data in self.ready_to_move:
            temp = self.current_matrix.index(data)
            self.current_matrix[self.current_matrix.index(0)] = data
            self.current_matrix[temp] = 0

    def game_start(self):
        while not self.__bool__():
            self._choose()
        else:
            print("You win")


if __name__ == "__main__":
    game = Fives()
    game.game_start()
