import unittest

from lib import config_load


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        self.config_file = "spider_test.conf"
        config_file = \
            """
            [spider]
            feed_file = './urls'    # 种子文件路径
            result = './result.data'    # 抓取结果存储文件, 一行一个
            max_depth = 6  # 最大抓取深度(种子为0级)
            crawl_interval = 1  # 抓取间隔. 单位: 秒
            crawl_timeout = 2  # 抓取超时. 单位: 秒
            thread_count = 8 #抓取线程数
            """

    def test_config_parser(self):
        try:
            conf = config_load.Config.conf_load(self.config_file)
            self.assertEqual('./urls', conf.get('urls'))
            self.assertEqual('./result.data', conf.get('output_dir'))
            self.assertEqual(6, conf.get('mex_depth'))
            self.assertEqual(float(1), conf.get('crawl_interval'))
            self.assertEqual(float(2), conf.get('crawl_timeout'))
            self.assertEqual(8, conf.get('thread_count'))
        except ValueError as e:
            print("try to read conf failed. msg: %s" % e)


if __name__ == '__main__':
    unittest.main()
