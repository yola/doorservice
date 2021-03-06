#!/bin/bash

# exit on error
set -exu
cd "$(dirname "$0")/.."

npm prune
npm install
$(npm bin)/bower prune
$(npm bin)/bower install

# installs GPIO from the RPi's existing packages.
virtualenv -p python2.7 --system-site-packages virtualenv
virtualenv/bin/pip install -r requirements.txt

if [ ! -f doorservice/settings.py ]; then
  cp doorservice/settings.example.py doorservice/settings.py
fi
