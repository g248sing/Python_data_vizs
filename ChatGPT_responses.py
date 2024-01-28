#importing all useful modules for data vizs

import pandas as pd                    
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns


# Load the CSV file into a Pandas DataFrame
data = pd.read_csv(r'C:\Users\Gurveer Singh\Documents\Source_data.csv')     #Put the source file (Source_data.csv) code here inside the parenthesis


#setting up count variables for responses

counts1 = data['Have you ever used chatGPT'].value_counts()

counts2 = data['Do you think chat GPT is unethical?'].value_counts()

counts3 = data['Do you think ChatGPT is useful?'].value_counts()

counts4 = data['Do you think universities should allow the use of ChatGPT?'].value_counts()

counts5 = data['Do you think ChatGPT is plagiarism?'].value_counts()

counts6 = data['What is your age range?'].value_counts()

counts7 = data['What is your gender?'].value_counts()

counts8 = data['What is your field of work/study? (Faculty)'].value_counts()

counts9 = data['What is your level of education'].value_counts()

labels = ['Yes', 'No']

#Creating plots for responses from survey

fig, axs = plt.subplots(9, 1, figsize= (30, 30))

sns.countplot(x='Have you ever used chatGPT', data=data, order= labels, ax=axs[0])
axs[0].set_title('Have you ever used chatGPT')

sns.countplot(x='Do you think chat GPT is unethical?', data=data, order= labels, ax=axs[1])
axs[1].set_title('Do you think chat GPT is unethical?')

sns.countplot(x='Do you think ChatGPT is useful?', data=data,order= labels, ax=axs[2])
axs[2].set_title('Do you think ChatGPT is useful?')

sns.countplot(x='Do you think universities should allow the use of ChatGPT?', data=data,order= labels, ax=axs[3])
axs[3].set_title('Do you think universities should allow the use of ChatGPT?')

sns.countplot(x='Do you think ChatGPT is plagiarism?', data=data,order= labels, ax=axs[4])
axs[4].set_title('Do you think ChatGPT is plagiarism?')


axs[5].bar(counts6.index, counts6.values, width=0.3)
axs[5].set_title('What is your age range?')
axs[5].set_xlabel(['18-20', '21-25', '26-35', '45+'])
axs[5].set_xlabel('Age Range')
axs[5].set_ylabel('Number of People')

sns.countplot(x='What is your gender?', data=data, order= ['M', 'F', 'Other'], ax=axs[6])
axs[6].set_title('What is your gender?')

axs[7].pie(counts8, labels = counts8.index, autopct='%1.1f%%', startangle=90)
axs[7].legend(title='Field')
axs[7].set_title('What is your field of work/study? (Faculty)')

axs[8].pie(counts9, labels= counts9.index, autopct='%1.1f%%', startangle=90)
axs[8].legend(title='Level of Education')
axs[8].set_title('What is your level of education')


plt.tight_layout()

#plotting the result
plt.show()
