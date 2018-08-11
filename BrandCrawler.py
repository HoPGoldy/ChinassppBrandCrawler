from ChinassppControl import Chinasspp
import time
import xlwt
import xlrd

def getBrand(minPageNum, maxPageNum,brandType = '全部', excelName = '品牌介绍'):
    #实例化控制器，验证输入页码可靠性
    chinasspp = Chinasspp()
    if minPageNum > maxPageNum:
        print('输错了')
        return False

    #新建excel，默认填写列首信息
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('品牌介绍', cell_overwrite_ok=True)
    sheet.write(0, 0, '序号')
    sheet.write(0, 1, '品牌名')
    sheet.write(0, 2, '来源')
    sheet.write(0, 3, '介绍')
    writeRow = 1
    
    #开始抓取
    for i in range(minPageNum, maxPageNum + 1):
        if brandType == '全部':
            itemUrls = chinasspp.getPageItems(i)
        elif brandType == '女装':
            itemUrls = chinasspp.getLadiesPageItems(i)
        else:
            itemUrls = chinasspp.getPageItems(i)

        for j in range(0, len(itemUrls)):
            time.sleep(2)
            itemInfo = chinasspp.getItemInfo(itemUrls[j])
            print(f'  {itemInfo["name"]}    {itemUrls[j]}\n————————————————————————————————————————\n{itemInfo["introduce"]}\n\n')
            sheet.write(writeRow, 0, writeRow)
            sheet.write(writeRow, 1, itemInfo["name"])
            sheet.write(writeRow, 2, itemUrls[j])
            sheet.write(writeRow, 3, itemInfo["introduce"])
            writeRow += 1

        book.save(excelName + '.xls')
        print(f'第{i}页抓取完毕，休息5秒\n')
        time.sleep(5)


if __name__ == '__main__':
    getBrand(minPageNum = 1, maxPageNum = 50, brandType = '女装', excelName = '女装品牌介绍')

