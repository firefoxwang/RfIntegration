# coding: utf-8
# Created by firefoxwang 
# Data:  2017/9/17
import projectHelper
import publicCommon


class MyListener:
    """
    监听器，用来获取执行结果；项目数据入库；发送邮件
    """
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, project_name):
        print "MyListener开始监听"
        self.name = project_name
        self.case_info = []  # dict格式case通过为pass，不通过为报错信息
        self.suite_info = []  # ，统计用力个数，分别失败跟成功个数,时间
        self.suite_status = ''  # 整个projcet是成功还是失败的
        self.path = ''  # 生成的报告路径
        self.dbOperater = projectHelper.db_operater.DbOperater()
        self.mailSender = publicCommon.mail_sender.SendMail()
        self.configGetter =  publicCommon.get_config.GetConfig()

    def end_test(self, name, attrs):
        case_dict = {name: "PASS" if attrs['status'] == 'PASS' else attrs['message']}
        self.case_info.append(case_dict)

    def end_suite(self, name, attrs):
        if name == self.name:  # 项目与套件匹配
            self.suite_info.append(attrs['statistics'])
            self.suite_info.append(attrs['starttime'])
            self.suite_info.append(attrs['endtime'])
            self.suite_status = attrs['status']

    def log_file(self, path):
        self.path = path

    def close(self):
        global_config = self.configGetter.get_goabal_config()
        self.dbOperater.write_db_operation(self.name, self.case_info, self.suite_info, self.suite_status, global_config)
        self.mailSender.send_mail(self.name, self.case_info, self.suite_info, global_config)

