import argparse
import subprocess
import os
import time
from InternetArchiveUploader import InternetArchiveUploader


parser = argparse.ArgumentParser(
            prog='Pipeline Invoker',
            description='Downloads TikTok videos with its own arguments then calls the upload script',
        )
#------------------------------------------------------------------------------------------
parser.add_argument('-d', '--dir',required=True)      
parser.add_argument('-i', '--identifier',required=True)

# -----------------------------------------------------------------------------------------
parser.add_argument('-w', action='store_true',help='Downloads Videos With Watermark')
parser.add_argument('-s', action='store_true',help='Only does a single iteration of link-gathering')


group=parser.add_mutually_exclusive_group(required=True)

group.add_argument('-f', '--txt', help='Download All Video URL\'s In A Text File')
group.add_argument('-m', '--mass',help= 'Mass Download Via Username eg.(@catpippi)')
group.add_argument('-u','--url', help= 'Tiktok Url eg. (https://www.tiktok.com/@catpippi/video/7310806096568945962)')

args =parser.parse_args()
tik_tok_downloader_args=['node','index.js']

if args.txt:
    tik_tok_downloader_args.extend(['-f',args.txt])
elif args.url:
    tik_tok_downloader_args.extend(['-u',args.url])
else:
    tik_tok_downloader_args.extend(['-m',args.mass])

if args.s:
    tik_tok_downloader_args.extend(['-s'])
if args.w:
    tik_tok_downloader_args.extend(['-w'])

    



while(True):
    
    subprocess.run(tik_tok_downloader_args)
    if os.path.exists(args.dir):
        uploader=InternetArchiveUploader(args.identifier,{
        'title': f'@{args.mass}',
        'mediatype': 'video',
        'collection': 'opensource_movies',
        'date': time.strftime("%Y-%m-%d"),
        'description': os.getenv('DESCRIPTION'),
        'subject': os.getenv('SUBJECT').split(','),
        'creator': os.getenv('CREATOR'),
        'language': 'English',
        'licenseurl': 'http://creativecommons.org/publicdomain/zero/1.0/'
        },os.getenv('IA_USERNAME'),os.getenv('IA_PASSWORD'))
        uploader.uploadDirectory(args.dir)
        
