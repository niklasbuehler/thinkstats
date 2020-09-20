import Pmf
from operator import itemgetter

def Mode(hist):
    mode = 0
    max_freq = 0
    for val, freq in hist.Items():
	if freq > max_freq:
	    mode = val
	    max_freq = freq
    return mode

def AllModes(hist):
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)
