# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'Git'
'''
  * @File    :   Git.py
  * @Time    :   2024/11/24 12:15:16
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
'''

from .platform.Platform import Platform


class Git:
    @staticmethod
    def fetch_repos(
        platform: Platform,
        page: int = 1,
        per_page: int = 100,
        type_str: str = "all",
    ):
        pass

    @staticmethod
    def clone_repos(
        platform: Platform,
        page: int = 1,
        per_page: int = 100,
        type_str: str = "all",
    ):
        pass
