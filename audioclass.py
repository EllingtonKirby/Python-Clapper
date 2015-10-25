import pyaudio
import wave

                
class AudioPlayer:

    def __init__(self, file):
        self.__openFile = wave.open(file, 'r')
        self.__ins = pyaudio.PyAudio()
        self.__stream = self.__ins.open(format = self.__ins.get_format_from_width(self.__openFile.getsampwidth()),
                                        channels = self.__openFile.getnchannels(),
                                        rate = self.__openFile.getframerate(),
                                        output = True)
                                        

    def play(self):
        
        data = self.__openFile.readframes(55)
        while data != '':
            self.__stream.write(data)
            data = self.__openFile.readframes(55)

    def close(self):
        self.__stream.close()
        self.__ins.terminate()
