ChinassppBrandCrawler
====
介绍
----
用于爬取网站 http://www.chinasspp.com/ 上的品牌数据，目前支持爬取全部品牌和女装分类

安装与使用
----
1. **安装依赖**
	cd 到文件跟目录下后键入：
	
	```pip3 install -r requirements.txt```
3. **启动测试用例**

	测试用例会在chinasspp上搜索ZARA的品牌介绍并返回

	```python example.py```

getBrand方法
----
**getBrand( minPageNum, maxPageNum, brandType = '全部', excelName = '品牌介绍')**

参数：
1. **minPageNum**: 需要爬取的最小页码
 
2. **maxPageNum**: 需要爬取的最大页码
  
3. **brandType**： 需要爬取的品牌类型，目前支持“全部”以及"女装"，输入未知类型则爬取全部
		
4. **excelName**： 保存输入的excel文件名
