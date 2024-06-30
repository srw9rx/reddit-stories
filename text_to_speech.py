from gtts import gTTS
from pydub import AudioSegment
import datetime
import json
from typing import Union

def replace_words(text:str, vocab_path:str) -> str:
    '''
    :param text:str: the text that we are cleaning
    :param vocab_path: the path to a json document of vocab being replaced
    :return: the string with the listed vocabulary words replaced'''
    assert(vocab_path[-4:]=='json')
    with open(vocab_path, 'r') as f:
        mappings = json.load(f) # read in the json document
    for mapping in mappings:
        text = text.replace(mapping['term'], mapping['replacement'])
    return text
    
def speedup_mp3(mp3:str, speedup_rate:float=1.3) -> AudioSegment:
    segment = AudioSegment.from_file(mp3)
    speed_update = segment.speedup(speedup_rate)
    return speed_update

def text_to_speech(text:str, path:str):
    '''
    :param text:str: the story we are converting to speech
    :param path:str: the folder where the story is being saved
    :return: the file path that will be used to get the mp3 to overlay on video
    '''
    tts = gTTS(text)
    time = datetime.datetime.now().strftime('%d-%m-%YT%H:%M:%S')
    path = f'{path}/story_{time}.mp3'
    tts.save(savefile=path)
    fast_tts = speedup_mp3(path)
    fast_tts.export(path, format="mp3")
    return path

text = "AITA for slapping a teenager? \n I (32f) was at a water park this last weekend with my husband (32m) and my daughter. We were in one of the pools practicing swimming and keeping to our self. There was a group of teen boys there and while I was working with my daughter on swimming one of them came up behind me and I felt a tug on the strings of my top untying it. I spun around saw this 15 to 17 yo with a smirk and slapped him. \nThis quickly caused a scene. The park staff got involved as well the boys parents who were livid at me. My husband and another lady saw it happen and confirmed that he really did grab my top. There was also camera around the pool that kind of show it, wasn't the best angle. The boys parents threaten assault charges and I threaten sexual assault charges if they decided to go that way. Eventually we were both asked to leave and haven't heard anything since. My husband though still thinks I over reacted a bit which I don't. AITA?"
text = replace_words(text, 'reddit_vocab.json')
print(text)
text_to_speech(text, "stories/speech")