# get creation time of files in a directory
# rename all the files by adding the date of creation

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import pathlib
import os
import time
import shutil
import argparse

parser = argparse.ArgumentParser(description = "CLI tool for sorting files by\
                                                creation time")

parser.add_argument("--path", type = str, help = "The path to the directory.")

args = parser.parse_args()

media_dir = pathlib.Path(f"{args.path}")

if "files_with_dates" not in os.listdir():
    os.mkdir(f"./files_with_dates")
else:
    print("Files with dates directory already exists")

for filename in media_dir.iterdir():
    if filename.is_file():
        if filename.suffix.lower() in [".jpg", ".png", ".svg", ".jpeg"]:
            im = Image.open(filename)
            exif = im.getexif()
            creation_time = exif.get(36867)
            if creation_time:
                creation_time = creation_time[:10].replace(":", "-") + " " + creation_time[11:]
            if type(creation_time)!=str:
                creation_time = time.gmtime(os.path.getmtime(filename))
                creation_time = f"{creation_time.tm_year}-{creation_time.tm_mon:02d}-{creation_time.tm_mday:02d} {creation_time.tm_hour:02d}:{creation_time.tm_min:02d}:00"
            print(creation_time)
            new_filename = creation_time + filename.suffix
            new_filepath = pathlib.Path("files_with_dates") / new_filename
            shutil.copy(filename, new_filepath)
        else:
            creation_time = time.gmtime(os.path.getmtime(filename))
            creation_time = f"{creation_time.tm_year}-{creation_time.tm_mon:02d}-{creation_time.tm_mday:02d} {creation_time.tm_hour:02d}:{creation_time.tm_min:02d}:00"
            print(creation_time)
            new_filename = creation_time + filename.suffix
            new_filepath = pathlib.Path("files_with_dates") / new_filename
            shutil.copy(filename, new_filepath)
        

print("A folder named 'files_with_dates' was created in the current directory.")
