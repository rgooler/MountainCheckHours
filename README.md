Mountain Check Hours
====================

[![Build status](https://ci.appveyor.com/api/projects/status/jnglba08gx5y0fkr?svg=true)](https://ci.appveyor.com/project/rgooler/mountaincheckhours)


Check how far you are in the "YOU ARE GOD" achievement for Mountain

NOTE: Windows defender might alert that this is unknown and its protected you, just click 'more info' and run anyways. Its just because I'm packing a python program as an exe for your convinience, and don't have a certificate to sign the application.

Installation
------------

For windows, just download the latest version from the releases tab.

For OSX/Linux, or development work, you will need python 3 and pip installed. These may be available by default, or googling something like "Install python 3 and pip on debian" should get you proper instructions. They are not replicated here, as the instructions have varied over time, and google is better than I am at keeping those things up to date.

Once you're set up with those, open a terminal window. You can then install the required libraries and make sure the script is executeable by running the following commands:

    python -m pip install -r requirements.txt
    chmod +x MountainCheckHours.py
    
Then to run the script, simply run the following command:

    ./MountainCheckHours.py
