# coding: utf-8
# Created by firefoxwang 
# Data:  2017/9/21
import re


class MailTemple:
    def __init__(self):
        self.version = "1.0.0"
        self.output = None
        self.html_temple = u'''<?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>%(title)s</title>
            <meta name="generator" content="%(generator)s"/>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
            %(stylesheet)s
            <link href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
        <div id="div_base">
        %(teststatis)s

        </div>
        </body>
        </html>'''

        self.stylesheet_temple = u"""
        <style type="text/css" media="screen">
        body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
        table       { font-size: 100%; }
        pre         { white-space: pre-wrap;word-wrap: break-word; }

        /* -- heading ---------------------------------------------------------------------- */
        h1 {
        	font-size: 16pt;
        	color: gray;
        }
        .heading {
            margin-top: 0ex;
            margin-bottom: 1ex;
        }

        .heading .attribute {
            margin-top: 1ex;
            margin-bottom: 0;
        }

        .heading .description {
            margin-top: 2ex;
            margin-bottom: 3ex;
        }

        /* -- css div popup ------------------------------------------------------------------------ */
        a.popup_link {
        }

        a.popup_link:hover {
            color: red;
        }

        .popup_window {
            display: none;
            position: relative;
            left: 0px;
            top: 0px;
            /*border: solid #627173 1px; */
            padding: 10px;
            background-color: #E6E6D6;
            font-family: "Lucida Console", "Courier New", Courier, monospace;
            text-align: left;
            font-size: 8pt;
            /* width: 500px;*/
        }

        }
        </style>
        """
        self.teststatis = u'''<p></p>
        <p class='description'>总用例分布与执行情况</p>
        <table id='result_table' class="table table-bordered">
        <colgroup>
        <col align='left' />
        <col align='right' />
        </colgroup>
        <tr id='header_row'>
            <td>CASE NAME</td>
            <td>CASE STATUS</td>

        </tr>
        %(test_list)s
            <td>总计</td>
            <td>%(count)s</td>
            <td>%(Pass)s</td>
            <td>%(fail)s</td>
            <td>&nbsp;</td>
        </tr>
        </table>
        '''
        self.testlist = u"""<tr><td>%(case_name)s</td><td>%(case_status)s</td></tr>"""

    def _case_parser(self, case_info):
        """
        解析传过来case的信息
        :param case_info: 监听器传过来的caseinfo
        :return: 返回变成类似html图表的值
        """
        testrow = []
        for i in case_info:
            for k, v in i.iteritems():
                row = self.testlist % dict(case_name=k, case_status=v)
                testrow.append(row)
        return testrow

    def _teststatis(self, suite_info, case_info):
        """
        用正则表达式截取到总数跟成功失败个数
        :param suite_info: 套件信息
        :return:_teststatis模板信息
        """
        p = re.compile(r'\d+')
        suite_list = p.findall(suite_info)
        testrow = self._case_parser(case_info)
        list_suite = self.teststatis % dict(test_list=testrow, count=suite_list[0], Pass=suite_list[1],
                                            fail=suite_list[2])
        return list_suite

    #
    def parserhtml(self, name, case_info, suite_info, path, suite_status, global_config):
        list_suite = self._teststatis(suite_info, case_info)
        generator = 'RfIntegrationTest %s' % self.version
        self.output = self.html_temple % dict(title=('[AutoTest]' + name + 'is' + suite_status), generator=generator,
                                              stylesheet=self.stylesheet_temple, teststatis=list_suite)
        print self.output
        return self.output
