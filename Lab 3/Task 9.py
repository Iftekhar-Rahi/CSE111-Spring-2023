class Patient:
    def __init__(self,name,age,w,h):
        self.name=name
        self.age=age
        self.w=w
        self.h=h
        self.bmi=self.w/((self.h/100)*(self.h/100))
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.w} kg")
        print(f"Height: {self.h} cm")
        print(f"BMI: {self.bmi}")
p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()
