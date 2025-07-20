import pandas as pd
import numpy as np
import re
import random
from datetime import datetime

file_path = r"C:\Users\Mohan Krishna\OneDrive\Desktop\student_data_with_errors.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")
df = df.drop_duplicates()
data = df.sort_values(by='SurName')

#counting total blank values
df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
blank_count = data.isna().sum().sum()
print(f"Total blank values in raw data: {blank_count}")

#deleting rows with empty values which can't be replaced
data = data[data['SurName'].notna()]
data = data[data['FirstName'].notna()]
data = data[data['DOB'].notna()]
data = data[data['Branch'].notna()]
data = data[data['Year'].notna()]
data = data[data['College_Id'].notna()]


def clean_name(name):
    name = re.sub(r'\s+', '', name.strip())
    return name.title()

def clean_DOB(date):
    try:
        date = re.sub(r"[/.]", "-", date.strip())
        formats = ["%y-%m-%d", "%Y-%m-%d", "%d-%m-%Y", "%d-%m-%y"]
        for fmt in formats:
            try:
                date_obj = datetime.strptime(date, fmt)
                if date_obj.year >= datetime.today().year:
                    date_obj = date_obj.replace(year=random.randint(2001, 2007))
                return date_obj.strftime("%Y-%m-%d")
            except ValueError:
                continue
        return pd.NA
    except Exception:
        return pd.NA

def clean_branch(branch):
    branch = branch.upper().strip()
    branch = re.sub(r"\s+", "", branch)
    branch = re.sub(r"INFOTECH", "IT", branch)
    branch = re.sub(r"MECHANICAL", "MECH", branch)
    branch = re.sub(r"COMPSCI", "CSE", branch)
    branch = re.sub(r"ELECTRICAL", "EEE", branch)
    return branch

def clean_year(year):
    year = str(year).strip().lower()
    year = re.sub(r'[^a-z0-9]', '', year)
    year_map = {
        "1": "1st", "1st": "1st", "first": "1st", "firstyear": "1st", "i": "1st", "yr1": "1st",
        "2": "2nd", "2nd": "2nd", "second": "2nd", "secondyear": "2nd", "ii": "2nd", "yr2": "2nd",
        "3": "3rd", "3rd": "3rd", "third": "3rd", "thirdyear": "3rd", "iii": "3rd", "yr3": "3rd",
        "4": "4th", "4th": "4th", "fourth": "4th", "fourthyear": "4th", "iv": "4th", "yr4": "4th"
    }
    return year_map.get(year, pd.NA)


def clean_id(college_id):
    college_id = str(college_id).strip().upper()
    college_id = re.sub(r'[^A-Z0-9]', '', college_id)
    return college_id


def clean_email(email,row=None):
    email = email.strip().lower()
    email_pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    if re.fullmatch(email_pattern, email):
        return email
    if row is not None:
        s_name=re.sub(r"\s+","",str(row['SurName'])).lower()  
        f_name=re.sub(r"\s+","",str(row['FirstName'])).lower()
        email= f_name + '_' + s_name + "@gmrit.edu"
        return email
    return None

def clean_phone(phone):
    phone = re.sub(r"\D", "", phone)
    if len(phone) == 0:
        phone = str(random.randint(6, 9))
    while len(phone) < 10:
        phone += str(random.randint(0, 9))
    phone = phone[-10:]
    if phone[0] not in ['6', '7', '8', '9']:
        phone = str(random.randint(6, 9)) + phone[1:]
    return "+91" + phone


data['SurName'] = data['SurName'].astype(str).apply(clean_name)
data['FirstName'] = data['FirstName'].astype(str).apply(clean_name)
data['DOB'] = data['DOB'].astype(str).apply(lambda x: clean_DOB(x) if pd.notna(x) else x)
data['Branch'] = data['Branch'].astype(str).apply(lambda x: clean_branch(x) if pd.notna(x) else x)
data['Year'] = data['Year'].astype(str).apply(lambda x: clean_year(x) if pd.notna(x) else x)
data['College_Id'] = data['College_Id'].astype(str).apply(lambda x: clean_id(x) if pd.notna(x) else x)
data['Email'] = data.apply(lambda row: clean_email(row['Email'], row), axis=1)
data['Phone'] = data['Phone'].astype(str).apply(lambda x: clean_phone(x) if pd.notna(x) else x)

df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
b_count = data.isna().sum().sum()
print(f"Total blank values after cleaning data: {b_count}")

result_file_path=r"C:\Users\Mohan Krishna\OneDrive\Desktop\cleaned_data.xlsx"
data.to_excel(result_file_path, index=False, engine='openpyxl')

