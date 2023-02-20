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


CompleteData = pd.read_csv("/Users/nerdbear/Documents/GitHub/human-wildlife-coexistence-data-analysis/CompleteData.csv", index_col=0)

profile = ProfileReport(CompleteData, title="Human Wildlife Coexistence Data - EDA Report")

#To view report inside Jupyter Notebook:
profile

#To export report to html:
profile.to_file("HWC_Data_EDA_Report.html")

#In Jupyter, go to "Files" and then go to your root folder
#to locate the generated html document.

