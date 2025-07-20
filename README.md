#Transforming Simple Raw Data into Clean Format 
##Overview
In this project, we cleaned a raw Excel dataset, and converted it into a clean and  structured version, using Python. The process involved removing inconsistencies, filling missing values, and standardizing key fields. 
##dataset used
- <a href="https://github.com/tejesh-gorajana/simple-data-cleaning/blob/main/student_data_with_errors.xlsx">Dataset</a>
##Problems in Raw Data
•	Duplicate records. 
•	Inconsistent name formats. 
•	Irregular date formats in DOB. 
•	standard branch/year entries. 
•	Invalid or missing emails and phone numbers. 
•	Blank values in essential fields like Name, Branch, College_Id etc.
##The steps involved in cleaning data are:
1.	Load & Preprocess
2.	Drop Duplicates
3.	Field/Column Formatting
4.	Export cleaned file
 <img width="940" height="681" alt="image" src="https://github.com/user-attachments/assets/5c3fe601-9d4a-4b86-92cf-6dd766f8784b" />
##1.Load & Preprocess 
•	Loaded data with pandas 
•	Sorted by SurName
•	Removed duplicates.
•	Replaced blank cells with NaN to count the blank cells using “.isna().count()” method.
##2. Drop Incomplete Rows 
Removed rows with missing essential fields: Name, DOB, Branch, College_Id etc. 
##3. Field Cleaning Functions 
•	Names: Stripped spaces and standardized to title case 
•	DOB: Parsed multiple formats to YYYY-MM-DD, fixed unrealistic years 
•	Branch: Mapped variants to standard codes (e.g., "INFOTECH" → "IT") 
•	Year: Normalized variants (e.g., "first", "1", "I") to "1st", "2nd", etc. 
•	College ID: Removed unwanted characters 
•	Email: Validated or reconstructed using firstname_surname@gmrit.edu 
•	Phone: Ensured 10-digit numbers starting with 6-9; padded as needed
<img width="940" height="650" alt="image" src="https://github.com/user-attachments/assets/a9721309-3663-4ea3-b77c-c1a7e5d836bd" />
##4. Save Cleaned Data 
Exported the cleaned data to another excel file.
##Result:
This cleaning process standardized your dataset into a consistent, analysis-ready format. It now contains:
•	No duplicates
•	Uniform formats across all fields
•	Valid entries with minimal missing data
•	Readable and professional structure
<img width="875" height="933" alt="image" src="https://github.com/user-attachments/assets/98299147-a6e8-40e0-bc48-26d6b512f351" />

