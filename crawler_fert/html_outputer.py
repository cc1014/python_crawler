import xlwt


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将数据写入excel
    def output_excel(self):
        # fout = open('output.html','w')
        #
        # fout.write("<html>")
        # fout.write("<body>")
        # fout.write("<table>")
        #
        # # ascii
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td>%s</td>" % data['url'])
        #     fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
        #     fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
        #     fout.write("<tr>")
        #
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        #
        # fout.close()

        try:
            workbook = xlwt.Workbook(encoding='utf-8')
            sheet = workbook.add_sheet('BaiKeDetails')

            head = ['URL', 'title', 'summary']
            for h in range(len(head)):
                sheet.write(0, h, head[h])

            row = 1
            for data in self.datas:
                sheet.write(row, 0, data['url'])
                sheet.write(row, 1, data['title'])
                sheet.write(row, 2, data['summary'])
                row = row + 1

            workbook.save('BaikeList.xlsx')
            print('写入excel成功')
        except Exception:
            print('写入excel失败')