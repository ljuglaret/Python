class Complexe : 
    def __init__(self,r,im):
        self._r = r
        self._im = im


    def _get_r(self):
        return self._r

    def _get_im(self):
        return self._im


    def __add__(self,other) : 
        return Complexe(self.r + other.r, self.im + other.im)

    def __sub__(self,other) : 
            return Complexe(self.r - other.r, self.im - other.im)

    def aff(self) : 
        if (self.im < 0) : 
            print(str(self.r) + "" + str(self.im ) + "i")
        else : 
            print(str(self.r) + " + " + str(self.im ) + "i")


    r  =  property(_get_r)
    im =  property(_get_im)

c1 = Complexe(4,5)
c2 = Complexe(2,-3)
c2.aff()