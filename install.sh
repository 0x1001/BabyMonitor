#!/bin/bash

#Install pyaudio
cd ..
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
sudo apt-get install -y libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt-get install -y python-dev
cd pyaudio
sudo python setup.py install

# Install matplotlib
sudo apt-get install -y python-matplotlib

# Install turbosmtp
sudo pip install turbosmtp

