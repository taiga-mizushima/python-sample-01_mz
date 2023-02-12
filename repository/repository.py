import pandas as pd
from entity.entity import DataClassCard

replist=[]

def insert(item :DataClassCard):
    replist.append(item)

def read():
    return replist

def class_to_frame():
    return pd.DataFrame(replist)

def frame_to_class(df :pd.DataFrame):
    return df.apply(lambda row: DataClassCard(**row), axis=1)