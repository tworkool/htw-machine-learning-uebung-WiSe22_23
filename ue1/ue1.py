import math
import numpy as np
import seaborn as sns
import numpy as np
import pandas as pdm
import pprint
import matplotlib.pyplot as plt

# %%
metadata = [
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


def analyse_datasets(datasets_metadata):
    analysed_dataset = {}
    raw_data_from_datasets = {}
    for dm in datasets_metadata:
        print(f"INFO *** ---Dataset: {dm['name']}---")
        # LOAD DATA
        if dm['name'] in analysed_dataset:
            raw_data = raw_data_from_datasets[dm['name']]
        else:
            try:
                raw_data = sns.load_dataset(dm['name'])
                analysed_dataset[dm['name']] = {
                    "measurements": [],
                    "raw_data": "WRITE 'raw_data' HERE TO DISPLAY"
                }
                raw_data_from_datasets[dm['name']] = raw_data
            except Exception:
                print(f"ERROR *** Could not load dataset")

        # DO CALCULATIONS
        measurement = {
            "params": dm['params'],
            "data": {}
        }
        for p in dm['params']:
            print(
                f"INFO *** ------Parameter in Dataset: {dm['name']}/{p}------")
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
        analysed_dataset[dm['name']]['measurements'].append(measurement)

    return analysed_dataset, raw_data_from_datasets


# analyse multiple tables
""" al_ds, rd_ds = analyse_dataset(metadata)
pprint.pprint(al_ds) """
# print(rd_ds) # print raw data from datasets

# analyse 2 tables and visualize
titanic_data = sns.load_dataset("titanic")
print(titanic_data.head())
titanic_data_score = Zscore(titanic_data["age"])
scores = titanic_data_score.get_score()
print(f"INFO *** Scores: {scores}")
avg_scores = titanic_data_score.get_average_score()
print(sns.scatterplot(data=titanic_data, x="age", y="deck",
      style="survived", hue="sex", size="survived"))

plt.show()
