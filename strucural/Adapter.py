# Adapter pattern works as a bridge between two incompatible interfaces.
# This pattern involves a single class which is responsible to join functionalities
# of independent or incompatible interfaces.
#

from abc import ABC, abstractmethod

# Target interface
class Target(ABC):
    def __init__(self):
        self._adaptee = Adaptee()

    @abstractmethod
    def request(self):
        pass

class Adapter(Target):
    def request(self):
        self._adaptee.adaptee_request()

class Adaptee:
    def adaptee_request(self):
        print("Adaptee function called.")


## Client code
print("Adapter 1")
adapter = Adapter()
adapter.request()



class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audioType, fileName ):
        pass

class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def playVlc(self, filename):
        pass

    @abstractmethod
    def playMp4(self, filename):
        pass

class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self, filename):
        print("Playing vlc file:", filename)

    def playMp4(self, filename):
        print("not supported")

class Mp4Player(AdvancedMediaPlayer):
    def playVlc(self, filename):
        print("not supported")
    def playMp4(self, filename):
        print("Playing mp4 file: ", filename)

class MediaAdapter(MediaPlayer):
    def __init__(self, audiotype):
        if audiotype == 'vlc':
            self._advancedMediaPlayer = VlcPlayer()
        elif audiotype == 'mp4':
            self._advancedMediaPlayer = Mp4Player()

    def play(self, audioType, fileName):
        if audioType == 'vlc':
            self._advancedMediaPlayer.playVlc(fileName)
        elif(audioType == 'mp4'):
            self._advancedMediaPlayer.playMp4(fileName)

class AudioPlayer(MediaPlayer):
    def __init__(self):
        self._mediaPlayerVlc = MediaAdapter('vlc')
        self._mediaPlayerMp4 = MediaAdapter('mp4')

    def play(self, audioType, fileName):
        if audioType == 'mp3':
            print("internal MP3 feature fileName:", fileName)
        elif audioType == 'vlc':
            self._mediaPlayerVlc.play(audioType, fileName)
        elif audioType == 'mp4':
            self._mediaPlayerMp4.play(audioType, fileName)
        else:
            print("not supported: " + audioType)




#Cleint Code
print("Adapter 2")
adapter = AudioPlayer()
adapter.play("mp3", "some mp3")
adapter.play("vlc", "some mp4")