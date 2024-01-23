import cv2
import cv2.aruco as aruco

# Define the ArUco dictionary and parameters
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Create the ArUco marker with the desired ID (e.g., 23)
marker_id = 2
marker_size = 200  # You can adjust the size as needed

# Generate the ArUco marker image
marker_image = aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

# Save the image to a file
output_filename = f"aruco_marker_{marker_id}.png"
cv2.imwrite(output_filename, marker_image)

# Display the generated image
cv2.imshow("ArUco Marker", marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()