import os
from playsound import playsound
from win10toast import ToastNotifier

def natficatsion(sound, message):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toasst = ToastNotifier()
    tit = 'Budilnik'
    xabar = message
    len = 3
    toasst.show_toast(tit, xabar, duration=len)
    for i in range(0, 2):
        playsound(sound)
