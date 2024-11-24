# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'GitLab'
'''
  * @File    :   GitLab.py
  * @Time    :   2024/11/24 11:19:01
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
'''

from urllib.request import urlopen
import json
import subprocess
from pathlib import Path
import time

class GitLab:
    @staticmethod
    def repos(access_token: str, page: int=1, per_page:int=100,):
        pass
def main():
    #获取当前group下的所有仓库
    private_token = ""
    projects = urlopen(f"https://gitlab.com/api/v4/projects?private_token={private_token}&per_page=100&page=1")
    projects_list = json.loads(projects.read().decode())
    for project in projects_list:
        try:
            full_path = Path(project.get("path_with_namespace")).resolve()
            project_url = project.get('http_url_to_repo')
            if project_url.endswith("/"):
                project_url = project_url[:-1]
            try:
                if full_path.exists() is False:
                    full_path.mkdir(parents=True, exist_ok=True)
                    #因为我本地git clone 配置的是http格式的，所以我选择了http_url_to_repo, 如果你是用的git@格式，你就选择ssh_url_to_repo
                    targit_dir_path = full_path.resolve().as_posix().replace(" ", "\ ")
                    git_clone_command = f"git clone {project_url} {targit_dir_path}"
                    print("git_clone_command", git_clone_command)
                    reresultCode = subprocess.Popen(git_clone_command, shell=True, start_new_session=True,)
                    print(f"project url {project_url} reresultCode {reresultCode}")
                else:
                    continue
            except Exception as exception:
                print(f"mkdir Error on {project_url} {exception}")
            time.sleep(0.5)
        except Exception as exception:
            print(f"Error on {exception}")
