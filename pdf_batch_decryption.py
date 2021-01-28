import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


import sys
from os import system, getcwd, listdir
from os.path import isfile, join

mypath = sys.argv[1]
mypass = sys.argv[2]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".pdf")]

print("Password to use for decryption: {0}".format(mypass))

with cd(mypath):
    print("PDF containing folder:\n{0}\n".format(getcwd()))
    for f in onlyfiles:
        infile = f
        outfile = f[:-4] + "_OPEN.pdf"
        print("Decrypt: {0} to {1}".format(infile, outfile))
        system("qpdf --password={0} --decrypt {1} {2}".format(mypass, infile, outfile))

