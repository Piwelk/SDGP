#!/bin/sh

sudo apt install git
sudo apt install python3-pip
git config --global user.name ""
git config --global user.email ""

pip3 install nltk
pip3 install gensim
pip3 install sklearn
pip3 install matplotlib