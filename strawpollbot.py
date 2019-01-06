import os
import signal
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--id", type=str, required=True) #id of the strawpoll. The id for 'https://www.strawpoll.me/12132829' would be 12132829
parser.add_argument("-o", "--option", type=str, required=True) #the checkbox option value. To find this right click desired checkbox box and 'inspect' and look for the 'value' option.
args = parser.parse_args()

#reads porxy_list.txt file to read list of proxies
#change contents of file for desired proxy
file = open('proxy_list.txt', 'r')
line = file.readline()
while line:
    proxy = "http://" + line.strip()
    print("Attempting proxy: " + proxy)
    proxy_dictionary = {"https": proxy}
    url = args.id
    data= "options=" + args.option

    headers = {
        'accept': "/",
        'origin': "https://www.strawpoll.me",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'referer': args.id,
        'Cookie': 'lang=en',
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        'cache-control': "no-cache"
    }

    try:
        response = requests.post(url=("https://www.strawpoll.me/" + str(url)), data=data, proxies=proxy_dictionary, headers=headers)
        print("Success!\n")
    except:
        print("Failure :(\n")

    line = file.readline()

print("Voting has finished.")