from Perceptron import Perceptron
from DataSetUtils import get_data

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

p = Perceptron(data=train_data,
               weights=START_WEIGHTS,
               bias=BIAS,
               learning_rate=LEARNING_RATE,
               max_epochs=MAX_EPOCHS)

converged, epoch, wheights = p.start()

if converged:
    print(f"Convergiu em {epoch} épocas com os pesos", wheights)
    
    for t in test_data:
        predicted,expected = p.test_weights(t)
        
        if predicted != expected:
            print(f"Erro ao testar perceptron, resultado esperado: {expected} e encontrou:{predicted}")
    
else:
    print(f"Não foi possível convergir após {epoch} épocas")
