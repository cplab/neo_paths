# neoblock.py

class NeoBlock(NeoContainer):

    def __init__(self, name=None, obj=obj):
        super(NeoBlock, self).__init__(name=name, obj=obj)

    def get_segments(self):
        for s in self.obj.segments:
            yield s.get_contents()

    def get_recordingchannelgroups(self):
        for r in self.obj.recordingchannelgroups:
            yield r.get_contents()

    def get_contents(self):
        self.get_segments()
        self.getrecordingchannelgroups()


