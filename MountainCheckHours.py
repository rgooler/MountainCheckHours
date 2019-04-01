import numpy

if __name__ == "__main__":
    fname = "%UserProfile%\\AppData\\LocalLow\\David OReilly\\Mountain\\apsdfpboasdfhsa.sav"
    a = numpy.fromfile(fname, dtype=int, count=-1, sep='')
    hours_done = a[11]
    input("%s of 987 hours complete" % hours_done) 