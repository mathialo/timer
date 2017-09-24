# Timer
Command line utility for taking time. Stores timestamps as a file in the user's home directory, so that no program is running in the background.


### Requirements and installation
Timer is written in Python 3. To install, copy timer.py to a suitable directory, and make sure it's executable:
``` bash
 $ chmod +x timer.py
```
now create a symlink to it from one of the bin-directories so that it's available from the command line:
``` bash
 $ ln -s /link/to/timer.py /usr/local/bin/timer
```
Now, Timer should be installed. Try writing:
``` bash
 $ timer start
 $ timer stop
```
for confimation. 


### Usage
Once installed, the following commands are available:

|    Command      |  Discription                                                      |
|  :---------:    |  -------------------------------------------------------          |
| `timer start`   |  Starts the timer                                                 |
| `timer stop`    |  Stops the timer and displays the time passed                     |
| `timer pause`   |  Pauses the timer                                                 |
| `timer resume`  |  Resumes the timer after a `timer pause`                          |
| `timer show`    |  Shows the current time passed (without stopping the timer)       |
| `timer status`  |  Shows the current state of the timer (stopped, going or paused)  |


