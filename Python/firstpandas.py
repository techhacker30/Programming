#!/bin/python3

import pandas as pd

data = {1: "Bulbasaur", 2: "Ivysaur", 3:"Venusaur", 4:"Charmander", 5: "Charmeleon", 6: "Charizard"}

series = pd.Series(data)

print(series)
