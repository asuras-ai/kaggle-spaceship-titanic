#Kaggle Spaceship Titanic excercise

#We import the useful libraries.
#%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)
import pandas as pd
pd.options.display.max_columns = 100
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pylab as plot
params = { 
    'axes.labelsize': "large",
    'xtick.labelsize': 'x-large',
    'legend.fontsize': 20,
    'figure.dpi': 150,
    'figure.figsize': [25, 7]
}
plot.rcParams.update(params)

#Now let's start by loading the training set.
data = pd.read_csv('./data/train.csv')
print(data.shape)
#(8693, 14)

#Pandas allows you to have a sneak peak at your data.
print(data.head())