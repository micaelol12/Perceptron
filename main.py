import pandas as pd
import numpy as np

from Perceptron import Perceptron

DATASET_PATH = "Dataset/breast-cancer-wisconsin.data"
CLEAN_DATASET_PATH = "Dataset/breast-cancer-wisconsin-clean.csv"

COL_NAMES= [
    "clump_thickness", # 0
    "uniformity_cell_size",# 1
    "uniformity_cell_shape",# 2
    "marginal_adhesion",# 3
    "single_epithelial_size",# 4
    "bare_nuclei",# 5
    "bland_chromatin",# 6
    "normal_nucleoli",# 7
    "mitoses",# 8
    "class"
]

WHEIGHTS = [
    0.1,
    0.2,
    0.3,
    0.4,
    0.3,
    0.2,
    0.1,
    0.3,
    0.4
]

def clear_dataset():
    df = pd.read_csv(DATASET_PATH, header=None)
    df = df.replace("?", np.nan)
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df.dropna()
    df.iloc[:, 10] = df.iloc[:, 10].replace({2: 0, 4: 1}).astype(int)
    
    df.drop(df.columns[0], axis=1, inplace=True)
    
    df.to_csv(CLEAN_DATASET_PATH, index=False,header=None)

clear_dataset()

df = pd.read_csv(CLEAN_DATASET_PATH, header=None)
p = Perceptron(df,WHEIGHTS)
p.start()