#!/bin/sh
apt -y install virtualenv npm
cp doorservice.service /etc/systemd/system/doorservice.service
systemctl daemon-reload
systemctl enable doorservice.service
