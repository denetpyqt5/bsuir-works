import random
from random import shuffle
from input import ValidInput


# Пятнашки

class Fives:
    def __init__(self):
        self.correct_matrix = [x for x in range(1,9)] + [0]
        self.current_matrix = [x for x in range(9)]

        self.random_spread()

    def __str__(self):
        return f"{self.current_matrix[0:3]} \n{self.current_matrix[3:6]} \n{self.current_matrix[6:9]}"

    def __bool__(self):
        return True if self.current_matrix == self.correct_matrix else False

    def _move(self) -> list:
        index = self.current_matrix.index(0)
        line = 1 if index < 3 else 2 if index < 6 else 3

        ready_to_move = []

        # Вертикальные соседи
        if line == 2:
            ready_to_move.extend([
                self.current_matrix[index - 3],
                self.current_matrix[index + 3]
            ])
        elif line == 1:
            ready_to_move.append(self.current_matrix[index + 3])
        else:
            ready_to_move.append(self.current_matrix[index - 3])

        # Горизонтальные соседи
        if (index + 1) % 3 == 0:
            ready_to_move.append(self.current_matrix[index - 1])
        elif (index + 2) % 3 == 0:
            ready_to_move.extend([
                self.current_matrix[index - 1],
                self.current_matrix[index + 1]
            ])
        else:
            ready_to_move.append(self.current_matrix[index + 1])
        return ready_to_move

    def choose(self, data: int):
        ready_to_move = self._move()
        if data in ready_to_move:
            temp = self.current_matrix.index(data)
            self.current_matrix[self.current_matrix.index(0)] = data
            self.current_matrix[temp] = 0

    def random_spread(self):
        for _ in range(100):
            ready_to_move = self._move()
            info = random.choice(ready_to_move)
            self.choose(info)


class UserInterface:
    def __init__(self, five: Fives):
        self.__five = five

    def __game_start(self):
        while not self.__five.__bool__():
            print(self.__five.__str__())
            data = ValidInput.valid_int_input(self, 1, 9, "Enter number to switch: ")
            self.__five.choose(data)
        else:
            print("You win")

    def start_dialog(self):
        print("Game 'Fives' 3x3")
        print("1.Start game\n2.Exit")
        info = ValidInput.valid_int_input(self, 1, 2, "Choose number: ")
        if info == 1:
            self.__game_start()
        else:
            return


if __name__ == "__main__":
    game = Fives()
    interface = UserInterface(game)
    interface.start_dialog()

