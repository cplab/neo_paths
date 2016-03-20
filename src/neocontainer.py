# neocontainer.py

class NeoContainer(NeoBase):
    
    def __init__(self, name=None, obj=None):
        super(NeoContainer, self).__init__(name=name, obj=obj)
        self.blocks = []

    def get_contents(self):
        self.blocks = self.neoobject.read(lazy=False, cascade=False)
        for b in self.blocks:
            print b.self.name
            yield b.get_contents()
