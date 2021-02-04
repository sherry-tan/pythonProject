import pandas as pd
# print(os.listdir)
path = '/Users/SherryT/Documents/MachineLearning/MachineLearning/titanic/test.csv'
df = pd.read_csv(path)
print(df.head())