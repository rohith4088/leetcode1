#polymorphism at work
#In essence, a class method is a special type of method that is bound to the class itself, not to instances of that class. This means you can call it directly on the class (e.g., MyClass.my_class_method()) 
# without needing to create an object first.
class AudioFile:
    def __init__(self , filename):
        self.filename = filename

    def play(self):
        raise NotImplementedError("subclass must implement abstract method")
    @classmethod
    def get_ext(cls):
        raise NotImplementedError("subclass must implement abstract method")
class mp3(AudioFile):
    ext = "mp3"
    def play(self):
        print(f"Playing {self.filename} as MP3")
    @classmethod
    def get_ext(cls):
        return cls.ext
class wav(AudioFile):
    ext = "wav"
    def play(self):
        print(f"Playing {self.filename} as wav")
    @classmethod
    def get_ext(cls):
        return cls.ext

def get_audio_file(filename):
    for cls in AudioFile.__subclasses__():
        if filename.endswith(cls.get_ext()):
            return cls(filename)
    raise Exception("unsopported file format")


af = get_audio_file("rohith.wav")
af.play()
print(id(af))
