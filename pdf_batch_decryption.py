import os

def help():
    print("Use with the following arguments:\n1. Path containing the encrypted PDF(s)\n2. The password to open and decrypt the PDF(s)"
    "\nExample: pdf_batch_decryption.py $PATH_TO_PDF(S) $PASSWORD")

class cd:
    """Context manager class for changing the current working directory"""
    def __init__(self, new_path):
        self.new_path = os.path.expanduser(new_path)

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.saved_path)


import sys
from os import system, getcwd, listdir
from os.path import isfile, join


if sys.argv[1] == "--help" or len(sys.argv) != 3:
    help()
    sys.exit(0)

my_path = sys.argv[1]
my_pass = sys.argv[2]

# Get all files with the extension ".pdf"
only_files = [f for f in listdir(my_path) if isfile(join(my_path, f)) and f.endswith(".pdf")]

print("Password to use for decryption: {0}".format(my_pass))

with cd(mypath):
    print("PDF containing folder:\n{0}\n".format(getcwd()))
    for f in only_files:
        infile = f
        outfile = f[:-4] + "_OPEN.pdf"
        print("Decrypt: '{0}' to '{1}'".format(infile, outfile))
        system("qpdf --password={0} --decrypt '{1}' '{2}'".format(my_pass, infile, outfile))
