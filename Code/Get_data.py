import pandas as pd
from pandas_datareader import data


class DataHandler:

    def __init__(self, stock_basket, start_date, end_date):
        self.symbols = stock_basket
        self.start = start_date  # the earliest date for create ma variable
        self.end = end_date  # the last trading day
        self.data_close = pd.DataFrame()

    def get_data(self):
        # Use pandas_reader.data.DataReader to load the desired data
        for symbol in self.symbols:
            df = data.DataReader(symbol, 'yahoo', self.start, self.end)
            self.data_close[symbol] = pd.DataFrame(df['Close'])

        return self.data_close


# class processing:
#     # 后续改进：如果停牌……
#     def __init__(self):

