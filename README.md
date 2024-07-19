# Persian SpeechToText Android App


## About The Project

This application records your voice and then shows what you said in written text. You can also give it a voice file and it converts it into text.
Although this is an android application written in Kotlin, it also uses python libraries such as PyTorch, Transformers, scikit-learn, etc. for speech recognition and text generation.    

## Report a bug

You can report a bug by [opening an issue](https://github.com/mkdmc/PersianSpeechToText/issues/new).

#### How to report a bug
* A detailed description of the bug
* Logcat
* Make sure there are no similar bug reports already

## Download & Build

Clone the project and come in:

``` bash
$ git clone git://github.com/mkdmc/PersianSpeechToText.git
$ cd PersianSpeechToText
$ ./gradlew build
```

#### Notes
* You must place the trained speech recognition model in this path: /app/src/main/python/AsrFiles/whisper-small-fa/
* You can use [Hezar AI whisper-small-fa](https://huggingface.co/hezarai/whisper-small-fa) as the model

## Credits

* Hezar: [The all-in-one AI library for Persian](https://github.com/hezarai/hezar)
* Chaquopy: [Python SDK for Android](https://chaquo.com/)
* FFmpegKit: [FFmpegKit for Android](https://github.com/arthenica/ffmpeg-kit/tree/main/android)
* Alireza Tabatabaei: [Tabatabaei1999](https://github.com/Tabatabaei1999)

## License

    Copyright (C) 2024-2025 Mehrshad Kavousi
    
    Persian SpeechToText is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Persian SpeechToText is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Persian SpeechToText.  If not, see <http://www.gnu.org/licenses/>.
