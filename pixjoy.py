## Combination of Hacks by Josh Jacobs, William Peale and Ian McNanie
## Useful for running things like FPV Freerider with an Artoo
## Run with Sudo
## Run modprobe uinput


import pixrc
import paramiko
import subprocess
import uinput
import time

def flash():
    key = subprocess.check_output("hostname -I", shell=True)[:-2]
    
    #print "Enter your IP on the artoo network (enter if you're g):",
    #key = raw_input()
    
    if key != "":
        print "Flashing IP..."
    
        pcc = paramiko.Transport(("10.1.1.1", 22))
        pcc.connect(username = "root", password = "TjSDBkAu")
    
        sesh = pcc.open_channel(kind = 'session')
    
        cmd = "echo \'"+key+"\' > /var/run/solo.ip"
    
        sesh.exec_command(cmd)
        #sesh.exec_command("init 3")
        #sesh.exec_command("init 4")
    
        sesh.close()
        pcc.close()
    else:
        print "lol"

# via: https://github.com/tuomasjjrasanen/python-uinput/blob/ffbf1c90458811a359e5bb300db2e16e347a2cb5/examples/joystick.py
events = (
    uinput.ABS_X + (1000, 2000, 0, 0),
    uinput.ABS_Y + (1000, 2000, 0, 0),
    uinput.ABS_RX + (1000, 2000, 0, 0),
    uinput.ABS_RY + (1000, 2000, 0, 0),
)
device = uinput.Device(events)
device.emit(uinput.ABS_X, 1500, syn=False)
device.emit(uinput.ABS_Y, 1500)
device.emit(uinput.ABS_RX, 1500, syn=False)
device.emit(uinput.ABS_RY, 1500)
def enjoy(breh):
    if breh is not None:
        # syn=False to emit an "atomic" (5, 5) event.
        device.emit(uinput.ABS_X, breh[3], syn=False)
        device.emit(uinput.ABS_Y, breh[0])
        device.emit(uinput.ABS_RX, breh[1], syn=False)
        device.emit(uinput.ABS_RY, -breh[2]+3000)
        #device.emit_click(uinput.BTN_JOYSTICK)
        #time.sleep(0.1)

        
if __name__ == "__main__":  
    flash()
    rc = pixrc.controller()
    while True:
        enjoy(rc.rcChansOut)
        #print rc.rcChansOut
