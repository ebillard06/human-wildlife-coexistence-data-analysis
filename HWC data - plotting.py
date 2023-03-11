#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


#pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)


# In[2]:


Complete_HWC_Data = pd.read_csv("/Users/nerdbear/Downloads/Complete_HWC_Data.csv", index_col=0, dtype=str)


# In[3]:


Complete_HWC_Data["Sum of Number of Animals"] = Complete_HWC_Data["Sum of Number of Animals"].astype("float")

Complete_HWC_Data["Total Staff Hours"] = Complete_HWC_Data["Total Staff Hours"].astype("float")

Complete_HWC_Data["Total Staff Involved"] = Complete_HWC_Data["Total Staff Involved"].astype("float")

Complete_HWC_Data["Latitude Public"] = Complete_HWC_Data["Latitude Public"].astype("float")

Complete_HWC_Data["Longitude Public"] = Complete_HWC_Data["Longitude Public"].astype("float")

Complete_HWC_Data[Complete_HWC_Data.columns[20:170]] = Complete_HWC_Data[Complete_HWC_Data.columns[20:170]].astype("float")


# In[4]:


Complete_HWC_Data.head()


# In[19]:


Complete_HWC_Data.dtypes


# In[5]:


import matplotlib.pyplot as plt
from matplotlib import *


# In[6]:


plt.hist(Complete_HWC_Data["Field Unit"], width = 0.8, bins = 19)
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()

### This histogram was only showing the frequency count for each park - only every 2, 
### I fixed this by setting the bins = 19 (taking 19 from the distinct values of 
### "field units" from the EDA report)


# In[7]:


plt.hist(Complete_HWC_Data["Protected Heritage Area"], width = 0.8, bins = 35)
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[8]:


plt.hist(Complete_HWC_Data["Incident Type"], width = 0.8, bins = 9)
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[9]:


plt.hist(Complete_HWC_Data["Latitude Public"])
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[10]:


plt.hist(Complete_HWC_Data["Longitude Public"])
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[22]:


#Not sure why this data needs to be set as str (it was imported as str and already showing as being "object" type but the histogram wouldn't work unless i did this...)


Complete_HWC_Data["Species Common Name"] = Complete_HWC_Data["Species Common Name"].astype("str")


# In[23]:


plt.hist(Complete_HWC_Data["Species Common Name"])
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()

## THis histogram is showing one speciies with almost 70,000 frequency but the eda shows 
### the most frequent value to be black bear at 20898 count. I think it's because there 
## are too many unique values to inlcude here and the top counts are being lumped together 
## into one bin. 



# In[ ]:





# In[12]:


#Check for outliers - i doubt this variable will be useful...

plt.hist(Complete_HWC_Data["Sum of Number of Animals"])
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[14]:



#Not sure why this data needs to be set as str (it was imported as str and already showing as being "object" type but the histogram wouldn't work unless i did this...)

Complete_HWC_Data["Animal Health Status"] = Complete_HWC_Data["Animal Health Status"].astype("str")


# In[15]:


plt.hist(Complete_HWC_Data["Animal Health Status"], width = 0.8, bins = 9)
plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[25]:


Incident_types = Complete_HWC_Data["Incident Type"]


# In[31]:


df = Incident_types.groupby(Complete_HWC_Data["Incident Date"]).value_counts()


# In[35]:


df.plot()


# In[49]:


Incident_Date = Complete_HWC_Data["Incident Date"]


# In[52]:


df2 = Incident_Date.groupby(Complete_HWC_Data["Incident Type"]).value_counts()


# In[53]:


df2


# In[54]:


df2.plot()


# In[67]:


plt.figure(figsize=(16, 10), dpi=80)
plt.plot(Complete_HWC_Data["Incident Type"].value_counts(), Complete_HWC_Data["Incident Date"],data=Complete_HWC_Data)


# In[58]:


plt.ylabel('Frequency count')
plt.xlabel('Data');
plt.title('My histogram')
plt.xticks(rotation='vertical')
plt.show()


# In[89]:


Human_Wildlife_Interaction = Complete_HWC_Data[["Incident Type", "Incident Date"]].loc[Complete_HWC_Data["Incident Type"] == "Human Wildlife Interaction"]

#df.loc[df['column_name'] == some_value]

Human_Wildlife_Interaction


# In[96]:


Human_Wildlife_Interaction["Frequency Count"] = Human_Wildlife_Interaction["Incident Date"].value_counts()


# In[97]:


Human_Wildlife_Interaction


# In[98]:


plt.plot('Incident Date','Incident Type', data=Human_Wildlife_Interaction)


# In[99]:


Human_Wildlife_Interaction2 = Complete_HWC_Data[["Incident Type", "Incident Date"]]


# In[101]:


plt.plot('Incident Date','Incident Type', data=Human_Wildlife_Interaction2)

#Try to figure out how to make these lines, and how to group the dates by month per year. Separate graph for trends each year? 


# In[75]:


plt.figure(figsize=(16,10), dpi=80)
plt.plot(Human_Wildlife_Interaction['Incident Date'], Human_Wildlife_Interaction['Incident Type'].value_counts())


