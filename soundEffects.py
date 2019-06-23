from playsound import playsound
from config import cfg
from random import choices
import os


def playIntroSoundEffect():
    playsound(
        os.path.join(cfg['soundEffectsDir'], 'intro', 'intro.mp3')
    )


def playOutroSoundEffect():
    outroVersion = 'outro'

    population = [1, 2, 3]
    weights = [0.6, 0.3, 0.1]
    outroVersion = outroVersion + str(choices(population, weights)[0]) + ".mp3"

    playsound(
        os.path.join(cfg['soundEffectsDir'], 'outro', outroVersion)
    )


def playSetupSoundEffect():
    setupVersion = 'setup'

    population = [1, 2]
    weights = [0.75, 0.25]
    setupVersion = setupVersion + str(choices(population, weights)[0]) + ".mp3"

    playsound(
        os.path.join(cfg['soundEffectsDir'], 'setup', setupVersion)
    )


def playSetupCompleteSoundEffect():
    playsound(
        os.path.join(cfg['soundEffectsDir'],
                     'setup complete', 'setup_complete.mp3')
    )


def playListeningSoundEffect():
    listeningVersion = 'listening'

    population = [1, 2, 3, 4, 5, 6, 7]
    weights = [0.20, 0.20, 0.20, 0.175, 0.125, 0.075, 0.02]

    listeningVersion = listeningVersion + \
        str(choices(population, weights)[0]) + ".mp3"

    playsound(
        os.path.join(cfg['soundEffectsDir'], 'listening', listeningVersion)
    )


def playUnknownCommandSoundEffect():
    repeatVersion = 'repeat'

    population = [1, 2, 3]
    weights = [0.4, 0.4, 0.2]

    repeatVersion = repeatVersion + \
        str(choices(population, weights)[0]) + ".mp3"

    playsound(
        os.path.join(cfg['soundEffectsDir'], 'repeat', repeatVersion)
    )


def playConfirmCommandSoundEffect():
    confirmVersion = 'confirm'

    population = [1, 2, 3, 4, 5, 6]
    weights = [0.4, 0.35, 0.15, 0.19, 0.1, 0.05]

    confirmVersion = confirmVersion + \
        str(choices(population, weights)[0]) + ".mp3"

    playsound(
        os.path.join(cfg['soundEffectsDir'], 'confirm command', confirmVersion)
    )
