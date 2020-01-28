 #!/usr/bin/env python2.7

import rospy
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError

import numpy as np
import sys
import math

class Camera:
  def __init__(self):
    rospy.init_node('opencv_camera', anonymous=True)
    self.bridge = CvBridge()
    rospy.loginfo("Init Camera!")

  # Define a function to show the image in an OpenCV Window
  def show_image(self, img):
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Converte BGR (Gazebo) to RGB (OpenCv)
    cv2.namedWindow("Image Window", 1)
    cv2.imshow("Image Window", im_rgb)
    cv2.waitKey(3)

  # Define a callback for the Image message
  def image_callback(self, img_msg):
    cv_image = self.bridge.imgmsg_to_cv2(img_msg, "passthrough")
    img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)

    import pdb; pdb.set_trace()
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)

    if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
      _a, b, _c = circles.shape
      for i in range(b):
        cv2.circle(cv_image, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(cv_image, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA)  # draw center of circle
  
    self.show_image(cv_image)

  def run(self):
    self.sub_image = rospy.Subscriber("/diff/camera_top/image_raw", Image, self.image_callback)

if __name__ == "__main__":
  cam = Camera()
  cam.run()
  while not rospy.is_shutdown():
    rospy.spin()