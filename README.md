# MatchMe Game Unity Automation

Scenarios Covered:
1. Completion of the first level with validation of score
2. Completion of second level with validation of score

Reporting:
Reports are generated and saved under reports folder

How to run:

To run the framework, there is a Run.bat file which will trigger the execution of complete framework.
1. Download the framework
2. Connect the device and enable the USB debugging mode from developer options in device
3. Open command prompt execute 'adb devices'
4. Execute 'adb forward tcp:13001 tcp:13000' in cmd
5. Launch the appium server and start the server with 'Host - 0.0.0.0' and 'Port - 4723'
6. Double click on the 'Run.bat' file from the framework to start execution
