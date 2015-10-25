import pyaudio
import wave

class recorder:

    def __init__(self, seconds, file):
        self.__nFrames = 1000
        self.__channels = 1
        self.__rate = 44100
        self.__recordingTime = seconds
        self.__fileToWrite = file
        self.__format = pyaudio.paInt24
        self.__ins = pyaudio.PyAudio()
        self.__stream = self.__ins.open(format = self.__format,
                                        channels = self.__channels,
                                        rate = self.__rate,
                                        input = True,
                                        frames_per_buffer = self.__nFrames)
        
        
    def record(self):
        print("RECORDING")

        frames = []
        for i in range(0, int(self.__rate / self.__nFrames * self.__recordingTime)):
            data = self.__stream.read(self.__nFrames)
            frames.append(data)

        print("done recording")

        #closes and terminates stream
        self.__stream.stop_stream()
        self.__stream.close()
        self.__ins.terminate()

        #writes to the file
        a = wave.open(self.__fileToWrite, 'w')
        a.setnchannels(self.__channels)
        a.setsampwidth(self.__ins.get_sample_size(self.__format))
        a.setframerate(self.__rate)
        a.writeframes(b''.join(frames))
        a.close()
