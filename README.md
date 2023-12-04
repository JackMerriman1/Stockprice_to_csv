# Stockprice_to_csv
This program will generate a CSV file viewable in Excel/Google sheets, located within this folder, with data regarding the prices of stocks.  All you need to do is follow the instrucitons below:

How to use the program!
1. Go to https://polygon.io/dashboard/api-keys
	a. Create an account and generate an API Key, you will need to enter this into the Api Key field in the program
2. Run the Stock_Price_To_CSV_EXE file
3. Enter the corresponding information into each field, make sure the format is correct for the start and end date field otherwise it will not work.
4. Go to the folder this program is located in to find your CSV file.

NOTES: Every time you click Fetch Data the program will generate a new CSV file.
I.E if you want multiple CSV files representing different ticker symbols just edit the ticker field and press Fetch Data, no need to restart the program. :)

To turn into an .exe file you can either use 3rd party software, or download python and enter the following into you command prompt:
pyinstaller --onefile Path\To\File\Python_Script.py


Author - Jack Merriman
Email - jack.merriman2@gmail.com
