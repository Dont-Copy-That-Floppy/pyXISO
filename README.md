# pyXISO
A python GUI frontend for the xbox [extract-xiso](https://github.com/XboxDev/extract-xiso) program.

Run the python program gui.py with Python 3+. When the window loads, select either the xbe file inside the directory meant to compress into a iso file, or select the iso file you wish to extract to a directory. If you'd like, select an output directory, otherwise the default is the parent to the file or xbe. The text labels will show you what you selected, and the detected processs based on what you selected. Click start to perform the process.

There is an issue with the output directory during the extract process that seems to be a downstream error from [extract-xiso](https://github.com/XboxDev/extract-xiso).
