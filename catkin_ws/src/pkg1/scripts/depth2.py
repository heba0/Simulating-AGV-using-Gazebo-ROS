#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
import sys
import struct
import cv2
import numpy as np





def get_pixels_depth(ini_x, ini_y, end_x, end_y, depth_image=None):
	rospy.loginfo(
		"Getting average depth at: " + str((ini_x, ini_y, end_x, end_y)))
	# rospy.loginfo("Waiting for a depth image...")
	# img = rospy.wait_for_message('/xtion/depth/image_raw',
	#                              Image)
	img = depth_image
	rospy.loginfo("The image has size: " + str(img.width) +
				  " width, " + str(img.height) + " height")
	if ini_x < 0:
		rospy.logerr("Can't ask for a pixel depth out of image (ini_x < 0)")
		return None
	if ini_y < 0:
		rospy.logerr("Can't ask for a pixel depth out of image (ini_y < 0)")
		return None
	if end_x > img.width:
		rospy.logerr("Can't ask for a pixel depth out of image (end_x > img.width [%s])" % (
			str(img.width)))
		return None
	if end_y > img.height:
		rospy.logerr("Can't ask for a pixel depth out of image (end_x > img.height [%s])" % (
			str(img.height)))
		return None

	if (img.step / img.width) == 4:
		rospy.loginfo("Got a rectified depth image (4 byte floats)")
	else:
		rospy.loginfo("Got a raw depth image (2 byte integers)")

	# Compute the average of the area of interest
	sum_depth = 0
	pixel_count = 0
	nan_count = 0
	for x in range(ini_x, end_x):
		for y in range(ini_y, end_y):
			pixel = get_pixel_depth(x, y, img)
			# print "Curr pixel is: '" + str(pixel) + "' of type: " + str(type(pixel))
			if pixel != pixel:  # check if nan
				nan_count += 1
			else:
				sum_depth += pixel
				pixel_count += 1

	if pixel_count > 0:
		avg = sum_depth / float(pixel_count)
		rospy.loginfo("Average is: " + str(avg) + " (with " + str(pixel_count) +
					  " valid pixels, " + str(nan_count) + " NaNs)")

		return avg
	else:
		rospy.logwarn("No pixels that are not NaN, can't return an average")
		return None


def get_pixel_depth(x, y, depth_image=None):
	img = depth_image

	if x < 0:
		rospy.logerr("Can't ask for a pixel depth out of image (x < 0)")
		return None
	if y < 0:
		rospy.logerr("Can't ask for a pixel depth out of image (y < 0)")
		return None
	if x > img.width:
		rospy.logerr("Can't ask for a pixel depth out of image (x > img.width [%s])" % (
			str(img.width)))
		return None
	if y > img.height:
		rospy.logerr("Can't ask for a pixel depth out of image (x > img.height [%s])" % (
			str(img.height)))
		return None

	index = int((y * img.step) + (x * (img.step / img.width)))

	if (img.step / img.width) == 4:
		# rospy.loginfo("Got a rectified depth image (4 byte floats)")
		# byte_data = 0.0
		# for i in range(0, 4):
		#     print("indexxx ",index)
		#     print(img.data[index + i])
		#     byte_data += (img.data[index + i])
	 #   print(struct.unpack('f', (img.data[index + 0]+img.data[index + 1]+img.data[index + 2]+img.data[index + 3]))[0])
		byte_data = (img.data[index + 0]+img.data[index + 1]+img.data[index + 2]+img.data[index + 3])
		# print(byte_data, " ", type(byte_data))
		# print(img.data[index + 0], " ", type(img.data[index + 0]))
		#distance = struct.unpack('f', (img.data[index + 0]+img.data[index + 1]+img.data[index + 2]+img.data[index + 3]))[0]
		distance = struct.unpack('f', img.data[0:4])#[0]
		print("Distance  ",distance)
		return distance
	else:
		# rospy.loginfo("Got a raw depth image (2 byte integers) (UNTESTED)")
		# Expecting the data to be an unsigned short representing mm
		if img.is_bigendian:
			distance = struct.unpack('>H', img.data[index:index + 2])[0]
		else:

			distance = struct.unpack('<H', img.data[index:index + 2])[0]
		return distance


def from_compressed_image_to_image(compressed_image, bridge=None):
	# compressed_image must be from a topic compressedDepth (not just compressed)
	# as it's encoded in PNG
	# Code from: https://answers.ros.org/question/249775/display-compresseddepth-image-python-cv2/
	msg = compressed_image
	depth_fmt, compr_type = msg.format.split(';')
	# remove white space
	depth_fmt = depth_fmt.strip()
	compr_type = compr_type.strip()
	if compr_type != "compressedDepth":
		raise Exception("Compression type is not 'compressedDepth'."
						"You probably subscribed to the wrong topic.")

	# remove header from raw data
	depth_header_size = 12
	raw_data = msg.data[depth_header_size:]

	depth_img_raw = cv2.imdecode(np.frombuffer(raw_data, np.uint8),
								 # the cv2.CV_LOAD_IMAGE_UNCHANGED has been removed
								 -1)  # cv2.CV_LOAD_IMAGE_UNCHANGED)
	if depth_img_raw is None:
		# probably wrong header size
		raise Exception("Could not decode compressed depth image."
						"You may need to change 'depth_header_size'!")

	if not bridge:
		bridge = CvBridge()
	return bridge.cv2_to_imgmsg(depth_img_raw, "mono16")


# def callback(data):
#     print("jjjjjjjjjjjjj")
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

# def listener():

#     #In ROS, nodes are uniquely named.If two nodes with the same# name are launched, the previous one is kicked off.The# anonymous = True flag means that rospy will choose a unique# name
# #for our 'listener'
#         #node so that multiple listeners can# run simultaneously.
#     rospy.init_node('depth2', anonymous = True)

#     #rospy.Subscriber("chatter", String, callback)
#     rospy.Subscriber("/camera/depth/image_raw", Image, callback)

#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()

if __name__ == '__main__':
	print("fffff")
	rospy.init_node('depth2', anonymous = True, log_level=rospy.DEBUG)
	#listener()
	print(sys.argv)
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

	img = rospy.wait_for_message('/camera/depth/image_raw',Image)
	print(type(img))
	print("height:  ", img.height)
	print("width:   ",img.width)
	print("step:   ",img.step)
	print("data:   ",type(img.data))
	# bridge = CvBridge()
	# cv_image = bridge.imgmsg_to_cv2(img.data, "bgr8")
	#print(cv_image)
	while True:


		w = 639
		h = 479
		d = get_pixel_depth(w, h, img)
		print (str(w) + ", " + str(h) + ": " + str(d))

		w = 0
		h = 0
		d = get_pixel_depth(w, h, img)
		print (str(w) + ", " + str(h) + ": " + str(d))

		w = 0
		h = 479
		d = get_pixel_depth(w, h, img)
		print (str(w) + ", " + str(h) + ": " + str(d))

		w = 639
		h = 0
		d = get_pixel_depth(w, h, img)
		print (str(w) + ", " + str(h) + ": " + str(d))
	# for w in range(0, 640):
	# 	for h in range(0, 480):
	# 		d = get_pixel_depth(w, h, img)
	# 		if d is not float('nan'):
	# 			print (str(w) + ", " + str(h) + ": " + str(d))
	# 			#print (get_pixel_depth(x, y, img))