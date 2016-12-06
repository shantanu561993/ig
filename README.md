
# How to gather dns information ?

Let's create a python project for dns information gathering. Information tree:

|**idns - passive mode**|methods|description|
|:-----------------------|:----------|:--------------|
|dns query|A|***Address record***, Returns a 32-bit IPv4 address, most commonly used to map hostnames to an IP address of the host, but it is also used for DNSBLs, storing subnet masks in RFC 1101, etc.|
|dns query|CNAME|***Canonical name record***, Alias of one name to another: the DNS lookup will continue by retrying the lookup with the new name.|
|dns query|AAAA|***IPv6 address record***, Returns a 128-bit IPv6 address, most commonly used to map hostnames to an IP address of the host.|
|dns query|MX|***Mail exchange record***, Maps a domain name to a list of message transfer agents for that domain|
|dns query|NS|***Name server record***, Delegates a DNS zone to use the given authoritative name servers|
|dns query|SOA|***zone of] authority record***, Specifies authoritative information about a DNS zone, including the primary name server, the email of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.|
|dns query|SPF|***Sender Policy Framework***, a simple email-validation system designed to detect email spoofing by providing a mechanism to allow receiving mail exchangers to check that incoming mail from a domain comes from a host authorized by that domain's administrators.|
|dns query|TXT|***Text record***, Originally for arbitrary human-readable text in a DNS record.|
|dns query|PTR|***Pointer record***, Pointer to a canonical name. Unlike a CNAME, DNS processing stops and just the name is returned. The most common use is for implementing reverse DNS lookups, but other uses include such things as DNS-SD.|
|dns query|SRV|***Service locator***, Generalized service location record, used for newer protocols instead of creating protocol-specific records such as MX.|
|dns query|NSEC|***Next Secure record***, Part of DNSSEC—used to prove a name does not exist. Uses the same format as the (obsolete) NXT record.|
|dns query|AXFR|***Authoritative Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers.|
|dns query|IXFR|***Incremental Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers.|
|dns query|DNS Wildcard|Check if nameserver enable wildcard query, or dns faked.|
|dns query|domain bruteforce|bruteforce subdomains with wordlists.|
|dns query|reverse bruteforce|reverse ip for domain|
|dns query|srv bruteforce|bruteforce srv records|
|dns query|gtld bruteforce|bruteforce gtld records|
|dns query|tld bruteforce|bruteforce tld records|
|OSInt|Google|Spider domains from Google pages with domain:`demo.com`|
|OSInt|Bing|Spider domains from Bing pages with domain:`demo.com`|
|OSInt|Yahoo|Spider domains from Yahoo with domain:`demo.com`|
|OSInt|Baidu|Spider domains from Baidu with domain:`demo.com`|
|OSInt|Netcraft|Spider domains from netcraft searchdns pages|
|OSInt|Github|Spider domain from github pages|
|OSInt|Shodan|Search domains from Shodan|
|OSInt|Censys|Search domains from censys|
|OSInt|ZoomEye|Search domains from ZoomEye|
||||
|**idns - offensive mode**|**methods**|**description**|
|Websites|Spider default page|Scan default pages and spider domains|
|Websites|Certificates|Scan domains certificates|

# How to gather information with automation tools ?

In order to solve time, The tool called [**ig**](https://github.com/nixawk/ig/) is created. You don't need to gather information manually (from browsers, or something else)

```
Usage: python ig.py [options]

Options:
  -h, --help            show this help message and exit

  DOMAIN INFORMATION:
    scan domains/subdomains information

    -d DOMAIN, --domain=DOMAIN
                        domain name
    --bruteforce        brute force subdomains
    --wordlist=WORDLIST
                        wordlist for subdomains bruteforce
    --pages=PAGES       pages number to spider
    --sleep             enable sleep to bypass spider ban
    --baidu             search domains from baidu.com
    --bing              search domains from bing.com
    --google            search domains from google.com
    --yahoo             search domains from yahoo.com
    --censys            search domains from censys.io
    --censys_uid=CENSYS_UID
                        a censys api id
    --censys_secret=CENSYS_SECRET
                        a censys api secret
    --github            search domains from github.com
    --netcraft          search domains from netcraft.com
    --zoomeye           search domains from zoomeye.org
    --zoomeye_username=ZOOMEYE_USERNAME
                        a zoomeye username
    --zoomeye_password=ZOOMEYE_PASSWORD
                        a zoomeye password
```

## How to search domains from searchengines ?

If you want to spider domains from searchengines, **--pages** is a must. Please try the following examples.

```
(ig)  ->> python ig.py -d google.com --pages 2 --baidu --bing --yahoo
[*] search domains from baidu.com
{'google.com': {'baidu': [u'www.google.com',
                          u'news.google.com',
                          u'cloud.google.com',
                          u'feedburner.google.com',
                          u'play.google.com',
                          u'drive.google.com',
                          u'helpouts.google.com',
                          u'books.google.com']}}
[*] search domains from bing.com
{'google.com': {'bing': ['www.google.com',
                         'earth.google.com',
                         'scholar.google.com',
                         'accounts.google.com',
                         'images.google.com',
                         'news.google.com',
                         'developers.google.com',
                         'photos.google.com',
                         'books.google.com',
                         'hangouts.google.com',
                         'translate.google.com',
                         'docs.google.com',
                         'myactivity.google.com',
                         'code.google.com',
                         'm.google.com',
                         'gsuite.google.com',
                         'bookmarks.google.com',
                         'sandbox.google.com',
                         'fiber.google.com',
                         'picasa.google.com',
                         'desktop.google.com',
                         'orkut.google.com']}}
[*] search domains from yahoo.com
{'google.com': {'yahoo': ['translate.google.com',
                          'www.google.com',
                          'search.google.com',
                          'desktop.google.com',
                          'support.google.com',
                          'adwords.google.com',
                          'mapmaker.google.com',
                          'doodles.google.com']}}
[+] all domains as follow:
[u'www.google.com',
 u'news.google.com',
 u'cloud.google.com',
 u'feedburner.google.com',
 u'play.google.com',
 u'drive.google.com',
 u'helpouts.google.com',
 u'books.google.com',
 'www.google.com',
 'earth.google.com',
 'scholar.google.com',
 'accounts.google.com',
 'images.google.com',
 'news.google.com',
 'developers.google.com',
 'photos.google.com',
 'books.google.com',
 'hangouts.google.com',
 'translate.google.com',
 'docs.google.com',
 'myactivity.google.com',
 'code.google.com',
 'm.google.com',
 'gsuite.google.com',
 'bookmarks.google.com',
 'sandbox.google.com',
 'fiber.google.com',
 'picasa.google.com',
 'desktop.google.com',
 'orkut.google.com',
 'translate.google.com',
 'www.google.com',
 'search.google.com',
 'desktop.google.com',
 'support.google.com',
 'adwords.google.com',
 'mapmaker.google.com',
 'doodles.google.com']
```

## How to brute force subdomains ?

Subdomains bruteforce is a good way to discover something hidden. I've created a gevent worker for the job. Wish you happy.

```
(ig) ->> python ig.py -d google.com --bruteforce
[!] bruteforce domain may cost long time
[!] use default wordlist to bruteforce subdomains
google.com does not really have wildcards
{'www.google.com': {'A': [u'216.58.196.228']}}
{'mail.google.com': {'A': [u'74.125.203.18', u'74.125.203.19', u'74.125.203.83', u'74.125.203.17']}}
{'ns2.google.com': {'A': [u'216.239.34.10']}}
{'news.google.com': {'A': [u'216.58.197.14']}}
{'calendar.google.com': {'A': [u'74.125.23.113', u'74.125.23.100', u'74.125.23.102', u'74.125.23.138', u'74.125.23.101', u'74.125.23.139']}}
{'ftp.google.com': {'A': []}}
{'smtp.google.com': {'A': []}}
{'pop.google.com': {'A': []}}
{'m.google.com': {'A': []}}
{'webmail.google.com': {'A': []}}
......
bruteforce log....
....
['www.google.com',
 'mail.google.com',
 'ns2.google.com',
 'news.google.com',
 'calendar.google.com',
 'docs.google.com',
 'ns4.google.com',
 'images.google.com',
 'api.google.com',
 'apps.google.com',
 'tools.google.com',
 'sites.google.com',
 'dl.google.com',
 'feeds.google.com',
 'groups.google.com',
 'map.google.com',
 'maps.google.com',
 'accounts.google.com',
 'investor.google.com',
 'doc.google.com',
 'id.google.com',
 'whois.google.com',
 'enterprise.google.com',
 'asia.google.com',
 'history.google.com',
 'developers.google.com',
 'earth.google.com',
 'drive.google.com',
 'play.google.com',
 'talk.google.com',
 'plus.google.com',
 'pki.google.com',
 'publish.google.com',
 'fusion.google.com',
 'chrome.google.com',
 'apis.google.com',
 'pack.google.com',
 'purchase.google.com',
 'dai.google.com']
```


# Links

1. https://en.wikipedia.org/wiki/List_of_DNS_record_types
2. https://www.google.com/
3. https://www.bing.com/
4. https://search.yahoo.com/
5. https://www.baidu.com/
6. http://searchdns.netcraft.com/
7. https://github.com/search/
8. https://www.shodan.io
9. https://www.censys.io
10. https://www.zoomeye.org
