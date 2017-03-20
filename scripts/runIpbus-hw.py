import os
from optparse import OptionParser

def mycallback(option,opt,value,parser):
    setattr(parser.values, option.dest, value.split(','))

parser = OptionParser()

parser.add_option("-p","--port",type='string',action='callback',
                  callback=mycallback, dest='port')

(options, args) = parser.parse_args()
print options

for i in options.port:
    startudponport="\"/opt/cactus/bin/uhal/tests/DummyHardwareUdp.exe -p "+i+" -v 2\""
    cmd="\'bash -c "+startudponport+" \'"
    cmd="gnome-terminal -e "+cmd
    print cmd
    os.system(cmd)
