# Power-BI-historic-electricity-demand
Power BI - Historic Electricity Demand

**Aims:**

The project analyses and visualises data on historic electricity demand in Great Britain. The impetus for the project was that I wanted to use Power BI to compare daily load curves for Great Britain for different days on the same graph, as I could not find anything like this available. I wanted to be able to compare different days visually to see how they varied according to factors like day of the week, time of the year, bank holidays and weather data.

**Objectives:** 
-	Use data from multiple sources to gain insights into demand for electricity in Great Britain.
-	Produce interactive visuals using slicers in Power BI to allow for further analysis of data.
-	Learn more about using DAX in order to create measures and calculated columns in Power BI.  
-	Use a repeatable workflow so that additional data can be added as it becomes available. 
-	Devise a scalable data model. 
Programs Used:
Power BI Desktop, Python, PostgreSQL. 

**Data Sources:**
-	Historic electricity demand data came from the National Grid ESO Data Portal at https://www.nationalgrideso.com/data-portal/historic-demand-data.
-	Weather data was sourced from the Met Office’s Midas-open dataset at https://catalogue.ceda.ac.uk/uuid/dbd451271eb04662beade68da43546e1.
-	Bank holiday data came from a UK government website https://www.gov.uk/bank-holidays. 

**Next steps:**
-	Add 2023 weather data when it becomes available.
-	Compare demand on bank holidays and working days. 
-	Look at possible correlation between weather and demand.

**Things I would do differently next time:** 
-	Use Python to write ETL scripts for all the data prior to importing it into Power BI. I loaded the electricity demand data straight into Power Query as it was clean and complete. I wanted to try using the Get Data from Folder connection to make it easy to add and refresh new csv files. However, because later data from ESO had more columns (as new interconnectors went live) this didn’t work well. So, for the weather data I used Python scripts to clean and transform the data before storing it in a PostgreSQL database. Using Python for all the ETL steps prior to importing it into Power BI would also allow for more automation of the data pipeline in future.
