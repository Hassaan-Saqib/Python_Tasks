class R:
    def __init__(self,n,l):
        self.n=n
        self.l=l
    def print_(self):
        print(self.n,self.l)
x=R("Ali","Sham")
x.print_()

class H(R):
    def __init__(self,f,l):
        R.__init__(self,f,l)

h=H("zain","Ali")
h.print_()

class Student(R):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
x.graduationyear=2020
print(x.graduationyear)