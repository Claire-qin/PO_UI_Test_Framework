import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'../element_infos_datas/element_infos.xlsx')

class ElementdataUtil:
    def __init__(self,page_name,element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.row_count = self.sheet.nrows  # 行数

    def get_elemnet_info(self):
        elemnet_infos = {}
        for i in range(1,self.row_count):
            elemnet_info = {}
            elemnet_info['element_name'] = self.sheet.cell_value(i,1).strip()  #.strip() 去除字符串两头的空格
            elemnet_info['locator_type'] = self.sheet.cell_value(i,2).strip()
            elemnet_info['locator_value'] = self.sheet.cell_value(i,3).strip()
            elemnet_info['timeout'] = self.sheet.cell_value(i,4)
            elemnet_infos[self.sheet.cell_value(i,0).strip()] = elemnet_info
        return elemnet_infos

if __name__ == '__main__':
    elments = ElementdataUtil('main_page')
    print(elments.get_elemnet_info())



