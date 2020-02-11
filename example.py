from OpenCV_utils import *
import matplotlib.pyplot as plt
# First instantiate the respective reader: "vid_feed", "recorder" or "cam_feed" with parameters required and then use respective methods to retrieve relevant outputs 
# Always remember to close the cam, video, or recorder


# Uncomment this snippet to view the cam feed 
"""
cam = cam_feed()
cam.show_continuous_feed() #press q to quit (this method closes cam by definition)
"""

# Uncomment the following to view a single shot of the cam feed
"""
cam1 = cam_feed()
_, img1 = cam1.read()
cam1.close()
plt.imshow(img1)
plt.show()
"""

# Uncomment the following to record 100 frames of the default cam feed
"""
rec = recorder(640,480) # resolution of web cam
cam2 = cam_feed()
for i in range(100):
    _, img2 = cam2.read()
    rec.record_shot(img2)
cam2.close()
rec.close()
"""

#Uncomment the following to save a set of 100 images in an image folder as a video
"""
image_seq_to_vid(example_path, output_vid="v1test.avi")#, num_images=100)
"""
