from Perceptron import Perceptron
from DataSetUtils import clear_dataset,get_data

DATASET_PATH = "Dataset/breast-cancer-wisconsin.data"
CLEAN_DATASET_PATH = "Dataset/breast-cancer-wisconsin-clean.csv"
LINEAR_DATASET_PATH = "Dataset/linear_dataset.csv"

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

clear_dataset(DATASET_PATH,CLEAN_DATASET_PATH)
data = get_data(LINEAR_DATASET_PATH)
p = Perceptron(data,WHEIGHTS)
p.start()