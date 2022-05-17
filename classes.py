class computer:
    def __init__(self):
        self.name = 'uday'
        self.age = 20
    def compare(self, other):
        if c1.age == other.age:
            return True
        else:
            return False
c1 = computer()
c1.age = 20
c2 = computer()
if c1.compare(c2):
    print("they are same")
else:
    print('they are different')


