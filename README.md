# MicroAngio
Demonstration interface for the MicroAngio UX project.

[![Build status](https://api.travis-ci.org/WasatchPhotonics/MicroAngio.svg?branch=master)](https://travis-ci.org/WasatchPhotonics/MicroAngio)
[![Build status](https://ci.appveyor.com/api/projects/status/cqsxoj43q9v5jc16/branch/master?svg=true)](https://ci.appveyor.com/project/NathanHarrington/microangio/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/WasatchPhotonics/MicroAngio/badge.svg?branch=master)](https://coveralls.io/github/WasatchPhotonics/MicroAngio?branch=master)


Clickable, navigatable demonstration of the new user experience design
for OCT Angiography. No actual OCT processing is included. See the
instructions below for running this demo on your windows 7 system. Also
runs on Linux, and should run on any environment that supports conda.
This interface rates approximately 5.8 [TRAUDS](https://github.com/JasonTraud "TRAUDS") of darkness.

![MicroAngio Screenshot](/microangio/assets/demo_screenshots/thumbnails/Screenshot_2016-04-28_09-38-26.png "MicroAngio Screenshot")

HiDPI displays are not supported with pyqt4. This demonstration was
developed for a target resolution of 1920x1080.

PySide and PyQt are required to show svg icons on controls on MS
Windows.

    Instructions for environment creation on windows 7:

    Install miniconda 2.7 64bit
    export PATH=/home/nharrington/miniconda2/bin:$PATH
    conda update conda

    conda create --name conda_install_only pyside

    Windows:
    activate conda_install_only

    conda install pyqt numpy pillow pytest pyqtgraph
    
    cd projects\MicroAngio
    python setup.py develop

    py.test

    python -u scripts\MicroAngio.py
