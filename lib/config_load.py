# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""配置读取封装模块"""
import configparser
import os
import logging

import read_urls


class Config(object):
    """配置类"""

    def __int__(self, config_path):
        self.config_path = config_path
        self.cfg = configparser.ConfigParser()

    # get_value获取全部的字符串，section区域名, option选项名
    def get_value(self, section, option):
        self.cfg.read(self.config_path)
        return self.cfg.get(section, option)

    # get_int获取整型，section区域名, option选项名
    def get_int(self, section, option):
        """
        get_int获取整型
        :param section: 区域名
        :param option: 选项名
        :return:
        """
        self.cfg.read(self.config_path)
        return self.cfg.getint(section, option)

    # get_float获取浮点数类型，section区域名, option选项名
    def get_float(self, section, option):
        self.cfg.read(self.config_path)
        return self.cfg.getfloat(section, option)

    # get_boolean获取布尔类型，section区域名, option选项名
    def get_boolean(self, section, option):
        self.cfg.read(self.config_path)
        return self.cfg.getboolean(section, option)

    # get_eval_data获取列表，section区域名, option选项名
    def get_eval_data(self, section, option):
        self.cfg.read(self.config_path)
        return eval(self.cfg.get(section, option))

    @staticmethod
    def write_config(datas, filename):
        """
        写入配置操做
        :param datas: 须要传入写入的数据
        :param filename: 指定文件名
        :return:
        """
        # 作校验，为嵌套字典的字典才能够（意思.隐私.谈.ce)
        if isinstance(datas, dict):  # 在外层判断是否为字典
            # 再来判断内层的 values 是否为字典
            for value in datas.values():  # 先取出value
                if not isinstance(value, dict):  # 在判断
                    return "数据不合法, 应为嵌套字典的字典"

            config = configparser.ConfigParser()  # 1.建立配置解析器---与写入配置操做一致
            for key in datas:  # 写入操做
                config[key] = datas[key]
            with open(filename, "w") as file:  # 保存到哪一个文件filename=须要指定文件名
                config.write(file)
            # return "写入成功"

    @staticmethod
    def conf_load(filepath):
        log = logging.getLogger('Spider.crawler')
        if not os.path.exists(filepath):
            log.error('config file %s not exist' % filepath)
            return None
        conf = {}
        try:
            conf.urls = Config.get_value('spider', 'feed_file')
            conf.output_dir = Config.get_value('spider', 'result')
            conf.mex_depth = Config.get_int('spider', 'max_depth')
            conf.crawl_interval = Config.get_float('spider', 'crawl_interval')
            conf.time_out = Config.get_float('spider', 'crawl_timeout')
            conf.thread_count = Config.get_int('spider', 'thread_count')
            conf.target_url = read_urls.read_file('../urls')
        except IOError as e:
            log.error("failed to open config file: %s, err: %s" % (filepath, e))
            return None
        except configparser.NoSectionError as e:
            log.error("config parser: no section error: %s" % e)
            return None
        except configparser.NoOptionError as e:
            log.error("config parser: no option error: %s" % e)
            return None
        except Exception as e:
            log.error("unknown error: %s" % e)
            return None
        return conf
