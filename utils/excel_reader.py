import openpyxl

def read_excel(file_path,sheet_name="Sheet1"):
    #加载工作表
    workbook =openpyxl.load_workbook(file_path,data_only=True)
    #根据表名来获取工作表
    sheet =workbook[sheet_name]
    #获取表的第一行作为cell的值
    headers = [cell.value for cell in sheet[1]]

    test_data = []
    #从表的第二行开始依次遍历
    for row in sheet.iter_rows(min_row=2,values_only=True):
        #将表头和每一行一一对应作为字典
        row_data =dict(zip(headers,row))
        #if any(v is not None and v != "" for v in row_data.values()):
        #any过滤全空行
        if any(row_data.values()):
            test_data.append(row_data)

    workbook.close()
    return test_data
