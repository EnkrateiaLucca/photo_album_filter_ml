# labels: keep it, don't keep it, do nothing (because it'a video)
# loop through the images in the files_with_dates folder
# label them 
# automatically move them to the folder with the same name as the label
import os
import pathlib
import matplotlib.pyplot as plt
import shutil

if "data" not in os.listdir():
    os.mkdir("./data")
    os.mkdir("./data/raw")
    os.mkdir("./data/raw/keep_it")
    os.mkdir("./data/raw/dont_keep_it")
else:
    print("Data directory already exists")

media_dir = pathlib.Path("./files_with_dates")

for file in media_dir.iterdir():
    if file.suffix.lower() in [".jpg", ".png", ".svg", ".jpeg"]:
        try:
            plt.imshow(plt.imread(str(file)))
            plt.show()
            label = input("Keep it? (y/n)")
            if label == "y":
                shutil.move(str(file), "./data/raw/keep_it")
            elif label == "n":
                shutil.move(str(file), "./data/raw/dont_keep_it")
            else:
                print("Invalid input, skipping...")
        except:
            pass



