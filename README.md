# WSUS_Offline_Updater

This executable automatics the process of downloading [WSUS Offline Update][wsus] files.

## Notable Features

- Checks the versions to see if your current install is the same as the websites
    - Proceeds to download
- Checks internet connectivity

## Filesystem Anatomy
+ WSUS_Offline_Updater
    + Download
        + Contains Downloaded .zip installers
    + Source
        +  esr_url.txt & new_url.txt hold the current version downloaded
        +  The requirements bash script are the python libraries required
        +  The updater python file holds the main logic
    + License
        +  The GNU license allows the work to be reproduced if it is also open sourced
        
## Use Out Of The Box
**!!Use this if you do not want to alter the code!!**

- Click the green "clone or download" button in the top right
- Unzip
- grab the file titled "WSUS_updater.exe" and use wherever you want

## Compile From Source or Run In Python
**!!Use this method if you want to alter the code in some way!!**

- Click the green "clone or download" button in the top right
- Unzip
- Navigate to /source and run ```./requirements.sh```
 - Will install dependencies
- Run ```python3 updater.py```
- TODO

## TODO

- Add functionality to auto-extract the file and run the GUI
- add AllInOneEXE compiled version
- Finish documentation


Created by Max Novak with :heart: for lazy server admins.











[wsus]:     http://download.wsusoffline.net/
