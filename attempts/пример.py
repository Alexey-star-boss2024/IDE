import pandas as pd

melb_data = pd.read_csv('C:/DST-187/Data/melb_data_ps', sep=',')
melb_data.head()
delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01') 
display(delta_days)
display(delta_days.dt.days)
melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
display(melb_df['AgeBuilding'])
melb_df = melb_df.drop('YearBuilt', axis=1)