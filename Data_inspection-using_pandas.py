import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

print(df['Age'].mean())

print(df['City'].value_counts())

print(df[df['Age'] > 30])

print(df[df['City'] == 'New York'])

print(df.sort_values(by='Age'))

print(df.sort_values(by='Name', ascending=False))

print(df.isnull().sum())

print(df['Age'].unique())

print(df['City'].nunique())

print(df['City'].value_counts(normalize=True))

print(df.groupby('City')['Age'].mean())

print(df.groupby('City')['Age'].agg(['mean', 'min', 'max']))

print(df.pivot_table(values='Age', index='City', aggfunc='mean'))

print(df.corr(numeric_only=True))

print(df['Age'].plot(kind='hist', bins=5, title='Age Distribution'))

import matplotlib.pyplot as plt

df.plot(kind='scatter', x='Age', y='Name', title='Age vs Name')
#df.plot(kind='hist', x='Age', y='Name', title='Age vs Name')

plt.show()


