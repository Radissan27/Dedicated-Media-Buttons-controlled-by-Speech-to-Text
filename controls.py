import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

MAPVK_VK_TO_VSC = 0

# Source for the keyboard codes: msdn.microsoft.com/en-us/library/dd375731

# Play/Pause Media key
VK_MEDIA_PLAY_PAUSE = 0xB3
# Stop Media key
VK_MEDIA_STOP = 0xB2
# Next Track key
VK_MEDIA_NEXT_TRACK = 0xB0
# Previous Track key
VK_MEDIA_PREV_TRACK = 0xB1
# Volume Up key
VK_VOLUME_UP = 0xAF
# Volume Down key
VK_VOLUME_DOWN = 0xAE
# Volume Mute key
VK_VOLUME_MUTE = 0xAD

# C struct definitions
wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT,  # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize


# Functions
def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def PlayPauseMediaTrack():
    PressKey(VK_MEDIA_PLAY_PAUSE)
    ReleaseKey(VK_MEDIA_PLAY_PAUSE)


def NextTrack():
    PressKey(VK_MEDIA_NEXT_TRACK)
    ReleaseKey(VK_MEDIA_NEXT_TRACK)


def PreviousTrack():
    PressKey(VK_MEDIA_PREV_TRACK)
    ReleaseKey(VK_MEDIA_PREV_TRACK)


def VolumeMute():
    PressKey(VK_VOLUME_MUTE)
    ReleaseKey(VK_VOLUME_MUTE)


def VolumeUp():
    PressKey(VK_VOLUME_UP)
    ReleaseKey(VK_VOLUME_UP)


def VolumeDown():
    PressKey(VK_VOLUME_DOWN)
    ReleaseKey(VK_VOLUME_DOWN)
