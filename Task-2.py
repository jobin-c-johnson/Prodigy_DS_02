import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(r"C:\Users\ASUS\Downloads\gender_submission.csv")
df2 = pd.read_csv(r"C:\Users\ASUS\Downloads\test.csv")

df = pd.concat([df1, df2], axis=1).reindex(df1.index)
df=df.dropna(subset=['Age'])
df.drop(['Cabin', 'Embarked'], axis=1, inplace=True)


plt.figure(figsize=(17, 10))

# Graph one
plt.subplot(2, 2, 1)
plt.pie(df['Survived'].value_counts(), labels=['Not Survived', 'Survived'], autopct='%1.1f%%', startangle=90)
plt.title('Overall Survival Distribution')

# Graph Two
counts = pd.crosstab(df['Pclass'], df['Survived'])
not_survived = counts[0].tolist()
survived = counts[1].tolist()
counts_flat = not_survived + survived
print(counts)
labels = [f'Class {Pclass} - Not Survived' for Pclass in counts.index] + \
         [f'Class {Pclass} - Survived' for Pclass in counts.index]

plt.subplot(2, 2, 2)
plt.pie(counts_flat, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Survival Distribution by Passenger Class')

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]

age_survived = df[df['Survived'] == 1]['Age']
age_not_survived = df[df['Survived'] == 0]['Age']

# Graph Three
plt.subplot(2, 2, 3)
plt.hist(age_survived, bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Survived Passengers')

# Graph Four
plt.subplot(2, 2, 4)
plt.hist(age_not_survived, bins=bins, edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Not Survived Passengers')


plt.tight_layout()
plt.show()
