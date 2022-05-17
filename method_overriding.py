class A:
    def show(self):
        print('From class A')
class B(A):
    def show(self):
        print('From class B')
a1 = B()
a1.show()