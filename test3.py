class A :
    def rk(self):
        print(" In class A")
    
class B(A):
    pass

class C():
    def rk(self):
        print(" In class C")

class D(B, C):
    pass

r = D()\

print(D.__mro__)