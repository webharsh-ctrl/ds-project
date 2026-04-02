import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('zomato-data-analysis/data/zomato.csv')

df['rate'] = df['rate'].replace('NEW',np.nan)
df['rate'] = df['rate'].replace('-',np.nan)
df['rate'] = df['rate'].astype('str').str.split('/').str[0]

df['rate']=pd.to_numeric(df['rate'],errors='coerce')
df['rate']=df['rate'].fillna(df['rate'].median())


df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',','')
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'],errors='coerce')

print(df['location'].value_counts().head(10))
location_df = df['location'].value_counts().head(10).copy()
plt.figure(figsize=(10,5))
location_df.plot(kind='bar')

plt.xticks(rotation=45)
plt.title("Top 10 Restaurant Locations")
plt.xlabel("Location")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('zomato-data-analysis/images/location.png')
plt.show()

# Insight:
# BTM, HSR, and Koramangala are the top restaurant hubs, indicating high demand and strong competition in these areas.

# ////////////////////////////////////////////////////////////////////////////////////////
sns.histplot(df['rate'], bins=15)
plt.title("Ratings Distribution")
plt.savefig('zomato-data-analysis/images/rating.png')
plt.show()

# Insight:
# Most restaurants have ratings between 3.5 and 4.5, showing generally positive customer satisfaction with very few poorly rated restaurants.

# ////////////////////////////////////////////////////////////////////////////////////////

plt.hist(df['approx_cost(for two people)'], bins=10)
plt.xlabel('Approx_cost(for two people)')
plt.ylabel('Number of restaurants')
plt.title("Cost Distribution")
plt.savefig('zomato-data-analysis/images/cost.png')
plt.show()
# Insight:
# The cost distribution is right-skewed, with most restaurants priced under ₹1000, indicating that affordability is a key factor in the market.

# print(df['rest_type'].value_counts().head(10))
df['rest_type'].value_counts().head(10).plot(kind='bar')
plt.savefig('zomato-data-analysis/images/rest_type.png')
plt.show()

# Insight
# Quick Bites and Casual Dining are the most common restaurant types, reflecting a preference for convenient and moderately priced dining options.