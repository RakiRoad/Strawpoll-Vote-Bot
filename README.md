# Strawpoll Vote Bot

![](https://img.shields.io/badge/Language-Python-brightgreen.svg) ![](https://img.shields.io/badge/Release-V1.1-blue.svg) ![](https://img.shields.io/badge/License-MIT-orange.svg)

WARNING!!! This is for Educational Purposes Only. I will not be liable for how you will use this script

## Features
- Vote Bot Strawpoll

## Requirements
- Python 3.0+
- requests
- argparse

## Installation
1. pip install requests and argparse if haven't done so
2. Clone or download the repository 

## Usage
1. Fill proxy_list.txt with desired proxies
2. Run command similar to example below

Example command:
```bash
python strawpollbot.py -i 12132829 -o 138885063
```

-i defines the id of the strawpoll. For example the id for 'https://www.strawpoll.me/12132829' would be 12132829
-o defines the checkbox option on the poll. To find this, right click desired checkbox option box and 'inspect' and look for the 'value' option

## License

All source code in this app is released under the MIT license. See LICENSE for details. 