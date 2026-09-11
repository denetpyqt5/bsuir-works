from random import shuffle
from input import ValidInput


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

        # Вертикальные соседи
        if line == 2:
            self.ready_to_move.extend([
                self.current_matrix[index - 3],
                self.current_matrix[index + 3]
            ])
        elif line == 1:
            self.ready_to_move.append(self.current_matrix[index + 3])
        else:
            self.ready_to_move.append(self.current_matrix[index - 3])

        # Горизонтальные соседи
        if (index + 1) % 3 == 0:
            self.ready_to_move.append(self.current_matrix[index - 1])
        elif (index + 2) % 3 == 0:
            self.ready_to_move.extend([
                self.current_matrix[index - 1],
                self.current_matrix[index + 1]
            ])
        else:
            self.ready_to_move.append(self.current_matrix[index + 1])

    def choose(self):
        print(self)
        data = int(input("Number to switch: "))
        self._move()
        if data in self.ready_to_move:
            temp = self.current_matrix.index(data)
            self.current_matrix[self.current_matrix.index(0)] = data
            self.current_matrix[temp] = 0


class UserInterface:
    def __init__(self, five: Fives):
        self.__five = five

    def __game_start(self):
        while not self.__five.__bool__():
            self.__five.choose()
        else:
            print("You win")

    def start_dialog(self):
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
