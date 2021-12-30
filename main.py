class Neuron:
    def __init__(self):
        self.weigth = 0.01
        self.last_error = 1.1
        self.smoothing = 0.00001

    def get_last_error(self):
        return self.last_error

    def get_smoothing(self):
        return self.smoothing

    def get_weight(self):
        return self.weigth

    def procces_input_data(self, input_data):
        return input_data * self.weigth

    def train(self, input, expectedResult):
        result_now = input * self.weigth

        self.last_error = expectedResult - result_now
        correction = self.last_error / result_now
        correction = correction * self.smoothing

        self.weigth += correction

    def check_training(self):
        if(self.last_error > self.smoothing or self.last_error < -self.smoothing):
            return True
        else:
            False

neuron = Neuron()

input_data = 10
expected_result = 6.21

print(neuron.procces_input_data(input_data))

iteration = 1
while(neuron.check_training()):
    neuron.train(input_data, expected_result)
    print(f"Iteration {str(iteration)} | Weight {str(neuron.get_weight())}")
    iteration += 1

print("--Successful training--")
print(neuron.get_weight())
print(neuron.procces_input_data(input_data))

