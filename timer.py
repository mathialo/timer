#! /usr/bin/python3
import sys
import os
import time


HOME = os.path.expanduser('~')
FILENAME = "%s/.timertime" % HOME


def starttimer():
    if (checkifexists()):
        response = input("Timer is already going! Overwrite previous timer? [y/n]  ")
        
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

    if (command == "pause"):
        print("Timer paused at %s" % display())


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
    
    print(display())
    
    os.remove(FILENAME)


def display():
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

    if h > 23:
        d, h = divmod(h, 24)
        return "%d d, %d:%02d:%02d" % (d, h, m, s)

    else:
        return "%d:%02d:%02d" % (h, m, s)


def showtimer():
    if (not checkifexists()):
        print("Timer not started!")
        return
    
    print(display())


def statustimer():
    if (not checkifexists()):
        print("Timer inactive")

    else:
        if filelen() % 2 == 0:
            print("Timer paused")

        else:
            print("Timer running at %s" % display())
            

def main():
    try:
        command = sys.argv[1]
        
        if (command == "start"):
            starttimer()
            
        elif (command == "stop"):
            stoptimer()
            
        elif (command == "pause" or command == "resume"):
            pausetimer(command)

        elif (command == "show"):
            showtimer()

        elif (command == "status"):
            statustimer()
            
        else:
            print("Timer: Unknown command '%s'" % command)
        
    except IndexError:
        print("No command given. Proper use:")
        print("\n  > timer [cmd]\n")
        print("Where [cmd] is either start, stop, pause, resume, status or show.")
    
if __name__ == "__main__":
    main()


