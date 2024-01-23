"""
finds the aruco markers in a video feed
"""

import cv2
import cv2.aruco as aruco

import serial #ard
import time #ard

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1) #ard

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


FRIENDLY = 23
BAD = 24

# Define the ArUco dictionary and parameters
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Define the detector parameters
parameters = aruco.DetectorParameters()

detector = aruco.ArucoDetector(aruco_dict, parameters)

# Define the video capture device
cap = cv2.VideoCapture(0)

# Continuously capture and process frames
while True:
    # Capture a frame
    ret, frame = cap.read()

    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(frame)

    # Draw the detected markers and display the frame
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow("Frame", frame)

    num = input("Enter a number: ")
    value = write_read(num)

    # Exit if the user presses the "q" key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break