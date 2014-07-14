#Doorservice
![Yodoor](yodoor.png)

Doorservice opens the door.

##Introduction

As is customary, the lowest ranking member of any office is to open the door
when the bell chimes.

As of now, this tradition is no more.

We now live in an era of machines and computers, with the mere press of an
oversized button, the door will open itself.

The wait is over, the captives are free. Ne'er again will man obey the chime.

Button pressing is now virtual.

##Installation

###Prerequisites
>Note: This setup requires a Raspberry Pi, a relay controlled by said Raspberry
Pi and for the relay to be connected to the door control.

These packages are required on the Raspberry Pi before you can run `./scripts/build.sh`.

1. Node.js `sudo apt-get install nodejs`
2. Pip `sudo apt-get install python-pip`
3. Virtualenv `pip install virtualenv`
4. GPIO on the Raspberry Pi `sudo apt-get install python-rpi.gpio`

###Instructions
1. Clone this repository.
2. Run  `scripts/build.sh`.
3. Set all your settings in the `./doorservice/settings.py` file. (An example is provided)
3. Move all the files in the directory onto the Raspberry Pi.
4. Set up a server. (Documentation [here](http://flask.pocoo.org/docs/deploying/wsgi-standalone/))
5. Run `./run.py`.

Now you can access the button by connecting to the server you set up in step 4.

An authentication pop-up should appear, enter your username and password as set
in `./doorservice/settings.py`.

After successfully authenticating, you should see a large blue button.

Press the button. Go on, press it.

That's it.

If it's green, it means the door should be open. If it's red, it means something
went wrong.

##Button Colours

###1. Green
Everything is probably working just fine. All the code executed without error.

###2. Orange
You aren't authenticated and will be unable to operate the button.

###3. Red
Something went wrong, horribly wrong.
