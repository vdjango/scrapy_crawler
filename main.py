from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 设置工程目录

# execute(["scrapy", "crawl", "bilibili"]).strip()
execute(["scrapy", "crawl", "painting"]).strip()
