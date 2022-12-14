import os
import cv2
from PIL import Image


def png2jpg(folder):
    '''
    png2jpg:
        This function changes all images in a folder into JPEG format.
    input: 
        folder - path of the image folder
    '''
    all_files = os.listdir(folder)
    for file in all_files:
        # Convert .png images to jpg images
        if file.endswith('.png'):
            img_png = cv2.imread(f'{folder}/{file}')
            cv2.imwrite(f'{folder}/{file[:-4]}.jpg', img_png, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            os.remove(f'{folder}/{file}')
        # For .jpg or .jpeg images, double-check the format
        elif file.endswith('jpg') or file.endswith('jpeg'):
            img = Image.open(f'{folder}/{file}')
            if img.format != 'JPEG':
                rgb_img = img.convert("RGB")
                rgb_img.save(f'{folder}/{file}')