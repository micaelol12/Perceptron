from Perceptron import Perceptron
from utils import get_data,test_acurracy

DATASET_PATH = "Dataset/breast-cancer-linear.csv"
START_WEIGHTS = [
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
BIAS = 1 
LEARNING_RATE = 1
MAX_EPOCHS = 200

data = get_data(DATASET_PATH)
test_data = data[-10:]
train_data = data[:-10]

perceptron = Perceptron(data=train_data,
               weights=START_WEIGHTS,
               bias=BIAS,
               learning_rate=LEARNING_RATE,
               max_epochs=MAX_EPOCHS)

converged, epoch, wheights = perceptron.train()

if converged:
    accuracy = test_acurracy(perceptron,test_data)
    print(f"Convergeu em {epoch} épocas. A taxa de acerto do Perceptron é: {accuracy:.2f} ({(accuracy * 100):.2f}%)")
else:
    print(f"Não foi possível convergir após {epoch} épocas")
