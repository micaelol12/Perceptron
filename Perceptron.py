class Perceptron:
    def __init__(self, data: list[float], weights: list[float], bias: float, learning_rate: float, max_epochs: int):
        self.inputs = data
        self.weights = weights
        self.max_epochs = max_epochs
        self.learning_rate = learning_rate
        self.bias = bias

        self.converged = False
        self.epoch = 0

    def train(self):
        while self.epoch < self.max_epochs and not self.converged:
            self.__run_epoch()
            self.epoch += 1

        return (self.converged, self.epoch, self.weights)

    def test_weights(self, values):
        x = values[:-1]
        predicted_y = self.__calculate_y(x)
        expected_y = values[-1]

        return predicted_y, expected_y

    def __run_epoch(self):
        corections = 0

        for row in self.inputs:
            x = row[:-1]
            predicted_y = self.__calculate_y(x)
            expected_y = row[-1]

            if predicted_y != expected_y:
                self.__correct_weights(expected_y, predicted_y, x)
                corections += 1

        if corections == 0:
            self.converged = True

    def __calculate_y(self, values):
        z = self.__calculate_z(values)

        return 0 if z < 0 else 1

    def __calculate_z(self, values):
        z = 0

        for i in range(len(values)):
            z += values[i] * self.weights[i]

        z += self.bias

        return z

    def __correct_weights(self, y_expected, y_predicted, values):
        err = y_expected - y_predicted

        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + \
                (self.learning_rate * err * values[i])

        self.bias = self.bias + self.learning_rate * err
