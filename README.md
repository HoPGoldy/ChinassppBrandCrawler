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


Chinasspp类提供的方法
----
1. **searchBrand(brandName):

	参数：

	**brandName**: 搜索的品牌名

	返回值：
	**list**类型 元素为包含了搜索到的品牌名称和介绍的字典

2. **getPageItems(pageNum)**

	参数：

	**pageNum**: 想要爬取的页数

	返回值：
	**list**类型 元素为该页所包含的品牌url
	
3. **getLadiesPageItems(pageNum)**

	参数：

	**pageNum**: 想要爬取的页数，目标是女装品牌

	返回值：
	**list**类型 元素为该页所包含的品牌url
	
4. **getItemInfo(url)**

	参数：

	**url**: chinasspp的品牌详情页

	返回值：
	**dict**类型 包含了品牌名和品牌介绍
