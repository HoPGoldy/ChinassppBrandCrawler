# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 19:12
# @Author  : HoPGoldy

from ChinassppControl import Chinasspp

if __name__ == '__main__':
    chinasspp = Chinasspp()
    result = chinasspp.searchBrand('zara')

    if result is not None:
        for item in result:
            print(f'[名称] {item["name"]}')
            print(f'[介绍] {item["introduce"]}')
