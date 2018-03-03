import os
import os.path
import numpy as np
from PIL import Image

if __name__ == '__main__':
    def image_classifier(path):
        valid_images = [".jpg", ".gif", ".png", ".tga"]
        imgs = []
        for f in os.listdir(path):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in valid_images:
                continue
            img = Image.open(os.path.join(path, f))
            img = np.array(img.resize((64, 64), Image.ANTIALIAS))
            imgs.append(img)

        return np.array(imgs)

    # converts all images in a particular directory to a 64*64*3
    # (3 for the rgb value of image) dimension vector
    # use - in machine learning and image processing
