import pandas as pd
from numpy import NaN

Activities = pd.read_csv("/Users/nerdbear/Documents/GitHub/human-wildlife-coexistence-data-analysis/3. pca-human-wildlife-coexistence-activities-detailed-records-2010-2021.csv", encoding='cp1252')
#Note, encoding='cp1252' needed to be specified in order to read .csv withour parser errors
Activities.head()
Activities.shape #to check number of rows, columns match .csv file
Activities.dtypes

Act_subset = Activities[["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area"]]
duplicate_Act_subset = Act_subset.duplicated(keep=False)
sum(duplicate_Act_subset)

duplicate_Act_Inc_Num = Activities.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Act_Inc_Num)

sum(duplicate_Act_Inc_Num)==sum(duplicate_Act_subset)
#Conclusion, The Activity Type column is the column that differs between rows - all other columns are identical when the incident number duplicates

##** I would like to merge all Activity Types across duplicates on an Incident Number into one column "List of Activities" so that there are unique Incident Numbers for this dataset.

#Checking how many of the duplicates have NA values in "Activity Type"
dup_Activities = Activities[duplicate_Act_subset]
dup_Activities

dup_Activities["Activity Type"].isna().sum()
#Conclusion, only a small amount (46) of the duplicated rows (total of 4051) contain NA values for "Activity Type". Therefore that means that several individual Incident Number's contain more than one "Activity Type"


######


Animals = pd.read_csv("/Users/nerdbear/Documents/GitHub/human-wildlife-coexistence-data-analysis/4. pca-human-wildlife-coexistence-animals-involved-detailed-records-2010-2021.csv", encoding='cp1252')
Animals.head()
Animals.shape
Animals.dtypes

Animals_subset = Animals[["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area", "Incident Type"]]
#Duplicate subset includes Incident Type attribute. This is what leads to me to dig deeper into why the Incident Types vary for the "Incidents" Dataset and finding the Null values.
duplicate_Animals_subset = Animals_subset.duplicated(keep=False)
sum(duplicate_Animals_subset)

duplicate_Animals_Inc_Num = Animals.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Animals_Inc_Num)

sum(duplicate_Animals_Inc_Num)==sum(duplicate_Animals_subset)

#each individual animal "Species Common Name" involved in a given "Incident Number" is listed in a separate row for that incident number and is what is causing the duplication.
#There is also lots of data (up to 8 other variables) that are specific to the "Species Common Name" value. Becuase of this, I don't want to modify the data in this dataset at all. 
#Instead, I will treat this dataset as the "main dataset". I'm going to create a new column which will merge the "Incident Number" with the "Species Common Name" value to create a Unique identifier for each row.
#When i join the other 3 datasets, I will then join them based on Incident Number. This means the data coming in from the other 3 datsets will be identical for each incident number and will not vary based on "Species Common Name" (becase that information is not provided to us in the other datsets. I believe this approach will gain us the most insight and maintain the most data of what we were given.


#########

Incidents = pd.read_csv("/Users/nerdbear/Documents/GitHub/human-wildlife-coexistence-data-analysis/5. pca-human-wildlife-coexistence-incidents-detailed-records-2010-2021.csv", encoding = 'cp1252')
Incidents.head()
Incidents.shape
Incidents.dtypes

Inc_subset = Incidents[["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area", "Latitude Public", "Longitude Public", "Within Park"]] 
duplicate_Inc_subset = Inc_subset.duplicated(keep=False)
sum(duplicate_Inc_subset)

duplicate_Inc_Inc_Num = Incidents.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Inc_Inc_Num)

sum(duplicate_Inc_Inc_Num)==sum(duplicate_Inc_subset)
##Conclusiong, The "Incident Type" and "Total Staff Involved" and "Total Staff Hours" attributes differ but all other attributes remain consistent when the incident number duplicates. 
#Will further investigate duplicates:

dup_bool = Incidents["Incident Number"].duplicated(keep=False)
print (dup_bool)
Dup_Incidents = Incidents[dup_bool]
Dup_Incidents
Dup_Incidents["Incident Type"].isna().sum()

Incidents[Incidents["Incident Type"].isna()]

Incidents["Incident Type"].isna().sum()

Incidents["Incident Type"].isna().sum() == Dup_Incidents["Incident Type"].isna().sum()
#Number of NA's in "Incident Type" column is the same in the entire dataset as it is in the subsetted duplicate dataset (i.e. all of the NA values occur in rows that are duplicate and they occur in half the duplicate rows). Remove these rows. 
#There are only 32 Incident Types that are NaN and they are the 32 Incidents Types that are duplicate.

#There are a total of 64 duplicate rows and of the 64 duplicate rows, there are 32 missing values. Looking at the outputs generated above, it is clear that duplicated rows have missing values for "Incident Type", "Total Staff Involved" and "Total Staff Hours" so no additional information is being provided by the duplicate rows. 
#If "Incident Type" is Nan AND Incident type is duplicate, I will delete that row. The new dataset with removed rows will be called Incidents2. I will then evaluate the remaining rows for duplicates/missing values to ensure I am left with the data I want (no duplicate rows and the total number of rows remaining will be Incidents.shape[0] - Incidents2.shape[0] = 32)

#There are only 32 Incident Types that are NaN and they are the 32 Incidents Types that are duplicate. 
#Delete these rows
Incidents2 = Incidents[Incidents["Incident Type"].notnull()]

#Checking to confirm there are no duplicates remaining: 
#Looking for duplicates in subset
Inc_subset = Incidents2[["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area", "Latitude Public", "Longitude Public", "Within Park"]] 
duplicate_Inc_subset = Inc_subset.duplicated(keep=False)
sum(duplicate_Inc_subset)
#Looking for duplicates in just Incident Number column.
duplicate_Inc_Inc_Num = Incidents2.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Inc_Inc_Num)
#Comparing the two
sum(duplicate_Inc_Inc_Num)==sum(duplicate_Inc_subset)
#Conclusion, there are no duplicate Incident Numbers remaining. 

#Confirming there are no NA values remaining in "Incident Type" column of new dataframe:
Incidents2["Incident Type"].isna().sum()
#Conclusion, no missing values remaining in new Incidents2 dataset. Will use this dataset for joining with others.


#############

Responses = pd.read_csv("/Users/nerdbear/Downloads/6. pca-human-wildlife-coexistence-responses-detailed-records-2010-2021.csv", encoding = 'cp1252')
Responses.head()
Responses.shape
Responses.dtypes

Resp_subset = Responses[["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area"]]
duplicate_Resp_subset = Resp_subset.duplicated(keep=False)
sum(duplicate_Resp_subset)

duplicate_Resp_Inc_Num = Responses.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Resp_Inc_Num)

sum(duplicate_Resp_Inc_Num)==sum(duplicate_Resp_subset)
#Where the Incident Number is duplicated, all column values are duplicated except for the Response column. This tells me that some incidents had more than one response. In order to join this dataset with the others, we need the Incident Number to be unique so we are going to modify this dataset so that there are no duplicate Incident Numbers. We will do this by keeping the first listing of each incident number, and moving all subsequent responses for duplicate incidents numbers to a new column called "Second Response Type" and 

#Finding unique Response Types. *** Emailed David Gummer about whether there is a reference table for which incident types or animal health status's require which response type.
Responses["Response Type"].unique()
