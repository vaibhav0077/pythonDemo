import xlrd

loc = "C:\Users\Vaibhav\Desktop\Book1.xlsx"

wb = xlrd.open_workbook(loc)     
sheet = wb.sheet_by_index(0)  

sheet.cell_value(0, 0) 
      
  