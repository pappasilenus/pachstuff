# Program To Read video 
# and Extract Frames 
import cv2
import os
import sys

# Function to extract frames 
def FrameCapture(outPath, inPath, filename): 


    inFullPath =  os.path.join(inPath, filename)
    vidObj = cv2.VideoCapture(inFullPath) 

    # Used to name files
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while (success & (count < 11)): 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 

        # Saves the frames with frame-count
        outFilename = "%s-frame%d.jpg" % (filename, count)
        outFullPath = os.path.join(outPath, outFilename)

        cv2.imwrite(outFullPath, image)

        count += 1


# Driver Code 
if __name__ == '__main__': 
  
    for dirpath, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            FrameCapture(sys.argv[2], dirpath, file) 

