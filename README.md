# Power-BI-historic-electricity-demand

**PROJECT OVERVIEW**

**Aims:**

The project analyses and visualises data on historic electricity demand in Great Britain from 2018-2024. The impetus for the project was that I wanted to use Power BI to compare daily load curves for Great Britain for different days on the same graph, as I could not find anything like this available. I wanted to be able to compare different days visually to see how they varied according to factors like day of the week, time of the year, bank holidays and weather data.

**Objectives:** 
-	Use data from multiple sources to gain insights into demand for electricity in Great Britain.
-	Produce interactive visuals using slicers in Power BI to allow for further analysis of data.
-	Learn more about using DAX in order to create measures and calculated columns in Power BI.  
-	Use a repeatable workflow so that additional data can be added as it becomes available. 
-	Devise a scalable data model. 

**Programs Used:**

Power BI Desktop, Python, PostgreSQL. 

**Data Sources:**
-	Historic electricity demand data came from the National Grid ESO Data Portal at https://www.nationalgrideso.com/data-portal/historic-demand-data.
-	Weather data was sourced from the Met Office’s Midas-open dataset at https://catalogue.ceda.ac.uk/uuid/dbd451271eb04662beade68da43546e1.
-	Bank holiday data came from a UK government website https://www.gov.uk/bank-holidays.

  **Visuals Produced Include:**
  - Daily national demand curve by settlement period where you can compare up to 7 days, along with information about working/non-working day/bank holiday and weather information.
  - A demand curve where you can choose a date and compare the demand curve for National Demand, Transmission System Demand, ND plus estimated embedded generation, and TSD plus estimated embedded generation.
  - Sorted annual demand curves along with data about annual maximum and minimum periods of demand.

**Next steps:**
-	Add 2023 weather data when it becomes available.
-	Compare demand on bank holidays and working days. 
-	Look at possible correlation between weather and demand.
-	Add sunrise/sunset times to model.

**Things I would do differently next time:** 
-	Use Python to write ETL scripts for all the data prior to importing it into Power BI. I loaded the electricity demand data straight into Power Query as it was clean and complete. I wanted to try using the Get Data from Folder connection to make it easy to add and refresh new csv files. However, because later data from ESO had more columns (as new interconnectors went live) this didn’t work well. So, for the weather data I used Python scripts to clean and transform the data before storing it in a PostgreSQL database. Using Python for all the ETL steps prior to importing it into Power BI would also allow for more automation of the data pipeline in future.



**MORE DETAILED EXPLANATION**


**Data sources:**
-	Electricity demand data
The historic electricity demand data came from the National Grid ESO Data Portal at https://www.nationalgrideso.com/data-portal/historic-demand-data. The data covers historic electricity national demand and transmission system demand per settlement period. It also includes figures for interconnector imports and exports, estimated embedded solar and wind generation, and hydro storage pumping demand and Non-BM Short Term Operating Reserve. I used data from 2018 to May 2024.
The data is available under the National Grid ESO Open Data Licence v1.0. This allows users to copy, publish, distribute, adapt and exploit the data commercially and non-commercially provided the source is acknowledged. So, this project is supported by National Grid ESO Open Data.

-	Weather data 
Weather data was sourced from the Met Office’s Midas-open dataset, a subset of the Met Office Integrated Data Archive System (MIDAS) Land and Marine Surface Stations Data. Midas-open contains land surface observations from 1832-present. At the time of obtaining this data the most recent data available was from 2022 so I used hourly weather observations from 2018 to 2022. It is available at: https://catalogue.ceda.ac.uk/uuid/dbd451271eb04662beade68da43546e1. The data is available under the Open Government licence. This allows users to copy, publish, distribute, adapt and exploit the data commercially and non-commercially.

I chose data from one location as a rough approximation for the weather data for Great Britain, rather than produce any averages as these might not make sense for things like wind direction. Obviously, there are limitations in choosing one location including that the temperature, wind speed etc. might vary significantly across Great Britain at any one time. However, I chose a weather station in Nottingham at Sutton-Bonington as it relatively central in England, which is the most populous country in Great Britain so likely to have the greatest impact on demand for electricity. The weather station at this location is at a height of 43m near to the average height for England (54m) and it is located rurally so will not suffer from the urban heat island effect. I may yet add data from a Scottish location to offer an approximation for Scottish weather as this can sometimes vary significantly from the weather in central England. 

Some of the weather data from Sutton-Bonington was missing, including reasonaly significant amounts of the data on wind direction and wind speed in  2021 and 2022. To deal with this I considered adding in data from the nearby weather station of Watnall (also in Nottinghamshire but at a higher elevation) to replace the missing values as this would have been reasonably similar. However, I ultimately decided against this as it would have been tricky to do this while also preserving the origin of the Watnall data.  

-	Bank Holiday Data
This data came from a UK government website https://www.gov.uk/bank-holidays. The data is available under the Open Government licence. This allows users to copy, publish, distribute, adapt and exploit the data commercially and non-commercially.

**Data Pipeline**

The electricity demand data was clean and complete, so I imported the csv files for the various years into Power Query and appended all the years to a fact table. 
The weather data needed quite a lot of cleaning and had data missing so with this I used functions in Python to clean the data, identify missing values, and to append DataFrames from different years together. 
I might use the weather data for other projects, so I wanted to store the data in a relational database. I created a database and tables in PostgreSQL then imported data from csv files into tables. An ODBC (Open Database Connectivity) interface was used to import the data from import data from PostgreSQL into Power BI. 
The bank holiday data I pulled directly into Power Query using the web connector. 
Once the data sets were in Power BI I created various measures. Text scripts of these can be found in the repository for this project.


**REFERENCES:**

Met Office (2019): Met Office MIDAS Open: UK Land Surface Stations Data (1853-current). Centre for Environmental Data Analysis, 15/07/2024. http://catalogue.ceda.ac.uk/uuid/dbd451271eb04662beade68da43546e1
	

Weber, C., Möst, D., Fichtner, W., (2022) _Economics of Power Systems_. Cham: Springer Nature.

