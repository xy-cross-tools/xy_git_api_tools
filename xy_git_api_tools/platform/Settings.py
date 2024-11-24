# -*- coding: UTF-8 -*-
__author__ = '余洋'
__doc__ = 'Settings'
'''
  * @File    :   Settings.py
  * @Time    :   2024/11/24 20:57:20
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
'''

from pathlib import Path

from xy_settings.Settings import Settings as xy_s


class Settings(xy_s):
    default_cfg_path: Path = Path.home().joinpath(".xy_config/xy_git.toml")

    def initial_cfg_path(self):
        cfg_dir_path = self.default_cfg_path.parent
        if cfg_dir_path.exists() == False:
            cfg_dir_path.mkdir(parents=True, exist_ok=True)
        if self.default_cfg_path.exists() == False:
            self.default_cfg_path.touch()
