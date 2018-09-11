# Data_splitter
Splits data using a data seperator mentioned, into multiple columns.


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
        
        
      
