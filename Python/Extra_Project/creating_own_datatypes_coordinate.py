
class Coordinate_Geometry:
    
    def __init__(self,p1,p2):
        self.abscissa=p1
        self.ordinate=p2
        
    def __str__(self):
        return (f"({self.abscissa},{self.ordinate})")
    
    def slope(self,other):
        if(self.abscissa-other.abscissa)==0:
            return "Indeterminate Answer"
        else:
           self.m=(self.ordinate-other.ordinate)/(self.abscissa-other.abscissa)
           return self.m
    def distance(self,other):
        self.dist=((self.abscissa-other.abscissa)**2+(self.ordinate-other.ordinate)**2)**0.5
        return self.dist
         
    def eqn(self,other):
        print(self.m)
        self.constant=self.abscissa*self.m+self.ordinate
        if(self.constant >0):
            return (f"{self.m}x-y+{self.constant}=0")
        elif(self.constant <0):
             return (f"{self.m}x-y{self.constant}=0")
        else:
            return (f"{self.m}x-y=0")
x=Coordinate_Geometry(10,5)
y=Coordinate_Geometry(5,7)
print(x)
print(y)
print("Slope:",x.slope(y))
print("Distance:",x.distance(y))
print("Equation:",x.eqn(y))

