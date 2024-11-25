<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /git_api_tools/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# git_api_tools

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

xy open source software package operating environment.

## Source Code Repositories

| [Github](https://github.com/xy-cross-tools/xy_git_api_tools.git)         | [Gitee](https://gitee.com/xy-opensource/xy_git_api_tools.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_git_api_tools.git)          |
| ----------- | -------------|---------------------------------------|
 

## Installation

```bash
# bash
pip install xy_git_api_tools
```

## How to use

> !!! Note: When requesting a GitHub repository, you must include the username parameter, whether it is passed in from the command line or configured into the configuration file
> !!! The default configuration file path is ~/xy_config/xy_git.toml

###### 1. Configuration File

```toml
# config.toml
[git_config]
platform = "github"
# platform = "https://gitlab.com/api/v4/projects"
# platform = 0
# platform = "GitCode"
# platform = "giTcOde"
# platform = "giTCODe"

access_token = "ghp_454545454sadf1dfsa"
# access_token = "glpat-asdjklfjweroijweoirjwoer"

username = "yuyangit"
```

2. View Command

```bash
xy_git_api_tools -w list_api
# =========================================================

# 1. fetch_repos  获取所有仓库信息
# 2. clone_repos  克隆所有仓库, 
# 本地对应目录结构和仓库url相同

```

1. Get all repositories information

```bash
xy_git_api_tools -c fetch_repos -cfg ./config.toml
# [
#     {
#         "id": 4357570,
#         "full_name": "xy-opensource/xy_git_api_tools",
#         "human_name": "xy-opensource / xy_git_api_tools",
#         "url": "https://api.gitcode.com/api/v5/repos/xy-opensource/xy_git_api_tools",
#         "namespace": {
#             "id": 3536801,
#             "type": "enterprise",
#             "name": "xy-opensource",
#             "path": "xy-opensource",
#             "html_url": "https://gitcode.com/xy-opensource"
#         },
#         "path": "xy_git_api_tools",
#         "name": "xy_git_api_tools",
#         "description": "\u5173\u4e8eGit\u7684Api\u5de5\u5177",
#         "status": "\u5f00\u59cb",
#         "ssh_url_to_repo": "git@gitcode.com:xy-opensource/xy_git_api_tools.git",
#         "http_url_to_repo": "https://gitcode.com/xy-opensource/xy_git_api_tools.git",
#         "web_url": "https://gitcode.com/xy-opensource/xy_git_api_tools",
#         "created_at": "2024-11-24T13:11:49.606+08:00",
#         "updated_at": "2024-11-24T13:11:49.606+08:00",
#         "homepage": "https://gitcode.com/xy-opensource/xy_git_api_tools",
#         "members": [
#             "yuyangit"
#         ],
#         "assignee": [
#             {
#                 "id": "2173437",
#                 "login": "yuyangit",
#                 "name": "yuyangit",
#                 "avatar_url": "https://cdn-img.gitcode.com/fe/fd/f06483269e5f85434d8dc1aa80c1361e9f1fed704b5681043bed4eecaaffce8e.jpeg?time=1731978609795",
#                 "html_url": "https://gitcode.com/yuyangit",
#                 "type": "User"
#             }
#         ],
#         "forks_count": 0,
#         "stargazers_count": 0,
#         "project_labels": [],
#         "relation": "master",
#         "permission": {
#             "pull": true,
#             "push": true,
#             "admin": true
#         },
#         "internal": false,
#         "open_issues_count": 0,
#         "has_issue": false,
#         "watched": false,
#         "watchers_count": 0,
#         "assignees_number": 1,
#         "enterprise": {
#             "id": 3536801,
#             "path": "xy-opensource",
#             "html_url": "https://gitcode.com/xy-opensource",
#             "type": "enterprise"
#         },
#         "default_branch": "main",
#         "fork": false,
#         "owner": {
#             "id": "2173437",
#             "login": "yuyangit",
#             "name": "yuyangit",
#             "type": "User"
#         },
#         "assigner": {
#             "id": "2173437",
#             "login": "yuyangit",
#             "name": "yuyangit",
#             "type": "User"
#         },
#         "issue_template_source": "project",
#         "language": "Python",
#         "private": false,
#         "public": true
#     },
#     {
#         "id": 4357105,
#         "full_name": "xy-opensource/xy_pypi_builder_mirror",
#         "human_name": "xy-opensource / xy_pypi_builder_mirror",
#         "url": "https://api.gitcode.com/api/v5/repos/xy-opensource/xy_pypi_builder_mirror",
#         "namespace": {
#             "id": 3536801,
#             "type": "enterprise",
#             "name": "xy-opensource",
#             "path": "xy-opensource",
#             "html_url": "https://gitcode.com/xy-opensource"
#         },
#         "path": "xy_pypi_builder_mirror",
#         "name": "xy_pypi_builder_mirror",
#         "description": "\u7f16\u8bd1python\u6a21\u5757\u7684pypi\u73af\u5883\u7684\u955c\u50cf.",
#         "status": "\u5f00\u59cb",
#         "ssh_url_to_repo": "git@gitcode.com:xy-opensource/xy_pypi_builder_mirror.git",
#         "http_url_to_repo": "https://gitcode.com/xy-opensource/xy_pypi_builder_mirror.git",
#         "web_url": "https://gitcode.com/xy-opensource/xy_pypi_builder_mirror",
#         "created_at": "2024-11-24T08:55:04.966+08:00",
#         "updated_at": "2024-11-24T13:05:59.513+08:00",
#         "homepage": "https://gitcode.com/xy-opensource/xy_pypi_builder_mirror",
#         "members": [
#             "yuyangit"
#         ],
#         "assignee": [
#             {
#                 "id": "2173437",
#                 "login": "yuyangit",
#                 "name": "yuyangit",
#                 "avatar_url": "https://cdn-img.gitcode.com/fe/fd/f06483269e5f85434d8dc1aa80c1361e9f1fed704b5681043bed4eecaaffce8e.jpeg?time=1731978609795",
#                 "html_url": "https://gitcode.com/yuyangit",
#                 "type": "User"
#             }
#         ],
#         "forks_count": 0,
#         "stargazers_count": 0,
#         "project_labels": [],
#         "relation": "master",
#         "permission": {
#             "pull": true,
#             "push": true,
#             "admin": true
#         },
#         "internal": false,
#         "open_issues_count": 0,
#         "has_issue": false,
#         "watched": false,
#         "watchers_count": 0,
#         "assignees_number": 1,
#         "enterprise": {
#             "id": 3536801,
#             "path": "xy-opensource",
#             "html_url": "https://gitcode.com/xy-opensource",
#             "type": "enterprise"
#         },
#         "default_branch": "main",
#         "fork": false,
#         "owner": {
#             "id": "2173437",
#             "login": "yuyangit",
#             "name": "yuyangit",
#             "type": "User"
#         },
#         "assigner": {
#             "id": "2173437",
#             "login": "yuyangit",
#             "name": "yuyangit",
#             "type": "User"
#         },
#         "issue_template_source": "project",
#         "language": "Dockerfile",
#         "private": false,
#         "public": true
#     },
# ]
```

3. Git clone all repositories to the local, and store according to the corresponding path of the repository address structure

```bash
xy_git_api_tools -c clone_repos -cfg ./config.toml
```


## License
xy_git_api_tools is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![pay-total](./pay-total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```