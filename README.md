[![Build Status](https://travis-ci.org/firefoxwang/RfIntegration.svg?branch=master)](https://travis-ci.org/firefoxwang/RfIntegration)

##RfIntegration是什么?

是一个robotframework可持续集成框架，可通用扩展,通过robot监听器实现

##RfIntegration有哪些功能？

* 主函数
    * 监听器
        * 记录每次项目运行的结果入库（已实现）
        * 项目运行结束发送测试结果邮件（已实现）
    * 公共类
       * 获取配置文件类
       * 获取jenkins api相关信息
    * 项目工具类（可考虑实现成远程库）
        * http重写
        * 项目接口入参配置
        * 数据库操作类
            * mysql操作
            * redis操作
            * sqlserver操作
        * json校验
* RFproject
	* 测试用例集
	* 项目关键字
	* 项目数据

* api
	* 提供全部并发执行的接口（脚本）
	* 提供定时任务执行接口（脚本）
	* 提供jenkins执行接口（脚本）

##有问题反馈
在使用中有任何问题，欢迎反馈给我，可以用以下联系方式跟我交流

* 邮件(1228137800@gmail.com)
* QQ: 1228137800


##如何使用
直接修好好配置就可以，分为接口测试本地跟远程的定时任务两个项目。

接口测试本地大多使用ride作为编辑器，在运行参数里加入监听器的路径跟参数，如:--listener D:\python_project\RfIntegration\MyListener.py:TestProject

远程比较复杂，有空写一个教程。

##注意
可持续集成框架主要是放在linux服务器上起定时任务跑的，再根据jenkins api跟jenkins

交互，根据入库结果判断一个自动化项目是否可以发布到验收环境。不建议在ride框架中使用

