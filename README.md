- <b>简体中文</b>

这是一个能让您搜索到的百度图片 进行随意的下载并分类保存到本地的一个项目，可用于深度学习数据集收集、发布和分享, 可配合标柱工具一起使用更加完美。
这是基于 scrapt框架 开发的一个可用于深度学习数据集收集的项目，您可以自由地在您的服务器上部署它。

环境要求
-----------
用于深度学习数据集收集 对您的服务器有一定的要求

- 一台Linux主机（Windows并非不可以）
- **Python >= 3.6**
- 安装 requeirement.txt 下 pip 包：

爬取数据
------------
如果你想快速运行，不考虑爬取内容时，默认爬取口罩相关内容

> 具体移步 `scrapt_crawler/scrapt_crawler/spiders/painting.py` PaintingSpider.__init__.search_word 部分

```bash
$ git clone git@github.com:vdjango/scrapt_crawler.git
$ pip3.6 install -r requeirement.txt
$ python3.6 main.py
```

* 遵循robots原则 `scrapt_crawler/scrapt_crawler/settings.py -> ROBOTSTXT_OBEY`
* 可爬取多个分类 search_word 是列表
* 爬取图片路径位于 `scrapt_crawler/scrapt_crawler/images/[分类]/`


定义爬取分类
-----

根据百度图片搜索结果，找到最适合的关键词，添加到项目相应的位置-搜索关键词。

> https://image.baidu.com/search/index?tn=baiduimage&word=戴口罩的人群

```bash
$ vim scrapt_crawler/scrapt_crawler/spiders/painting.py
...
class PaintingSpider(scrapy.Spider):
    ...
    def __init__(self, name=None, **kwargs):
        ...
        self.search_word = [
            '戴口罩的人群',  # 搜索关键词
            '人物图片原图',  # 搜索关键词
            # 修改具体爬取的分类（搜索关键词）
        ]
        ...
    ...
...
```

对数据进行标柱
-----

> 到这一步，需要提前将以爬取到的数据进行初步整理，然后使用标柱根据对数据进行标柱工作
具体移步labelme官网

```bash
$ pip3.6 install labelme
$ labelme
```



以爬取对部分数据预览
-----

* 戴口罩的人群

![](scrapt_crawler/images/戴口罩的人群/12.jpg)
![](scrapt_crawler/images/戴口罩的人群/14.jpg)
![](scrapt_crawler/images/戴口罩的人群/16.jpg)
![](scrapt_crawler/images/戴口罩的人群/19.jpg)
![](scrapt_crawler/images/戴口罩的人群/22.jpg)

* 人物图片原图

![](scrapt_crawler/images/人物图片原图/11.jpg)
![](scrapt_crawler/images/人物图片原图/13.jpg)
![](scrapt_crawler/images/人物图片原图/15.jpg)
![](scrapt_crawler/images/人物图片原图/19.jpg)
![](scrapt_crawler/images/人物图片原图/21.jpg)
