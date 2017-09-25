# coding: utf-8
# Created by firefoxwang 
# Data:  2017/9/19
from ConfigParser import ConfigParser


class GetConfig(object):
    def __init__(self, name):
        cfg = ConfigParser()
        cfg.read('./publicCommon/get_config/public_config.ini')
        self.name = name
        self.publicdb = cfg.get('soraka', 'config')
        self.from_addr = cfg.get('mail', 'from_addr')
        self.password = cfg.get('mail', 'password')
        self.smtp_server = cfg.get('mail', 'smtp_server')
        self.smtp_port = cfg.get('mail', 'smtp_port')
        self.config = cfg.get('config', 'config')
        self.to_addr = project_mails[self.name]

    def get_goabal_config(self):
        return self.config

    def get_publicdb(self):
        return self.publicdb

    def mail_config(self):
        return [self.from_addr,
                self.password,
                self.to_addr,
                self.smtp_server,
                self.smtp_port
                ]

# 项目需邮件接收人
project_mails = {

    "Testsuit1": ['wanglingbo1228137800@gmail.com'],

}