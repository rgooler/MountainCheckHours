import numpy
from os import path
import os

savefile = "apsdfpboasdfhsa.sav"

def find_savedir():
    if path.isfile(savefile):
        return '.'

    winpath = path.expandvars(r"%USERPROFILE%\\AppData\\LocalLow\\David OReilly\\Mountain")
    if path.isdir(winpath):
        return winpath

    linpath = path.expandvars(r"~/.steam/steam/steamapps/compatdata/897330/pfx/dosdevices/z:/home")
    linpath_x = "/.config/unity3d/David OReilly/Mountain"
    if path.isdir(linpath):
        for x in os.listdir(linpath):
            if os.path.isdir(x):
                fullpath = "%s/%s/%s" % (linpath, x, linpath_x)
                if path.isdir(fullpath):
                    return fullpath

if __name__ == "__main__":
    path = find_savedir()
    if path is None:
        print("Cannot find savegame. Please move this exe/script to your save folder for Mountain.")
    else:
        filename = "%s/%s" % (path, savefile)
        a = numpy.fromfile(filename, dtype=numpy.int32, count=-1, sep='')
        hours_done = a[11]
        print("%s of 987 hours complete" % hours_done)
    print("")
    input("Press enter to exit program...")
