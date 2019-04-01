import numpy
from os import path

if __name__ == "__main__":
    fname = path.expandvars(r"%USERPROFILE%\\AppData\\LocalLow\\David OReilly\\Mountain\\apsdfpboasdfhsa.sav")
    a = numpy.fromfile(fname, dtype=int, count=-1, sep='')
    hours_done = a[11]
    print("%s of 987 hours complete" % hours_done) 
    print("")
    input("Press enter to exit program...")