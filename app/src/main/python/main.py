from AsrSource.models import *
from com.chaquo.python import Python
import os
context = os.path.dirname(os.path.realpath(__file__))
file_path = context + "/AsrFiles/whisper-small-fa/"
whisper = Model.load(file_path, load_locally=True)
def asr(Sound_file):
    return whisper.predict(Sound_file)[0]['text']
