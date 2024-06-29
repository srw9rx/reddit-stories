from gtts import gTTS
import datetime

def text_to_speech(text:str, path:str):
    '''
    :param text:str: the story we are converting to speech
    :param path:str: the folder where the story is being saved
    :return: the file path that will be used to get the mp3 to overlay on video
    '''
    tts = gTTS(text)
    time = datetime.datetime.now().strftime('%d-%m-%Y%H:%M:%S')
    path = f'{path}/story_{time}.mp3'
    tts.save(savefile=path)
    return path

text_to_speech("AITA for slapping a teenager? \n I (32f) was at a water park this last weekend with my husband (32m) and my daughter. We were in one of the pools practicing swimming and keeping to our self. There was a group of teen boys there and while I was working with my daughter on swimming one of them came up behind me and I felt a tug on the strings of my top untying it. I spun around saw this 15 to 17 yo with a smirk and slapped him. \nThis quickly caused a scene. The park staff got involved as well the boys parents who were livid at me. My husband and another lady saw it happen and confirmed that he really did grab my top. There was also camera around the pool that kind of show it, wasn't the best angle. The boys parents threaten assault charges and I threaten sexual assault charges if they decided to go that way. Eventually we were both asked to leave and haven't heard anything since. My husband though still thinks I over reacted a bit which I don't. AITA?", "stories/speech")