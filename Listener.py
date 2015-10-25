import pyaudio
import math
import struct

def rms(data):
    normalize = (1.0/32768.0)
    datalen = len(data)/2
    format = "%dh"%(datalen)
    #uses built in struct format types to create correct format
    samps = struct.unpack(format,data)
    sumsamps = 0.0
    for bit in samps:
        n = bit*normalize
        sumsamps+=n*n
    return math.sqrt(sumsamps/datalen)

def listen():
    initialThresh = .2
    Format = pyaudio.paInt16
    channels2 = 2
    Rate = 44100
    inputBlockTime = .05
    framesPblock = int(Rate * inputBlockTime)
    pa = pyaudio.PyAudio()
    streamit = pa.open(format = Format, channels = channels2, rate=Rate,
                       input=True,frames_per_buffer = framesPblock)
    for i in range(1000):
        try:
            take = streamit.read(framesPblock)
        except OSError:
            print("(%d) Error recording"%(errcount))
        amp = rms(take)
        if amp>initialThresh:
            print("Tap!")
            return True
        
#I would like to give credit to user Russel Borogove on StackOverflow for his
#"Detect tap with pyaudio from live mic"
#http://stackoverflow.com/questions/4160175/detect-tap-with-pyaudio-from-live-mic
#I created a simplified version of his listening device, eliminating the classes
#and modifying the threshold process
#I would also like to give credit to Hubert Pham and those that assisted him
#in creating the python program pyaudio, as without pyaudio this project would
#have been impossible. He also posted several extremely helpful examples
            
