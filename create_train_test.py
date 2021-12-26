import os
import pathlib
import matplotlib.pyplot as plt
import shutil
import numpy as np

if "preprocessed" not in os.listdir("./data"):
    os.mkdir("./data/preprocessed")
    os.mkdir("./data/preprocessed/train")
    os.mkdir("./data/preprocessed/test")
    os.mkdir("./data/preprocessed/train/keep_it")
    os.mkdir("./data/preprocessed/train/dont_keep_it")
    os.mkdir("./data/preprocessed/test/keep_it")
    os.mkdir("./data/preprocessed/test/dont_keep_it")
else:
    print("Preprocessed directory already exists")

keepit_images = list(pathlib.Path("./data/raw/keep_it").iterdir())
dont_keepit_images = list(pathlib.Path("./data/raw/dont_keep_it").iterdir())

random_keepit_images = np.random.choice(keepit_images, size=int(len(keepit_images)*0.2))
random_dont_keepit_images = np.random.choice(list(dont_keepit_images), size=int(len(list(dont_keepit_images))*0.2))

for image in random_keepit_images:
    shutil.copy(str(image), "./data/preprocessed/test/keep_it")

for image in random_dont_keepit_images:
    shutil.copy(str(image), "./data/preprocessed/test/dont_keep_it")

for image in pathlib.Path("./data/raw/keep_it/").iterdir():
    shutil.copy(str(image), "./data/preprocessed/train/keep_it")

for image in pathlib.Path("./data/raw/dont_keep_it/").iterdir():
    shutil.copy(str(image), "./data/preprocessed/train/dont_keep_it")







