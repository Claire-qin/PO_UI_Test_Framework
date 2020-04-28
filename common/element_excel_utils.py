import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'../element_infos_datas/element_infos.xlsx')

class ElementExcelUtil:
    def __init__(self,page_name,element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.row_count = self.sheet.nrows  # 行数

    def get_elemnet_info(self):
        element_infos = {}
        for i in range(1,self.row_count):  # 行
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i,1).strip()  #.strip() 去除字符串两头的空格
            element_info['locator_type'] = self.sheet.cell_value(i,2).strip()
            element_info['locator_value'] = self.sheet.cell_value(i,3).strip()
            element_info['timeout'] = self.sheet.cell_value(i,4)
            if self.sheet.ncols > 5:
                element_info['is_iframe'] = self.sheet.cell_value(i, 5)
            if self.sheet.ncols > 6:
                element_info['iframe_id_name'] = self.sheet.cell_value(i, 6).strip()
            if self.sheet.ncols > 7:
                element_info['iframe_locator_value'] = self.sheet.cell_value(i, 7).strip()

            key = self.sheet.cell_value(i, 0).strip()
            element_infos[key] = element_info
        return element_infos

if __name__ == '__main__':
    elements = ElementExcelUtil('delete_depts_page')
    print(elements.get_elemnet_info())



