import sys
from lidar.rplidar import RPLidar
from time import sleep
from roomba.pyroombaadapter import PyRoombaAdapter

PORT_NAME_LIDAR = '/dev/ttyUSB1'
PORT_NAME_ROOMBA = "/dev/ttyUSB0"

def run(path):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    outfile = open(path, 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measurments():
            line = '\t'.join(str(v) for v in measurment)
            outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    outfile.close()

if __name__ == '__main__':
    run(sys.argv[1])
