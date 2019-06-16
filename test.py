import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import json
import glob

from mrcnn.config import Config
import mrcnn.utils as utils
import mrcnn.model as modellib
import mrcnn.visualize as visualize

np.set_printoptions(threshold=np.inf)

# path of the trained model
dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = dir_path + "/models/"
MODEL_PATH = MODEL_DIR +"/moles20190615T1047/mask_rcnn_moles_0025.h5"

class CocoConfig(Config):
    ''' 
    MolesConfig:
        Contain the configuration for the dataset + those in Config
    '''
    NAME = "moles"
    NUM_CLASSES = 1 + 2 # background + (malignant , benign)
    IMAGE_MIN_DIM = 128
    IMAGE_MAX_DIM = 128
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    DETECTION_MAX_INSTANCES = 3

# create and instance of config
config = CocoConfig()

# take the trained model
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
model.load_weights(MODEL_PATH, by_name=True)

# background + (malignant , benign)
class_names = ["BG", "malignant", "benign"]
'''
img = cv2.imread(dir_path +"/ISIC_0034262.jpg")
img = cv2.resize(img, (128, 128))
if img.all():
   print("No Image")
#ground truth of the class
print(data["meta"]["clinical"]["benign_malignant"])
''' 

# predict the mask, bounding box and class of the image
for file in os.listdir(dir_path +"/test"):
    print(file)
    img = cv2.imread(dir_path +"/test/"+file)
    img = cv2.resize(img, (128, 128))
    r = model.detect([img])[0]
    print(r['class_ids'] , class_names , r['scores'])
    visualize.display_instances(img, r['rois'], r['masks'], r['class_ids'],
                                class_names, r['scores'])
