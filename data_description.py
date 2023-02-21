import pandas as pd
Complete_HWC_Data = pd.read_csv("/Users/nerdbear/Downloads/Complete_HWC_Data.csv", index_col=0)
Complete_HWC_Data

Complete_HWC_Data.head()
#Data types for attributes in columns 0-20 are listed below. 
#All attributes in columns 21-170 are the encoded binary categories of Activity Type and Response Type and are data type float 64.

Complete_HWC_Data[Complete_HWC_Data.columns[0:20]].dtypes

Complete_HWC_Data[Complete_HWC_Data.columns[0:11]].describe(include='object') 
Complete_HWC_Data[Complete_HWC_Data.columns[11:20]].describe(include='object') 
Complete_HWC_Data[Complete_HWC_Data.columns[0:20]].describe()
pd.set_option('display.max_rows', 100)

#Can these sums be used to generate a histogram?

ActivityTypeSums = Complete_HWC_Data[Complete_HWC_Data.columns[21:121]].sum() 
ActivityTypeSums

ResponseTypeSums = Complete_HWC_Data[Complete_HWC_Data.columns[121:170]].sum() 
ResponseTypeSums