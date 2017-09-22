# coding: utf-8
# Created by firefoxwang 
# Data:  2017/9/19
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from contextlib import contextmanager

from publicCommon.mail_sender import mailtemple


class SendMail:
    def __init__(self):
        self.config = 1
        self.from_addr = "1228137800@qq.com"
        self.password = "wang19951211"
        self.to_addr = "wanglingbo1228137800@gmail.com"
        self.smtp_server = "smtp.qq.com"
        self.htmltemple = mailtemple.MailTemple()
        self.msg = ""  # 邮件内容配置
        self.smtp_port = 587
#name, case_info, suite_info, path, suite_status,  global_config
    @contextmanager
    def mail_sender(self, name, case_info, suite_info, path, suite_status,global_config):
        self.msg = MIMEText(self.htmltemple.parserhtml(name, case_info, suite_info, path, suite_status, global_config),  'html', 'utf-8')
        self.msg['From'] = Header(u"Robtfromwork Integration", 'utf-8').encode()
        self.msg['To'] = u"自动化收件人".encode("utf-8")
        self.msg['Subject'] = Header(u'自动化测试报告', 'utf-8').encode()
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        try:
            yield server
        except:
            print "邮件配置出错，请检查"
            raise
        finally:
            server.quit()
    def send_mail(self, name, case_info, suite_info, path,suite_status, global_config):
        with self.mail_sender(name, case_info, suite_info, path, suite_status,  global_config) as mailsend:
            mailsend.starttls()  # 邮件加密
            mailsend.set_debuglevel(1)
            mailsend.login(self.from_addr, self.password)
            mailsend.sendmail(self.from_addr, [self.to_addr], str(self.msg))

if __name__ == '__main__':
    demo = SendMail()
    demo.send_mail('Testsuit1',[{u'testcase01': 'PASS'}, {u'testcase02': 'PASS'}],['2 critical tests, 2 passed, 0 failed\n2 tests total, 2 passed, 0 failed', '20170922 10:07:33.166', '20170922 10:07:33.181'],u'c:\\users\wangli~1\\appdata\local\\temp\RIDEyde2ig.d\\log-20170922-102939.html' ,'PASS', 1)