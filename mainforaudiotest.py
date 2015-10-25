import audioclass

def main():
    a = audioclass.AudioPlayer("facebook.wav")
    a.play()
    a.close()


main()
