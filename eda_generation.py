#I did not have success generating the profile report from 
#within Google Colab or from directly in terminal, but I was 
#able to generate and export to html from Jupyter Notebook.
#Installed Anaconda package including Jupyter Notebook 
#from https://www.anaconda.com/products/distribution

#Ran in terminal before launching Jupyter Notebook
#jupyter nbextension enable --py widgetsnbextension
#pip install --upgrade --force-reinstall pandas
#pip install ydata-profiling
#pip install pandas-profiling


import pandas as pd
from pandas_profiling import ProfileReport 


CompleteData = pd.read_csv("/Users/nerdbear/Documents/GitHub/human-wildlife-coexistence-data-analysis/CompleteData.csv", index_col=0, dtype=str)
profile = ProfileReport(CompleteData, title="Human-Animal Coexistence Data - EDA Report")

CompleteData["Sum of Number of Animals"] = CompleteData["Sum of Number of Animals"].astype("float")

CompleteData["Total Staff Hours"] = CompleteData["Total Staff Hours"].astype("float")

CompleteData["Total Staff Included"] = CompleteData["Total Staff Included"].astype("int")

CompleteData["Latitude Public"] = CompleteData["Latitude Public"].astype("float")

CompleteData["Longitude Public"] = CompleteData["Longitude Public"].astype("float")

#To view report inside Jupyter Notebook:
profile

#To export report to html:
profile.to_file("Human-Animal_Coexistence_Data_EDA_Report.html")

#In Jupyter, go to "Files" and then go to your root folder
#to locate the generated html document.

### To Do:
#1.  modify "CompleteData" so the rows that were not a part of "animals3" 
#	 (there are only about 3) have the same "UniqueID" format as all other rows
#2.  modify "CompleteData" to remove the columns that don't 
#    need to be part of the final dataset (the ones i created for the merging)
#3.  Modify how I read_csv into Jupyter for EDA generation. Right now I am 
#	 putting all columns as "str" but at least column should actually be "int"
#    Should I be setting any columns as "categorical" at this point in time or 
# 	 is that just later? Some of the categorical ones will be messed up becuase
# 	 I made them lists by merging rows from the other datasets.
#4.  Generate new EDA report based on changes made to "CompleteData". 
#5.  Save .html EDA report to Github.
#4.  Update README file in GitHub to explain how datasets were treated for the 
#	 joining (if too long for README, put in a separate document that is linked 
# 	 in the README)
#5.  Invite Professor Abdou to my Github. 
#6.  Work on methodology
