# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'GitHub'
'''
  * @File    :   GitHub.py
  * @Time    :   2024/11/24 10:46:00
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
'''
import requests
from .urls import api_url
from urllib.parse import urlencode

class GitHub:
    @staticmethod
    def repos(access_token: str, page: int=1, per_page:int=100,):
        
        access_token = ""
        url = "https://api.github.com/users/user/repos?type=all&per_page=100&page=1"

        query_map = {
            "type": "all",
            "per_page": 100,
            "page": 1,
        }
        repos_url = api_url.get("repos")
        query = urlencode(query_map)
        url = f"{repos_url}{query}"
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {access_token}',
            'X-GitHub-Api-Version': '2022-11-28',
        }

        resp = requests.get(url, headers=headers,)
        print(resp.text)