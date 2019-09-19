# Spider4Novel

这是为学习《海量数据处理》课程准备的简单文本爬虫作业.
****
主要利用Python爬虫对两个小说网站进行了按章节的文本爬取实验，并将结果输出到txt文件中：
+ [十分朴素的小说网站](http://www.jingcaiyuedu.com/novel/GLSmM4.html)
+ [js修饰过的小说网站](https://doupocangqiong1.com/1/)

处理方法：
+ 对于前者，直接在Chrome浏览器中审查元素，利用request获取html源码，利用re正则表达式进行筛选，最后replace进行数据清洗.
+ 对于后者，采取同样的思路处理，发现网页会有一个加载的过程，无法爬取到正确的内容。因此使用selenium等待文本加载完毕后再读取.
