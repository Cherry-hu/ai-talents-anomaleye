import pandas as pd
df = pd.read_csv('Dataset - HAWKAI challenge 1.csv')
fraud = df.loc[(df['counter_party_country'] == 'AF')|(df['counter_party_country'] == 'BS')|(df['counter_party_country'] == 'BB')|
      (df['counter_party_country'] == 'BA')|(df['counter_party_country'] == 'BW')|(df['counter_party_country'] == 'KH')|
      (df['counter_party_country'] == 'GH')|(df['counter_party_country'] == 'IQ')|(df['counter_party_country'] == 'IR')|
       (df['counter_party_country'] == 'JM')|(df['counter_party_country'] == 'KP')|(df['counter_party_country'] == 'MU')|
       (df['counter_party_country'] == 'MN')|(df['counter_party_country'] == 'MM')|(df['counter_party_country'] == 'NI')|
       (df['counter_party_country'] == 'PK')|(df['counter_party_country'] == 'PA')|(df['counter_party_country'] == 'SY')|
       (df['counter_party_country'] == 'TT')|(df['counter_party_country'] == 'UG')|(df['counter_party_country'] == 'VU')|
       (df['counter_party_country'] == 'YE')|(df['counter_party_country'] == 'ZW')|(df['amount'] > 15000)]
new = fraud.drop_duplicates(subset=['amount']).sort_values(['amount'],ascending=False)
new.to_csv('Fraud cases.csv',index=False)
df = pd.read_csv('Fraud cases.csv')
print(df.iloc[[0,1,2,3,4,21,22,23,24,25],:])