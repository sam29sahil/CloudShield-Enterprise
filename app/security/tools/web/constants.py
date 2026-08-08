"""
CloudShield Enterprise
Web Tool Constants
"""

WHATWEB_DEFAULT = [

    "--color=never",

    "--log-json=-"

]

NIKTO_DEFAULT = [

    "-ask",

    "no"

]

NUCLEI_DEFAULT = [

    "-severity",

    "low,medium,high,critical"

]

GOBUSTER_DEFAULT = [

    "dir",

    "-w",

    "/usr/share/wordlists/dirb/common.txt"

]

FFUF_DEFAULT = [

    "-w",

    "/usr/share/wordlists/dirb/common.txt",

    "-mc",

    "200"

]

DIRSEARCH_DEFAULT = [

    "-w",

    "/usr/share/wordlists/dirb/common.txt"

]

SQLMAP_DEFAULT = [

    "--batch"

]

ZAP_DEFAULT = [

    "-cmd"

]

DALFOX_DEFAULT = [

    "url"

]

XSSTRIKE_DEFAULT = [

    "--crawl"

]

WAFW00F_DEFAULT = [

    "-a"

]