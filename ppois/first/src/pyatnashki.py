import random
from input import ValidInput


# Пятнашки

class Fives:
    """A 3x3 sliding puzzle board.

    The board is stored as a flat list of nine integers. The value ``0``
    represents the empty cell. The target configuration is
    ``[1, 2, 3, 4, 5, 6, 7, 8, 0]``.
    """

    def __init__(self):
        """Create a shuffled board.

        Initializes the target and current configurations and shuffles
        the current one by performing 100 random valid moves.
        """
        self.correct_matrix = [x for x in range(1, 9)] + [0]
        self.current_matrix = [x for x in range(9)]

        self.random_spread()

    def __str__(self):
        """Return a printable 3x3 representation of the board.

        :return: three rows of three tiles separated by newlines
        """
        return f"{self.current_matrix[0:3]} \n{self.current_matrix[3:6]} \n{self.current_matrix[6:9]}"

    def __bool__(self):
        """Return whether the puzzle is solved.

        :return: ``True`` if the current configuration equals the
            target configuration, ``False`` otherwise
        """
        return True if self.current_matrix == self.correct_matrix else False

    def _move(self) -> list:
        """Return the tiles adjacent to the empty cell.

        Determines the row of the empty cell and collects the values
        that can legally be swapped into it (up to four neighbors).

        :return: list of tile values adjacent to the empty cell
        """
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
        """Move the tile with the given value into the empty cell.

        Does nothing if ``data`` is not adjacent to the empty cell.

        :param data: value of the tile to move
        """
        ready_to_move = self._move()
        if data in ready_to_move:
            temp = self.current_matrix.index(data)
            self.current_matrix[self.current_matrix.index(0)] = data
            self.current_matrix[temp] = 0

    def random_spread(self):
        """Shuffle the board by making random valid moves.

        Performs 100 random moves, which produces a reachable
        (solvable) configuration.
        """
        for _ in range(100):
            ready_to_move = self._move()
            info = random.choice(ready_to_move)
            self.choose(info)


class UserInterface:
    """Dialog-based interface for playing the 3x3 sliding puzzle.

    Wraps a :class:`Fives` instance and drives the game loop, reading
    the player's moves from standard input.
    """

    def __init__(self, five: Fives):
        """Create the interface for the given puzzle.

        :param five: the puzzle instance to play on
        """
        self.__five = five

    def __game_start(self):
        """Run the main game loop until the puzzle is solved.

        Prints the board, asks the player for a tile to move, and
        applies the move. Repeats until :meth:`Fives.__bool__` returns
        ``True``, then prints a win message.
        """
        while not self.__five.__bool__():
            print(self.__five.__str__())
            data = ValidInput().valid_int_input(1, 9, "Enter number to switch: ")
            self.__five.choose(data)
        else:
            print("You win")

    def start_dialog(self):
        """Show the start menu and run or exit the game.

        Option ``1`` starts the game; any other valid option exits.
        """
        print("Game 'Fives' 3x3")
        print("1.Start game\n2.Exit")
        info = ValidInput().valid_int_input(1, 2, "Choose number: ")
        if info == 1:
            self.__game_start()
        else:
            return


if __name__ == "__main__":
    game = Fives()
    interface = UserInterface(game)
    interface.start_dialog()
