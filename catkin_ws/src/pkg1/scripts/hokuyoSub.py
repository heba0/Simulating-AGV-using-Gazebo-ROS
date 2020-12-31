#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from sensor_msgs.msg import Image, CompressedImage,LaserScan
from cv_bridge import CvBridge
from std_srvs.srv import Empty
import time
import sys
# import struct
# import cv2
# import numpy as np


if __name__ == '__main__':
	print("fffff")
	rospy.init_node('hokuyoSub', anonymous = True, log_level=rospy.DEBUG)  #initilizin subscriber node
	pubLeft = rospy.Publisher('/my_robot/vel_cmd', Float32, queue_size=10)

	pubRight = rospy.Publisher('/my_robot/vel_cmd2', Float32, queue_size=10)
	#listener()
	print("dsdfsf")
	#print(sys.argv)
	# if len(sys.argv) != 5:
	# 	print("111111111111111")
	# 	rospy.logerr("Usage:\n" + sys.argv[0] + "ini_x ini_y end_x end_y")
	# 	print("222222222222222")
	# 	exit(0)
	#print("3333333333333333333")
	# ini_x = int(sys.argv[1])

	# ini_y = int(sys.argv[2])
	# end_x = int(sys.argv[3])
	# end_y = int(sys.argv[4])
	# depth = get_pixels_depth(ini_x, ini_y, end_x, end_y)
	# print ("Result is: " + str(depth))
	# x = int(sys.argv[1])
	# y = int(sys.argv[2])

	img = rospy.wait_for_message("/hokuyo_laser",LaserScan)  #topic
	print(type(img))
	##print("height:  ", img.ranges)
	print(len(img.ranges))
	print((img.ranges[5]))
	# print("width:   ",img.width)
	# print("step:   ",img.step)
	# print("data:   ",type(img.data))


	def move(inp=False):
		if(inp):#default testing data
			print("Moving..")
			pubRight.publish(10)
			pubLeft.publish(10)
		else:

			try:
				outfile = open(	"/home/admin/catkin_ws/src/pkg1/scripts/move.txt", 'r')
			except IOError:
				move()
			with outfile:
				s = outfile.readlines()
				outfile.close()
				data = []
				for line in s:
					i = line.split("\n")
					data.append(i[0])
				if (s!= []):
					pubRight.publish(float(data[0]))
					pubLeft.publish(float(data[1]))

	path= "/home/admin/catkin_ws/src/pkg1/scripts/lidar.txt"
	while(True):

		img = rospy.wait_for_message("/hokuyo_laser",LaserScan)  #topic
		print(type(img))
		#print("height:  ", img.ranges)
		outfile = open(path, 'r+')
		outfile.seek(0)
		outfile.truncate(0)
		line = ''
		count = 0
		for measurment in img.ranges:
				if (count> 309 and count<329):
					line = line +str(measurment)+ '\n'
				count += 1
		outfile.write(line)
		outfile.close()
		print(img.angle_min)
		print(img.angle_max)
		print(img.angle_increment)
		print(img.time_increment)
		print(len(img.ranges))
		print((img.ranges[5]))
		move(True)
		#time.sleep(5000)
		# rospy.wait_for_service('/gazebo/reset_world')
		# reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)

		# reset_world()
		#reset_simulation = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
		# invoke
		#reset_simulation()
		
		#right =
		#left =
		#move(right, left)

	
         