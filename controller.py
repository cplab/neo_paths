# controller.py

"""Controller module

Receives the Neo object and manages the user interaction with the simplified
representation of the Neo object found in the Model class."""

from models import *

class Controller:

    def __init__(self, neoobject):
        self.neoobject = neoobject

    def getSummary(self):
        model = Model(self.neoobject)
        model.walk()
        return model.getContents()        

