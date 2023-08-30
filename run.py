# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import numpy as np

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bike_Data_Project3')

bikesharing = SHEET.worksheet('bike_dataset')

data = bikesharing.get_all_values()

values = bikesharing.range('P2:P32')
number_values = [float(cell.value) for cell in values]
sum_of_values_jan_eleven = sum(number_values)
jan_eleven_average = sum_of_values_jan_eleven / 31
print(f"The average for January was {jan_eleven_average}")



