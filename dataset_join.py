import pandas as pd
from numpy import NaN
from sklearn.preprocessing import OneHotEncoder

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

#Checking how many of the duplicates have NA values in "Activity Type"
dup_Activities = Activities[duplicate_Act_subset]
dup_Activities["Activity Type"].isna().sum()
#Conclusion, only a small amount (46) of the duplicated rows (total of 4051) contain NA values for "Activity Type". Therefore that means that several individual Incident Number's contain more than one "Activity Type"
#Count number of unique Incident Numbers in duplicates.
dup_Activities["Incident Number"].nunique()

#I would like to encode Acitivity Type so each distinct activity type is it's own column with a binary indicator (0 for no and 1 for yes) if a given activity type was involved in a given incident number.

#Count distinct values in Activity Type
Activities["Activity Type"].nunique()

encoder = OneHotEncoder(handle_unknown='ignore')
encoder_df = pd.DataFrame(encoder.fit_transform(Activities[["Activity Type"]]).toarray())
encoder_df.columns = encoder.get_feature_names_out(["Activity Type"])
encoder_df.head()
Activities_encoded = Activities.join(encoder_df)
Activities_encoded.head()
Activities_encoded.drop('Activity Type', axis = 1, inplace=True)
Activities_encoded.head()


##** I would like to merge all columns relating to Activity Types (columns 4-105) across duplicates on an Incident Numbe so that there are unique Incident Numbers for this dataset.
Activities2 = Activities_encoded[Activities_encoded.columns[4:105]].groupby([Activities['Incident Number'], Activities["Incident Date"], Activities["Field Unit"], Activities["Protected Heritage Area"]]).apply(sum).reset_index()
Activities2
# The way I've merged the encoded activity type columns using the (sum) function means that instead of being a binary indicator, it is now a count of the number of times each activity was recorded per incident. 
#I think that is fine (#check with Prof. Abdou)

#Confirming whether the new dataset has any duplicate incident numbers
duplicate_Act2_Inc_Num = Activities2.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Act2_Inc_Num)

#Cross checking to ensure correct number of rows remain.
#Number of rows in Original Dataset, minus (number of rows in duplicates subset minus number of UNIQUE rows in duplicates subset) == Number of final rows in new subset. 
Activities.shape[0] - (dup_Activities.shape[0] - dup_Activities["Incident Number"].nunique()) == Activities2.shape[0]

#(In other words, I want to ensure that our new dataset has the same number of Unique incident numbers as our original dataset)
Activities["Incident Number"].nunique() == Activities2["Incident Number"].nunique()

#Conclusion, correct number of rows are remaining in our new dataset.



######

import pandas as pd
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

#There are several duplicates of incident numbers here. My first assumption is that the duplicate incident numbers are being caused by each unique "species common name" being recorded individually for each incident number.
#I will add a new column to this dataset that combines the Incident Number with the "Species Common Name" to create a UNIQUE identifier. 
#I will join the other 3 datasets to this dataset using the Incident Number (and any other common attributes (like Incident Date, Field Unit, Projected Heritage Area, and maybe Incident Type). 
#So the each occurence of the incident number in the Animal dataset will have the same information imported from the other 3 datasets, but I believe this is the best method for preserving all the data we want (and there is no association between the various Response Types, Incident Types or other information that would allow us to do anything else when joining * I emailed David Gummer to ask and am waiting on a response). 


Animals2 = Animals

Animals2.insert(0, "UniqueID", Animals2[["Incident Number", "Species Common Name"]].apply("-".join, axis=1))
#Forest.insert(13, "fireOccurred", Forest['area']>0, True)
#df["Period"] = df[["Courses", "Duration"]].apply("-".join, axis=1)

#Check for duplicates to ensure the newly generated column is unique. 
duplicate_Animals2_Inc_Num = Animals2.duplicated(subset="UniqueID", keep=False)
sum(duplicate_Animals2_Inc_Num)
#This option won't work, there are duplicate reports of the same incident number with the same Species Common Name. 
#There is no other column here that is unique to separate instances of the same incident number so 
#Will instead do decimal points added for the count of duplicates. So if the incident number occurs 3 times, the first will get a .1, the second a .2, and the third a .3

Animals3 = Animals

Animals3.insert(0, "Duplicate Inc_Num", Animals3.duplicated(subset="Incident Number", keep=False))

ValueCounts = Animals3["Incident Number"].value_counts()

ValueCounts["BAN2013-1151"]

Counts = []
for i in Animals3["Incident Number"]:
                Counts.append(ValueCounts[i])

Animals3.insert(0, "Duplicate Counts", Counts)
                    
UniqueCounts = []
for i in Animals3["Incident Number"]:
                if ValueCounts[i] >= 1:
                    UniqueCounts.append(ValueCounts[i])
                    ValueCounts[i] -= 1

Animals3.insert(0, "Unique Counts", UniqueCounts)

#Need to convert "Unique Counts" to string type (from integer type) before i'm able to join it with the string "Incident Number" values.

Animals3["Unique Counts"]= Animals3["Unique Counts"].astype(str)

Animals3.insert(0, "UniqueID", Animals3[["Incident Number", "Unique Counts"]].apply(".".join, axis=1))

#Checking to ensure there are no duplicates in the the UniqueID 
duplicates_UniqueID = Animals3.duplicated(subset="UniqueID", keep=False)
sum(duplicates_UniqueID)



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

#Checking how many of the duplicates have NA values in "Response Type"
dup_Responses = Responses[duplicate_Resp_subset]
dup_Responses

#Checking how many of the duplicates have NA values in "Activity Type"
dup_Responses["Response Type"].isna().sum()

#Count number of unique Incident Numbers in duplicates.
dup_Responses["Incident Number"].nunique()



#I would like to encode Response Type so each distinct Response type is it's own column with a binary indicator (0 for no and 1 for yes) if a given Response type was involved in a given incident number.

#Count distinct values in Response Type
Responses["Response Type"].nunique()

encoder = OneHotEncoder(handle_unknown='ignore')
encoder_df = pd.DataFrame(encoder.fit_transform(Responses[["Response Type"]]).toarray())
encoder_df.columns = encoder.get_feature_names_out(["Response Type"])
encoder_df.head()
Responses_encoded = Responses.join(encoder_df)
Responses_encoded.head()
Responses_encoded.drop('Response Type', axis = 1, inplace=True)
Responses_encoded.head()

#Viewing sums of each response type column. 
print(Responses_encoded[Responses_encoded.columns[4:53]].sum()) 

##** I would like to merge all columns relating to Reponse Types (columns 4-53) across duplicates on an Incident Numbe so that there are unique Incident Numbers for this dataset.
Responses2 = Responses_encoded[Responses_encoded.columns[4:53]].groupby([Responses['Incident Number'], Responses["Incident Date"], Responses["Field Unit"], Responses["Protected Heritage Area"]]).apply(sum).reset_index()
Responses2


#Confirming whether the new dataset has any duplicate incident numbers
duplicate_Resp2_Inc_Num = Responses2.duplicated(subset="Incident Number", keep=False)
sum(duplicate_Resp2_Inc_Num)

#Cross checking to ensure correct number of rows remain.
#Number of rows in Original Dataset, minus (number of rows in duplicates subset minus number of UNIQUE rows in duplicates subset) == Number of final rows in new subset. 
Responses.shape[0] - (dup_Responses.shape[0] - dup_Responses["Incident Number"].nunique()) == Responses2.shape[0]

#(In other words, I want to ensure that our new dataset has the same number of Unique incident numbers as our original dataset)
Responses["Incident Number"].nunique() == Responses2["Incident Number"].nunique()

#Conclusion, correct number of rows are remaining in our new dataset.


##############
#Joining datasets without losing any rows from any dataset.

#Checking all 4 datasets and comparing Incident Numbers. Because we'll be using Animals dataset as our main one to join the others into,
#I Want to see if there are any incident numbers included in the other 3 datasets that are not already in the Animals dataset.
#Conclusion based on results below, there are three (3) incident numbers included in other datasets that do not exist in Animals.

AnimalIDs = Animals3["Incident Number"].unique()
AnimalIDs
AnimalIDs = np.sort(AnimalIDs)
AnimalIDs
AnimalIDs.size
ActivityIDs = Activities2["Incident Number"]
ActivityIDs
ActivityIDs = np.sort(ActivityIDs)
ActivityIDs
ActivityIDs.size
dif1 = list(set(ActivityIDs)-set(AnimalIDs))
dif1
IncidentIDs = Incidents2["Incident Number"]
IncidentIDs.size
IncidentIDs = np.sort(IncidentIDs)
IncidentIDs
dif2 = list(set(IncidentIDs)-set(AnimalIDs))
dif2
ResponseIDs = Responses2["Incident Number"]
ResponseIDs.size
ResponseIDs = np.sort(ResponseIDs)
ResponseIDs
dif3 = list(set(ResponseIDs)-set(AnimalIDs))
dif3
print(dif1, dif2, dif3)


#Now joining datasets together.
#Doing Outer Joins to ensure no loss of data at this stage for Incident Numbers that exist in other datasets but not in the Animals datset we are joining to.

JoinedData1 = pd.merge(Animals3, Activities2, how="outer", on = ["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area"])
JoinedData1
#Confirming that Incident Numbers contained in Activities but not in Animals dataset were still joined into the new dataset. 
JoinedData1.loc[JoinedData1["Incident Number"].isin(dif1)]

JoinedData2 = pd.merge(JoinedData1, Incidents2, how="outer", on = ["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area"])
JoinedData2

#Both Animals3 and Incidents2 contained a column for "Incident Type" so joining the two created columns "_x" and "_y"
#Looking for differences between the two columns. 
JoinedData2["Incident Type_x"] == JoinedData2["Incident Type_y"]
difference = list(set(JoinedData2["Incident Type_x"]) - set(JoinedData2["Incident Type_y"]))
difference
JoinedData2["Incident Type_x"].isna().sum()
JoinedData2["Incident Type_y"].isna().sum()

#Conclusion, Incident Type_x column contains 3 na values, whereas Incident Type_y contains none. 
#Will drop "Incident Type_x". 

JoinedData2.drop('Incident Type_x', axis = 1, inplace=True)
JoinedData2.head()

#Moving columns around so key information is closer to start of dataframe and all the activity types are at the end. 
eight = JoinedData2.pop('Incident Type_y')
JoinedData2.insert(8, 'Incident Type', eight)
nine = JoinedData2.pop('Latitude Public')
JoinedData2.insert(9, 'Latitude Public', nine)
ten = JoinedData2.pop('Longitude Public')
JoinedData2.insert(10, 'Longitude Public', ten)
eleven = JoinedData2.pop('Within Park')
JoinedData2.insert(11, 'Within Park', eleven)
twelve = JoinedData2.pop('Total Staff Involved')
JoinedData2.insert(12, 'Total Staff Involved', twelve)
thirteen = JoinedData2.pop('Total Staff Hours')
JoinedData2.insert(13, 'Total Staff Hours', thirteen)
JoinedData2.head()


#Confirming that Incident Numbers contained in Incidents but not in Animals dataset were still joined into the new dataset. 
JoinedData2.loc[JoinedData2["Incident Number"].isin(dif2)]


JoinedData3 = pd.merge(JoinedData2, Responses2, how="outer", on = ["Incident Number", "Incident Date", "Field Unit", "Protected Heritage Area"])
JoinedData3

#Confirming that Incident Numbers contained in Responses but not in Animals dataset were still joined into the new dataset. 
JoinedData3.loc[JoinedData3["Incident Number"].isin(dif3)]

#Renaming our final complete Dataset.
CompleteData = JoinedData3
CompleteData

CompleteData.drop('Unique Counts', axis = 1, inplace=True)
CompleteData.drop('Duplicate Counts', axis = 1, inplace=True)
CompleteData.drop('Duplicate Inc_Num', axis = 1, inplace=True)
CompleteData.head()

#Adding "UniqueID" values for the 3 incident ID observations that did not exist in the Animal dataframe and therefore didn't get UniqueID assigned. Checked earlier that there are only 3 rows effected and they are all unique Incident numbers (no duplicates).
CompleteData['UniqueID'] = CompleteData['UniqueID'].fillna(CompleteData['Incident Number'])


#download CompleteData as .csv file from Jupyter Notebook
Complete_HWC_Data.to_csv("/Users/nerdbear/Downloads/CompleteData.csv")


