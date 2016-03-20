# Abstract base class

class BaseNeo(object):

    def __init__(self, obj=None):
        self.obj = obj

    def descend_one_level(self):
        pass

    def get_contents(self):
        pass

    
