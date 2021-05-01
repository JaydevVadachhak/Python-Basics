class person:
    counter = 0
    def __init__(self,a='Jay',b='20'):
        self.name = a
        self.gender = b
        person.counter = person.counter + 1
    def ShowInfo(self):
        print('Name:',self.name)
        print('gender:',self.gender)
    @classmethod
    def ShowCount(cls):
        print("No of objects so far:",cls.counter)
