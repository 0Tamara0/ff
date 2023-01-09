''''
class Car:
    model = "q"
    year = 129
    def start(self):
        print("start")
    def stop(self):
        print("stop")
q1 = Car()
q1.start()
q1.stop()
'''

class ST:
    av_q = 0
    def __init__(self, name, math, rus, eng):
        self.__name = name
        self.__math = math
        self.__rus = rus
        self.__eng = eng
    def getinf(self):
        print("name", self.name)
        print("math", self.math)
        print("rus", self.rus)
        print("eng", self.eng)
q1 = ST("q", 8,10,9)
q1.getinf()

q2 = ST("w",9,6,7)
q2.getinf()
'''
class An:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def ien(self):
      print("a", self.a)
      print("b", self.b)
      print("c", self.c)
    def rt(self):
        print("Run")
    def ry(self):
        print("stop")
q1 = An("Dog",7,13)
q1.ien()
q1.rt()
q1.ry()
'''
