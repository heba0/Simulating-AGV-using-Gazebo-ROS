#!/usr/bin/env python3
'''Records scans to a given file in the form of numpy array.
Usage example:
$ ./record_scans.py out.npy'''
import sys
from lidar.rplidar import RPLidar


PORT_NAME = '/dev/ttyUSB1' # should be 1 if running with roomba
NUMBER_BEAMS = 19 #for model

def run(path):
  '''Main function'''
  lidar = RPLidar(PORT_NAME)
  try:
   print('Recording measurments... Press Crl+C to stop.')
   for scan in lidar.iter_scans():
    outfile = open(path, 'r+')
    count = 0
    outfile.seek(0)
    outfile.truncate(0)
    line = ''
    for measurment in scan:
     if (int(measurment[1]) >= 280 or int(measurment[1]) <= 20): #if (((int(measurment[1])+9)% 360) >= 0): #if (((int(measurment[1])+9)% 360) <= 30):
       if (count < NUMBER_BEAMS):
        line = line + '\t'.join(str(v) for v in measurment)
        line = line + '\n'
        count = count + 1
    outfile.write(line )
    outfile.close()
  except KeyboardInterrupt:
   print('Stoping.')
  lidar.stop()
  lidar.disconnect()

if __name__ == '__main__':
    run(sys.argv[1])
