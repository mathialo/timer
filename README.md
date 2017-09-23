# Timer
Command line utility for taking time. Stores timestamps as a file in home, so that no program is running in the background.


### Requirements and installation
Timer is written in Python 3. To install, copy timer.py to a suitable directory, and make sure it's executable:
``` bash
 $ chmod +x timer.py
```
now create a symlink to it from one of the bin-directories so that it's available from the command line:
``` bash
 $ ln -s /link/to/timer.py /usr/local/bin/timer
```
Now, timer should be installed. Try writing
``` bash
 $ timer start
 $ timer stop
```
for confimation. Additional commands available are `timer pause` and `timer resume`, they do what you would expect them to do. 
