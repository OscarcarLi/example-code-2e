#!/usr/bin/env python3

import asyncio
import sys
from keyword import kwlist

from netaddr import multi_probe


async def main(tld: str) -> None:
    tld = tld.strip('.')
    names = (kw for kw in kwlist if len(kw) <= 4)
    domains = (f'{name}.{tld}'.lower() for name in names)
    async for domain, found in multi_probe(domains):
        mark = '.' if found else '?\t\t'
        print(f'{mark} {domain}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        asyncio.run(main(sys.argv[1]))
    else:
        print('Please provide a TLD.', f'Example: {sys.argv[0]} COM.BR')