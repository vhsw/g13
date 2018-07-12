#!/usr/bin/python2.7
'''
Simple test script to update G13 LCD with temperature values from lm-sensors

'''

import subprocess, re, os, time

def doCmd( cmd ):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = p.communicate()
    except Exception as e:
        print 'Cannot run sensors. Chech if lm-sensors is installed.'
        print e
        exit(1)
    return out

def get_sensors():

    sensor_lines = doCmd( 'sensors' ).split('\n')
    print( "sensor_lines = %r" % (sensor_lines,) )
    temp_re = re.compile( r'''([a-zA-Z])[a-zA-Z s]+([0-9])\:\s*\+([0-9.]+)[\xc2\xb0C]*C.*''' )
     
    temps = []
    for line in sensor_lines:
        m = temp_re.match(line)
        if m:
            tag, index, value = m.groups()
            print( "%s%s = %s" % (tag, index, value))
            #temps.append( "%s%s:%s" % (tag, index, value) )
            temps.append( "%s" % (value,) )
        # else:
        #   print( "failed to match %r" % (line,))
            
        
    with open( '/tmp/g13-0', 'w') as p:
        p.write( 'pos 0 0 \n' )
        p.write( 'out %s\n' % (' '.join(temps)) )
    
    
def main():
    while 1:
        get_sensors()
        time.sleep(1.0)


if __name__ == "__main__":
    main()


