from input import ValidInput

# Нормальные алгоритмы Маркова


class Alphabet:
    def __init__(self, *args,**kwargs):
        self._symbols: list = [*args]
        super().__init__(**kwargs)


class Rules:
    def __init__(self, **kwargs):
        self._rules: dict = kwargs
        super().__init__()


class MarkovNormalAlgorithms(Alphabet, Rules):
    def __init__(self, state: str, *args, **kwargs):
        self.state = state + '\n'
        super().__init__(*args,**kwargs)

    def __str__(self) -> str:
        return (f"state: {self.state[:-1]},"
                f" alphabet of algorithm: {self._symbols},"
                f" rules: {self._rules}")

    def _change(self, i: int):
        try:
            result = list(self.state)
            result[i] = self._rules[self.state[i]]
            self.state = ''.join(result)
            print(self.state[:-1])
            return self.state
        except Exception:
            return False

    def change_state(self):
        print("Menu:\n1. Add data\n2. New data")
        choose = ValidInput.valid_int_input(self, 1, 2, "Choose option: ")
        new = input("Input data: ")
        self.state = self.state[:-1] + new +'\n' if choose == 1 else new + '\n'

    def convert(self):
        i = 0
        while self.state[i] != '\n':
            if not MarkovNormalAlgorithms._change(self, i):
                i += 1


class UserInterface:
    def __init__(self, algorithm: MarkovNormalAlgorithms):
        self.__algorithm = algorithm

    def __str__(self):
        return self.__algorithm.__str__()

    def start_dialog(self):
        while True:
            print("""Choose option:
1. convert state into final form
2. change state
3  check info
4. exit""")
            choose = ValidInput.valid_int_input(self, 1, 4, "Choose number: ")
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
    print(MarkovNormalAlgorithms.__mro__)
    interface = UserInterface(alg)
    interface.start_dialog()
