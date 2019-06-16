import urllib
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

ISIC_ENDPOINT = 'https://isic-archive.com/api/v1/image/{}/download'
OUT_PATH = dir_path + '/limages/{}.jpg'

if not os.path.exists(dir_path+'/limages'):
    os.makedirs('limages')

ISIC_ENDPOINT_META = 'https://isic-archive.com/api/v1/image/{}/'
OUT_PATH_META  = dir_path +'/ldescript/{}.json'

if not os.path.exists(dir_path+'/ldescript'):
    os.makedirs('ldescript')

def download_image(image_id,name):
    print(ISIC_ENDPOINT.format(image_id))
    img = urllib.request.urlopen(ISIC_ENDPOINT.format(image_id))

    with open(OUT_PATH.format(name), 'wb') as f:
        f.write(img.read())

def download_meta(image_id,name):
    print(ISIC_ENDPOINT_META.format(image_id))
    img = urllib.request.urlopen(ISIC_ENDPOINT_META.format(image_id))

    with open(OUT_PATH_META.format(name), 'wb') as f:
        f.write(img.read())

import pandas as pd

data = pd.read_csv('csv.csv')
ids,names= data['id'],data['name']


count=-1
for i in ids:
    count+=1
    print(i,names[count])

    if os.path.exists(dir_path+'/limages/'+names[count]+".jpg"):
        continue

    if os.path.exists(dir_path+'/ISIC-images/Segmentation/'+names[count]+"_segmentation.png"):
        download_image(i,names[count])
        download_meta(i,names[count])
    else:
        continue 

