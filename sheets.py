"""To install the code you need to install following packages with pip -"""
"""pip install gspread oauth2client"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",  # targets
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("YOUR_CREDS.JSON_FILE", scope)
client = gspread.authorize(creds)
sheet = client.open("My_Flight_Deals").sheet1

data = sheet.get_all_records()
row = sheet.row_values(3)
column = sheet.col_values(3)
cell = sheet.cell(2, 2).value

insert_row = ["Moscow", "SVO", 357]
# sheet.insert_row(insert_row, 12)
# sheet.delete_row(12)
# sheet.update_cell(12,2,"SVO")

num_rows = sheet.row_count  # Counts all the rows from the sheet (including the ones with content)
print(len(data))  # Len of rows with content
