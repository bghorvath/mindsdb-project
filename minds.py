# %%

import pandas as pd
import mindsdb
import os
import requests
import pymongo

# %%

imdb_url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

save_filename = "aclImdb_v1.tar.gz"
if not os.path.exists(save_filename):
    requests.urlretrieve(imdb_url, save_filename)

imdb_folder = "aclImdb"
if not os.path.exists(imdb_folder):
    with tarfile.open(save_filename) as tar:
        tar.extractall()

