import Listener
import audioclass
import recordclass

class controller1:

    def listening(self):
        if Listener.listen():
            return True
    def playA(self):
        a = audioclass.AudioPlayer("Facebook.wav")
        a.play()
    def playB(self):
        b = audioclass.AudioPlayer("Marvin Gaye.wav")
        b.play()
    def playC(self):
        c = audioclass.AudioPlayer("01 Track 01.wav")
        c.play()
    def recordit(self):
        d = recordclass.recorder(10,"RecordingOutput.wav")
        d.record()
    def playrecord(self):
        d2 = audioclass.AudioPlayer("RecordingOutput.wav")
        d2.play()
        
