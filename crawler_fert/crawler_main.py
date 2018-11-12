from crawler_fert import url_manager, html_download, html_parser, html_outputer


class CrawlerMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            if count == 101:
                break
            try:
                # 如果有待爬取的URL，则取一个URL
                new_url = self.urls.get_new_url()
                print("craw %d : %s"%(count,new_url))
                # 下载对应的页面
                html_cont = self.downloader.download(new_url)
                # 页面下载好之后，进行对应页面的解析
                # 解析后得到新的URL和数据
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                # 将新的URL补充进URL管理器
                self.urls.add_new_urls(new_urls)
                #进行数据的收集
                self.outputer.collect_data(new_data)

                count = count+1
                print("爬取成功")
            except:
                print("爬取失败")

        # 输出结果
        self.outputer.output_excel()


if __name__=="__main__":
    root_url="https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_crawler=CrawlerMain()
    obj_crawler.craw(root_url)