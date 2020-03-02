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