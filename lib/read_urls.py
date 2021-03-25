# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""读取 urls 文件夹中文件"""

import logging


def read_file(filename):
    """
    读文件函数
    :param filename: 文件名
    :return:
    """
    log = logging.getLogger("Spider.crawler")
    try:
        f = open(filename)
    except IOError:
        log.error("read file failed: in open: %s" % filename)
        return None

    try:
        data = f.readlines()
    except IOError:
        log.error("read file lines failed: in open: %s" % filename)
        return None
    try:
        f.close()
    except IOError:
        log.error("failed to close file: in open: %s" % filename)
        return None
    return data
