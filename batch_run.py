#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 3:37 下午
# @File    : batch_run.py
# @Project : jd_scripts
# @Desc    : 批量运行脚本
import time
import os
from pathlib import Path
from utils.logger import logger


def get_py():
    """
    获取python 文件
    """
    pwd = Path.cwd()

    py_list = [i[2] for i in os.walk(pwd)][0]

    shell_list = []

    for i in py_list:
        if i.startswith('jr') or i.startswith('jd') or i.startswith('dj'):
            shell_list.append(i)

    return shell_list


if __name__ == '__main__':
    logger.info('批量执行py脚本开始！')
    pylist = get_py()
    num = len(pylist)
    while num:
        for j in pylist:
            time.sleep(5)
            sh = f'python3 {j}'
            os.system(sh)
            logger.info(f'执行{j}脚本完成')
            num = -1
    logger.info(f'批量执行py脚本完成！！本次共执行{len(pylist)}个脚本文件')
