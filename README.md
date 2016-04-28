# MicroAngio
Demonstration interface for the MicroAngio UX project.

[![Build status](https://api.travis-ci.org/WasatchPhotonics/MicroAngio.svg?branch=master)](https://travis-ci.org/WasatchPhotonics/MicroAngio)
[![Build status](https://ci.appveyor.com/api/projects/status/cqsxoj43q9v5jc16/branch/master?svg=true)](https://ci.appveyor.com/project/NathanHarrington/microangio/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/WasatchPhotonics/MicroAngio/badge.svg?branch=master)](https://coveralls.io/github/WasatchPhotonics/MicroAngio?branch=master)

PySide and PyQt are required to show svg icons on controls on MS
Windows.


2016-04-27 15:51 Instructions for environment creation on windows 7:

    Install miniconda 2.7 64bit
    conda update conda

    conda create --name conda_install_only pyside
    activate conda_install_only
    conda install pyqt numpy pillow pytest pyqtgraph
    
    cd projects\MicroAngio
    python setup.py develop

    py.test

    python -u scripts\MicroAngio.py
