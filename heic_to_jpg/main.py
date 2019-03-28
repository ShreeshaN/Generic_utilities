# -*- coding: utf-8 -*-
"""
@created on: 28/03/19,
@author: Shreesha N,
@version: v0.0.1

Description:

Sphinx Documentation Status:

..todo::

"""

import glob
import os
from shutil import copyfile


def convert_heic_to_jpg(file, out_filename):
    """
    Calls tifig utility and converts heic file to jpg file
    :param file: Input .HEIC file
    :param out_filename: output file path having .jpg extension
    :return:
    """
    cmd = "tifig -v -p " + file + " " + out_filename
    os.system(cmd)


if __name__ == '__main__':

    # input file paths, output path
    in_path = "/your/input/path/having/heic/files/*"
    out_path = "/Users/shreeshan/Downloads/Last_date_before_engagement_jpg/"

    extension_to_convert = '.HEIC'

    # list all files in folder
    files = glob.glob(in_path)
    l = len(files)

    # iterate over listed files and convert if heic, else just copy to out_path
    for i, file in enumerate(files):
        print("Processing file", i, "/", l)
        filename = file.split("/")[-1]
        if extension_to_convert in file:
            out_filename = out_path + filename + '.jpg'

            # if the file contains extension you are looking for, call convert method
            convert_heic_to_jpg(file, out_filename)
        else:
            copyfile(file, out_path + filename)
