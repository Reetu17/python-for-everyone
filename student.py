class student(object): 
    def __init__(self): 
        self.name = "reetu"
        print("student") 
  
class Qualification(object): 
    def __init__(self): 
        self.address = "BTech"        
        print("Qualification") 
  
class Derived(student, Qualification): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        student.__init__(self) 
        Qualification.__init__(self) 
        print("address") 
          
    def printStrs(self): 
        print(self.name, self.address) 
         
  
ob = Derived() 
ob.printStrs() 