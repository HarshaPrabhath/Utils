#%% working on windows not tested on other operating systems

import cv2 as cv;
import numpy as np
import matplotlib.pyplot as plt;
import os

example_path = "C:/Users/Harsha/Desktop/img_folder/"
def _select_codec(video_name):
    extension = video_name.split('.')[-1]
    if extension == "mp4":
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
    elif extension == "avi":
        fourcc = cv.VideoWriter_fourcc(*'XVID')
    else:
        print('Unidentified extension to find codec')
        return False
    return fourcc

class recorder():
    def __init__(self, width, height, filename="out_vid.mp4", fps=20):
        self.fourcc = _select_codec(filename)
        self.out_video = cv.VideoWriter(filename, self.fourcc, fps, (width, height))
        self.frame = None
    def record_shot(self, frame, BGR=False):
        if BGR:
            self.frame = frame
        else:
            self.frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        self.out_video.write(self.frame)
    def close(self):
        self.out_video.release()

def image_seq_to_vid(folder, output_vid = 'output_video.mp4', num_images=None):
    # converts a sequence of images in a folder (alphanumeric order) to a video
    # Frame sizes of the images should be the same
    # folder must be specified as absolute path and forward slash to delimit directories. Only the image files should be present in the folder
	# num_images = max number of images taken for making video default None takes all images available
    filenames = os.listdir(folder)
    if not(num_images): num_images = len(filenames)

    def read(folder, file):
        img = cv.imread(os.path.join(folder,file),1)
        height, width, layers = img.shape
        return img, width, height
    
    img, width, height = read(folder, filenames[0])
    recorder1 = recorder(width, height, filename=output_vid)
    for id,i in enumerate(filenames):
        img, w, h = read(folder,i)
        assert(w == width and h == height), "frame size mismatch"
        recorder1.record_shot(img,BGR=True)
        if id + 1 == num_images:
            break
    recorder1.close()
    return

class vid_feed():
    def __init__(self, src):
        # if the soure of the video is a file: mention its absolute path delimited by forward slash
        # if the source is a camera insert its id
        self.cap = cv.VideoCapture(src)
        self.frame = None
    def read(self):
        ret, frame = self.cap.read()
        self.frame = cv.flip(cv.cvtColor(frame, cv.COLOR_BGR2RGB),1)
        return ret, self.frame
    def show_continuous_feed(self):
        # This is only to check the feed closes the capture at the end
        # press key 'q' to end (Press on the viewer window)
        ret = True
        while ret:
            ret, frame = self.read()
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            cv.imshow("frame", frame)
            if cv.waitKey(50) == ord('q'):
                break
        self.close()
    def close(self):
        self.cap.release()
        cv.destroyAllWindows()
    def show_output(self, image, frame_name):
        # This function takes a numpy RGB array of shape = [image_height, image_width, 3] as input and shows the figure
        # This function can be used inside a loop but when the loop terminates, the self.close() method should be called
        img = cv.cvtColor(image, cv.RGB2BGR)
        cv.imshow(frame_name,image)
        cv.waitKey(1)

class cam_feed(vid_feed):
    def __init__(self, cam_id=0):
        super().__init__(cam_id+cv.CAP_DSHOW)
