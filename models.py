# models.py

"""Models module

Contains simplified representations of the structures in the Neo object. 
Provides methods for easy access to the information in the Neo object via 
the Controller for the user."""

class Model: 
    def __init__(self, neoobject):
        self.neoobject = neoobject
        self.blocks = []    
    
    def walk(self):
        # Get list of blocks
        self.blocks = self.neoobject.read(lazy=False, cascade=True)

    def getContents(self):
        contents = 'There are {} blocks in this Neo object'.format(len(self.blocks))
        return contents    
    

class Block(Model):
    def __init__(self):
        Model.__init__(self)
        self.segments = []
        self.recordingchannels = []

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def walk(self):
        pass

    def getContents(self):
        pass        


class Segment(Model):
        def __init__(self):
        pass


class RecordingChannel(Model):
    def __init__(self):
        pass

