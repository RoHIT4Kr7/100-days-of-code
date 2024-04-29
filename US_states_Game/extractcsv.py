import pandas as pd


class StateData:

    def __init__(self):
        data = pd.read_csv("50_states.csv")
        self.list_of_states = data["state"].tolist()
        self.list_of_xc = data["x"].tolist()
        self.list_of_yc = data["y"].tolist()
