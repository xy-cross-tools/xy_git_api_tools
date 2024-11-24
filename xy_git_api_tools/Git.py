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
import json

from xy_console.utils import print_exe

from .platform.Platform import Platform


class Git:
    @staticmethod
    def fetch_repos(
        channel_code: str | int,
        access_token: str,
        url: str = "",
        page: int = 1,
        per_page: int = 100,
        type_str: str = "all",
        params: dict = {},
    ):
        platform = Platform(channel_code)
        repos = platform.repos(
            url,
            access_token,
            page,
            per_page,
            type_str,
            params,
        )
        print_exe(json.dumps(repos))

    @staticmethod
    def clone_repos(
        channel_code: str | int,
        access_token: str,
        url: str = "",
        page: int = 1,
        per_page: int = 100,
        type_str: str = "all",
        params: dict = {},
    ):
        pass
