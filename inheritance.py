class A:
    def featureA1(self):
        print('feature A1 is working')
    def featureA2(self):
        print('feature A2 is working')
class B:
    def featureB1(self):
        print('feature B1 is working')
    def featureB2(self):
        print('feature B2 is working')
class C(A,B):
    def featureC(self):
        print('feature C is working')
a1 = A()
a1.featureA1()
a1.featureA2()
b1 = B()
b1.
c1 = C()
