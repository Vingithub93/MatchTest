#!/bin/bash

##
## Work in progress! The dependency installations need to be done to the
## container so that we don't need to install them here.
##

replace #Name of the test file

##### Cloud testrun dependencies start
echo "Extracting tests.zip..."
unzip tests.zip

adb devices
adb forward tcp:13001 tcp:13000


echo "Installing pip for python"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py

echo "Installing Appium Python Client 0.26, selenium 3.0.2, altunityrunner 0.1.3 and xmlrunner 1.7.7"
chmod 0755 requirements.txt
sudo pip install -r requirements.txt

echo "Starting Appium ..."

appium-1.6 --log-no-colors --log-timestamp

ps -ef|grep appium
##### Cloud testrun dependencies end.

export APPIUM_APPFILE=$PWD/match.apk #App file is at current working folder

## Desired capabilities:

export APPIUM_URL="http://localhost:4723/wd/hub" # Local & Cloud
export APPIUM_DEVICE="Local Device"
export APPIUM_PLATFORM="android"

APILEVEL=$(adb shell getprop ro.build.version.sdk)
APILEVEL="${APILEVEL//[$'\t\r\n']}"
echo "API level is: ${APILEVEL}"


## APPIUM_AUTOMATION 
if [ "$APILEVEL" -gt "16" ]; then
  echo "Setting APPIUM_AUTOMATION=Appium"
  export APPIUM_AUTOMATION="Appium"
else
  echo "Setting APPIUM_AUTOMATION=selendroid"
  export APPIUM_AUTOMATION="Selendroid"
fi

## Run the test:
echo "Running test ${TEST}"
rm -rf screenshots

pytest ${TEST}

mv test-reports/*.xml TEST-all.xml
