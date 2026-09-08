# Нормальные алгоритмы Маркова

class Alphabet:
    def __init__(self,*args):
        self.symbols : list = [*args]

class Rules:
    def __init__(self,**kwargs):
        self.rules : dict = kwargs

class MarkovNormalAlgorithms(Alphabet,Rules):
    def __init__(self,state,*args,**kwargs):
        self.state = state
        Alphabet.__init__(self,*args)
        Rules.__init__(self,**kwargs)

    def __str__(self):
        return (f"initial state:{self.state},"
                f" alphabet of algorithm: {self.symbols},"
                f" rules: {self.rules}")

if __name__ == "__main__":
    alg = MarkovNormalAlgorithms("ABC","A","B","C",A = "B",B = "C", C = "@")
    print(alg)