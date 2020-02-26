import os
import pickle
import pandas as pd

os.chdir('C:\\Users\\User\\source\\repos\\delta-hedging')

with open("test.txt", "rb") as fp:   # Unpickling
    b = pickle.load(fp)

pd.set_option('display.max_columns', None)
print(b)