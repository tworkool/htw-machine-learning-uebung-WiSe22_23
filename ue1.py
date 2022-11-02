import math
import numpy as np
from helpers import visualize_array
import seaborn as sns
import numpy as np
import pandas as pdm

# %%
tit = sns.load_dataset("titanic")
iris = sns.load_dataset("iris")
diamonds = sns.load_dataset('diamonds')
tips = sns.load_dataset('tips')
planets = sns.load_dataset('planets')

class Zscore:
    def __init__(self, np_columns: np.ndarray):
        self.raw_np_columns = np_columns
        self.std_deviation = np.std(np_columns)
        self.mean = np.mean(np_columns)

    def get_score(self):
        z_index_score = abs((self.raw_np_columns - self.mean) / self.std_deviation)
        return z_index_score

    def get_average_score(self):
        score = self.get_score()
        average_score = np.mean(score, axis=0)
        return average_score


score_calc = Zscore(tit["age"])
scores = score_calc.get_score()
print(f"INFO | Scores: {scores}")
avg_scores = score_calc.get_average_score()
print(f"INFO | Average Score: {avg_scores}")
