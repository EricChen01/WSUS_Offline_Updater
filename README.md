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
## TODO

- Add functionality to auto-extract the file and run the GUI


Created by Max Novak with :heart: for lazy server admins.











[wsus]:     http://download.wsusoffline.net/
