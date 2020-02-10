#%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
plt.style.use
plt.rcParams['figure.figsize'] = (15, 5)

bike_stats = pd.read_csv('data/bysykkel/trips-2016.10.1-2016.10.31.csv', sep=',')


bike_stats_types = pd.read_csv('data/bysykkel/trips-2016.10.1-2016.10.31.csv', sep=',', parse_dates=['Start time', 'End time'])

bike_stats_types["Start time"].dtype == np.dtype('datetime64[ns]')

bike_stats_types['Start station'].head(100).plot()
plt.show()
