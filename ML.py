import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import to_datetime
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
from tensorflow.keras.models import Sequential

def data_frame(data):
  df = pd.DataFrame.from_dict(data)
  return df[:-24]

def cleansing(data):
  df['timestamp'] = pd.to_datetime(df['timestamp'])
  df['timestamp'] = df['timestamp'].dt.tz_localize(Jakarta)
  # Menambahkan kolom 'date' dengan tanggal tertentu
  df['date'] = pd.to_datetime('2024-01-01') + pd.to_timedelta(df.index, unit='m')

  # Memformat kolom 'avgPower' sebagai number
  df['power'] = pd.to_numeric(df['avgPower'].str.replace(',', '.'))

  columns_to_drop = ['timestamp']
  df = df.drop(columns=columns_to_drop)

