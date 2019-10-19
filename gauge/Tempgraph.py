import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#headers = ['ID', 'Date','pH', 'ORP', 'Temp', 'DO', 'EC', 'NaN']
df = pd.read_csv('cpu.csv')

df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))


x = df['Date']
y = df['Temp']


# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()