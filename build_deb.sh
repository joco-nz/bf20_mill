#!/bin/bash

#make sure build deps are in place
sudo apt install dpkg-dev
sudo apt install devscripts build-essential lintian
sudo apt install dh-python
sudo apt install python3-build
sudo apt install pybuild-plugin-pyproject
sudo apt install python3-poetry

debuild -ePATH  -b -uc -us


