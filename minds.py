# %%

import json
import os

import numpy as np
import pandas as pd

import mindsdb
import pymongo

# %%

with open("data/imdb_reviews.json","r") as f:
    data = json.load(f)

# %%

