class Start:
    explanation = "We are testing the ..."
    @staticmethod
    def start():
        print("-"*100)
        print("Start Coursework")
        print("For this run: ")
        print(Start.explanation)
        Hyperparam.print_hyperparameters()
        print("-"*100)

class Finish:
    @staticmethod
    def finish():
        print("-"*100)
        print("End Coursework")
        print("For this run: ")
        print(Start.explanation)
        Hyperparam.print_hyperparameters()
        print("-"*100)

class Hyperparam:
    batch_size = 256
    num_epochs = 1
    lrate = 1e+0
    weight_decay = 1e-3

    @staticmethod
    def print_hyperparameters():
        print("** Hyperparameters")
        print("batch size = ", Hyperparam.batch_size)
        print("learning rate = ", Hyperparam.lrate)
        print("Weight decay = ", Hyperparam.weight_decay)