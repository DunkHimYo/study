import matplotlib.pyplot as plt, pandas as pd

names=['Bob','Jessica','Mary','John','Mel']
births=[968,155,77,578,973]
custom=[1,5,25,13,23232]

BabyDataSet=list(zip(names,births))
df=pd.DataFrame(data=BabyDataSet,columns=['Names','Births'])

y=df['Births']
x=df['Names']

plt.bar(x,y)
plt.xlabel('Names')
plt.ylabel('Births')
plt.title('Bar plot')
plt.show()
