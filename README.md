# human-wildlife-coexistence-data-analysis
## Project Description
A data analysis project looking at human and wildlife coexistence in Canadian National Parks with the purpose of discovering trends in reportCancel changesed incidents and identifying target areas for promoting health and safety of humans and wildlife and mitigating negative incidents in our National Parks. 
### Our Research Questions:
1.	What patterns can be found in location and time of year for each of the following variables: human activities, animals involved, cause, and incident type. How do these patterns differ year over year?
2.	What incidents are the most concerning (i.e. where there is potential risk for humans or animals)?
3.	What variables are most correlated with the occurrence of each incident type? Can we predict future similar incidents will occur near that location or that time of year? 
## The Data: 
Parks Canada Agency collected human-wildlife coexistence incident reports in 35 National Parks from 2010-2021 and compiled them into four data-sets accessible at [Open Canada's Human-wildlife coexistence incidents in selected national parks form 2010 to 2021](https://open.canada.ca/data/en/dataset/cc5ea139-c628-46dc-ac55-a5b3351b7fdf)
### This project uses the the following files available at that link. These files have also been download and are saved to this repo. 
1. pca_national_human_wildlife_conflict_data_dictionary (This one document contains both English and French). *This file is used for reference and information purposes but is not joined into the dataset we used.* (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/434001359f0cc1c9500c71a07bb1b7e62c6f723e/1.%20pca_national_human_wildlife_conflict_data_dictionary.csv)
2. pca-national-human-wildlife-coexistence-header-descriptions (One document contains both English and French). *This file is used for reference and information purposes but is not joined into the dataset we used.* (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/434001359f0cc1c9500c71a07bb1b7e62c6f723e/2.%20pca-national-human-wildlife-coexistence-header-descriptions.csv)
3. pca-human-wildlife-coexistence-activities-detailed-records-2010-2021 (Just the English version) (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/434001359f0cc1c9500c71a07bb1b7e62c6f723e/3.%20pca-human-wildlife-coexistence-activities-detailed-records-2010-2021.csv)
4. pca-human-wildlife-coexistence-animals-involved-detailed-records-2010-2021 (Just the English version) (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/434001359f0cc1c9500c71a07bb1b7e62c6f723e/4.%20pca-human-wildlife-coexistence-animals-involved-detailed-records-2010-2021.csv)
5. pca-human-wildlife-coexistence-incidents-detailed-records-2010-2021 (Just the English version) (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/434001359f0cc1c9500c71a07bb1b7e62c6f723e/5.%20pca-human-wildlife-coexistence-incidents-detailed-records-2010-2021.csv) 
6. pca-human-wildlife-coexistence-responses-detailed-records-2010-2021 (Just the English version) (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/434001359f0cc1c9500c71a07bb1b7e62c6f723e/6.%20pca-human-wildlife-coexistence-responses-detailed-records-2010-2021.csv)

**Items 3-6 are individual datasets containing different information related to each incident: human activity, animal(s) involved, incident details, and responses. For this project we will join the four datasets together using the unique Incident Number, and analyze the complete set of data.**

## How to Install and Run the Project
***Note, for all code documents listed below, I've included the .ipynb file as well as the .html and .pdf formats. Please note the .pdf format cuts off some of the comments added in the code so while it can be viewed in github (while .html cannot be), it is not my preferred format).***

The file named "Clean and Join datasets" (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/2b377a9c2ef584563676a8795b24d7d1e7042bb4/Clean%20and%20Join%20datasets.ipynb) contains all the code used to clean and join the four datasets. The data description on the Government of Canada Open Data website had indicated that each observation consisted of a unique incident number; however, there are actually several observations in each dataset which have duplicate incident numbers because more than observation was made per each incident. Because of this, there were some preprocessing steps that I needed to take before merging the datasets together. I also cleaned the data by comparing entries in the datasets to the list of valid possible entries that are listed in the 1. pca_national_human_wildlife_conflict_data_dictionary.csv file. 

The code in "Clean and Join datasets" includes many comments about how the datasets were modified to combine or account for duplicate occurences of the incident numbers along with my reasons why. At the end of that code, a .csv file is generated called "Complete_HWC_Data.csv" (that .csv can also be found in the files here). The "Clean and Join datasets" file was run using Jupyter Notebook and only the links to the datasets would need to be modified in order to be able to run this code on another machine. 

The "EDA Report Generation" file (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/2b377a9c2ef584563676a8795b24d7d1e7042bb4/EDA%20Report%20Generation.ipynb) contains the code used to import the "Complete_HWC_Data.csv" file, any data type modification settings needed, and the command for generating an 'Exploratory Data Analysis' (EDA) Report using the Pandas Profiling package. The generated EDA report in html format can be found in the files and is called "HWC_Data_EDA_Report". 

The "HWC_Data_Description" file (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/2b377a9c2ef584563676a8795b24d7d1e7042bb4/HWC_Data_Description.ipynb) contains the basic code used to pull some basic Data descriptions for the datsets. 

The "HWC Data - Plotting and Initial Analysis" file (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/2b377a9c2ef584563676a8795b24d7d1e7042bb4/HWC%20Data%20-%20Plotting%20and%20Initial%20Analysis.ipynb) contains all the code used to in the exploratory analysis and generation of histograms, time series plots, initial analysis and response to research questions #1.  

The "HWC Data - Augmented Fuller Test" file (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/2b377a9c2ef584563676a8795b24d7d1e7042bb4/HWC%20Data%20-%20Augmented%20Fuller%20Test.ipynb) contains the code used in answering Research Question #2. 

The "HWC Data - Modeling and Evaluation" file (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/2b377a9c2ef584563676a8795b24d7d1e7042bb4/HWC%20Data%20-%20Modeling%20and%20Evaluation.ipynb) contains the code used in modeling and evaluating the models for use in answering Research Question #3. 

## Results
A brief summary of the results of my analysis for each research question are laid out below: 
1.	Most incidents are occurring in the Banff and Jasper National Parks of Canada. The most prevalent Incident Types are “Human Wildlife Interaction” and “Rescued/Recovered/Found Wildlife”. Incidents have tended to increase over the years, and increase in frequency during the warmer months of May – October. 
2.	The statistical properties of the data are stationary over time. 
3.	The features most correlated with Incident Type (looking at the Features used in both the Random Forest and Decision Tree models) are: Total Staff Hours, Incident Month, Species Common Name, Total Staff Involved, Total Staff Hours, Protected Heritage Area, Field Unit, Latitude Public, and Activity Type_Railway. The Decision Tree Model and Random Forest models perform statistically the same in predicting Incident Type; however the Random Forest model is more efficient in that it requires less time and computer memory.

The full Final Project Report can be found with file name "Final Results and Project Report" (https://github.com/ebillard06/human-wildlife-coexistence-data-analysis/blob/4613da3a557e3372eebe8b2745a1cdfd2d773965/Final%20Results%20and%20Project%20Report.pdf). 

