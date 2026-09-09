# Нормальные алгоритмы Маркова

class Alphabet:
    def __init__(self, *args):
        self.symbols: list = [*args]


class Rules:
    def __init__(self, **kwargs):
        self.rules: dict = kwargs


class MarkovNormalAlgorithms(Alphabet, Rules):
    def __init__(self, state : str, *args, **kwargs):
        self.state = state + '\n'
        Alphabet.__init__(self, *args)
        Rules.__init__(self, **kwargs)

    def __str__(self):
        return (f"initial state:{self.state[:-1]},"
                f" alphabet of algorithm: {self.symbols},"
                f" rules: {self.rules}")

    def _change(self, i: int):
        try:
            result = list(self.state)
            result[i] = self.rules[self.state[i]]
            self.state = ''.join(result)
            print(self.state[:-1])
            return self.state
        except Exception:
            return False

    def convert(self):
        i = 0
        while self.state[i] != '\n':
            if not MarkovNormalAlgorithms._change(self, i):
                i += 1


if __name__ == "__main__":
    alg = MarkovNormalAlgorithms("DABCCBCCD", "A", "B", "C", A="B", B="C", C="@@", D="S")
    alg.convert()
    print(alg)