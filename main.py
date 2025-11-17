from Perceptron import Perceptron
from DataSetUtils import clear_dataset, get_data

DATASET_PATH = "Dataset/breast-cancer-wisconsin.data"
CLEAN_DATASET_PATH = "Dataset/breast-cancer-wisconsin-clean.csv"
LINEAR_DATASET_PATH = "Dataset/linear_dataset.csv"
START_WHEIGHTS = [
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

#clear_dataset(DATASET_PATH, CLEAN_DATASET_PATH)

data = get_data(LINEAR_DATASET_PATH)
test_data = data[-10:]
train_data = data[:-10] 

p = Perceptron(data=train_data,
               wheights=START_WHEIGHTS,
               bias=1,
               n=0.1,
               max_epochs=100)

converged, epoch, wheights = p.start()

if converged:
    print(f"Convergiu em {epoch} épocas com os pesos", wheights)
    
    for t in test_data:
        predicted,expected = p.test_wheights(t)
        
        if predicted != expected:
            print(f"Erro ao testar perceptron, resultado esperado: {expected} e encontrou:{predicted}")
    
else:
    print("Não foi possível convergir")
