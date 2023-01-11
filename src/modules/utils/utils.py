import cv2
import shutil
import os


class path():

    def clear_or_create_folder(path: str):
        if os.path.exists(path):
            shutil.rmtree(path)
            os.mkdir(path)
        else:
            os.mkdir(path)

def transform_pixel(img: cv2.Mat, input_num: int, output_num: int):
    target = img.copy()
    target[target == input_num] = output_num
    return target
