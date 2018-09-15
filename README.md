# scrapy_meizitu
scrapy框架爬取meizitu
scrapy进阶：
   scrapy中的Data Flow：
   1.引擎（Engine）打开第一个网站（domain）并向spider请求第一个要爬取的url。
   2.Engine从spider中获取第一个要爬取的url并在调度器（scheduler）中以request调度。
   3.Engine向scheduler请求下一个要爬取的url。
   4.Scheduler返回下一个要爬取的url给engine，engine通过下载中间件（Downloader Middleware）（request方向）转发给下载器（Downloader）。
   5.一旦页面下载完毕，Downloader生成一个response通过Downloader Middleware（response方向）发送给 engine。
   6.Engine从Downloader接收到response并通过Spider中间件（middleware）（输入方向）发送给spider处理。
   7.Spider处理Response返回Item并把跟进的url新的Request给Engine。
   8.Engine将Spider返回的Item给Item Pipline，并将spider返回的Request给调度器。
   9.（从第二步）重复该过程直到Scheduler中没有request，引擎关闭该网站。
