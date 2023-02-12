import pandas as pd
from entity.entity import DataClassCard

replist=[]

def insert(item :DataClassCard):
    replist.append(item)

def read():
    return replist

def convert_to_dataframe():
    return pd.DataFrame(replist)