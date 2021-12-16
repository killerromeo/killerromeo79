#marks scored in all the cycle tests and visualize the data in a bar plot.
import matplotlib.pyplot as plt
import pandas as pd
cycle_test = {
     'subjects': ['sub 1', 'sub 2', 'sub 3', 'sub 4','sub 5','sub 6'],
     'Marks': [76, 35, 30, 72,88,78]
}
df=pd.DataFrame(cycle_test)
 
# display data
print(df)

#bar charts
x=df.plot(kind='bar',color='r')

plt.title('cycle test')
x.set_ylabel('marks')
x.set_xlabel('subject')

#to display bar chart
plt.show()
