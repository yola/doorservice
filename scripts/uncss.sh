#!/bin/bash

set -exu
cd "$(dirname "$0")/.."

rm -rf node_modules bower_components
rm doorservice/static/css/doorservice.uncss.css

npm install bower uncss
$(npm bin)/bower install "bootstrap#3.x.x"

touch doorservice/static/css/doorservice.uncss.css
cp bower_components/bootstrap/dist/css/bootstrap.css doorservice/static/css/
$(npm bin)/uncss -H doorservice -i "/.btn-(primary|success|danger)/" -s ../static/css/bootstrap.css, ../static/css/doorservice.css doorservice/templates/index.html > doorservice/static/css/doorservice.uncss.css
