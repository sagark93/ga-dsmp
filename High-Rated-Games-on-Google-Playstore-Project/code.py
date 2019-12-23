# --------------
import matplotlib.pyplot as plt
import pandas as pd 
data = pd.read_csv(path)

plt.hist(data["Rating"].dropna(),10)
plt.show()

data = data[data["Rating"] <= 5]
plt.hist(data["Rating"].dropna(),10)
plt.show()


# --------------
# code starts here

total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null] , keys = ['Total','Percent'], axis = 1)

print(missing_data)

data = data.dropna(how = 'any')

total_null_1 = data.isnull().sum()

percent_null_1 = (total_null/data.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1] , keys = ['Total','Percent'], axis = 1)

print(missing_data_1)


# code ends here


# --------------

#Code starts here
import seaborn as sns


g = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
g.set_xticklabels(rotation=30)
plt.title('Rating vs Category [BoxPlot]')


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

# Removing , and + from Installs column

data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','')

print(data['Installs'].value_counts())

data['Installs'] =pd.to_numeric(data['Installs'])
le = LabelEncoder()

data["Installs"] = le.fit_transform(data["Installs"])

sns.regplot(x = "Installs", y = "Rating", data= data)

plt.title('Rating vs Installs [RegPlot]')

#Code ends here



# --------------
#Code starts here
print(data["Price"].value_counts())

data["Price"]  = data["Price"].str.replace('$','')
data["Price"] = pd.to_numeric(data["Price"])

sns.regplot(x = "Price", y = "Rating", data = data)
plt.title('Rating vs Price [RegPlot]')


#Code ends here


# --------------

#Code starts here
print(data["Genres"].unique())

data["Genres"] = data["Genres"].str.split(';').str[0]

gr_mean = data[['Genres','Rating']].groupby(['Genres'], as_index = False).mean()

gr_mean.describe()

gr_mean = gr_mean.sort_values(by = ["Rating"])

print(type(gr_mean))

print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])

#Code ends here




# --------------

#Code starts here

#print(data['Last Updated'])
#plt.plot(data['Last Updated'])

from datetime import datetime

#print(data['Last Updated'])
data['Last Updated'].value_counts()
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
#datetime.strptime(data['Last Updated'], '%b %d %Y %I:%M%p')
#data['Last Updated'] = data['Last Updated'].astype('datetime64[ns]')
print(data['Last Updated'].head())
max_date = max(data['Last Updated'])

print(type(data['Last Updated']))
print(type(max_date))
print(max_date)

data["Last Updated Days"] = (max_date - data["Last Updated"]).dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title("Rating vs Last Updated [RegPlot]")
#Code ends here


