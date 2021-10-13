class Koordinat(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def jarak(self,lain):
        x_jar = (self.x - lain.x)**2
        y_jar = (self.y - lain.y)**2
        return (x_jar+y_jar)**0.5 
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def __neg__(self):
        return Koordinat(-self.x,-self.y)
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")