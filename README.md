
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
|dns query|AXFR|***Incremental Zone Transfer***, Transfer entire zone file from the master name server to secondary name servers.|
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
