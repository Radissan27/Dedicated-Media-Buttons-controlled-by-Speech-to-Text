# Dedicated-Media-Buttons-controlled-by-Speech-to-Text

I designed this app with the intention to have some basic controls over Spotify but it can be easily adapted for other similar apps or purposes (it's compatible only with the Windows OS in the current state).

One big thing to take into consideration here is that I used a basic open source library for the speech-to-text part (that uses the en-US language by default) so it only produces half-decent results, therefore there are some things that may influence the results such as: the quality of the microphone, the proximity of the speaker to the microphone, the intensity/volume of the speech, pronunciation and related problems (such as three sounding awfully similar as tree).

## Prerequisites:
* [Python 3.6.4](https://www.python.org/downloads/release/python-364/)
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
* [PyAudio](https://pypi.org/project/PyAudio/)
* [playsound](https://pypi.org/project/playsound/)
* [word2number](https://pypi.org/project/word2number/)

## Instalation:
* pip install -r requirements.txt
* go into the 'config.py' file and set the path for your 'Sound Effects' dirrectory
* (optionally) change the keyword and/or what sounds do you want to hear (if you set the 'intro', 'outro' or 'setup' flags to False you will disable those specific sound effects)

## Usage: 
First, you must say the keyword for the application (the one from the config file) and then the keyword for one of the following available commands:

## Available commands([keyword]: [action description]):

#### (Play/Pause button behavior)
- play/start: Plays/Pauses the current track
- pause/stop: Plays/Pauses the current track

#### (Next track button behavior)
- next: Plays the next track

#### (Previous track button behavior)
- previous: This command will simply use the Previous track button twice in order to ensure the previous song will play so it will not repeat the current one
- repeat: Based on how early or late into the song you are using this command (same as the actual button) it will either repeat the current track (if you use the command AFTER the first few seconds from it strating) or it will play the previous track (if you use it IN the first few seconds from it starting); it is recommended that you wait the first few seconds from the beginning of the song and then use the suitable command in order to guarantee the expected result

#### (Mute volume button behavior)
- mute: mutes/unmutes the volume
- unmute: mutes/unmutes the volume

#### (Volume up button behavior)
- volume up X: increase the volume up by X times, where X represents a natural number ∈ [1, 50] that can be missing (in this case it                    will be assumed as 1)


  - if X < 1, then X = 0
  - if X > 50, then X = 50
  - if X is anything other than an integer the command will not work
  - one thing to note here is that (at least on the keyboard that I tested the app) the volume would go up and down by 2%                    on one press of the button => X = 50 means the button will be pressed 50 times and the volume will be for sure to                        100%

#### (Volume down button behavior)
- volume down X: decrease the volume up by X times, where X represents a natural number ∈ [1, 50] that can be missing (in this case it                    will be assumed as 1)
               
  - if X < 1, then X = 0
  - if X > 50, then X = 50
  - if X is anything other than an integer the command will not work
  - one thing to note here is that (at least on the keyboard that I tested the app) the volume would go up and down by 2%                    on one press of the button => X = 50 means the button will be pressed 50 times and the volume will be for sure to                        0%
