import speech_recognition as SR
from config import cfg
from word2number import w2n
from controls import (PlayPauseMediaTrack, NextTrack, PreviousTrack,
                      VolumeMute, VolumeDown, VolumeUp)
from soundEffects import (playIntroSoundEffect, playConfirmCommandSoundEffect,
                          playSetupCompleteSoundEffect, playSetupSoundEffect,
                          playListeningSoundEffect, playOutroSoundEffect,
                          playUnknownCommandSoundEffect
                          )


# Command functions
def PlayPauseTrack():
    PlayPauseMediaTrack()


def PlayNextTrack():
    NextTrack()


def PlayPreviousTrack():
    PreviousTrack()
    PreviousTrack()


def RepeatTrack():
    PreviousTrack()


def MuteUnmuteVolume():
    VolumeMute()


def UpVolume(timesToRepeat):
    timesToRepeat = w2n.word_to_num(timesToRepeat)
    if timesToRepeat > 50:
        timesToRepeat = 50
    elif timesToRepeat < 1:
        timesToRepeat = 0
    while timesToRepeat > 0:
        VolumeUp()
        timesToRepeat -= 1


def DownVolume(timesToRepeat):
    timesToRepeat = w2n.word_to_num(timesToRepeat)
    if timesToRepeat > 50:
        timesToRepeat = 50
    elif timesToRepeat < 1:
        timesToRepeat = 0
    while timesToRepeat > 0:
        VolumeDown()
        timesToRepeat -= 1


# Main
if __name__ == "__main__":

    keywordRecognizer = SR.Recognizer()
    commandRecognizer = SR.Recognizer()
    keywordRecognizer.energy_threshold = 400
    commandRecognizer.energy_threshold = 400

    simpleCommands = {
        'play': PlayPauseTrack,
        'start': PlayPauseTrack,
        'pause': PlayPauseTrack,
        'stop': PlayPauseTrack,
        'next': PlayNextTrack,
        'previous': PlayPreviousTrack,
        'repeat': RepeatTrack,
        'mute': MuteUnmuteVolume,
        'unmute': MuteUnmuteVolume
    }
    complexCommands = {
        'volume up': UpVolume,
        'volume down': DownVolume,
    }

    # Setup
    with SR.Microphone() as inputSource:
        if cfg['intro']:
            playIntroSoundEffect()

        if cfg['setup']:
            playSetupSoundEffect()

        keywordRecognizer.dynamic_energy_threshold = False
        commandRecognizer.dynamic_energy_threshold = False

        if cfg['setup']:
            playSetupCompleteSoundEffect()

        # Listen for commands
        while 1:
            audio = keywordRecognizer.listen(inputSource)
            try:
                text = keywordRecognizer.recognize_google(audio)
                print('Keyword: ' + text)
                if cfg['keyword'] in text.lower():
                    playListeningSoundEffect()

                    audio = commandRecognizer.listen(inputSource)
                    text = commandRecognizer.recognize_google(audio)

                    print("You said: " + text)
                    if text.lower() in simpleCommands.keys():
                        simpleCommands[text.lower()]()
                        playConfirmCommandSoundEffect()
                    elif len(text.split(' ')) == 3:
                        cmd = text.lower().split(' ')[:2]
                        cmd2 = cmd[0]
                        for i in range(1, len(cmd)):
                            cmd2 = cmd2 + ' ' + cmd[i]
                        if cmd2 in complexCommands.keys():
                            complexCommands[cmd2](text.lower().split(' ')[2])
                        else:
                            raise SR.UnknownValueError
                    elif len(text.split(' ')) == 2:
                        if text.lower() in complexCommands.keys():
                            complexCommands[text.lower()]('one')
                        else:
                            raise SR.UnknownValueError
                    elif text.lower() == 'exit':
                        break
                    else:
                        playUnknownCommandSoundEffect()

            except SR.UnknownValueError:
                # print("Google Speech Recognition could not understand audio")
                pass
            except ValueError:
                pass

        if cfg['outro']:
            playOutroSoundEffect()
