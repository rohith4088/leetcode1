# import abc

# class MediaPlayer(metaclass = abc.ABCMeta):
#     @abc.abstractmethod
#     def play(self):
#         pass
#     @abc.abstractproperty
#     def ext(self):
#         pass
#     @classmethod
#     def __subclasshook__(cls, subclass: C):
#         if cls is MediaPlayer:
#             attrs = set(dir(C))
#             if set(cls.__abstractmethods__) <= attrs:
#                 return True
#         return NotImplemented


