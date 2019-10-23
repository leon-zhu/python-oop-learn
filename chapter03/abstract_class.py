import abc


class MediaLoader(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


class Ogg(MediaLoader):
    def play(self):
        pass

    def ext(self):
        pass
