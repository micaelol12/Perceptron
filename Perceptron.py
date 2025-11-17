from pandas import DataFrame

class Perceptron:
   
    def __init__(self, data: list, wheights: list[float]):
        self.inputs = data
        self.wheights = wheights
        self.max_epochs = float('inf')
        self.converged = False
        self.epoch = 0
        self.bias = 1
        self.n = 0.1

    def start(self):
        while self.epoch < self.max_epochs and not self.converged:
            self.run_epoch()
            self.epoch += 1

        if self.converged:
            print(f"Convergiu em {self.epoch} épocas com os pesos", self.wheights)
        else:
            print("Não foi possível convergir")

    def run_epoch(self):
        corections = 0

        for row in self.inputs:
            x = row[:-1]         
            predicted_y = self.calculate_y(x)
            expected_y = row[-1]  

            if predicted_y != expected_y:
                self.correct_wheights(expected_y, predicted_y, x)
                corections += 1

        if corections == 0:
            self.converged = True
        
        print(f"Época {self.epoch} finalizada.Correções: {corections}. Pesos atualizado para: {self.wheights}")

    def calculate_y(self, values):
        z = self.calculate_z(values)

        return 0 if z < 0 else 1

    def calculate_z(self, values):
        z = 0

        for i in range(len(values)):
            z += values[i] * self.wheights[i]

        z += self.bias

        return z

    def correct_wheights(self, y_expected, y_predicted, values):
        err = y_expected - y_predicted

        for i in range(len(self.wheights)):
            self.wheights[i] = self.wheights[i] + (self.n * err * values[i])

        self.bias = self.bias + self.n * err
