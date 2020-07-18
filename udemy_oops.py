class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    def volume(self):
        self.volume=3.14*(self.radius)**2*self.height
        print(self.volume)
    def surface_area(self):
        self.area=2*3.14*(self.radius)*(self.height)
        print(self.area)
