import json
import yaml
from conftest import base_url, base_sep



# 读取文件


def read_data(filename):
    # 读取数据文件
    with open(base_url + "data" + base_sep + filename, encoding="UTF-8") as r:
        data_list = list()
    #调用方法解释数据文件
        if filename[-4:] == "yaml" or filename[-4:] == ".yml":
            for data in yaml.safe_load(r).values():
                data_list.append(tuple(data.values()))
        elif filename[-4:] == "json":
            for data in json.load(r).values():
                data_list.append(tuple(data.values()))
        return data_list

if __name__ == '__main__':
    print(read_data("login.json"))