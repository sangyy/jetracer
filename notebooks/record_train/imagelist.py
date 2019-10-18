import os
import glob
import PIL.Image
import cv2
import subprocess

class ImageList():
    def __init__(self, directory):
        self.directory = directory
        self.size = 0
        self.index = 0
        self.images = []
        if not os.path.exists(directory):
            subprocess.call(['mkdir', '-p', directory]) 
        self.size = len(glob.glob(os.path.join(self.directory, '*.jpg')))
        for i in range(0, self.size) :
            if os.path.exists(self.directory+'/'+str(i)+'.jpg'):
                self.images.append(cv2.imread(self.directory+'/'+str(i)+'.jpg',cv2.IMREAD_COLOR))
        self.size = len(self.images)
        
    def get_next(self, step=1):
        self.index = (self.index+step) % self.size
        return self.images[self.index]
                               
    def get_value(self):
#        image = cv2.imread(self.directory+'/'+str(self.index)+'.jpg', cv2.IMREAD_COLOR)
#         image = PIL.Image.fromarray(image)
        return self.images[self.index]
    
    def get_count(self):
        return self.size
         
    def save_entry(self, image):
        filename = '%d.jpg' % (self.size)
        image_path = os.path.join(self.directory, filename)
        cv2.imwrite(image_path, image)
        self.images.append(image)
        self.size += 1

        