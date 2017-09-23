#! /usr/bin/python
import sys
import os
import time


HOME = os.path.expanduser('~')
FILENAME = "%s/.timertime" % HOME


def starttimer():
    if (checkifexists()):
        print("Timer is already going! Overwrite previous timer? [y/n]")
        
        response = input(" > ")
        
        if (not (response == "y" or response == "Y" or response == "yes")):
            print("Aborting")
            return
    
    f = open(FILENAME, "w")
    f.write(str(int(time.time())) + "\n")
    f.close()


def pausetimer(command):
    if (not checkifexists()):
        print("No timer going! Use 'timer start' to initialize timer!")
        return
    
    if (filelen() % 2 == 0 and command == "pause"):
        print("Timer already paused! Use 'timer resume' to resume")
        return
    
    if (filelen() % 2 == 1 and command == "resume"):
        print("Cannot resume, timer not paused!")
        return
    
    f = open(FILENAME, "a")
    f.write(str(int(time.time())) + "\n")
    f.close()


def checkifexists():
    return os.path.isfile(FILENAME)


def filelen():
    f = open(FILENAME)
    for i, l in enumerate(f):
        pass
    
    f.close()
    return i + 1


def stoptimer():
    if (not checkifexists()):
        print("Timer not started!")
        return
    
    lines = []
    
    f = open(FILENAME, "r")
    for line in f:
        lines.append(int(line.rstrip()))
    
    if (len(lines) % 2 == 1):
        lines.append(int(time.time()))
    
    stoptimes = [lines[i] for i in range(1, len(lines), 2)]
    starttimes = [lines[i] for i in range(0, len(lines), 2)]
    
    secnum = sum(stoptimes) - sum(starttimes)
    
    m, s = divmod(secnum, 60)
    h, m = divmod(m, 60)
    print("%d:%02d:%02d" % (h, m, s))
    
    os.remove(FILENAME)


def main():
    try:
        command = sys.argv[1]
        
        if (command == "start"):
            starttimer()
            
        elif (command == "stop"):
            stoptimer()
            
        elif (command == "pause" or command == "resume"):
            pausetimer(command)
            
        else:
            print("Unknown command '%s'" % command)
        
    except IndexError:
        print("No command given. Proper use:")
        print("\n  > timer [cmd]\n")
        print("Where [cmd] is either start, stop, pause or resume")
    
if __name__ == "__main__":
    main()


