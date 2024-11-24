# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'Gitee'
'''
  * @File    :   Gitee.py
  * @Time    :   2024/11/24 10:45:56
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
'''
"""
    https://gitee.com/api/v5/user/repos?per_page=100&page=1&access_token=
"""

class Gitee:
    @staticmethod
    def repos(access_token: str, page: int=1, per_page:int=100,):
        pass