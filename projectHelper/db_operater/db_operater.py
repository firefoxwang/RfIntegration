# coding: utf-8
# Created by firefoxwang 
# Data:  2017/9/19
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class DbOperater():
    def __init__(self):
        self.config = "sqlite:///Soraka.db"  # 在本目录下生成一个sql数据库 类似engine://user:password@host:port/database
        self.engine = create_engine(self.config, echo=False)  # 真实环境设置为false
        self.Base = declarative_base()  # 创建一个声明类，映射类到表的关系。

    def write_db_operation(self, name, case_info, suite_info, suite_status, global_config):
        # 建表
        class Soraka(self.Base):
            __tablename__ = "soraka"
            id = Column(Integer, primary_key=True)  # 主键类型为整数默认自增
            name = Column(String)
            case_info = Column(String)
            suite_info = Column(String)
            suite_status = Column(String)
            start_time = Column(DateTime)
            end_time = Column(DateTime)
            global_config = Column(String)

        class WriteDb(object):
            def write_result(self, session):
                star_time = datetime.datetime.strptime(suite_info[1], "%Y%m%d  %H:%M:%S.%f")
                end_time = datetime.datetime.strptime(suite_info[2], "%Y%m%d  %H:%M:%S.%f")
                strcaseinfo = str(case_info)  # case_info的格式需要转换
                result = Soraka(name=name, case_info=strcaseinfo, suite_info=suite_info[0], suite_status=suite_status,
                                global_config=global_config, start_time=star_time, end_time=end_time)
                session.add(result)

        # 创建数据库，如果已创建，则不执行
        self.Base.metadata.create_all(self.engine)
        # 创建会话
        Session = sessionmaker(bind=self.engine)

        @contextmanager
        def session_scope():
            """Provide a transactional scope around a series of operations."""
            session = Session()
            try:
                yield session
                session.commit()
            except:
                    session.rollback()
                    raise
            finally:
                session.close()

        with session_scope() as session:
            WriteDb().write_result(session)
