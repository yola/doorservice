#!/bin/bash

# exit on error
set -exu
cd "$(dirname "$0")/.."

npm prune
npm install
$(npm bin)/bower prune
$(npm bin)/bower install

virtualenv virtualenv
virtualenv/bin/pip install -r requirements.txt
