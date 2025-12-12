import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv('ASX200.csv')
stock_indices = ['CAC40', 'DAX', 'FTSE100', 'Hang Seng', 'Nikkei 225', 'NASDAQ', 'Shanghai', 'Dow Jones', 'S&P500']
currency = ['10 AED', '10 CNY', '10,000 IDR', '100 INR', '100 JPY', '1000 KRW', 'EUR', 'GBP', 'SGD', 'USD']
bond = ['AU 10yr', 'AU 1yr', 'China 1yr', 'China 30yr', 'Germany 1yr', 'Germany 30yr', 'Japan 1yr', 'Japan 30yr', 'Korea 1yr', 'Korea 20yr',
        'Singapore 1yr', 'Singapore 30yr', 'Swiss 1yr', 'Swiss 30yr', 'UK 1yr', 'UK 30yr', 'US 1yr', 'US 30yr']
aus_market = ['RBA-rate']

#corr asx vs other indices
corr_indices = df[stock_indices + ['ASX200']].corr()['ASX200'].loc[stock_indices]
plt.figure(figsize=(10,5))
asx_and_indices = sns.barplot(x=corr_indices.values, y=corr_indices.index)
asx_and_indices.bar_label(asx_and_indices.containers[0], fmt="%.2f", padding=3) #2 decimal place
plt.title('Correlation: ASX200 vs Global Market Indices')
plt.xlabel('Correlation Coefficient'); plt.xlim(0,1)
plt.tight_layout(); plt.show()

#corr asx vs currency
corr_currency = df[currency + ['ASX200']].corr()['ASX200'].loc[currency]
plt.figure(figsize=(10,5))
asx_and_currency = sns.barplot(x=corr_currency.values, y=corr_currency.index)
asx_and_currency.bar_label(asx_and_currency.containers[0], fmt="%.2f", padding=3)
plt.title('Correlation: ASX200 vs Currency')
plt.xlabel('Correlation Coefficient'); plt.xlim(-1,1)
plt.tight_layout(); plt.show()

#corr asx vs bond
corr_bond = df[bond + ['ASX200']].corr()['ASX200'].loc[bond]
plt.figure(figsize=(10,5))
asx_and_bond = sns.barplot(x=corr_bond.values, y=corr_bond.index)
asx_and_bond.bar_label(asx_and_bond.containers[0], fmt="%.2f", padding=3)
plt.title('Correlation: ASX200 vs Bond')
plt.xlabel('Correlation Coefficient'); plt.xlim(-1,1)
plt.tight_layout(); plt.show()

#corr asx vs RBA-rate
corr_RBA = df[aus_market + ['ASX200']].corr()['ASX200'].loc[aus_market]
plt.figure(figsize=(4,1.5))
asx_and_RBA = sns.barplot(x=corr_RBA.values, y=corr_RBA.index)
asx_and_RBA.bar_label(asx_and_RBA.containers[0], fmt="%.2f", padding=3)
plt.title('Correlation: ASX200 vs RBA-rate')
plt.xlabel('Correlation Coefficient'); plt.xlim(-1,0)
plt.tight_layout(); plt.show()

#trend visualisation
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
df_2010_2020 = df[(df['Date'] >= '01-01-2010') & (df['Date'] <= '12-31-2020')] #2010-2020
plt.figure(figsize=(10,4))
plt.plot(df_2010_2020['Date'], df_2010_2020['ASX200'], color='blue')
plt.title('ASX200 Trend (2010-2020)')
plt.xlabel('Date')
plt.ylabel('ASX200 Index Level')
plt.grid(True)
plt.tight_layout
plt.show()

#distributional check
#histogram
plt.figure(figsize=(8,4))
sns.histplot(df['ASX200'], kde=True, color='skyblue')
plt.title('Distribution of ASX200 Index Level (2010-2020)')
plt.xlabel('ASX200 Index Level')
plt.ylabel('Frequency')
plt.tight_layout
plt.show()

#boxplot to detect outliers
plt.figure(figsize=(6,3))
sns.boxplot(x=df['ASX200'], color='lightcoral')
plt.title('Boxplot of ASX200 Index Level')
plt.xlabel('ASX200 Index Level')
plt.tight_layout()
plt.show()

#qq plot for normality
plt.figure(figsize=(5,5))
stats.probplot(df['ASX200'], dist="norm", plot=plt)
plt.title('Q-Q Plot for ASX200 Normality Check')
plt.tight_layout()
plt.show()

#summary statistics
print(df['ASX200'].describe())
print("\nSkewness:", df['ASX200'].skew())
print("Kurtosis:", df['ASX200'].kurt())






