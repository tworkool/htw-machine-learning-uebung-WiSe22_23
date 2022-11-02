import math
import numpy as np
from helpers import visualize_array
import seaborn as sns
import numpy as np
import pandas as pdm
import pprint

# %%
dataset_metadata = [
    {"name": "titanic", "params": ['parch', 'age', 'fare']},
    {"name": "iris", "params": [
        'sepal_length', 'sepal_width', 'petal_length']},
    {"name": "planets", "params": [
        'mass', 'distance', 'orbital_period', 'year']},
    {"name": "car_crashes", "params": ['total', 'speeding', 'alcohol']},
    {"name": "iris", "params": [
        'petal_length', 'petal_width', 'sepal_length']},
    {"name": "car_crashes", "params": [
        'not_distracted', 'no_previous', 'ins_premium']},
    {"name": "tips", "params": ['total_bill', 'tip', 'size']},
]

datasets = {

}

datasets_rd = {

}


class Zscore:
    def __init__(self, np_columns: np.ndarray):
        self.raw_np_columns = np_columns
        self.std_deviation = np.std(np_columns)
        self.mean = np.mean(np_columns)

    def get_score(self):
        z_index_score = abs(
            (self.raw_np_columns - self.mean) / self.std_deviation)
        return z_index_score

    def get_average_score(self):
        score = self.get_score()
        average_score = np.mean(score, axis=0)
        return average_score


for dm in dataset_metadata:
    print(f"INFO *** ---Dataset: {dm['name']}---")
    # LOAD DATA
    if dm['name'] in datasets:
        raw_data = datasets_rd[dm['name']]
    else:
        try:
            raw_data = sns.load_dataset(dm['name'])
            datasets[dm['name']] = {
                "measurements": [],
                "raw_data": "WRITE 'raw_data' HERE TO DISPLAY"
            }
            datasets_rd[dm['name']] = raw_data
        except Exception:
            print(f"ERROR *** Could not load dataset")

    # DO CALCULATIONS
    measurement = {
        "params": dm['params'],
        "data": {}
    }
    for p in dm['params']:
        print(f"INFO *** ------Parameter in Dataset: {dm['name']}/{p}------")
        try:
            score_calc = Zscore(raw_data[p])
            scores = score_calc.get_score()
            # print(f"INFO *** Scores: {scores}")
            avg_scores = score_calc.get_average_score()
            print(f"INFO *** Average Score: {avg_scores}")

            measurement['data'] = {
                "param_name": p,
                "scores": "WRITE 'scores' HERE TO DISPLAY SCORE TABLE",
                "avg_scores": avg_scores
            }
        except Exception:
            print(f"ERROR *** Could not load param for dataset")
    datasets[dm['name']]['measurements'].append(measurement)

pprint.pprint(datasets)
#print(datasets_rd) # print raw data from datasets
