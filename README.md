# MatchMe Game Unity Automation

## Scenarios Covered:

* Completion of the first level with validation of score
* Completion of second level with validation of score
* Reporting: Reports are generated and saved under '<MatchMe project-dir>/Automation/MatchMe/reports' folder
* Screenshots: Screenshots are generated and saved under "Automation/MatchMe/screenshots" folder

## Setup

### Prerequisites:
* Python 2.7
* Appium
* Android SDK
* JDK

### Execution

To use the MatchMe Automation framework, you need to:

1. Download the complete MatchMe.git folder and unzip it.
2. Installations from command prompt, run the following commands in cmd
* pip install Appium-Python-Client
* npm install -g appium
* cd <MatchMe project-dir>/Assets/AltUnityTester/Bindings/python and run following commands
* pip install altunityrunner
* python setup.py install
3. Connect the device to the system with USB debugging mode enabled and run the following commands in cmd
* adb devices
* adb forward tcp:13001 tcp:13001
4. Start the Appium server with 'Host - 0.0.0.0' and 'Port - 4723'
5. Run the Run.bat file under '<MatchMe project-dir>/Automation/MatchMe'
  
  