import abc

class MediaLoader(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

"""
class Wav(MediaLoader):
    pass
w = Wav()  

TypeError : Can't instantiate abstract class Wav with abstract methods
ext, play
"""

class Ogg(MediaLoader):
    ext = ".ogg"
    def play(self):
            pass
o = Ogg() 