import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from matplotlib.dates import YearLocator, MonthLocator, DayLocator, DateFormatter
from numpy import corrcoef, reshape
import pandas as pd


#This code will read in the weather data and sku data and plot various data in a variety of formats

#read in the data

data_en = pd.read_excel('Quant\ Assessment.xlsx', sheet_name=0, header=14, skiprows=14)
PRINT, data_en.info()