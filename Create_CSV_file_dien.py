import librosa
import os
import json
import csv
import numpy as np
import pandas as pd
from scipy.ndimage import label

#path to dataset
DATASET_PATH = r"E:\Dien_Project\data\wav_control\train"

labels = ["Background_noise", "Batden", "Batdieuhoa","Batmaychieu", "Battivi", "Tatden", "Tatdieuhoa","Tatmaychieu", "Tattivi", "Troly"]

def preprocess_dataset(dataset_path):

    # dictionary where we'll store slice_file_name, class, ClassID
    CSVdata = {
        "slice_file_name": [],
        "class": [],
        "ClassID": []
    }
    Num_file = 0
    # loop through all sub-dirs
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # ensure we're at sub-folder level
        if dirpath is not dataset_path:
            for f in filenames:
                file_path = os.path.join(dirpath, f)
                CSVdata["slice_file_name"].append(f)
                CSVdata["class"].append(labels[i-1])
                CSVdata["ClassID"].append(i-1)
                Num_file = Num_file +1
    print(Num_file)
    #save data in csv file
    X = pd.DataFrame(CSVdata)
    X.to_csv("train.csv", columns=["slice_file_name", "class", "ClassID"], index= False)

if __name__ == "__main__":
    preprocess_dataset(DATASET_PATH)
    print("end program")