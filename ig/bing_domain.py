#!/usr/bin/python
# -*- coding: utf-8 -*-

from bing import bing
import re


class spider(bing):
    def __init__(self):
        super(spider, self).__init__()

    def domain_search(self, domain, page=2, random_sleep=False):
        """parse domains from bing spider results"""
        dork = "site:{}".format(domain)
        regex = re.compile('[a-zA-Z0-9]+\.{}'.format(domain), re.I | re.M)
        results = self.dork_search(dork, page=page, random_sleep=random_sleep)
        data = results[dork]  # [['title', 'href']]
        bi_domains = []

        if not data:
            return {domain: {'bing': bi_domains}}

        for title, href in data:
            domains = regex.findall(href)
            for _ in domains:
                if _ in bi_domains:
                    continue
                bi_domains.append(_)

        return {domain: {'bing': bi_domains}}


def demo_spider():
    """A demo for spider class"""
    domain = "google.com"
    sp = spider()
    print(sp.domain_search(domain))


if __name__ == "__main__":
    demo_spider()
