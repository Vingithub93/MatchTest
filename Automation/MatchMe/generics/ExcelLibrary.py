import xlrd


def get_Cellvalue(excel_path, sheetName, columnNum, rowNum):
    
    book=xlrd.open_workbook(excel_path)
    sheet=book.sheet_by_name(sheetName)
    
    value=sheet.cell_value(rowNum, columnNum)
    
    return value

def get_columnValues(excel_path, sheetName, columnNum):
    book=xlrd.open_workbook(excel_path)
    sheet=book.sheet_by_name(sheetName)
    
    columnValues=sheet.col_values(columnNum)
    return columnValues

def get_rowValues(excel_path, sheetName, rowNum):
    book=xlrd.open_workbook(excel_path)
    sheet=book.sheet_by_name(sheetName)
    
    rowValues=sheet.row_values(rowNum)
    return rowValues
    