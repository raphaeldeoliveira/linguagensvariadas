# importamos as bibliotecas. O numpy é usado junto do pandas
import numpy as np
import pandas as pd

s = pd.Series()
print(s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)