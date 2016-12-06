#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
from optparse import OptionGroup
from optparse import OptionError
import sys
from webspider_domain import baidu_domain_spider
from webspider_domain import bing_domain_spider
from webspider_domain import yahoo_domain_spider
from webspider_domain import google_domain_spider
from webspider_domain import netcraft_domain_spider
from webspider_domain import zoomeye_domain_spider
from webspider_domain import censys_domain_spider
from webspider_domain import github_domain_spider
from bruteforce_domain import idns_bruteforce
from pprint import pprint


class cmdline(object):
    def getArgs(self):
        """This function parses the command line parameters and arguments.
        """
        usage = "python %prog [options]"
        parser = OptionParser(usage=usage)
        try:
            domainopt = OptionGroup(parser, "DOMAIN INFORMATION",
                                    "scan domains/subdomains information")
            domainopt.add_option('-d', '--domain', dest='domain', type='str',
                                 help='domain name')
            domainopt.add_option('--bruteforce', action='store_true',
                                 help='brute force subdomains')
            domainopt.add_option('--wordlist', dest='wordlist', type='str',
                                 help='wordlist for subdomains bruteforce')
            domainopt.add_option('--pages', dest='pages', type='int',
                                 help='pages number to spider')
            domainopt.add_option('--sleep', action='store_true',
                                 help='enable sleep to bypass spider ban')
            domainopt.add_option('--baidu', action='store_true',
                                 help='search domains from baidu.com')
            domainopt.add_option('--bing', action='store_true',
                                 help='search domains from bing.com')
            domainopt.add_option('--google', action='store_true',
                                 help='search domains from google.com')
            domainopt.add_option('--yahoo', action='store_true',
                                 help='search domains from yahoo.com')
            domainopt.add_option('--censys', action='store_true',
                                 help='search domains from censys.io')
            domainopt.add_option('--censys_uid', dest='censys_uid',
                                 help='a censys api id')
            domainopt.add_option('--censys_secret', dest='censys_secret',
                                 help='a censys api secret')
            domainopt.add_option('--github', action='store_true',
                                 help='search domains from github.com')
            domainopt.add_option('--netcraft', action='store_true',
                                 help='search domains from netcraft.com')
            domainopt.add_option('--zoomeye', action='store_true',
                                 help='search domains from zoomeye.org')
            domainopt.add_option('--zoomeye_username', dest='zoomeye_username',
                                 type='str', help='a zoomeye username')
            domainopt.add_option('--zoomeye_password', dest='zoomeye_password',
                                 type='str', help='a zoomeye password')
            parser.add_option_group(domainopt)

            (args, _) = parser.parse_args()
        except (OptionError, TypeError) as e:
            parser.error(e)
        else:
            return args


def main():
    """parse cmdline options
    """
    c = cmdline()
    args = c.getArgs()

    domains = []  # save all domains result
    if not args.domain:
        print('[!] please a domain to scan subdomains, ex: google.com')
        sys.exit(0)

    domain = args.domain

    if args.bruteforce:
        print('[!] bruteforce domain may cost long time')
        if args.wordlist:
            idns_bt = idns_bruteforce(domain, subdomains_wd=args.wordlist)
        else:
            print('[!] use default wordlist to bruteforce subdomains')
            idns_bt = idns_bruteforce(domain)
        idns_bt.work()
        idns_btret = []
        for item in idns_bt.domains:
            idns_btret.extend(item.keys())
        domains.extend(idns_btret)
        pprint(idns_btret)

    if not args.pages:
        print('[!] please set pages num to spider domains from searchengine')
        sys.exit(0)

    pages = args.pages

    sleep = True if args.sleep else False

    if args.baidu:
        print('[*] search domains from baidu.com')
        bd = baidu_domain_spider()
        bdret = bd.baidu_domain_search(domain, page=pages, random_sleep=sleep)
        domains.extend(bdret[domain]['baidu'])
        pprint(bdret)

    if args.bing:
        print('[*] search domains from bing.com')
        bi = bing_domain_spider()
        biret = bi.bing_domain_search(domain, page=pages, random_sleep=sleep)
        domains.extend(biret[domain]['bing'])
        pprint(biret)

    if args.google:
        print('[*] search domains from google.com')
        gg = google_domain_spider()
        ggret = gg.google_domain_search(domain, page=pages, random_sleep=sleep)
        domains.extend(ggret[domain]['google'])
        pprint(ggret)

    if args.yahoo:
        print('[*] search domains from yahoo.com')
        yh = yahoo_domain_spider()
        yhret = yh.yahoo_domain_search(domain, page=pages, random_sleep=sleep)
        domains.extend(yhret[domain]['yahoo'])
        pprint(yhret)

    if args.censys:
        print('[*] search domains from censys.io')
        uid = args.censys_uid
        secret = args.censys_secret
        assert (uid and secret)

        cs = censys_domain_spider(uid, secret)
        csret = cs.censys_domain_search(domain, page=2)
        domains.extend(csret[domain]['censys'])
        pprint(csret)

    if args.github:
        print('[*] search domains from github.com')
        gh = github_domain_spider()
        domain = 'google.com'
        ghret = gh.github_domain_search(domain)
        domains.extend(ghret[domain]['github'])
        pprint(ghret)

    if args.netcraft:
        print('[*] search domains from netcraft.net')
        nt = netcraft_domain_spider()
        ntret = nt.netcraft_domain_search(domain, page=pages,
                                          random_sleep=sleep)
        domains.extend(ntret[domain]['netcraft'])
        pprint(ntret)

    if args.zoomeye:
        print('[*] search domains from zoomeye.org')
        zoomeye_user = args.zoomeye_username
        zoomeye_pass = args.zoomeye_password
        assert (zoomeye_user and zoomeye_pass)

        zms = zoomeye_domain_spider(zoomeye_user, zoomeye_pass)
        zmret = zms.zoomeye_domain_search(domain)
        domains.extend(zmret[domain]['zoomeye'])
        pprint(zmret)

    print('[+] all domains as follow:')
    pprint(domains)
    return domains


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err)
