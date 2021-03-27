from pygame import mixer

def musica(musicFile, volume):
    mixer.init()
    mixer.music.set_volume(volume)
    mixer.music.load(musicFile)
    mixer.music.play()