class Vector:
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self):
        return f"x1:{self.x1}, y1:{self.y1}, x2:{self.x2}, y2:{self.y2}"

if __name__ == "__main__":
    a = Vector(2,3,1,0)
    print(a)