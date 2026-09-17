from input import ValidInput


# Нормальные алгоритмы Маркова


class Alphabet:
    """Stores the alphabet of a normal Markov algorithm.

        The alphabet is the set of symbols that may appear in the state
        string and in the substitution rules.

        :param args: alphabet symbols passed positionally
        """

    def __init__(self, *args, **kwargs):
        """Initialize the alphabet with the given symbols.

        :param args: alphabet symbols
        :param kwargs: extra arguments forwarded to ``super()``
        """
        self._symbols: list = [*args]
        super().__init__(**kwargs)


class Rules:
    """Stores the substitution rules of a normal Markov algorithm.

    Each rule is a pair ``symbol -> replacement``. The dict key is the
    symbol to look for in the state string, and the value is what it
    is replaced with.
    """
    def __init__(self, **kwargs):
        self._rules: dict = kwargs
        super().__init__()


class MarkovNormalAlgorithms(Alphabet, Rules):
    """Normal Markov algorithms.

    This module implements a normal Markov algorithm: an alphabet,
    a set of substitution rules, the string transformation itself,
    and a simple dialog-based user interface.

    Example::

        alg = MarkovNormalAlgorithms("DABCCBCCD", "A", "B", "C",
                                     A="B", B="C", C="@@", D="S")
        UserInterface(alg).start_dialog()
    """
    def __init__(self, state: str, *args, **kwargs):
        """Create an algorithm with the given initial state.

        :param state: initial state string
        :param args: alphabet symbols (positional)
        :param kwargs: substitution rules in the form ``symbol=replacement``
        """
        self.state = state + '\n'
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        """Return a human-readable representation of the algorithm.

        :return: a string with the current state, alphabet, and rules
        """
        return (f"state: {self.state[:-1]},"
                f" alphabet of algorithm: {self._symbols},"
                f" rules: {self._rules}")

    def _change(self, i: int):
        """Apply a rule to the symbol at position ``i``.

        If a rule exists for ``self.state[i]``, replace the symbol and
        return the new state. If there is no rule, or the position is
        out of range, return ``False``.

        :param i: index of the symbol in the state string
        :return: the new state (``str``) or ``False`` if the
            substitution failed
        """
        try:
            result = list(self.state)
            result[i] = self._rules[self.state[i]]
            self.state = ''.join(result)
            print(self.state[:-1])
            return self.state
        except Exception:
            return False

    def change_state(self):
        """Change the current state through a dialog with the user.

        Asks whether to append data to the current state or replace
        it entirely, then reads the new string.
        """
        print("Menu:\n1. Add data\n2. New data")
        choose = ValidInput().valid_int_input(1, 2, "Choose option: ")
        new = input("Input data: ")
        self.state = self.state[:-1] + new + '\n' if choose == 1 else new + '\n'

    def convert(self):
        """Apply the rules for as long as possible.

        Walks the state string from left to right. If a rule exists for
        the current symbol, it is applied and the position stays the
        same (so that cascading substitutions can be handled). If no
        rule exists, the position moves one symbol to the right.

        Stops when the terminating ``'\\n'`` character is reached.
        """
        i = 0
        while self.state[i] != '\n':
            if not self._change(i):
                i += 1


class UserInterface:
    """Dialog-based interface for working with a Markov algorithm.

    Allows the user to run the conversion, change the state, and
    view the current information about the algorithm.
    """
    def __init__(self, algorithm: MarkovNormalAlgorithms):
        """Create an interface for the given algorithm.

        :param algorithm: an instance of a normal Markov algorithm
        """
        self.__algorithm = algorithm

    def __str__(self):
        """Return the string representation of the algorithm.

        :return: the result of the wrapped algorithm's ``__str__``
        """
        return self.__algorithm.__str__()

    def start_dialog(self):
        """Run the main user dialog loop.

        Shows a menu and handles the user's choice:

        * ``1`` — run the state conversion;
        * ``2`` — change the state;
        * ``3`` — show information about the algorithm;
        * ``4`` — exit the dialog.

        The loop also exits on any value outside ``[1, 4]``
        (see ``ValidInput``).
        """
        while True:
            print("""Choose option:
1. convert state into final form
2. change state
3  check info
4. exit""")
            choose = ValidInput().valid_int_input(1, 4, "Choose number: ")
            if choose == 1:
                self.__algorithm.convert()
            elif choose == 2:
                self.__algorithm.change_state()
            elif choose == 3:
                print(self)
            else:
                return


if __name__ == "__main__":
    alg = MarkovNormalAlgorithms("DABCCBCCD", "A", "B", "C", A="B", B="C", C="@@", D="S")
    interface = UserInterface(alg)
    print(interface.__doc__)
    interface.start_dialog()
