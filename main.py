# AI SMART HOME project by HC01
import os.path

if not os.path.isdir("./VRM"):
    print("Didn`t found Voice Recognition Module, exiting!")
    exit()

from VRM.vr import *