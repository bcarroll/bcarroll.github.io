#!/usr/bin/python
import os
import sys

print ('')
print ('')
print ('')
print ('')
print ('######################################')
print ('#        Installing PiControl        #')
print ('######################################')
print ('')
print ('######################################')
print ('####### Installing Dependencies ######')
print ('######################################')
print (' Running apt-get update')
print ('')
os.popen('sudo apt-get -q update')
print ('done.')
print ('')
print ('######################################')
print (' Installing Operating System dependencies')
print ('')
os.popen('sudo apt-get -q -y install git gcc libffi-dev libssl-dev python-dev python-pip python-cryptography wiringpi')
print ('done.')
print ('')
print ('######################################')
print (' Installing Python dependencies')
print ('')
os.popen('sudo pip -q install Flask Flask-SSLify flask_socketio flask_sqlalchemy ipaddress netifaces netaddr psutil simplepam wiringpi requests xmltodict')
print ('done.')
print ('')
print ('######################################')
print ('# Directory to clone PiControl into #')
print ('######################################')
print ('')
PiControlDirectory = input(' Enter the path to install PiControl into (default: /usr/local/src) : ')

if len(PiControlDirectory) < 1:
    PiControlDirectory = "/usr/local/src"

os.chdir(PiControlDirectory)

if os.path.isdir(PiControlDirectory + '/PiControl'):
    overwrite = input(PiControlDirectory + '/PiControl already exists.  Do you want to overwrite this directory" [y/n]: ')
    if overwrite.lower == "y":
        os.popen('sudo rm -r PiControl')
    else:
        print('PiControl installation cancelled.')
        sys.exit()


print ('')
print ('######################################')
print (' Cloning PiControl from GitHub to ' + PiControlDirectory)
os.popen('sudo git clone https://github.com/bcarroll/PiControl.git')
print ('')
os.popen('sudo chmod +x PiControl/PiControl.sh')
os.popen('sudo chown -R $USER PiControl')

print ('')
print ('######################################')
print ('#      Start PiControl at boot?      #')
print ('######################################')
answer = input(' Do you want to run PiControl when the Raspberry Pi starts? [y/n]:')
if answer == "y":
    os.popen('sudo sed -i "$ a Start PiControl" /etc/rc.local')
    os.popen('sudo sed -i "$ a sudo -u pi python ' + PiControlDirectory + '/PiControl/PiControl.sh start &" /etc/rc.local')
else:
    print('PiControl will need to be started manually.')

print ('')
print ('######################################')
print ('#   Clean up local apt repository    #')
print ('######################################')
print ('Cleaning up')
print ('')
os.popen('sudo apt-get -q -y clean')
os.popen('sudo apt-get -q -y autoclean')
os.popen('sudo apt-get -q -y autoremove')
print ('')
print ('Done.')
print ('')
answer = input('Do you want to start PiControl now? [y/n]:')
if answer == "n":
    print ('To start PiControl run the following command: ' + PiControlDirectory + '/PiControl/PiControl.sh start')
    print ('')
else:
    print ('')
    os.popen(PiControlDirectory + '/PiControl/PiControl.sh start')
