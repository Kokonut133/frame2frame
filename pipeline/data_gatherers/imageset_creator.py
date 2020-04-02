from google_images_download import google_images_download       # currently broken 4.2.2020
import pipeline.data_gatherers.bing_scraper
from icrawler.builtin import GoogleImageCrawler

import os
from PIL import Image

__author__ = "cstur"

import settings


class ImagesetCreator():
    def __init__(self):
        pass

    def create_image_dataset(self, keyword, height, width, amount):
        path = os.path.join(settings.googled_dir, keyword)
        os.makedirs(path, exist_ok=True)
        self.download_images(keyword=keyword, path=path, amount=amount)

    def download_images(self, keyword, path, amount, size="medium"):
        google_crawler = GoogleImageCrawler(storage={'root_dir': path})
        google_crawler.crawl(keyword=keyword, max_num=amount)