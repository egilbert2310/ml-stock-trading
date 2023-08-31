

class RSICreator:

    def __init__(self) -> None:
        pass

    def rsi(self, prev_avg_gain, prev_avg_loss, curr_gain, curr_loss):

        rsi = 100 - [100/1+((prev_avg_gain * 13) + curr_gain/(prev_avg_loss * 13) + curr_loss )]


        pass

    def prev_avg_gain(self):
        pass

    def prev_avg_loss(self):
        pass

    def curr_gain(self):
        pass

    def curr_loss(self):
        pass