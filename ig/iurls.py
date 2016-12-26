#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
from optparse import OptionGroup
from optparse import OptionError
import sys
from baidu import baidu
from bing import bing
from yahoo import yahoo
from google import google


class cmdline(object):
    def getArgs(self):
        """This function parses the command line parameters and arguments.
        """
        usage = "python %prog [options]"
        parser = OptionParser(usage=usage)
        try:
            urlopt = OptionGroup(parser, "URL INFORMATION",
                                 "scan URLs information")
            urlopt.add_option('-d', '--domain', dest='domain', type='str',
                              help='domain name')
            urlopt.add_option('-u', '--url', dest='url', type='str',
                              help='url link')
            urlopt.add_option('--pages', dest='pages', type='int',
                              help='pages number to spider')
            urlopt.add_option('--sleep', action='store_true',
                              help='enable sleep to bypass spider ban')
            urlopt.add_option('--baidu', action='store_true',
                              help='search urls from baidu.com')
            urlopt.add_option('--bing', action='store_true',
                              help='search urls from bing.com')
            urlopt.add_option('--google', action='store_true',
                              help='search urls from google.com')
            urlopt.add_option('--yahoo', action='store_true',
                              help='search urls from yahoo.com')
            parser.add_option_group(urlopt)
            (args, _) = parser.parse_args()
        except (OptionError, TypeError) as e:
            parser.error(e)
        else:
            return args


class urlspider(baidu, bing, yahoo, google):
    def __init__(self):
        super(urlspider, self).__init__()

    def handle_exception(self, func, *args, **kwds):
        try:
            ret = func(*args, **kwds)
        except Exception as err:
            ret = err

        return ret

    def baidu_url_search(self, dork, page=0, random_sleep=True):
        bd = self.handle_exception(self.baidu_dork_search,
                                   dork, page=page, random_sleep=random_sleep)

        if bd and dork in bd:
            for title, href, link in bd[dork]:
                print("\n")
                print(title)
                print(href)
                print(link)

    def bing_url_search(self, dork, page=0, random_sleep=True):
        bi = self.handle_exception(self.bing_dork_search,
                                   dork, page=page, random_sleep=random_sleep)
        if bi and dork in bi:
            for title, href in bi[dork]:
                print("\n")
                print(title)
                print(href)

    def yahoo_url_search(self, dork, page=0, random_sleep=True):
        yh = self.handle_exception(self.yahoo_dork_search,
                                   dork, page=page, random_sleep=random_sleep)
        if yh and dork in yh:
            for title, href in yh[dork]:
                print("\n")
                print(title)
                print(href)

    def google_url_search(self, dork, page=0, random_sleep=True):
        gg = self.handle_exception(self.google_dork_search,
                                   dork, page=page, random_sleep=random_sleep)

        if gg and dork in gg:
            for title, href, link in gg[dork]:
                print("\n")
                print(title)
                print(href)
                print(link)


def main():
    """parse cmdline options
    """
    c = cmdline()
    args = c.getArgs()
    uspider = urlspider()
    dorks = []

    if args.domain and "site: {}".format(args.domain) not in dorks:
        dorks.append("site: {}".format(args.domain))

    if args.url and "inurl: {}".format(args.url) not in dorks:
        dorks.append("inurl: {}".format(args.url))

    if not args.domain and not args.url:
        print('[!] please use -d or -u to scan all links, ex: google.com')
        sys.exit(0)

    if not args.pages:
        print('[!] please set pages num to spider domains from searchengine')
        sys.exit(0)

    pages = args.pages
    sleep = True if args.sleep else False

    if args.baidu:
        print('[*] search urls from baidu.com')
        for dork in dorks:
            uspider.baidu_url_search(dork, pages, random_sleep=sleep)

    if args.bing:
        print('[*] search urls from bing.com')
        for dork in dorks:
            uspider.bing_url_search(dork, pages, random_sleep=sleep)

    if args.yahoo:
        print('[*] search urls from yahoo.com')
        for dork in dorks:
            uspider.yahoo_url_search(dork, pages, random_sleep=sleep)

    if args.google:
        print('[*] search urls from google.com')
        for dork in dorks:
            uspider.google_url_search(dork, pages, random_sleep=sleep)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
