"""
finds the aruco markers in a video feed
Sends signals on whether to send a water blast
sends signals on whether frame needs to move left or right or up or down
"""
"""
TODO: Make Marker for each opposite Target's Aruco Marker
TODO: Only send signal on first instance of detection for each different Aruco marker
"""
# import os
import cv2
import cv2.aruco as aruco
import serial
import time

CENTERED = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

FRIENDLY = 22
ENEMIES = [21,23,24]
arduino = serial.Serial(port='/dev/tty.usbmodem1101', baudrate=115200, timeout=.1)
# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1) #prob need to change com and baudrate


def main():

    # Define the ArUco dictionary and parameters
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

    # Define the detector parameters
    parameters = aruco.DetectorParameters()

    detector = aruco.ArucoDetector(aruco_dict, parameters)

    direction = CENTERED

    # pid = os.fork()
    # if (pid == 0):
    #     exit()


    # Define the video capture device
    cap = cv2.VideoCapture(0)
    marker_found = False
    # Continuously capture and process frames
    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Detect the markers
        corners, ids, rejected = detector.detectMarkers(frame)

        # Draw the detected markers and display the frame
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow("Frame", frame)

        # Print the detected frame coordinates
        # detect which way aruco marker needs to move to be centered
        #i commented that out so i could just get it to send signal when identify something
        if not marker_found and not FRIENDLY in ids:
            print("FOUND!")
            write_read('1')
            marker_found = True
    
        else:
            print("NOT FOUND")
            write_read('0')
            marker_found = False

        # found = 0
        # if ids is not None:

        #     found = 1
        #     for i in range(len(ids)):
        #         print(corners[i][0])
        #         if corners[i][0][0][0] < 200:
        #             direction = LEFT
        #         elif corners[i][0][0][0] > 400:
        #             direction = RIGHT
        #         elif corners[i][0][0][1] < 200:
        #             direction = UP
        #         elif corners[i][0][0][1] > 400:
        #             direction = DOWN
        #         else:
        #             direction = CENTERED

        # print(direction)
        # if(direction == CENTERED):
        #     write_read('1')
        # else:
        #     write_read('0')
        



        # Exit if the user presses the "q" key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
def write_read(x): 
	arduino.write(bytes(x, 'utf-8')) 
	time.sleep(0.05) 
	data = arduino.readline() 
	return data 


#run main
if __name__ == "__main__":
    main()


# """
# finds the aruco markers in a video feed
# """

# import cv2
# import cv2.aruco as aruco

# import serial #ard
# import time #ard

# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1) #ard

# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data


# FRIENDLY = 23
# BAD = 24

# # Define the ArUco dictionary and parameters
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# # Define the detector parameters
# parameters = aruco.DetectorParameters()

# detector = aruco.ArucoDetector(aruco_dict, parameters)

# # Define the video capture device
# cap = cv2.VideoCapture(0)

# # Continuously capture and process frames
# while True:
#     # Capture a frame
#     ret, frame = cap.read()

#     # Detect the markers
#     corners, ids, rejected = detector.detectMarkers(frame)

#     # Draw the detected markers and display the frame
#     frame = aruco.drawDetectedMarkers(frame, corners, ids)
#     cv2.imshow("Frame", frame)

#     num = input("Enter a number: ")
#     value = write_read(num)

#     # Exit if the user presses the "q" key
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break