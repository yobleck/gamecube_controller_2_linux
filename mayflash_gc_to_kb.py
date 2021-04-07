import struct, subprocess, json;
from math import copysign;
#subprocess Popen?

"""
first value on line is key code. do not change
second value is gamecude controller button. do not change
third value is keyboard key. change to desired
"""
#load config from file
fc = open("./config.json", "r");
config = json.load(fc);
fc.close();

#open controller input file
f = open("/dev/input/js0", "rb");
f.read(8*19);#idk why this buffer has to be cleared

#event loop
while True:
    gc_input = struct.unpack("IhH", f.read(8));
    print(gc_input);
    
    if gc_input[1] == 1:
        key = config[str(gc_input[2])][1];
        print("press:", key);
        #subprocess.run(["xdotool", "keydown", key]); 
    
    if gc_input[1] in [32767, -32767]:
        key = config[ str( gc_input[2] * int(copysign(1, gc_input[1])) ) ][1]; #deals with joystick quirk
        print("press:", key);
        #subprocess.run(["xdotool", "keydown", key]); 
    
    if gc_input[1] == 0:
        if abs(gc_input[2]) in [1282, 1026]:
            key = config[ str( gc_input[2] * int(copysign(1, gc_input[1])) ) ][1]; #deals with joystick quirk
            print("release", key);
            #subprocess.run(["xdotool", "keyup", key]);
        
        else:
            key = config[str(gc_input[2])][1];
            print("release", key);
            #subprocess.run(["xdotool", "keyup", key]);

#TODO: too much redundant code
