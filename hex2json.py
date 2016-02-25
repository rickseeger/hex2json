#!/usr/bin/python2.7

import sys
from common import convert


# read HEX from stdin
tx_hex = sys.stdin.read()

# convert to JSON
tx_json = convert(tx_hex)

# conversion failed
if (tx_json is None):
    sys.stderr.write('HEX -> JSON conversion failed\n')
    exit(1)

# success, send formatted version to stdout
print tx_json
