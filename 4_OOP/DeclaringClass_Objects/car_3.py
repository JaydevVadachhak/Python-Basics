class car:
    def __init__(self,a=40):
        self.set_speed(a)
    def get_speed(self):
        return self._speed
    def set_speed(self,a):
        if a<0 or a>160:
            print("speed is not valid:")
        else:
            self._speed = a
