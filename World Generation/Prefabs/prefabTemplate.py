import random as r

class platform():

    def __int__(self,height,distance,legnth,nextPlat):
        self._height = self.height
        self._distance = self.distance
        self._legnth = self.legnth
        self._nextPlat = self.nextPlat

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, newWord):
        self.height = newWord

    @property
    def distance(self):
        return self.distance

    @distance.setter
    def distance(self, newWord):
        self.distance = newWord

    @property
    def legnth(self):
        return self.legnth

    @legnth.setter
    def legnth(self, newWord):
        self.legnth = newWord

    @property
    def nextPlat(self):
        return self.previousPlat

    @nextPlat.setter
    def nextPlat(self, newWord):
        self.previousPlat = newWord


    def makePrefab(self, maxDist, maxHeight, type, maxLegnth, minLegnth):
        prefab = []
        prefab.append(platform(r.randint(1,2),r.randint(1,2), r.randint(maxLegnth,minLegnth), None))
        #If the type is verticle, create platforms going up eg.tree branches
        if type == "v":
            #Add platforms not too far away upwards until you reach the top
            while True:
                prefab.append(platform(r.randint))

        #If the type is horizontal;, create platforms groing across
        if type == "h":
