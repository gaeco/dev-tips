import sys
from unicodedata import normalize
import os

def change_nfc_all_dir(dirname):
    print("checking dir : "+dirname)
    if os.path.exists(dirname) == False:
        print("Not exists")
        return

    if os.path.isdir(dirname) == False:
        print("Not directory")
        return

    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        next_dir = before_filename
        if(before_filename != after_filename):
            print("changing : "+before_filename +" --> " + after_filename)
            next_dir = after_filename
            os.rename(before_filename, after_filename)

        if os.path.isdir(next_dir):
            change_nfc_all_dir(next_dir)

change_nfc_all_dir("C:/Users/user1/Desktop/TestDir")
