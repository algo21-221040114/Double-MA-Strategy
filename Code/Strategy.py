from Get_data import DataHandler
import numpy as np
import pandas as pd


class double_ma:

    def __init__(self, short_len, long_len):
        self.short_len = short_len
        self.long_len = long_len
        self.short_ma = 0
        self.long_ma = 0
        self.signal = []

    def create_signal(self, dataset):
        for i in range(dataset.shape[1]):
            self.short_ma = np.mean(dataset[-self.short_len:, i])
            self.long_len = np.mean(dataset[-self.long_len:, i])
            # 上穿
            if self.short_ma
            # 下穿
