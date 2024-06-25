#from utils import db_connect
#engine = db_connect()

import pandas as pd 
import matplotlib.pyplot as plt

file_path = "../data/raw/AB_NYC_2019.csv"
data = pd.read_csv(file_path)
data.head()