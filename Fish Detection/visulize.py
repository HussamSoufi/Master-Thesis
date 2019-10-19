import pandas as pd
import matplotlib.pyplot as plt
csv_file='fishcount.csv'
data = pd.read_csv(csv_file)

date = data["date"]
count = data["count"]

x=[]
y=[]

x=list(date)
y=list(count)

plt.scatter(x,y)
plt.xlabel('date->')
plt.ylabel('count->')
plt.title('fishcount')
plt.show()