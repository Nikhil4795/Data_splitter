"""
    Written @ Nikhil
    
    If you have any questions or suggestions regarding this script,
    feel free to contact me via nikhil.ss4795@gmail.com
    
    Report bugs to @ nikhil.ss4795@gmail.com
    
    Description :
    
    Splits data using a data seperator mentioned, into multiple columns.
    1. When given data which has no seperator then it remains same.
    2. When mentioned date seperator is not present, then it remains same.
    
    Example :
            Input  : Hai | Bye | Hola
            Output : Hai, Bye, Hola (Comes in three columns)
            Output : 2345 | 8235
            Input : 2345, 8235 (Comes in two columns)
            Output : 18/9/2011
            Output : 18/9/2011 (Comes in one column)
            
    Input Sheet Constraints :
            1. Must be either csv or xlsx. (recommended : csv)
            
    output sheet :
            1. The output sheet contains all the columns from the input sheet and
               the results of the splitted columns at last.
               
            2. If the input sheet is xlsx and the doesn't contain data seperator then,
               you need to do some external formatting, do the following :
               1. go to this link : https://github.com/Nikhil4795/Required_Date-extractor
               2. There will be a folder called xlsx_formatting_screenshots , explore it
                  you will find the answer for formatting.
                  
            3. If the input sheet is csv, then it works fine. No need to do any external formatting.
            
    How to run :
            1. Keep only two files in the folder. one should be script file and the other is input sheet.
            2. Hit run
            3. Mention the seperator used in your input sheet to seperate dates with quotes and without spaces.
            4. Mention the column number starting from 0, in which the dates are present.
    
    
    Requirements :
        1. python 2 or python 3.
        2. Modules required in python :
            csv, xlrd, xlsxwriter, os, sys, time.
            (To install modules : pip install module_name)
                
            
"""


import csv
import xlrd, xlsxwriter
import time
import os
import sys


file_names = os.listdir('.')
max_len = 0
head_count = 1

if len(file_names) == 2:
    pass
else:
    print("Error : Folder should contain only two files.")
    print("     One should be script file and the other is input sheet")
    sys.exit()

try:
    print("\n\n###  Please mention the seperator used to seperate your data")
    print("       Example : Hai | Bye | Hola")
    print("""       Here '|' is seperating the multiple dates""")
    date_seperator = input("\n###  Enter your data seperator with quotes : ")
except:
    print("\nError : Wrong Format of mentioning the seperator")
    print("        Please make sure that you've entered the seperator within quotes")
    sys.exit()


print("\n###  Please Mention in which column the data is present")
date_col = input("      ###  Enter the colum number starting from 0 : ")

input_type = ""
input_name = ""

for i in range(0,len(file_names)):
    if file_names[i][-4:] == 'xlsx':
        input_name = file_names[i][:-5]
        input_type = "xlsx"
    if file_names[i][-3:] == 'csv':
        input_name = file_names[i][:-4]
        input_type = "csv"

if input_type == 'csv' or input_type == 'xlsx':
    print("\n")
    print("Input file type found : ",input_type)
else:
    print("Error in file format : ")
    print("     Sheet must be either in csv or xlsx ")
    sys.exit()


start_time = time.time()

if input_type == 'csv':
    datain = csv.reader(open(input_name+".csv","rU"))
    dataout = open(input_name+"_results.csv","wb")
    datawrite = csv.writer(dataout)

    header = []
    all_rows = []
    all_rows.append(["temp_1","temp_2","temp_3"])


    for index,each in enumerate(datain):
        if index == 0:
            for i in range(0,len(each)):
                header.append(each[i])
        else:
            row_data = []
            for i in range(0,len(each)):
                row_data.append(each[i])
            
            try:
                temp = each[date_col].split(date_seperator)
            except:
                print("\nError : I guess, Mentioned data column number or data seperator is Incorrect. Please recheck it again.")
                sys.exit()
            
            final_temp = []
            for i in range(0,len(temp)):
                final_temp.append(temp[i].strip())


            if (len(final_temp)) > max_len :
                max_len = len(final_temp)

            for i in range(0,len(final_temp)):
                row_data.append(final_temp[i])

            all_rows.append(row_data)

    for i in range(0,max_len):
        header.append("split_"+str(head_count))
        head_count = head_count + 1

    all_rows[0] = header
    datawrite.writerows(all_rows)


if input_type == 'xlsx':
    
    datain = xlrd.open_workbook(input_name+".xlsx").sheet_by_index(0)
    dataout = xlsxwriter.Workbook(input_name+"_results.xlsx")
    datawrite = dataout.add_worksheet()
    
    header = []

    for row in range(0,datain.nrows):
        if row == 0:
            for j in range(0,datain.ncols):
                header.append(datain.cell_value(row,j))
        else:
            row_data = []
            for j in range(0,datain.ncols):
                row_data.append(datain.cell_value(row,j))

            try:
                temp = str(datain.cell_value(row,date_col)).split(date_seperator)
            except:
                print("\nError : I guess, Mentioned data column number or data seperator is Incorrect. Please recheck it again.")
                sys.exit()
                
            final_temp = []

            for i in range(0,len(temp)):
                final_temp.append(temp[i].strip())

            if (len(final_temp)) > max_len :
                max_len = len(final_temp)

            for i in range(0,len(final_temp)):
                row_data.append(final_temp[i])

            for col in range(0,len(row_data)):
                datawrite.write(row,col,str(row_data[col]))


    for i in range(0,max_len):
        header.append("split_"+str(head_count))
        head_count = head_count + 1

    for col in range(0,len(header)):
        datawrite.write(0,col,str(header[col]))


dataout.close()
print("\n\nTask Completed")
print("     Took around : %s seconds " % (time.time() - start_time))


"""

    Written @ Nikhil

    If you have any questions or suggestions regarding this script,
    feel free to contact me via nikhil.ss4795@gmail.com

    report bugs to @ nikhil.ss4795@gmail.com

"""

