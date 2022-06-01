from ast import increment_lineno
import pandas as pd
import numpy as np

# No warnings about setting value on copy of slice
pd.options.mode.chained_assignment = None

# Display up to 60 columns of a dataframe
pd.set_option('display.max_columns', 60)

# Matplotlib visualization
import matplotlib.pyplot as plt
%matplotlib inline

# Set default font size
plt.rcParams['font.size'] = 24

# Internal ipython tool for setting figure size
from IPython.core.pylabtools import figsize

# Seaborn for visualization
import seaborn as sns
sns.set(font_scale = 2)

# Splitting data into training and testing
from sklearn.model_selection import train_test_split

# Read in data into dataframe.
data = pd.read_csv('data/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')


# Display top of dataframe.
data.head()

# See the column data types and non-missing values.
data.info()

# Replace all occurences of Not Available with numpy.nan (Not A Number).
data = data.replace({'Not Available': np.nan})

# Iterate through the columns.
for col in list(data.columns):
  # Select columns that should be numeric.
  if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in
  col or 'therms' in col or 'gal' in col or 'Score' in col):
    # Convert the data type to float.
    data[col] = data[col].astype(float)

data.head()