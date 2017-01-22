from cx_Freeze import setup, Executable
from os import walk

sounds = []
files = []
for (dirpath, dirnames, filenames) in walk("assets/sounds"):
    sounds.extend(filenames)
    break
for i in range(len(sounds)):
    sounds[i]= "assets/sounds/"+sounds[i]

for (dirpath, dirnames, filenames) in walk("assets/levels"):
    files.extend(filenames)
    break
for i in range(len(files)):
    files[i]= "assets/levels/"+files[i]

includefiles = ['assets/emulogic.ttf', 'assets/images/spritesheet_1.png','assets/images/f1.png','assets/images/f2.png']+sounds+files
includes = []
excludes = ['Tkinter']
packages = ['pygame']

setup(
    name = 'Napohaku',
    version = '0.1',
    description = 'First Executable form of my Game',
    author = 'Clifton Kimber',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('Napohaku.py'),Executable('lev.py')]
)



