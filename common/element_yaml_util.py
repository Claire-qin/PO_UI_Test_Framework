import os
import yaml

current_path = os.path.dirname(__file__)

class ElementYamlUtil:
    def __init__(self,file_name):
        yaml_path = os.path.join(current_path, '../element_infos_datas/%s.yaml'%file_name)
        self.file = open(yaml_path, encoding='UTF-8')

    def get_elemnet_info(self):
        element_infos = yaml.load(self.file)
        return element_infos

if __name__ == '__main__':
    util = ElementYamlUtil()