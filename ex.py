import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = [el for el in range(int(math.sqrt(self.x**2 + self.y**2)+1))]

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,a):
        self.__x = a
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,a):
        self.__y = a
        


    def vectors_len(self):
        return len(self.vector)
    def rationing_vector(self):
        return self.x/self.vectors_len(),self.y/self.vectors_len()

    def __gt__(self, other):
        return self.vectors_len() > other.vectors_len()
    def __lt__(self, other):
        return self.vectors_len() < other.vectors_len()
    def __add__(self, other):
        return (other.x + self.x , other.y + self.y)
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return (self.x *other.x + self.y * other.y)
