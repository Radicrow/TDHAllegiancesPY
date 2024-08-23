import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Name': ['Firestar', 'Brambleclaw', 'Jayfeather', 'Ivypool', 'Dovwing', 'Hollyleaf'],
        'Class': ['Fighter', 'Fighter', 'Medicine cat', 'Fighter', 'Specialist', 'Specialist']}

df = pd.DataFrame(data)




specialist_pd = df[df['Class'] == 'Specialist']

plt.figure(figsize=(10, 9))
sns.countplot(x='Class', data=df, color = '#DC143C', alpha = 0.5)
plt.title('Number of Members in Each Class')
plt.xlabel('Class')
plt.ylabel('Number of Members')
plt.xticks(rotation=35)
plt.show()

print(specialist_pd)