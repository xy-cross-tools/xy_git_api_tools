# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "GitHub"
"""
  * @File    :   GitHub.py
  * @Time    :   2024/11/24 10:46:00
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
import requests

from urllib.parse import urlencode
import requests

from xy_string.utils import is_empty_string

from .urls import api_url


class GitHub:

    @staticmethod
    def get(
        url: str,
        page: int = 1,
        per_page: int = 100,
        params: dict | None = None,
        headers: dict | None = None,
    ):
        query = {
            "page": page,
            "per_page": per_page,
        }
        if isinstance(params, dict):
            query.update(params)
        if is_empty_string(url) == False:
            response = requests.get(
                url,
                params=query,
                headers=headers,
                timeout=30,
            )
            if response and response.status_code == 200:
                return response.json()
        return None

    @staticmethod
    def repos(
        access_token: str,
        page: int = 1,
        per_page: int = 100,
        type_str: str = "all",
    ):

        url = api_url.get("repos")
        params = {
            "type": type_str,
        }
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {access_token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if is_empty_string(url) == True:
            return None
        return GitHub.get(
            url,  # type: ignore
            page,
            per_page,
            params=params,
            headers=headers,
        )
