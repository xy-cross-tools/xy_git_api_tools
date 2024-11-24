# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'Runner'
'''
  * @File    :   Runner.py
  * @Time    :   2023/06/03 10:29:52
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, Ship of Ocean
  * @Desc    :   None
'''
from argparse import Namespace
from xy_argparse.ArgParse import ArgParse
import git_repo_api_tools

from .ModuleData import ModuleData
from .Resource import Resource

class Runner(ArgParse):
    _module_data = ModuleData()
    _resource = Resource()
    
    def __init__(self) -> None:
        self.quick_default_info(git_repo_api_tools.__name__)
        self.description = "Git仓库api工具"
        
    def main(self):
        self.default_parser()
        self.add_arguments()
        self.parse_arguments()
        self.run_arguments()

    def add_arguments(self):
        self.add_argument(
            flag="-w", 
            name="--work", 
            help_text="""
                1. list_api 展示api命令
            """
        )
        self.add_argument(
            flag="-c",
            name="--command",
            help_text="""
                工作方式: 1. api_repo_api_tools -c <api命令> 根据展示api命令对api进行操作
            """,
        )
        self.add_argument(
            flag="-at",
            name="--access_token",
            help_text="""
                输入access_token
            """,
        )
        self.add_argument(
            flag="-t",
            name="--type_value",
            help_text="""
                接口type参数
            """,
        )
        self.add_argument(
            flag="-p", 
            name="--page", 
            help_text="接口参数: 页码 => 默认: 1",
        )
        self.add_argument(
            flag="-pp", 
            name="--per_page", 
            help_text="接口参数: 每页个数 => 默认: 100, 最大100, 最小10",
        )

    def work(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.work
        return None
    
    def command(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.command
        return None
    
    def access_token(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.access_token
        return None
    
    def type_value(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.type_value
        return None
    
    def page(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.page
        return None
    
    def per_page(self):
        arguments = self.arguments()
        if isinstance(arguments, Namespace):
            return arguments.per_page
        return None
    
    def api_command(self):
        pass

    def list_api(self):
        pass