import pandas as pd
import random

class RandomDataFrame:
    def __init__(self, df, random_state=None):
        self.df = df
        self.random_state = random_state

    def randomize(self):
        df = self.df
        random_state = self.random_state
        if random_state:
            randomized = df.sample(len(df.index), random_state=random_state)
        else:
            randomized = df.sample(len(df.index))

        return randomized

    def null_count(self):
        df = self.df
        sum = df.isnull().sum().sum()

        return sum