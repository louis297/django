class A(object):
    def __init__(self):
        print('%d'%1)
        super(A,self).__init__()
        print("<%d>"%1)

class B(object):
    def __init__(self):
        print(2)
        super(B,self).__init__()
        print("<2>")

class C(A,B):
    def __init__(self):
        print(3)
        super(C,self).__init__()
        print('<3>')

C()
