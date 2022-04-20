import os
# import winsound
    
def play_sound(sound_path: str):
    os.system(f'afplay {sound_path}&') # mac only - & at the end is for playing async
    # os.system(f'aplay {sound_path}&') # linux only
    # winsound.Playsound(sound_path, winsound.SND_ASYNC) # windows only