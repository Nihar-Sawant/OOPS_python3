class Person:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
    
    def fullName(self):
        print(self.f_name+" "+self.l_name)
    
    def nameOnPaper(self):
        print(self.l_name+" "+self.f_name)
        
p1=Person("Nihar","Sawant")
p1.fullName()
p1.nameOnPaper()
p2=Person("Anup","Kulkarni")
p2.fullName()
p2.nameOnPaper()
  
    